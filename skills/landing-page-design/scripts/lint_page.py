#!/usr/bin/env python3
"""Check landing page source files against the landing-page-design rules.

Usage:
    python lint_page.py <file> [<file> ...] [--lang auto|ko|en]
                        [--theme base|tbnc] [--tokens tokens.json] [--json]

Reads .html, .css, .jsx, .tsx, .js, .ts, .vue, .svelte, .astro files.

Exit codes: 0 no errors (warnings allowed), 1 errors found, 2 usage error.

This checks what is mechanically checkable: fonts, Tailwind and CSS values,
easing, animated properties, banned words, meta tags, and Korean ship
requirements. It cannot judge layout, hierarchy, or what actually rendered.
A clean run is necessary, not sufficient; still look at the page.
"""

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

# ── Rule data ────────────────────────────────────────────────────────────────

ALLOWED_FONTS = {"geist", "geist mono", "manrope", "poppins"}
ALLOWED_FONTS_KO = {"pretendard", "pretendard variable", "suit", "suit variable", "wanted sans", "wanted sans variable"}
BANNED_FONTS = {
    "inter", "roboto", "arial", "open sans", "helvetica", "helvetica neue",
    "noto sans kr", "nanum gothic", "nanumgothic", "malgun gothic", "맑은 고딕",
    "gulim", "굴림", "dotum", "돋움", "batang", "바탕",
}
GENERIC_FAMILIES = {
    "sans-serif", "serif", "monospace", "system-ui", "-apple-system",
    "blinkmacsystemfont", "ui-sans-serif", "ui-monospace", "inherit", "initial",
}

FONT_SIZES_PX = {12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72, 96, 128}
SPACING_PX = {0, 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96}
# Tailwind spacing unit n -> n * 4px. Only units that land on SPACING_PX.
SPACING_UNITS = {"0", "px", "0.5", "1", "2", "3", "4", "6", "8", "10", "12", "16", "20", "24"}
RADIUS_PX = {0, 2, 4, 6, 8, 12, 16, 24, 32, 9999}
RADIUS_PX_TBNC = RADIUS_PX | {10, 18, 20, 999}

BANNED_WORDS_EN = [
    "revolutionize", "supercharge", "cutting edge", "cutting-edge", "effortless",
    "transform your workflow", "take it to the next level", "harness the power",
    "world class", "world-class",
]
BANNED_WORDS_KO = [
    "혁신적인", "획기적인", "차원이 다른", "압도적인", "새로운 패러다임",
    "원스톱", "토탈 솔루션", "극대화", "스마트한", "퀄리티 높은",
]
WEAK_CTA_KO = ["자세히 보기", "더 알아보기"]
WEAK_CTA_EN = ["learn more", "submit", "click here"]

HANGUL_RE = re.compile(r"[가-힣]")
SPACING_PREFIXES = (
    "p", "px", "py", "pt", "pb", "pl", "pr", "ps", "pe",
    "m", "mx", "my", "mt", "mb", "ml", "mr", "ms", "me",
    "gap", "gap-x", "gap-y", "space-x", "space-y",
)
SOURCE_SUFFIXES = {".html", ".htm", ".css", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".astro", ".mdx"}


# ── Helpers ──────────────────────────────────────────────────────────────────

class Report:
    def __init__(self):
        self.items = []

    def add(self, level, rule, path, text, pos, message):
        line = text.count("\n", 0, pos) + 1 if pos is not None else None
        self.items.append({"level": level, "rule": rule, "file": str(path), "line": line, "message": message})

    def error(self, *args):
        self.add("error", *args)

    def warn(self, *args):
        self.add("warn", *args)


class VisibleText(HTMLParser):
    """Collect visible text, skipping script, style, and code blocks."""

    SKIP = {"script", "style", "code", "pre", "noscript", "svg"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.chunks = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.depth += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.depth:
            self.depth -= 1

    def handle_data(self, data):
        if not self.depth and data.strip():
            self.chunks.append(data)


def visible_text(text, suffix):
    if suffix in {".html", ".htm", ".vue", ".svelte", ".astro"}:
        parser = VisibleText()
        parser.feed(text)
        return " ".join(parser.chunks)
    if suffix in {".jsx", ".tsx", ".mdx"}:
        # Text between JSX tags, minus expressions.
        return " ".join(m.group(1) for m in re.finditer(r">([^<>{}]+)<", text) if m.group(1).strip())
    return ""


def class_tokens(text):
    """Yield (token, pos) for every class in class / className attributes."""
    for m in re.finditer(r"\bclass(?:Name)?\s*=\s*(?:\{\s*)?([\"'`])(.*?)\1", text, re.S):
        start = m.start(2)
        for t in re.finditer(r"\S+", m.group(2)):
            raw = t.group(0)
            # Strip variants like md:hover: while keeping arbitrary values intact.
            base = re.sub(r"^(?:[^\[\]:\s]+:)+", "", raw).lstrip("!")
            yield base, raw, start + t.start()


def first_family(value):
    fam = value.split(",")[0].strip().strip("\"'`").strip()
    return fam.lower()


def px_values(value):
    """Return numeric px values from a CSS length list; rem converted at 16px."""
    out = []
    for num, unit in re.findall(r"(-?\d*\.?\d+)(px|rem)\b", value):
        v = float(num) * (16 if unit == "rem" else 1)
        out.append(abs(v))
    return out


def norm_hex(raw):
    h = raw.lstrip("#").lower()
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return "#" + h


# ── Checks ───────────────────────────────────────────────────────────────────

def check_fonts(path, text, ctx, rep):
    allowed = {"pretendard", "pretendard variable"} if ctx["theme"] == "tbnc" else ALLOWED_FONTS | ALLOWED_FONTS_KO
    for m in re.finditer(r"font-?[fF]amily[\"']?\s*:\s*[\"'`]?([^;}\n]+)", text):
        fam = first_family(m.group(1))
        if not fam or fam.startswith("var(") or fam in GENERIC_FAMILIES:
            continue
        if fam in BANNED_FONTS:
            rep.error("font-banned", path, text, m.start(), f"Banned primary font '{fam}'.")
        elif fam not in allowed:
            level = rep.error if ctx["theme"] == "tbnc" else rep.warn
            level("font-unlisted", path, text, m.start(), f"Primary font '{fam}' is not on the allowed list.")
    for m in re.finditer(r"fonts\.googleapis\.com/css2?\?family=([^\"'&>]+)", text):
        fam = m.group(1).split(":")[0].replace("+", " ").lower()
        if fam in BANNED_FONTS:
            rep.error("font-banned", path, text, m.start(), f"Loads banned font '{fam}' from Google Fonts.")
    for m in re.finditer(r"font-style\s*:\s*(italic|oblique)", text, re.I):
        rep.error("italic", path, text, m.start(), "Italic text is not allowed.")
    for m in re.finditer(r"font-weight\s*:\s*(800|900)\b", text):
        rep.add("warn" if ctx["theme"] == "tbnc" else "error", "weight", path, text, m.start(),
                f"Weight {m.group(1)} exceeds the 700 cap" + (" (TBNC allows 800 on the wordmark only)." if ctx["theme"] == "tbnc" else "."))


def check_classes(path, text, ctx, rep):
    radius_ok = RADIUS_PX_TBNC if ctx["theme"] == "tbnc" else RADIUS_PX
    tokens = list(class_tokens(text))
    class_strings = {}
    for m in re.finditer(r"\bclass(?:Name)?\s*=\s*(?:\{\s*)?([\"'`])(.*?)\1", text, re.S):
        class_strings[m.start(2)] = m.group(2)

    for base, raw, pos in tokens:
        if base in ("italic",):
            rep.error("italic", path, text, pos, "Tailwind 'italic' is not allowed.")
        elif base in ("font-extrabold", "font-black"):
            rep.add("warn" if ctx["theme"] == "tbnc" else "error", "weight", path, text, pos,
                    f"'{raw}' exceeds the 700 weight cap.")
        elif re.fullmatch(r"text-\[\d*\.?\d+(px|rem|em)\]", base):
            rep.error("type-arbitrary", path, text, pos, f"'{raw}' is off the type scale. Snap to the closest step below.")
        elif re.fullmatch(r"font-\[.+\]", base):
            fam = base[6:-1].replace("_", " ").strip("'\"").split(",")[0].strip("'\"").lower()
            if fam in BANNED_FONTS:
                rep.error("font-banned", path, text, pos, f"Banned font '{fam}' in '{raw}'.")
        elif re.fullmatch(r"-?(%s)-\[.+\]" % "|".join(map(re.escape, SPACING_PREFIXES)), base):
            rep.error("spacing-arbitrary", path, text, pos, f"'{raw}' uses an arbitrary spacing value.")
        elif re.fullmatch(r"-?(%s)-([\d.]+|px)" % "|".join(map(re.escape, SPACING_PREFIXES)), base):
            unit = base.lstrip("-").rsplit("-", 1)[1]
            if unit not in SPACING_UNITS:
                rep.error("spacing-scale", path, text, pos, f"'{raw}' is {unit} units, which is not in the spacing table.")
        elif re.fullmatch(r"rounded(-[trblse]{1,2})?-\[(\d*\.?\d+)px\]", base):
            v = float(re.search(r"\[(\d*\.?\d+)px\]", base).group(1))
            if v not in radius_ok:
                rep.error("radius", path, text, pos, f"'{raw}' is not an allowed radius.")
        elif base in ("ease-linear", "ease-in", "ease-out", "ease-in-out"):
            rep.error("easing", path, text, pos, f"'{raw}' is a default curve. Use ease-[cubic-bezier(0.22,1,0.36,1)].")
        elif re.fullmatch(r"duration-(75|100|150)", base):
            rep.error("duration", path, text, pos, f"'{raw}' is shorter than 200ms.")
        elif re.fullmatch(r"(bg-gradient-to-\w+|bg-linear-[\w\[\]-]+|bg-radial[\w\[\]-]*|bg-conic[\w\[\]-]*)", base):
            cls = next((s for p, s in class_strings.items() if p <= pos <= p + len(s)), "")
            if "bg-clip-text" not in cls:
                rep.error("gradient-bg", path, text, pos, f"'{raw}' is a background gradient. Backgrounds are flat.")
            elif ctx["theme"] == "tbnc":
                rep.error("gradient-bg", path, text, pos, "TBNC allows no gradients, including hero text.")
        elif re.fullmatch(r"border-[lrtbse](-\d+)?", base):
            rep.warn("border-one-side", path, text, pos, f"'{raw}' is a one sided border. Never on cards.")
        elif ctx["theme"] == "tbnc" and re.fullmatch(r"shadow(-\w+)?", base) and base != "shadow-none":
            rep.error("shadow", path, text, pos, f"'{raw}': TBNC uses no shadows.")
        elif ctx["theme"] == "tbnc" and re.fullmatch(r"(text|bg|border|ring|fill|stroke)-(red|rose)-\d+", base):
            rep.error("red", path, text, pos, f"'{raw}': TBNC uses no red.")
        elif ctx["theme"] == "tbnc" and re.fullmatch(
                r"(text|bg|border|ring|fill|stroke|from|to|via)-(slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-\d+", base):
            rep.error("palette", path, text, pos, f"'{raw}' is a Tailwind palette color. Use a TBNC token.")


def check_css(path, text, ctx, rep):
    radius_ok = RADIUS_PX_TBNC if ctx["theme"] == "tbnc" else RADIUS_PX
    for m in re.finditer(r"(?<![\w-])font-size\s*:\s*([^;}\n]+)", text):
        val = m.group(1)
        if "var(" in val or "clamp(" in val:
            if "clamp(" in val:
                rep.warn("type-arbitrary", path, text, m.start(), "clamp() font size: confirm each end lands on a scale step.")
            continue
        for v in px_values(val):
            if v not in FONT_SIZES_PX:
                rep.error("type-arbitrary", path, text, m.start(), f"font-size {v:g}px is off the type scale.")
    for m in re.finditer(r"(?<![\w-])(padding|margin|gap|row-gap|column-gap)(-[a-z]+)?\s*:\s*([^;}\n]+)", text):
        if "var(" in m.group(3) or "calc(" in m.group(3):
            continue
        for v in px_values(m.group(3)):
            if v not in SPACING_PX:
                rep.error("spacing-scale", path, text, m.start(), f"{m.group(1)} {v:g}px is not in the spacing table.")
                break
    for m in re.finditer(r"(?<![\w-])border(-[a-z-]+)?-radius\s*:\s*([^;}\n]+)", text):
        for v in px_values(m.group(2)):
            if v not in radius_ok:
                rep.error("radius", path, text, m.start(), f"border-radius {v:g}px is not an allowed radius.")
                break
    for m in re.finditer(r"(?<![\w-])background(-image)?\s*:\s*[^;}\n]*(linear|radial|conic)-gradient\(", text):
        block = text[max(0, text.rfind("{", 0, m.start())):text.find("}", m.start()) + 1]
        clipped = re.search(r"background-clip\s*:\s*text", block)
        if not clipped or ctx["theme"] == "tbnc":
            rep.error("gradient-bg", path, text, m.start(),
                      "TBNC allows no gradients." if clipped else "Background gradient. Backgrounds are flat.")
    for m in re.finditer(r"(?<![\w-])border-(left|right|top|bottom)\s*:\s*(?!none|0)", text):
        rep.warn("border-one-side", path, text, m.start(), f"border-{m.group(1)}: one sided borders are never used on cards.")
    if ctx["theme"] == "tbnc":
        for m in re.finditer(r"(?<![\w-])(box-shadow|text-shadow)\s*:\s*(?!none)", text):
            rep.error("shadow", path, text, m.start(), f"{m.group(1)}: TBNC uses no shadows.")


def check_motion(path, text, ctx, rep):
    has_motion = False
    for m in re.finditer(r"(?<![\w-])(transition|animation)(-timing-function)?[\"']?\s*:\s*[\"'`]?([^;}\n\"'`]+)", text):
        has_motion = True
        val = m.group(3).strip().lower()
        if val in ("none", "inherit", "initial"):
            continue
        if re.search(r"(?<![\w-])(ease|linear|ease-in|ease-out|ease-in-out)(?![\w-])", val):
            rep.error("easing", path, text, m.start(), f"'{val}' uses a browser default curve.")
        elif m.group(1) == "transition" and not m.group(2) and "cubic-bezier" not in val and "var(" not in val:
            rep.warn("easing", path, text, m.start(), f"'{val}' has no timing function, so it falls back to 'ease'.")
        for num, unit in re.findall(r"(\d*\.?\d+)(ms|s)\b", val):
            ms = float(num) * (1000 if unit == "s" else 1)
            if 0 < ms < 200:
                rep.error("duration", path, text, m.start(), f"Duration {ms:g}ms is shorter than 200ms.")
        if m.group(1) == "transition" and re.search(r"(?<![\w-])(top|left|right|bottom|width|height)(?![\w-])", val):
            rep.error("animated-layout", path, text, m.start(), "Transitions animate only transform and opacity.")
        if m.group(1) == "transition" and re.match(r"all\b", val):
            rep.warn("animated-layout", path, text, m.start(), "'transition: all' can animate layout properties. Name transform and opacity.")
    for m in re.finditer(r"@keyframes[^{]*\{((?:[^{}]*\{[^{}]*\})*)[^{}]*\}", text):
        if re.search(r"(?<![\w-])(top|left|right|bottom|width|height)\s*:", m.group(1)):
            rep.error("animated-layout", path, text, m.start(), "Keyframes animate a layout property.")
    if any(t[0].startswith(("transition", "animate-", "duration-")) for t in class_tokens(text)):
        has_motion = True
    if has_motion and not re.search(r"prefers-reduced-motion|motion-reduce:|motion-safe:|useReducedMotion", text):
        rep.error("reduced-motion", path, text, None, "Motion present but prefers-reduced-motion is not handled.")
    for m in re.finditer(r"addEventListener\(\s*[\"']scroll[\"']", text):
        if "requestAnimationFrame" not in text:
            rep.error("scroll-listener", path, text, m.start(), "Unthrottled scroll listener. Use IntersectionObserver or rAF.")


def check_behaviour(path, text, ctx, rep):
    for m in re.finditer(r"material[-+_ ]icons|material[-+_ ]symbols|@mui/icons-material|@material-symbols", text, re.I):
        rep.error("icons", path, text, m.start(), "Material icons are not allowed. Use Phosphor, Solar, or Iconamoon.")
    for m in re.finditer(r"(?<![\w.])(window\.)?alert\s*\(", text):
        rep.error("alert", path, text, m.start(), "window.alert() is not allowed. Show errors inline.")
    for m in re.finditer(r"href\s*=\s*[\"'](#?)[\"']", text):
        rep.error("dead-link", path, text, m.start(), "Dead link (href=\"#\" or empty).")


def check_copy(path, text, suffix, ctx, rep):
    vis = visible_text(text, suffix)
    if not vis:
        return
    low = vis.lower()
    for w in BANNED_WORDS_EN:
        if w in low:
            rep.error("banned-word", path, text, text.lower().find(w), f"Banned filler '{w}'.")
    for w in BANNED_WORDS_KO:
        if w in vis:
            rep.error("banned-word", path, text, text.find(w), f"금지 표현 '{w}'.")
    for w in WEAK_CTA_EN:
        for m in re.finditer(r"<(?:button|a)\b[^>]*>\s*%s\s*<" % re.escape(w), text, re.I):
            rep.warn("weak-cta", path, text, m.start(), f"Weak CTA '{w}'. Use a verb plus what they get.")
    for w in WEAK_CTA_KO:
        for m in re.finditer(r"<(?:button|a)\b[^>]*>\s*%s\s*<" % re.escape(w), text):
            rep.warn("weak-cta", path, text, m.start(), f"약한 CTA '{w}'. 구체 행동과 받는 것을 쓰세요.")
    for m in re.finditer(r"[A-Za-z가-힣]-[A-Za-z가-힣]", vis):
        rep.warn("hyphen", path, text, text.find(m.group(0)), f"Hyphen in copy '{m.group(0)}'. Rewrite the phrase.")
        break
    if "!" in vis:
        rep.warn("exclamation", path, text, None, "Exclamation mark in copy.")


def check_document(path, text, ctx, rep):
    if not re.search(r"<html\b", text, re.I):
        return
    required = [
        ("meta-title", r"<title>\s*[^<\s]", "Missing <title>."),
        ("meta-description", r"<meta[^>]+name=[\"']description[\"']", "Missing meta description."),
        ("meta-og", r"<meta[^>]+property=[\"']og:image[\"']", "Missing og:image."),
        ("favicon", r"<link[^>]+rel=[\"'][^\"']*icon", "Missing favicon link."),
        ("skip-link", r"href=[\"']#(main|content)[\"']|skip", "Missing skip to content link."),
        ("semantic", r"<main\b", "Missing <main> landmark."),
    ]
    for rule, pat, msg in required:
        if not re.search(pat, text, re.I):
            rep.error(rule, path, text, None, msg)
    lang = re.search(r"<html[^>]*\blang=[\"']([\w-]+)", text, re.I)
    if not lang:
        rep.error("lang", path, text, None, "Missing lang attribute on <html>.")
    elif ctx["korean"] and not lang.group(1).lower().startswith("ko"):
        rep.error("lang", path, text, None, f"Korean page but lang=\"{lang.group(1)}\".")


def check_korean(path, text, suffix, ctx, rep, project_text):
    if not ctx["korean"]:
        return
    if suffix in {".html", ".htm", ".css", ".vue", ".svelte", ".astro"} or re.search(r"<html\b", text, re.I):
        if not re.search(r"word-break\s*:\s*keep-all|\bbreak-keep\b", project_text):
            rep.error("ko-keep-all", path, text, None, "Korean page without word-break: keep-all (or Tailwind break-keep).")
    if not re.search(r"<html\b", text, re.I):
        return
    if "개인정보처리방침" not in text:
        rep.error("ko-privacy", path, text, None, "Footer is missing a 개인정보처리방침 link.")
    if "이용약관" not in text:
        rep.warn("ko-terms", path, text, None, "Footer is missing an 이용약관 link.")
    if "사업자등록번호" not in text:
        rep.warn("ko-business-info", path, text, None, "Footer is missing 사업자 정보 (사업자등록번호 등).")
    if re.search(r"<form\b", text, re.I) and re.search(r"type=[\"'](email|tel)[\"']|name=[\"'](name|phone|email)", text, re.I):
        if not re.search(r"개인정보.{0,20}(수집|이용).{0,20}동의", text, re.S):
            rep.error("ko-consent", path, text, None, "Form collects personal data without a 개인정보 수집·이용 동의 checkbox.")
        for m in re.finditer(r"<input[^>]*type=[\"']checkbox[\"'][^>]*\bchecked\b", text, re.I):
            rep.warn("ko-consent", path, text, m.start(), "Consent checkboxes must be unchecked by default.")


def check_tokens(path, text, ctx, rep):
    tokens = ctx.get("tokens")
    if not tokens:
        return
    allowed = {norm_hex(spec["hex"]): name for name, spec in tokens.get("core_palette", {}).items()}
    retired = {norm_hex(k): v for k, v in tokens.get("forbidden_hex", {}).items()}
    gated = {}
    for group in ("restricted", "exceptions"):
        for name, spec in tokens.get(group, {}).items():
            gated[norm_hex(spec["hex"])] = name
    indigo = next((h for h, n in allowed.items() if "INDIGO" in n), None)
    for m in re.finditer(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", text):
        hx = norm_hex(m.group(0))
        if hx in allowed:
            continue
        if hx in retired:
            rep.error("palette", path, text, m.start(), f"{m.group(0)} is retired: {retired[hx]}.")
        elif hx in gated:
            rep.error("palette", path, text, m.start(), f"{m.group(0)} ({gated[hx]}) is not allowed on landing pages.")
        else:
            rep.error("palette", path, text, m.start(), f"{m.group(0)} is not a token in the palette.")
    if indigo:
        for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", text):
            sel, body = m.group(1).lower(), m.group(2).lower()
            if indigo not in {norm_hex(h) for h in re.findall(r"#[0-9a-f]{3,6}\b", body)}:
                continue
            if re.search(r"\bh[1-6]\b", sel) and re.search(r"(?<![\w-])color\s*:\s*" + indigo, body):
                rep.error("indigo-misuse", path, text, m.start(), "Indigo on a heading. Indigo is for numbers, status, and cover planes.")
            if re.search(r"button|\.btn|\.cta", sel) and re.search(r"background(-color)?\s*:\s*" + indigo, body):
                rep.error("indigo-misuse", path, text, m.start(), "Filled indigo button. CTAs are CARBON_BLACK.")


# ── Driver ───────────────────────────────────────────────────────────────────

def collect(paths):
    files = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files += [f for f in sorted(p.rglob("*")) if f.suffix in SOURCE_SUFFIXES
                      and "node_modules" not in f.parts and ".next" not in f.parts and "dist" not in f.parts]
        elif p.is_file():
            files.append(p)
        else:
            print(f"not found: {p}", file=sys.stderr)
            sys.exit(2)
    return files


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--lang", choices=["auto", "ko", "en"], default="auto")
    ap.add_argument("--theme", choices=["base", "tbnc"], default="base")
    ap.add_argument("--tokens", help="Brand tokens JSON (core_palette / restricted / exceptions / forbidden_hex).")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    files = collect(args.paths)
    texts = {f: f.read_text(encoding="utf-8", errors="replace") for f in files}
    project_text = "\n".join(texts.values())
    korean = args.lang == "ko" or (args.lang == "auto" and len(HANGUL_RE.findall(project_text)) >= 20)
    tokens = None
    if args.tokens:
        tokens = json.loads(Path(args.tokens).read_text(encoding="utf-8"))
    elif args.theme == "tbnc":
        print("note: --theme tbnc without --tokens skips the palette check.", file=sys.stderr)
    ctx = {"korean": korean, "theme": args.theme, "tokens": tokens}

    rep = Report()
    for f, text in texts.items():
        suffix = f.suffix.lower()
        check_fonts(f, text, ctx, rep)
        check_classes(f, text, ctx, rep)
        check_css(f, text, ctx, rep)
        check_motion(f, text, ctx, rep)
        check_behaviour(f, text, ctx, rep)
        check_copy(f, text, suffix, ctx, rep)
        check_document(f, text, ctx, rep)
        check_korean(f, text, suffix, ctx, rep, project_text)
        check_tokens(f, text, ctx, rep)

    errors = [i for i in rep.items if i["level"] == "error"]
    if args.json:
        print(json.dumps({"korean": korean, "theme": args.theme, "items": rep.items}, ensure_ascii=False, indent=2))
    else:
        for i in sorted(rep.items, key=lambda i: (i["file"], i["line"] or 0)):
            loc = f"{i['file']}:{i['line']}" if i["line"] else i["file"]
            print(f"{i['level']:5} {i['rule']:18} {loc}  {i['message']}")
        print(f"\n{len(errors)} error(s), {len(rep.items) - len(errors)} warning(s) "
              f"· locale={'ko' if korean else 'en'} · theme={args.theme}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
