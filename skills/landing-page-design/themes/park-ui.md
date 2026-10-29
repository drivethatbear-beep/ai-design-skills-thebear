# Park UI theme

> Source: https://park-ui.com/docs/installation · https://park-ui.com/docs/theming · https://github.com/chakra-ui/park-ui (moved from `cschroeter/park-ui`; `packages/preset/src/**`, `packages/cli/src/**`, `website/src/content/changelog/2025-11-21.mdx`) · https://www.radix-ui.com/colors · Panda defaults: https://panda-css.com/docs/customization/theme and `chakra-ui/panda` `preset-panda` / `preset-base` source · `@park-ui/cli` 1.0.1 · checked 2026-10-29 · License: MIT

## When to apply

Only when the user names Park UI, or the project already uses Panda CSS with Park UI recipes (a `@park-ui/cli` config, `@ark-ui/*`, recipes such as `button.ts` under the theme folder). Park UI needs Panda CSS; never bolt it onto a Tailwind page. The project's local recipe files win over the defaults below, because Park UI v1 copies them into the codebase.

## Overrides of base rules

| Base rule (SKILL.md) | This theme |
|---|---|
| B1 fonts | Park UI ships no font. Panda's `fonts.sans` is a system stack. Keep B1 (Geist etc.) unless the project sets its own |
| B1 type scale and line heights | Use Park `textStyle` tokens; their line heights differ from Tailwind (see Typography) |
| B1 button type | Buttons are `fontWeight: semibold`, `textStyle: sm` at size `md` |
| B2 spacing set; button padding 8/12 | Panda 4px steps with half steps. Button `md` is `h 40px, px 14px`; keep component sizing, use B2 for page layout |
| B3 Tailwind radius only | Use `l1` / `l2` / `l3` semantic radii (2 / 4 / 6px by default) |
| B4 dark backgrounds | Dark canvas is `gray.1` (`#111111` with neutral gray), not the B4 hex list |
| B6 icons | Default is Lucide (`lucide-react`). Allowed under this theme; the docs say it can be swapped, so Phosphor is fine |
| B7 motion | Component animations keep Park durations and Panda easings (`cubic-bezier(0.4, 0, 0.2, 1)`); collapse keyframes animate height and width. Page level motion still uses B7 |

## Typography

- Font: not defined by Park UI. Panda default `sans`: `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, …`; `mono`: `ui-monospace, SFMono-Regular, Menlo, …`. The park-ui.com demo font picker offers Inter, Outfit, Roboto Mono, Space Grotesk, DM Sans (demo only, not a default).
- Text styles (font size / line height):

| textStyle | Size | Line height |
|---|---|---|
| `xs` | 0.75rem | 1.125rem |
| `sm` / `label` | 0.875rem | 1.25rem (`label` adds medium weight) |
| `md` | 1rem | 1.5rem |
| `lg` | 1.125rem | 1.75rem |
| `xl` | 1.25rem | 1.875rem |
| `2xl` | 1.5rem | 2rem |
| `3xl` | 1.875rem | 2.375rem |
| `4xl` | 2.25rem | 2.75rem, letter spacing -0.02em |
| `5xl` | 3rem | 3.75rem, -0.02em |
| `6xl` | 3.75rem | 4.5rem, -0.02em |
| `7xl` | 4.5rem | 5.75rem, -0.02em |

## Color tokens

Built on **Radix Colors**: 12 steps per mode (24 shades) instead of Panda's 50 to 950. One **accent** plus one **gray**, picked at `init`.

- Gray choices: `neutral`, `mauve`, `slate`, `sage`, `olive`, `sand`. Accent: any of the 31 palettes (amber, blue, bronze, brown, crimson, cyan, gold, grass, green, indigo, iris, jade, lime, mauve, mint, neutral, olive, orange, pink, plum, purple, red, ruby, sage, sand, sky, slate, teal, tomato, violet, yellow). `red` and `green` always install.
- Radix step roles: 1 to 2 app backgrounds, 3 to 5 component backgrounds (normal, hover, pressed), 6 to 8 borders (8 also focus rings), 9 to 10 solid fills, 11 to 12 text.

Global semantic tokens:

| Token | Light | Dark |
|---|---|---|
| `fg.default` / `fg.muted` / `fg.subtle` | `gray.12` / `gray.11` / `gray.10` | same steps |
| `canvas` (body background) | `gray.1` | `gray.1` |
| `border` | `gray.4` | `gray.4` |
| `error` | `red.9` | `red.9` |

Per palette aliases (accent pattern, e.g. `blue`): `solid.bg` = 9, `solid.bg.hover` = 10, `solid.fg` = white; `subtle.bg` = a3 (hover a4, active a5), `subtle.fg` = a11; `surface.bg` = a2 (active a3), `surface.border` = a6 (hover a7); `outline.border` = a7 (bg hover a2, active a3); `plain.bg` hover a3 / active a4; all `fg` = a11. The **neutral** gray differs: `solid.bg` black / white (light / dark), hover `gray.12`, `solid.fg` white / black; `surface.bg` white / `gray.1`; surface and outline borders `gray.6`; text `gray.12`.

Neutral scale (Radix gray), light → dark:

| Step | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Light | `#fcfcfc` | `#f9f9f9` | `#f0f0f0` | `#e8e8e8` | `#e0e0e0` | `#d9d9d9` |
| Dark | `#111111` | `#191919` | `#222222` | `#2a2a2a` | `#313131` | `#3a3a3a` |
| **Step** | **7** | **8** | **9** | **10** | **11** | **12** |
| Light | `#cecece` | `#bbbbbb` | `#8d8d8d` | `#838383` | `#646464` | `#202020` |
| Dark | `#484848` | `#606060` | `#6e6e6e` | `#7b7b7b` | `#b4b4b4` | `#eeeeee` |

Example accent: `blue.9` `#0090ff` (both modes), `blue.11` light `#0d74ce` / dark `#70b8ff`. Other palettes: read the installed `theme/colors/<name>.ts`.

Global CSS: `html { colorPalette: gray }`; focus ring color = `colorPalette.solid.bg`; selection = `colorPalette.subtle.bg`; placeholder = `fg.subtle`. Apply the accent with the `colorPalette` style prop (e.g. `colorPalette: 'blue'`) on a component or container.

## Spacing and layout

Panda spacing: 1 = 0.25rem (4px), half steps 0.125rem. Component sizes share heights across "primary" components: a `md` Button and `md` Input are both 40px. Card padding is `6` (24px).

## Radius

Semantic radii written by `init`: `l1` → `radii.xs` (0.125rem), `l2` → `radii.sm` (0.25rem), `l3` → `radii.md` (0.375rem). Nest them: `l1` inside `l2` inside `l3`. Buttons and inputs use `l2`; card, popover and dialog use `l3`. Panda radii for reference: lg 0.5rem, xl 0.75rem, 2xl 1rem, 3xl 1.5rem, 4xl 2rem, full 9999px.

The init prompt offers none, xs, sm (default), md, lg, xl, 2xl.

## Elevation

Semantic shadows `xs` to `2xl` and `inset`, adapting to mode. Light uses gray alpha (e.g. `md`: `0px 4px 8px gray.a4, 0px 0px 1px gray.a4`); dark uses `black.a8` plus a `0 0 1px inset gray.a8` edge. Steps: xs 1/2px, sm 2/4px, md 4/8px, lg 8/16px, xl 16/24px, 2xl 24/40px (offset / blur). Popover and dialog use `lg`; the `elevated` card uses `lg`.

## Motion

- Durations (Park override of Panda): fastest 50ms, faster 100ms, fast 150ms, normal 200ms, slow 250ms, slower 300ms, slowest 400ms.
- Easings (Panda preset): `default` and `in-out` `cubic-bezier(0.4, 0, 0.2, 1)`, `in` `cubic-bezier(0.4, 0, 1, 1)`, `out` `cubic-bezier(0, 0, 0.2, 1)`, `linear`.
- Animation styles: `slide-fade-in/out` (direction from `data-placement`), `scale-fade-in/out`. Keyframes: fade, slide (full and partial), scale, expand / collapse height and width.
- Popover: open `scale-fade-in` at `fast`, close at `faster`. Dialog: backdrop fade `normal` in / `fast` out; content `slowest` in / `normal` out.
- Button `transitionProperty: background-color, border-color, color, box-shadow`.

## Icons

Lucide via `lucide-react` (`npm install @ark-ui/react lucide-react`). Icon sizes in buttons: 14px at `2xs`, 16px at xs/sm, 20px at md/lg, 22px at xl, 24px at 2xl.

## Components

Five shared variants: `solid` (primary CTA), `subtle` (badges, selected), `surface` (cards, selectable items), `outline` (secondary), `plain` (text and ghost actions).

- **Button:** `l2`, semibold, gap 8px, default `solid` / `md`. Sizes (height / px / textStyle): 2xs 24/8/xs, xs 32/10/sm, sm 36/12/sm, md 40/14/sm, lg 44/16/md, xl 48/18/md, 2xl 64/24/xl.
- **Input:** `l2`, default `outline` / `md`: 40px tall, px 12px, textStyle md, 1px `gray.outline.border`. Sizes 2xs 28 to 2xl 64. Variants outline, surface, subtle, flushed.
- **Card:** root `l3`, default `outline` (`gray.surface.bg` + 1px border); `elevated` adds shadow `lg`; `subtle`. Header p 24px gap 4px, body px 24 pb 24, footer gap 12 right aligned. Title `lg` semibold, description `sm` `fg.muted`.
- **Focus ring (Panda `focusVisibleRing`):** button `outside` = 2px solid outline, 2px offset; input `inside` = 1px outline, no offset, border takes the ring color. Fallback color `#005FCC` if no global ring color.
- **Disabled:** `layerStyle: disabled` = opacity 0.67, grayscale, `cursor: not-allowed`.

## Install

Panda CSS must already be set up.

```bash
npm install @ark-ui/react lucide-react
npx @park-ui/cli init      # prompts: framework (react | solid), accent, gray, radius
npx panda codegen
npx @park-ui/cli add button card input
npx @park-ui/cli add teal  # extra color palette
```

Add the docs' plugin to `panda.config.ts` that omits `theme.tokens.colors` and `theme.semanticTokens.colors` from `@pandacss/preset-panda`, so only Radix based colors remain.

**`@park-ui/panda-preset` is retired.** The 2025-11-21 changelog ("No More Preset") replaced it with recipes copied into the project. Its last version is 0.43.1 (2024-11-22, `createPreset({ accentColor, grayColor, radius })`). Use it only to maintain an old project; do not add it to new ones.

## Limits

- MIT. Copy recipes through the CLI, not by pasting source here. Radix Colors values are MIT as well; credit Radix when you reproduce a full scale.
- Park UI is Panda specific. Do not translate recipes into Tailwind classes and still call it Park UI.
- Solid and Vue component folders exist in the repo; the CLI prompt offers only react and solid.
- 미확인: in the current CLI source the radius prompt result does not change what is written (always `l1 xs / l2 sm / l3 md`). Check the generated `panda.config.ts` after choosing a non default radius.
- 미확인: dialog uses easing names `emphasized-in` / `emphasized-out`, which are not defined in the Park preset or Panda preset source checked.
- 미확인: the selector behind Panda's `_dark` condition in a Park project (Park only adds `light: ':root &, .light &'`).
- 미확인: `canvas` is defined in the preset source but not in the CLI `__init` registry item; confirm it exists after `init`.
