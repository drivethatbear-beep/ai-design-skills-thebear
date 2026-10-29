# TBNC theme (더베어앤컴퍼니)

> Source: TBNC house brand system v1, measured against https://thebear.co.kr · License: the brand identity belongs to TheBear & Company. The rules here are shared for TBNC's own pages only.

## When to apply

Only when the page is for TBNC itself. **Never apply these tokens to a client's page.** Copying one brand's system onto another brand is a failure, not a shortcut.

This theme implies [../references/korean.md](../references/korean.md).

The source of truth for token values is the TBNC brand team's token file (`tbnc-tokens.json`). If it disagrees with this page, that file wins; update it first, then this page.

## Overrides of base rules

| Base rule (SKILL.md) | This theme |
|---|---|
| B1 fonts: Geist, Manrope, Poppins | **Pretendard only.** Paperlogy is reserved for ad creative and card news, never landing pages |
| B1 weight cap 700 | Same, except the wordmark at 800 |
| B3 radius: Tailwind steps only | Button 10px, card 18 to 20px, chip 999px |
| B4 one sided borders banned | Quotes and testimonials take a 1px PALE_SILVER rule on the **left**. Cards stay all or nothing |
| B4 dark backgrounds | Light first. No dark mode unless the user asks, and then ask for the dark tokens instead of inventing them |
| B5 hero heading gradient | **No gradient.** Solid CARBON_750. On an indigo cover plane, BARELY_WHITE |
| B9 error states | **No red.** Errors are CARBON_BLACK text with a warning icon and a 1px CARBON_BLACK border. Negative numbers take a `△` prefix |
| B11 muted to full word reveal | Muted tone is CARBON_750 at 30% opacity, rising to full CARBON_750. Value, not a new grey |

## Typography

Pretendard, via the K1 stack in korean.md. Hero and section headings 600 to 700, body 400, the eyebrow 500. Use the K3 sizes.

## Color tokens

Do not extend this palette. A lighter grey for secondary text is a value decision inside these tokens, never a new hex.

| Token | Hex | Allowed use |
|---|---|---|
| MIDNIGHT_INDIGO | `#060daa` | Sequence numbers, status chips, and cover planes only. **Never headings, body text, or a filled button** |
| CARBON_BLACK | `#191817` | Body text and the CTA fill |
| CARBON_750 | `#52504d` | Headings, and the `TB` and `C` of the wordmark |
| ASH_GRAY | `#555555` | Secondary text |
| BARELY_WHITE | `#fcfaee` | Alternating section planes, and text on dark planes |
| PURE_WHITE | `#ffffff` | Base background |
| PALE_SILVER | `#e5e5e5` | 1px rules and borders |

**Emphasis comes from value, not hue.** When something must stand out, make it lighter or darker. Do not color it.

## Spacing and layout

Use B2 as written. Alternate PURE_WHITE and BARELY_WHITE planes between sections instead of drawing dividers. At most one MIDNIGHT_INDIGO cover plane per page, typically the hero or the final CTA.

## Radius

- Button: 10px (`rounded-[10px]`)
- Card: 20px (`rounded-[20px]`), or 18px for small cards
- Chip and badge: `rounded-full`

The B3 nested radius formula still applies.

## Elevation

None. No `box-shadow`, no `text-shadow`, no Tailwind `shadow-*`. Separate surfaces with planes and 1px PALE_SILVER borders.

## Motion

Use B7 as written.

## Icons

Use B6 as written, in CARBON_750 or ASH_GRAY. Indigo icons are allowed only as status markers.

## Components

- **Primary CTA.** CARBON_BLACK fill, PURE_WHITE text, 10px radius, B2 padding. On an indigo plane, invert it: BARELY_WHITE fill, CARBON_BLACK text.
- **Secondary.** 1px CARBON_BLACK border on transparent.
- **How it works.** Indigo lives in the numbered badge (`01`, `02`, `03`), never in the shape or the text. Connectors are straight horizontal or vertical lines, never diagonal or curved.
- **Eyebrow signature.** `── THE BEAR & COMPANY ──` at 12px, weight 500, +0.18em tracking, uppercase, with 24×1px rules and a 12px gap. Place it above the hero headline and the final CTA. It is the only ornament in the system.
- **Wordmark.** `TBNC` with the **N alone** in MIDNIGHT_INDIGO and the rest in CARBON_750 at weight 800. Use it in the nav and the footer.
- **Copy.** Narrative 존댓말 in 합니다체, addressed to 대표님.

## Install

No package. Set the tokens as CSS custom properties:

```css
:root {
  --tbnc-indigo: #060daa; --tbnc-carbon: #191817; --tbnc-carbon-750: #52504d;
  --tbnc-ash: #555555; --tbnc-barely-white: #fcfaee; --tbnc-white: #ffffff; --tbnc-silver: #e5e5e5;
}
```

Check the result with the token file:

```bash
python scripts/lint_page.py page.html --lang ko --theme tbnc --tokens <path>/tbnc-tokens.json
```

## Limits

- The checker cannot tell whether indigo is doing a numbering job or has crept into a heading or button. Look at the render.
- A `font-family` string proves nothing about what rasterized. Capture the page and look.
