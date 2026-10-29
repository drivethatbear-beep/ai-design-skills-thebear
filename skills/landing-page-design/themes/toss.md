# Toss TDS theme

> Source: https://tossmini-docs.toss.im/tds-mobile/ (Foundation: colors, typography; Components: Button) · https://developers-apps-in-toss.toss.im/design/components · https://developers-apps-in-toss.toss.im/design/prepare/figma-ui-license · https://developers-apps-in-toss.toss.im/landing-page/landing-page-en/design/prepare/design · https://toss.im/tossfeed/article/beginning-of-tps · https://toss.tech/article/toss-design-system · https://github.com/toss/tossface · checked 2026-10-29 · License: proprietary. The TDS UI Kit license grants a limited right to use TDS only to build Apps in Toss (앱인토스) mini apps; use in other projects, commercial resale, modification and redistribution are prohibited. npm packages `@toss/tds-mobile`, `@toss/tds-colors` declare no open source license. Toss Product Sans is a Toss exclusive typeface (토스 전용 서체) and is not distributed.

## When to apply

Apply only when the user is building an Apps in Toss mini app (앱인토스, Toss WebView) or the project already depends on `@toss/tds-mobile`. TDS is not an open source package for general websites. If the user only says "make it feel like Toss" for their own site, keep the base rules, use Pretendard, and do not copy TDS assets or brand (see Limits). This file intentionally lists token names, not values.

## Overrides of base rules

| Base rule (SKILL.md) | This theme |
|---|---|
| Fonts: Geist, Manrope, Geist Mono, Poppins | Inside the Toss app: Toss Product Sans, applied automatically by the app and TDS components (do not load a font). Figma: SF Pro stands in. Outside Toss: Pretendard |
| Tailwind type scale | TDS Typography 1 to 7 plus sub Typography 1 to 13 (30px to 11px); use TDS tokens, never hard coded sizes, so iOS and Android "larger text" scaling works |
| Weight cap semibold or bold | Each token has Light, Regular, Medium, Semibold, Bold |
| Spacing set | 미확인 (TDS spacing tokens are not published); keep base spacing |
| Tailwind radius only | 미확인 (no published radius tokens); components own their radius |
| Main button 8px / 12px padding | TDS `Button` sizes small, medium, large, xlarge (default xlarge); pixel values 미확인 |
| Dark mode backgrounds | Apps in Toss: design for light mode only for now (official guide: dark mode "will be supported in the future") |
| Base motion curve | 미확인; TDS components ship their own motion, do not override |
| Icons: Phosphor, Solar, Iconamoon | TDS `Asset` / `IconButton` components inside mini apps; set contents 미확인 |
| Hero heading gradient text | Not a TDS pattern; use solid `colors.grey900` text |

## Typography

Font family: Toss Product Sans (Sandoll first version, 7 weights; Leedotype from the second version, adds Vietnamese). It cannot be downloaded or licensed for outside use; TDS components apply it inside the Toss app. For anything outside the Toss app use Pretendard (SIL OFL 1.1, `orioncactus/pretendard` v1.3.9).

TDS defines Typography 1 to 7 (30px down to 13px) plus sub Typography 1 to 13 between them. Use the TDS tokens from `@toss/tds-mobile`; the size and line height table lives in the official Foundation / Typography page. It is not reproduced here because the TDS license does not allow redistribution.

Accessibility: tokens scale with the OS "larger text" setting. iOS uses 9 steps from 100% (Large) to 310% (A11y_xxxLarge), each token with fixed values per step (Typography 1 reaches 42px at 275% and 310%). Android uses `base × NN × 0.01` with a per token maximum. Letter spacing: 미확인. Code level prop names for these tokens: 미확인 (check the component docs).

## Color tokens

Import the palette from the official package instead of hard coding hex values: `import { colors } from '@toss/tds-colors'`. Scales: grey, blue, red, orange, yellow, green, teal, purple (50 to 900), plus `greyOpacity50` to `900`. Semantic backgrounds: `background`, `greyBackground`, `layeredBackground`, `floatedBackground`. Values are in the official Foundation / Colors page and are not reproduced here because the TDS license does not allow redistribution.

Suggested roles (derived from the palette, not official semantic names): primary action `blue500`, primary text `grey900`, secondary text `grey700` or `grey600`, disabled text `grey400`, divider `grey200`, error `red500`.

Dark values: 미확인 (not published; Apps in Toss is light mode only for now).

## Spacing and layout

Spacing tokens, grid columns, page margins and breakpoints: 미확인 (not in the public TDS Mobile docs). TDS targets mobile WebView screens; `Button display="block"` stretches to screen width, `display="full"` fills the parent. Keep base spacing values when laying out custom sections.

## Radius

미확인. No radius tokens are published. Do not add custom radius to TDS components; for custom elements use the base Tailwind radius rules.

## Elevation

미확인. Background layers are expressed through `layeredBackground` and `floatedBackground` (both `#FFFFFF` in light). Shadow tokens are not published.

## Motion

미확인. Toss states that motion uses predefined values tuned for opacity, position, speed and acceleration, and that interactions and animations are part of TDS, but no durations, easings or spring parameters are public. Use the motion built into TDS components; for custom elements keep the base curve.

## Icons

Inside mini apps use the TDS `Asset` and `IconButton` components. Tossface (Toss emoji font, `github.com/toss/tossface`, Toss Face License) may be used and redistributed with its license text, but not sold as is or modified without permission. Icon set contents and sizes: 미확인.

## Components

- **Button** (`@toss/tds-mobile`): `size` small | medium | large | xlarge (default xlarge); `color` primary | danger | light | dark (default primary); `variant` fill (high saturation, primary action) | weak (lower saturation, semi transparent, secondary action); `display` inline | block | full; `loading` shows three sequential dots without changing button width. Heights, padding and radius: 미확인.
- **Input**: TDS lists `TextField` and `SearchField`; sizes and states: 미확인.
- **Card / lists**: TDS composes cards from `ListRow`, `ListHeader`, `Paragraph`, `Border`, `BottomCTA` rather than a single Card component. The 11 core components for Apps in Toss are Badge, Border, BottomCTA, Button, Asset, ListRow, ListHeader, Navigation, Paragraph, Tab, Top.

## Install

```sh
npm install @toss/tds-mobile @toss/tds-mobile-ait @emotion/react@^11 react@^18 react-dom@^18
yarn add @toss/tds-colors
```

Wrap the app root in `TDSMobileAITProvider` from `@toss/tds-mobile-ait`, then import components from `@toss/tds-mobile`. `@toss/tds-mobile-ait` peers on `@apps-in-toss/web-framework`, so it only works inside an Apps in Toss project. Current npm versions at check time: `@toss/tds-mobile` 2.5.1, `@toss/tds-colors` 0.1.0. Figma: download the TDS Mobile for Apps in Toss UI Kit `.fig` from the Apps in Toss design tools page and publish it as a library (no auto update; re download per release).

## Limits

- Licensing: the UI Kit and TDS may be used only to develop, design and prototype Apps in Toss services. Do not use TDS, its components, colors package or UI Kit in any other site, product or template, including this skill's general landing pages. Violation ends the license automatically.
- Font: Toss Product Sans is exclusive to Toss and cannot be shipped. Outside the Toss app always use Pretendard.
- Brand impersonation: never make a non-Toss page look like Toss or a Toss service. Do not use the Toss logo, the Toss name, Toss Product Sans, Tossface as a brand mark, or a full TDS look (`grey900` text on white with a `blue500` CTA and TDS layout patterns) for a page that could be mistaken for Toss, Toss Payments or Toss Bank. Pages in finance and payments carry phishing risk; refuse lookalike login, payment or transfer screens.
- 미확인: dark mode palette, spacing tokens, radius tokens, shadow tokens, motion durations and spring values, button and input pixel specs, typography letter spacing, code prop names for typography tokens, icon set contents.
