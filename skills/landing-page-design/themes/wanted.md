# Wanted Montage theme

> Source: https://montage.wanted.co.kr (Foundations, Terms of use) · https://github.com/wanteddev/montage-web (`packages/theme`, `packages/core`, v4.1.5) · https://github.com/wanteddev/wanted-sans · Figma UI Kit https://www.figma.com/community/file/1355516515676178246 · checked 2026-10-29 · License: Montage code MIT (Copyright 2026 Wanted Lab, Inc.); Wanted Sans and Pretendard SIL OFL 1.1; Wanted logo, wordmark and brand assets follow separate brand guidelines and may not be used to impersonate Wanted.

## When to apply

Apply only when the user names Wanted, 원티드, Montage or 몽타주 / Wanted Design System, or the project already depends on `@montage-ui/*`. Otherwise keep the base rules. Montage is free for commercial use under MIT, so it can style a non-Wanted product, but the result must carry its own brand (see Limits).

## Overrides of base rules

| Base rule (SKILL.md) | This theme |
|---|---|
| Fonts: Geist, Manrope, Geist Mono, Poppins | Pretendard JP (Korean, Latin, Japanese), loaded with Pretendard; Montage docs and `@montage-ui/core` README require it |
| Tailwind type scale | Montage scale below (Display 1 to Caption 2), including 11, 13, 15, 17, 22, 28px steps |
| Weight cap semibold or bold | Regular 400, Medium 500, Bold 700 (Display, Title) or Bold 600 (Heading and below) |
| Spacing set 0 to 96px | Montage spacing tokens 0 to 80px (adds 6, 10, 14, 20, 56, 72) |
| Tailwind radius only | Montage radius tokens 0, 4, 8, 10, 12, 14, 16, 20, 24, 28, 32, full |
| Main button 8px / 12px padding, `text-base` | Button large: min height 48px, padding 13px 20px, Body 2 bold (15px) |
| Dark backgrounds `#000000`, `#181818`... | Montage dark semantic tokens (`#1B1C1E`, `#0F0F10`, `#212225`) |
| Base motion curve, 500ms | Component transitions use 0.15s to 0.2s `ease` inside Montage components; no motion token exists, so page level reveals keep the base curve |
| Icons: Phosphor, Solar, Iconamoon | `@montage-ui/icon` (24 × 24 viewBox, sized by `1em`) |
| Hero heading gradient text | Not part of Montage; use `foreground.neutral.strong` solid text |

Base rules this theme does not touch: no background gradients, no italic, no hyphens in copy, no orphan words, animate only `transform` and `opacity`, reduced motion support.

## Typography

Font family: `"Pretendard JP", "Pretendard", system-ui, sans-serif`. Wanted Sans is Wanted's own OFL typeface (7 weights plus variable, Hangul and Latin; `Wanted Sans Std` is Latin only). Montage docs list only Pretendard JP, so use Wanted Sans only when the user asks for it, and then as the single typeface.

| Token (variant) | Size | Line height | Letter spacing | Bold weight |
|---|---|---|---|---|
| Display 1 (`display1`) | 56px | 72px | -0.0319em | 700 |
| Display 2 | 40px | 52px | -0.0282em | 700 |
| Display 3 | 36px | 48px | -0.027em | 700 |
| Title 1 | 32px | 44px | -0.0253em | 700 |
| Title 2 | 28px | 38px | -0.0236em | 700 |
| Title 3 | 24px | 32px | -0.023em | 700 |
| Heading 1 | 22px | 30px | -0.0194em | 600 |
| Heading 2 | 20px | 28px | -0.012em | 600 |
| Headline 1 | 18px | 26px | -0.002em | 600 |
| Headline 2 | 17px | 24px | 0em | 600 |
| Body 1 / Body 1 Reading | 16px | 24px / 26px | 0.0057em | 600 |
| Body 2 / Body 2 Reading | 15px | 22px / 24px | 0.0096em | 600 |
| Label 1 / Label 1 Reading | 14px | 20px / 22px | 0.0145em | 600 |
| Label 2 | 13px | 18px | 0.0194em | 600 |
| Caption 1 | 12px | 16px | 0.0252em | 600 |
| Caption 2 | 11px | 14px | 0.0311em | 600 |

Every style also has Regular 400 and Medium 500. "Reading" variants are for long paragraphs. Public variant names are kebab case (`body1-reading`). CSS variables follow `--typography-<key>-<prop>`.

Landing page mapping: hero heading Display 1 (desktop) / Title 1 (mobile), section heading Title 2 or Title 3, lead copy Body 1 Reading, buttons per Components.

## Color tokens

Atomic primary: `blue50 #0066FF` (45 `#005EEB`, 40 `#0054D1`, 55 `#1A75FF`, 60 `#3385FF`, 95 `#EAF2FE`). Neutrals use `coolNeutral` (5 `#0F0F10` to 99 `#F7F7F8`). Red 50 `#FF4242`, green 50 `#00BF40`, orange 50 `#FF9200`. Alpha values below are `#RRGGBB` + percent (hex8 in parentheses). CSS variables: `--semantic-<group>-<role>-<step>`, for example `--semantic-foreground-neutral-primary`, `--atomic-blue-50`.

| Semantic token | Light | Dark |
|---|---|---|
| `foreground.neutral.primary` | `#171719` | `#F7F7F8` |
| `foreground.neutral.strong` | `#000000` | `#FFFFFF` |
| `foreground.neutral.secondary` | `#2E2F33` 88% (`#2E2F33E0`) | `#C2C4C8` 88% (`#C2C4C8E0`) |
| `foreground.neutral.tertiary` | `#37383C` 61% (`#37383C9C`) | `#AEB0B6` 61% (`#AEB0B69C`) |
| `foreground.neutral.quaternary` | `#37383C` 28% (`#37383C47`) | `#AEB0B6` 28% (`#AEB0B647`) |
| `foreground.brand.primary` | `#0066FF` | `#3385FF` |
| `foreground.positive / cautionary / negative.primary` | `#00BF40` / `#FF9200` / `#FF4242` | `#1ED45A` / `#FFA938` / `#FF6363` |
| `foreground.disable.primary` | `#37383C` 16% | `#989BA2` 16% |
| `background.neutral.primary` | `#FFFFFF` | `#1B1C1E` |
| `background.neutral.secondary` | `#F7F7F8` | `#0F0F10` |
| `surface.neutral.primary` | `#FFFFFF` | `#1B1C1E` |
| `surface.neutral.secondary` | `#70737C` 8% (`#70737C14`) | `#70737C` 22% (`#70737C38`) |
| `surface.neutral.tertiary` | `#70737C` 5% | `#70737C` 12% |
| `surface.elevated.primary` | `#FFFFFF` | `#212225` |
| `surface.elevated.secondary` | `#F7F7F8` | `#141415` |
| `surface.brand.primary / strong / heavy` | `#0066FF` / `#005EEB` / `#0054D1` | `#3385FF` / `#1A75FF` / `#0066FF` |
| `surface.brand.subtle` | `#0066FF` 5% | `#3385FF` 5% |
| `surface.disable.primary` | `#F4F4F5` | `#2E2F33` |
| `line.neutral.primary` (opaque) | `#70737C` 22% (`#E1E2E4`) | `#70737C` 32% (`#37383C`) |
| `line.neutral.secondary` (opaque) | `#70737C` 16% (`#EAEBEC`) | `#70737C` 28% (`#333438`) |
| `line.neutral.tertiary` (opaque) | `#70737C` 8% (`#F4F4F5`) | `#70737C` 22% (`#2E2F33`) |
| `line.brand.strong / focus` | `#0066FF` 43% / 12% | `#3385FF` 43% / 12% |
| `effect.dimmer.primary` | `#171719` 52% | `#171719` 74% |
| `static.white / black` | `#FFFFFF` / `#000000` | same |

Accent families (lime, cyan, lightBlue, violet, purple, pink) exist for foreground, surface and line; read them from `@montage-ui/theme` instead of guessing.

## Spacing and layout

Spacing tokens: 0, 0.5px, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 32, 40, 48, 56, 64, 72, 80 (px), as `--spacing-<n>`. Grid guidance: multiples of 4px, 2px only for optical correction, 1px only when unavoidable.

Breakpoints: xs 0, sm 768px, md 992px, lg 1200px, xl 1600px. Max content width 1100px at lg and 1440px at xl (padding included). Columns: mobile 2 with 20px gutter, tablet 3, desktop 12, 20px gap. Reference artboards: web desktop 1440 × 960, web mobile 375 × 635.

## Radius

Tokens: 0, 4, 8, 10, 12, 14, 16, 20, 24, 28, 32px, `full` 9999px (`--radius-<n>`). Thumbnails and card images use 12px. Keep the base nested radius formula (inner = outer minus gap) using these steps.

## Elevation

Shadow tokens are identical in light and dark; color is `neutral10 #171717` with alpha.

| Token | Value |
|---|---|
| `shadow.normal.xsmall` | `0 1px 2px -1px` 10% |
| `shadow.normal.small` | `0 2px 4px -2px` 6%, `0 4px 6px -1px` 6% |
| `shadow.normal.medium` | `0 4px 6px -2px` 7%, `0 10px 15px -3px` 7% |
| `shadow.normal.large` | `0 6px 10px -4px` 8%, `0 16px 24px -6px` 8% |
| `shadow.normal.xlarge` | `0 10px 15px -5px` 10%, `0 24px 38px -10px` 12% |
| `shadow.spread.small / medium` | `0 0 60px 0` 10% / `0 15px 75px 0` 16% |

`shadow.drop.*` provides matching `filter: drop-shadow()` values for icons and cutouts. Floating navigation (iOS platform token): `surface.elevated.primary` at 88% with `backdrop-filter: blur(32px)`.

## Motion

`@montage-ui/theme` 4.1.5 ships no duration or easing tokens. Observed in component source: interaction overlay `opacity` and `transform` 0.15s ease; text field focus `box-shadow` 0.2s ease; card thumbnail image `transform` 0.2s ease. Interaction overlay opacity: hover 5% (light 3.75%, strong 7.5%), active 12% (light 9%, strong 18%), optional scale 0.95 to 1. Lottie animations ship in `@montage-ui/lottie`. For section reveals and navigation, keep the base curve and durations.

## Icons

Use `@montage-ui/icon` (React components such as `IconArrowLeft`, 24 × 24 viewBox, `width="1em"`, so size follows `font-size`). Docs describe the style as basic, simple and modern, with keyword search on the site. Button icon sizes: 20px (large), 18px (medium), 16px (small), 14px (xsmall). Icon grid and stroke width: 미확인.

## Components

**Button** (`variant` solid | outlined, `color` primary | assistive | negative):

| Size | Min height | Padding | Radius | Text |
|---|---|---|---|---|
| large | 48px | 13px 20px | 14px | Body 2 bold |
| medium | 40px | 10px 16px | 12px | Label 1 bold |
| small | 32px | 8px 12px | 10px | Caption 1 bold |
| xsmall | 28px | 6px 10px | 8px | Caption 1 bold |

Solid primary: `surface.brand.primary` fill, white text. Solid assistive: `surface.neutral.secondary` fill, `foreground.neutral.secondary` text, `blur(32px)`. Outlined: transparent fill, `inset 0 0 0 1px line.neutral.secondary`. Disabled: `surface.disable.primary` fill, `foreground.disable.primary` text.

**Text field**: large radius 14px, padding 12px 8px, Body 2 regular; medium radius 12px, padding 10px 6px, Label 1 regular. Border `inset 0 0 0 1px line.neutral.secondary`; focus `inset 0 0 0 1px line.brand.strong` plus `0 0 0 4px line.brand.focus`; error uses the negative line tokens.

**Card**: thumbnail radius 12px, ratio 3:2 desktop and 4:3 mobile; title Body 1 bold, caption Label 2 medium; gap 8px desktop, 6px mobile. No card shadow by default (shadow values above are opt in).

## Install

```sh
pnpm i @montage-ui/core @montage-ui/icon   # same version for every @montage-ui/* package
pnpm i @montage-ui/nextjs                  # Next.js App or Pages Router
```

Import `@montage-ui/core/global.css`, wrap the app in `ThemeProvider`, and load Pretendard JP and Pretendard from `cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/` (`pretendard-jp-dynamic-subset.min.css`, `pretendard-dynamic-subset.min.css`). Peer deps: React 18 or 19; styling is powered by Emotion via `@montage-ui/engine`. Tokens only: `@montage-ui/theme`. Native: `wanteddev/montage-ios`, `wanteddev/montage-android` (MIT). AI tooling: `@wanteddev/montage-mcp` in the same repo. Wanted Sans web font: `cdn.jsdelivr.net/gh/wanteddev/wanted-sans@v1.0.3/packages/wanted-sans/fonts/webfonts/variable/split/WantedSansVariable.min.css` (`font-family: "Wanted Sans Variable"`).

## Limits

- License: MIT code allows commercial use, modification and redistribution; keep the copyright notice and license text. Wanted recommends (does not require) stating that the product uses the Wanted Design System.
- Brand: never use the Wanted logo, wordmark, `@montage-ui/brand` assets, or Wanted product copy on a non-Wanted page, and never build a page that could be mistaken for Wanted or a Wanted service. Montage styling on your own brand is fine; impersonation is prohibited by the terms of use. Phishing, fraud and data theft uses are explicitly banned.
- Version drift: values come from `@montage-ui/*` 4.1.5 source. Older Figma files and posts use earlier token names (for example `label.*`); prefer the current package names.
- 미확인: motion duration and easing tokens; icon grid, stroke width and icon count guidance; dark mode switching mechanism (attribute or class name) in `ThemeProvider`; whether Wanted Sans is an official Montage UI font; page margins per breakpoint.
