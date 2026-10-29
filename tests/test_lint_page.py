"""Run with: python -m unittest discover -s tests"""

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINT = ROOT / "skills" / "landing-page-design" / "scripts" / "lint_page.py"
FIX = Path(__file__).resolve().parent / "fixtures"
TOKENS = FIX / "tokens_tbnc_sample.json"


def run(*args):
    proc = subprocess.run([sys.executable, str(LINT), *map(str, args), "--json"],
                          capture_output=True, text=True, encoding="utf-8")
    return proc.returncode, json.loads(proc.stdout)


class LintPageTest(unittest.TestCase):
    def test_good_korean_page_is_clean(self):
        code, out = run(FIX / "good_ko.html", "--theme", "tbnc", "--tokens", TOKENS)
        errors = [i for i in out["items"] if i["level"] == "error"]
        self.assertEqual(errors, [], errors)
        self.assertEqual(code, 0)
        self.assertTrue(out["korean"])

    def test_bad_korean_page_hits_every_rule(self):
        code, out = run(FIX / "bad_ko.html", "--theme", "tbnc", "--tokens", TOKENS)
        self.assertEqual(code, 1)
        rules = {i["rule"] for i in out["items"] if i["level"] == "error"}
        expected = {
            "font-banned", "italic", "type-arbitrary", "spacing-scale", "radius", "gradient-bg",
            "shadow", "red", "easing", "duration", "animated-layout", "reduced-motion",
            "scroll-listener", "icons", "alert", "dead-link", "banned-word", "meta-title",
            "lang", "ko-keep-all", "ko-privacy", "ko-consent", "palette", "indigo-misuse",
        }
        self.assertEqual(expected - rules, set())

    def test_base_theme_allows_clipped_text_gradient(self):
        code, out = run(FIX / "hero_gradient.css", "--lang", "en")
        self.assertNotIn("gradient-bg", {i["rule"] for i in out["items"]})


if __name__ == "__main__":
    unittest.main()
