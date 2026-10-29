# AI Design Skills · TheBear

A growing collection of design skills for AI coding tools — Claude Code, Cursor, Codex, Windsurf, and anything else that reads a markdown rules file.

Each skill is a self-contained folder. Install the ones you need.

Maintained by [더베어앤컴퍼니 (TheBear & Company)](https://github.com/drivethatbear-beep). Forked from [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) and developed independently here.

---

## Skills

| Skill | What it does |
|---|---|
| [`landing-page-design`](./skills/landing-page-design/SKILL.md) | Builds a landing page from scratch — intake questions, page structure, conversion copy, plus a full visual system (type, spacing, radius, motion). Korean locale rules, seven design system themes, and a rule checker included |

### What this fork adds

| Addition | Where |
|---|---|
| **Korean locale** — Pretendard, `keep-all` line breaking, Korean type scale, 한국어 카피 rules, Korean footer and consent requirements | [`references/korean.md`](./skills/landing-page-design/references/korean.md) |
| **Design system themes** — pick one and its official values replace the base visual system | [`themes/`](./skills/landing-page-design/themes/) |
| **Rule checker** — flags off-scale values, banned fonts, default easing, missing meta, Korean legal gaps | [`scripts/lint_page.py`](./skills/landing-page-design/scripts/lint_page.py) |

| Theme | Use for |
|---|---|
| [TBNC](./skills/landing-page-design/themes/tbnc.md) | 더베어앤컴퍼니's own pages only |
| [shadcn/ui](./skills/landing-page-design/themes/shadcn.md) | Projects built on shadcn/ui |
| [Park UI](./skills/landing-page-design/themes/park-ui.md) | Panda CSS / Ark UI projects |
| [Toss TDS](./skills/landing-page-design/themes/toss.md) | 앱인토스 mini apps, or on request |
| [Wanted Montage](./skills/landing-page-design/themes/wanted.md) | On request |
| [Material 3](./skills/landing-page-design/themes/material3.md) | Android adjacent products, or on request |
| [Apple HIG](./skills/landing-page-design/themes/apple-hig.md) | Apple platform product pages, or on request |

Themes describe each system's public tokens for building compatible UI. They never license a company's logo, brand fonts outside their terms, or a look that impersonates that company.

### Check a page

```bash
python skills/landing-page-design/scripts/lint_page.py path/to/page.html --lang ko
```

Exit code 1 means errors. Python 3.9+, standard library only. Run the checker's own tests with `python -m unittest discover -s tests`.

More on the way. [Upgrading an existing site instead of building new?](https://github.com/elayadesign/redesign-skill) That one lives in its own repo since it predates this collection.

---

## Install

Pick a skill from the table above, then swap `<skill-name>` below for its folder name.

<details open>
<summary><b>Claude Code</b></summary>

```bash
mkdir -p .claude/skills
git clone https://github.com/drivethatbear-beep/ai-design-skills-thebear.git /tmp/ai-design-skills-thebear
cp -r /tmp/ai-design-skills-thebear/skills/<skill-name> .claude/skills/
```

Then just ask, in plain language, for what that skill covers.

**Windows, kept in sync with a local clone** (edits in the clone apply immediately):

```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\<skill-name>" -Target "<clone>\skills\<skill-name>"
```
</details>

<details>
<summary><b>Cursor</b></summary>

```bash
mkdir -p .cursor/rules
curl -o .cursor/rules/<skill-name>.md \
  https://raw.githubusercontent.com/drivethatbear-beep/ai-design-skills-thebear/main/skills/<skill-name>/SKILL.md
```

Or paste the file into **Settings → Rules for AI**.
</details>

<details>
<summary><b>Codex / Windsurf / other</b></summary>

Copy the skill's `SKILL.md` into whatever your tool uses for project rules:

| Tool | Path |
|---|---|
| Codex | `AGENTS.md` |
| Windsurf | `.windsurfrules` |
| Cline | `.clinerules` |
| Generic | paste into your system prompt |
</details>

<details>
<summary><b>Claude.ai (no terminal)</b></summary>

Download the skill's `SKILL.md` and upload it to a Project, or attach it to a chat and say *"follow this."*
</details>

---

## Make it yours

Add your own brand as a theme: copy [`themes/tbnc.md`](./skills/landing-page-design/themes/tbnc.md), replace the tokens and overrides, and add a row to the theme table in `SKILL.md`. The base rules stay untouched, so every theme inherits the same structure, states, and ship requirements.

---

## Credits

This repository started as a fork of [elayadesign/ai-design-skills](https://github.com/elayadesign/ai-design-skills) by Elaya, MIT licensed.

`landing-page-design` adapts content realism and motion ideas from [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) by Leon Lin, MIT licensed. Details are at the end of [its SKILL.md](./skills/landing-page-design/SKILL.md#credits).

---

## License

MIT. Use it, fork it, ship it, sell what you build with it. Keep the [LICENSE](./LICENSE) notice when you redistribute the skill files themselves.
