# Material 3 theme

> Source: https://m3.material.io (styles/spacing, foundations/layout/breakpoints, styles/motion/overview) · https://github.com/material-components/material-web (`tokens/versions/latest/sass`, design system version 34.0.21) · https://github.com/material-foundation/material-color-utilities · https://github.com/google/fonts · https://github.com/google/material-design-icons · checked 2026-10-29 · License: material-web, material-color-utilities and Material Symbols are Apache 2.0. Roboto, Roboto Flex, Google Sans, Google Sans Flex and Google Sans Code are SIL OFL on Google Fonts. The Material Design guidelines are free to follow. Google trademarks and logos are not licensed.

## When to apply

Apply only when the user names Material, Material 3, M3, M3 Expressive or Material You, or when the project already uses `@material/web`, MUI with an M3 theme, Jetpack Compose Material 3, or `--md-sys-*` tokens. Otherwise keep the base rules from SKILL.md.

## Overrides of base rules

| Base rule (SKILL.md) | This theme |
|---|---|
| B1 fonts: Geist, Manrope, Geist Mono, Poppins; Roboto banned | Roboto is the default for both `--md-ref-typeface-brand` and `--md-ref-typeface-plain`. Roboto Flex, Google Sans or Google Sans Flex may replace it. The Roboto ban does not apply. |
| B1 Tailwind type scale | Use the M3 type scale below (rem values from tokens). Do not snap to Tailwind steps. |
| B1 weight cap (no 900) | Kept. M3 uses only 400, 500 and 700. |
| B1 button type 16px semibold | Button label = Label Large, 14px/20px, weight 500 (700 in the emphasized scale). |
| B2 spacing set | M3 spacing scale (8dp base, with nested 2, 4, 6, 10, 14dp units). |
| B2 button padding 8px/12px | Use component tokens: small button 40px tall with 16px leading and trailing space. |
| B3 Tailwind radius only | M3 shape scale: 0, 4, 8, 12, 16, 20, 28, 32, 48px and full. |
| B4 flat backgrounds | Kept. Use the surface and surface-container roles. M3 has no background gradients. |
| B4 dark backgrounds limited to six hex values | Use the M3 dark surface roles instead (e.g. `#141218`, `#211F26`). |
| B5 hero heading gradient text | Not part of M3. Use solid `on-surface` (or `primary`) text. |
| B6 icons: Material Symbols banned | Material Symbols is required. Phosphor, Solar and Iconamoon are not used. |
| B7 motion curve `cubic-bezier(0.22,1,0.36,1)` | M3 easing and duration tokens, or spring-to-curve conversions for Expressive. |

## Typography

Fonts: the material-web `md-ref-typeface` tokens set `brand: Roboto` and `plain: Roboto`, with weights 400 regular, 500 medium and 700 bold. Load all three weights. Roboto (wdth 75–100, wght 100–900), Roboto Flex, Google Sans (wght 400–700) and Google Sans Flex (wght 1–1000, wdth 25–151, opsz, slnt, ROND) are all OFL and served by `fonts.googleapis.com`. Display, headline and title-large use the brand face. The other roles use the plain face.

| Role | Size | Line height | Tracking | Weight (emphasized) |
|---|---|---|---|---|
| Display Large | 57px (3.5625rem) | 64px | -0.25px | 400 (500) |
| Display Medium | 45px | 52px | 0 | 400 (500) |
| Display Small | 36px | 44px | 0 | 400 (500) |
| Headline Large | 32px | 40px | 0 | 400 (500) |
| Headline Medium | 28px | 36px | 0 | 400 (500) |
| Headline Small | 24px | 32px | 0 | 400 (500) |
| Title Large | 22px | 28px | 0 | 400 (500) |
| Title Medium | 16px | 24px | 0.15px | 500 (700) |
| Title Small | 14px | 20px | 0.1px | 500 (700) |
| Body Large | 16px | 24px | 0.5px | 400 (500) |
| Body Medium | 14px | 20px | 0.25px | 400 (500) |
| Body Small | 12px | 16px | 0.4px | 400 (500) |
| Label Large | 14px | 20px | 0.1px | 500 (700) |
| Label Medium | 12px | 16px | 0.5px | 500 (700) |
| Label Small | 11px | 16px | 0.5px | 500 (700) |

The emphasized scale (`md-sys-typescale-emphasized`, M3 Expressive) keeps the same sizes and raises the weights. CSS classes ship as `md-typescale-<role>-<size>` in `@material/web/typography/md-typescale-styles.js`. On a landing page the hero is Display Large or Display Medium. Base copy rules (no italics, `text-wrap: balance` and `pretty`, no hyphens) still apply.

## Color tokens

Roles are generated from one source color with material-color-utilities (HCT tonal palettes). CSS variables follow `--md-sys-color-<role>`. Below is the material-web baseline scheme (source `#6750A4`), resolved from `md-ref-palette`.

| Role | Light | Dark |
|---|---|---|
| primary / on-primary | `#6750A4` / `#FFFFFF` | `#D0BCFF` / `#381E72` |
| primary-container / on-primary-container | `#EADDFF` / `#4F378B` | `#4F378B` / `#EADDFF` |
| secondary / on-secondary | `#625B71` / `#FFFFFF` | `#CCC2DC` / `#332D41` |
| secondary-container / on-secondary-container | `#E8DEF8` / `#4A4458` | `#4A4458` / `#E8DEF8` |
| tertiary / on-tertiary | `#7D5260` / `#FFFFFF` | `#EFB8C8` / `#492532` |
| tertiary-container / on-tertiary-container | `#FFD8E4` / `#633B48` | `#633B48` / `#FFD8E4` |
| error / on-error | `#B3261E` / `#FFFFFF` | `#F2B8B5` / `#601410` |
| error-container / on-error-container | `#F9DEDC` / `#8C1D18` | `#8C1D18` / `#F9DEDC` |
| surface = background / on-surface | `#FEF7FF` / `#1D1B20` | `#141218` / `#E6E0E9` |
| on-surface-variant | `#49454F` | `#CAC4D0` |
| surface-dim / surface-bright | `#DED8E1` / `#FEF7FF` | `#141218` / `#3B383E` |
| surface-container-lowest | `#FFFFFF` | `#0F0D13` |
| surface-container-low | `#F7F2FA` | `#1D1B20` |
| surface-container | `#F3EDF7` | `#211F26` |
| surface-container-high | `#ECE6F0` | `#2B2930` |
| surface-container-highest | `#E6E0E9` | `#36343B` |
| outline / outline-variant | `#79747E` / `#CAC4D0` | `#938F99` / `#49454F` |
| inverse-surface / inverse-on-surface / inverse-primary | `#322F35` / `#F5EFF7` / `#D0BCFF` | `#E6E0E9` / `#322F35` / `#6750A4` |
| scrim, shadow | `#000000` | `#000000` |

Fixed roles (`primary-fixed` `#EADDFF`, `primary-fixed-dim` `#D0BCFF`, and so on) are the same in both modes. Medium-contrast and high-contrast schemes also exist as token files. For a brand, generate a scheme from the brand color. Do not hand-edit tones.

State layers (opacity of the content color over the container): hover 0.08, focus 0.10, pressed 0.10, dragged 0.16, disabled content 0.38.

## Spacing and layout

- The spacing scale is 8dp based (`md.sys.measurement.space100` = 8dp). Tokens: 0, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 32, 36, 40, 48, 56, 64, 72dp (Space 0 through Space 900). M3 says these system tokens are implemented only in Jetpack Compose. On the web, use them as plain px values.
- Breakpoints: compact <600, medium 600–839, expanded 840–1199, large 1200–1599, extra-large ≥1600dp.
- Window margins: compact 16dp. Medium, expanded, large and extra-large 24dp. The spacer between panes is 24dp.
- Fixed pane width: 360dp in expanded, 412dp in large and extra-large.
- Prefer padding and gaps on the parent over margins on children.

## Radius

`md.sys.shape.corner.*`: none 0, extra-small 4px, small 8px, medium 12px, large 16px, large-increased 20px, extra-large 28px, extra-large-increased 32px, extra-extra-large 48px, full 9999px. The increased and extra-extra-large steps came with M3 Expressive. Partial variants exist (e.g. `extra-large-top` = 28px 28px 0 0). The base nested-radius formula may still be applied using these steps.

## Elevation

Levels 0–5 = 0, 1, 3, 6, 8, 12dp (`md.sys.elevation.level0..5`). M3 expresses elevation mainly through surface-container color steps. Shadows are reserved for elevated components (elevated card = level1; filled button hover = level1). The exact shadow CSS is generated by material-web's elevation component and is not published as a token value (미확인 as raw CSS).

## Motion

The M3 Expressive motion physics system (May 2025) uses springs (stiffness, damping) and replaces easing plus duration for most motion. Each scheme (expressive or standard) has fast, default and slow speeds, split into spatial springs (position, size, rotation, corners, with overshoot) and effects springs (color, opacity, no overshoot). The web has no spring tokens, so use M3's official spring-to-curve table:

| Spring | cubic-bezier | Duration |
|---|---|---|
| Expressive fast / default / slow spatial | (0.42,1.67,0.21,0.90) / (0.38,1.21,0.22,1.00) / (0.39,1.29,0.35,0.98) | 350 / 500 / 650ms |
| Standard fast / default / slow spatial | (0.27,1.06,0.18,1.00) | 350 / 500 / 750ms |
| Fast / default / slow effects (both schemes) | (0.31,0.94,0.34,1.00) / (0.34,0.80,0.34,1.00) / (0.34,0.88,0.34,1.00) | 150 / 200 / 300ms |

Standard scheme spring tokens: spatial damping 0.9 with stiffness 1400 / 700 / 300 (fast, default, slow). Effects damping 1 with stiffness 3800 / 1600 / 800. Expressive scheme stiffness and damping values: 미확인.

Legacy easing tokens (still valid fallbacks, used for transitions): standard `cubic-bezier(0.2,0,0,1)`, standard-decelerate `(0,0,0,1)`, standard-accelerate `(0.3,0,1,1)`, emphasized-decelerate `(0.05,0.7,0.1,1)`, emphasized-accelerate `(0.3,0,0.8,0.15)`. In web tokens, emphasized falls back to standard because a CSS path is unsupported. Legacy `(0.4,0,0.2,1)`, `(0,0,0.2,1)` and `(0.4,0,1,1)`. Durations: short1–4 = 50/100/150/200ms, medium1–4 = 250/300/350/400ms, long1–4 = 450/500/550/600ms, extra-long1–4 = 700/800/900/1000ms. Base rules kept: animate transform and opacity only, and honor `prefers-reduced-motion`.

## Icons

Material Symbols (Apache 2.0), a variable font in Outlined, Rounded and Sharp. Axes: FILL 0–100, wght 100–700 (400 default), GRAD -50 to 200, opsz 20–48 (24 default). Use Outlined at 24px by default, FILL 1 for selected states, and GRAD -50 for light-on-dark. Material Icons is the legacy set and is no longer updated. Do not use it in new work.

## Components

- Button (common sizes): xsmall 32px tall with 12px side space. Small (the default `md-filled-button`) 40px tall with 16px side space, 20px icon and 8px icon-label gap. Medium 56px tall with 24px side space and 24px icon. Shape `corner-full` (round) or a square variant (small: medium 12px, medium: large 16px). The filled button uses `primary` / `on-primary`, elevation level0, level1 on hover, and Label Large type.
- Text field (outlined): 56px tall, `corner-extra-small` 4px, 1px `outline`, 3px `primary` on focus, `error` outline on error. Input text is Body Large and the floating label is Body Small.
- Card: radius `corner-medium` 12px. Elevated = `surface-container-low` + level1. Filled = `surface-container-highest` + level0. Outlined = `surface` + 1px `outline-variant`.

## Install

```html
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet">
```

- Components: `npm i @material/web` (v2.5.0 on npm). The material-web README says it is in maintenance mode pending new maintainers, so pin the exact version.
- Color: `npm i @material/material-color-utilities` (v0.4.0), then `themeFromSourceColor(argbFromHex('#...'))` and `applyTheme(...)`, or export CSS from Material Theme Builder (https://material-foundation.github.io/material-theme-builder/ or the Figma plugin).
- Tailwind or plain CSS: map the `--md-sys-color-*`, `--md-sys-shape-*` and type tokens into CSS variables. Do not mix them with the base Tailwind radius and spacing scales.

## Limits

- Never use Google logos, the Google "G", product icons, Google brand colors or Google product names in a way that suggests a client site is a Google product. Material is a design system, not a brand license.
- Google Sans being OFL on Google Fonts does not make Google's brand identity free to use. Prefer Roboto or Roboto Flex for client brands.
- Expressive shape library (morphing shapes) and component-level Expressive specs were not read here and are not reflected.
- 미확인: Expressive spring stiffness and damping values. Raw elevation shadow CSS. Exact compact-to-medium Expressive component padding beyond the token files listed.
