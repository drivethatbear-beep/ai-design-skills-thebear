# shadcn/ui theme

> Source: https://ui.shadcn.com/docs/theming · https://ui.shadcn.com/docs/cli · https://ui.shadcn.com/docs/components-json · https://github.com/shadcn-ui/ui (`apps/v4/registry/config.ts`, `themes.ts`, `styles/style-nova.css`, `bases/base/ui/*`, `new-york-v4/ui/*`, `packages/shadcn/src/commands/init.ts`, `packages/registry/src/icons/libraries.ts`) · CLI `shadcn@4.23.0` (2026-10-27) · checked 2026-10-29 · License: MIT (© 2023 shadcn)

## When to apply

Only when the user names shadcn/ui, or the project already has a `components.json` / `@/components/ui` from the shadcn CLI. Otherwise use the base rules. If the project exists, its own `components.json` and CSS variables win over the defaults below.

## Overrides of base rules

| Base rule (SKILL.md) | This theme |
|---|---|
| B1 fonts | Geist is the font of the default preset (`base-nova`), so B1 holds. If the project was set up with a preset that ships Inter (vega, mira, luma), keep the project's font. Do not switch it silently |
| B1 button type: semibold | Buttons are `text-sm font-medium` (component source) |
| B1 type scale | Tailwind scale as in B1. One exception in Nova: `sm` button uses `text-[0.8rem]` |
| B2 spacing set; button padding 8/12 | Component padding stays as shipped: Nova default button `h-8 px-2.5`, input `px-2.5`. Use B2 for page layout only |
| B3 Tailwind radius only | `rounded-*` resolve to shadcn tokens derived from `--radius` (see Radius), not Tailwind's stock values |
| B4 dark backgrounds | Dark `--background` is `oklch(0.145 0 0)` and `--card` is `oklch(0.205 0 0)`, not the B4 hex list |
| B6 Phosphor/Solar/Iconamoon | Default is Lucide. Lucide is allowed under this theme. Prefer setting `iconLibrary: "phosphor"` for new projects (supported by the CLI) |
| B7 motion | Overlay components keep their `tw-animate-css` classes (`duration-100`, `zoom-in-95`, sheet `duration-200 ease-in-out`). Page level motion (nav, scroll reveals) still uses B7 |

## Typography

- Default preset `base-nova`: **Geist**. Registry font definition: family `'Geist Variable', sans-serif`, CSS variable `--font-sans`, Next.js import `Geist` from `next/font/google`, non Next dependency `@fontsource-variable/geist`.
- Other presets: vega / mira / luma use Inter, maia uses Figtree, lyra uses JetBrains Mono. Headings inherit the body font unless `fontHeading` is set.
- No custom type scale. Components use `text-xs`, `text-sm`, `text-base`; card title in Nova is `text-base leading-snug font-medium`.

## Color tokens

Base color `neutral` (default; others: stone, zinc, mauve, olive, mist, taupe). Values from the theming docs and `registry/themes.ts`, identical except charts.

| Token | `:root` | `.dark` |
|---|---|---|
| `--background` | `oklch(1 0 0)` | `oklch(0.145 0 0)` |
| `--foreground` | `oklch(0.145 0 0)` | `oklch(0.985 0 0)` |
| `--card` / `--popover` | `oklch(1 0 0)` | `oklch(0.205 0 0)` |
| `--card-foreground` / `--popover-foreground` | `oklch(0.145 0 0)` | `oklch(0.985 0 0)` |
| `--primary` | `oklch(0.205 0 0)` | `oklch(0.922 0 0)` |
| `--primary-foreground` | `oklch(0.985 0 0)` | `oklch(0.205 0 0)` |
| `--secondary` / `--muted` / `--accent` | `oklch(0.97 0 0)` | `oklch(0.269 0 0)` |
| `--secondary-foreground` / `--accent-foreground` | `oklch(0.205 0 0)` | `oklch(0.985 0 0)` |
| `--muted-foreground` | `oklch(0.556 0 0)` | `oklch(0.708 0 0)` |
| `--destructive` | `oklch(0.577 0.245 27.325)` | `oklch(0.704 0.191 22.216)` |
| `--border` | `oklch(0.922 0 0)` | `oklch(1 0 0 / 10%)` |
| `--input` | `oklch(0.922 0 0)` | `oklch(1 0 0 / 15%)` |
| `--ring` | `oklch(0.708 0 0)` | `oklch(0.556 0 0)` |
| `--sidebar` | `oklch(0.985 0 0)` | `oklch(0.205 0 0)` |
| `--sidebar-primary` | `oklch(0.205 0 0)` | `oklch(0.488 0.243 264.376)` |
| `--sidebar-accent` / `-border` / `-ring` | same as accent / border / ring | same as accent / border / ring |

Charts: the CLI registry ships grey charts for neutral (`--chart-1..5` = `oklch(0.87 0 0)`, `0.556`, `0.439`, `0.371`, `0.269`, both modes). The theming docs page still shows chromatic chart colors (e.g. light `--chart-1: oklch(0.646 0.222 41.116)`). Trust the project's generated CSS.

Rules: use the semantic utilities (`bg-background`, `text-muted-foreground`, `border-border`, `ring-ring`), never raw hex. A pair is `--x` for the surface and `--x-foreground` for text on it. Dark mode is the `.dark` class.

## Spacing and layout

Tailwind v4 default spacing (`--spacing` 0.25rem). Components use half steps (`px-2.5` = 10px, `gap-1.5` = 6px); leave them inside components. Nova card spacing is `--card-spacing: --spacing(4)` (16px), `--spacing(3)` (12px) for `size="sm"`. Page sections follow B2.

## Radius

`--radius: 0.625rem` (10px) by default. Derived in `@theme inline`:

| Token | Formula | At default |
|---|---|---|
| `--radius-sm` | `calc(var(--radius) * 0.6)` | 6px |
| `--radius-md` | `calc(var(--radius) * 0.8)` | 8px |
| `--radius-lg` | `var(--radius)` | 10px |
| `--radius-xl` | `calc(var(--radius) * 1.4)` | 14px |
| `--radius-2xl` | `calc(var(--radius) * 1.8)` | 18px |
| `--radius-3xl` / `-4xl` | `* 2.2` / `* 2.6` | 22px / 26px |

CLI radius options: none `0`, small `0.45rem`, medium `0.625rem`, large `0.875rem`. Nova: buttons and inputs `rounded-lg`, cards and dialogs `rounded-xl`. B3's nested formula still applies to page compositions.

## Elevation

Nova avoids shadows on cards and dialogs: `ring-1 ring-foreground/10` instead. Menus use `shadow-md`, sheets `shadow-lg`. Legacy `new-york-v4` uses `shadow-xs` (outline button, input) and `shadow-sm` (card).

## Motion

- Animation utilities come from `tw-animate-css` (`@import "tw-animate-css"` in shadcn's own `globals.css`) plus `@import "shadcn/tailwind.css"`, which `init` adds and which defines the accordion keyframes and `data-open` / `data-closed` / `data-checked` custom variants.
- Overlays (Nova): `data-open:animate-in fade-in-0 zoom-in-95`, `data-closed:animate-out fade-out-0 zoom-out-95`, `duration-100`; popovers and menus also `slide-in-from-*-2`. Dialog overlay `bg-black/10` with `backdrop-blur-xs`.
- Sheet: `transition duration-200 ease-in-out`. Buttons: `transition-all`, `active:translate-y-px`.
- No easing token is defined by shadcn; base B7 curve applies to anything you add.

## Icons

`iconLibrary` in config. Default `lucide` (`lucide-react`). Supported: lucide, tabler (`@tabler/icons-react`), hugeicons, phosphor (`@phosphor-icons/react`), remixicon. Icons inside buttons auto size to `size-4` (Nova `xs` 12px, `sm` 14px).

## Components

Current default is **Base UI + Nova** (`init -d` = `--template=next --preset=base-nova`). Styles live in `style-nova.css` as `cn-*` classes.

- **Button (Nova):** `rounded-lg border border-transparent text-sm font-medium`. Sizes: xs `h-6 px-2 text-xs`, sm `h-7 px-2.5`, default `h-8 px-2.5 gap-1.5`, lg `h-9 px-2.5`, icon `size-8` (icon-xs 6, icon-sm 7, icon-lg 9). Variants: default `bg-primary hover:bg-primary/80`, outline `border-border bg-background hover:bg-muted`, secondary, ghost `hover:bg-muted`, destructive `bg-destructive/10 text-destructive`, link.
- **Input (Nova):** `h-8 rounded-lg border border-input bg-transparent px-2.5 py-1 text-base md:text-sm`, dark `bg-input/30`, disabled `bg-input/50`.
- **Card (Nova):** `rounded-xl bg-card text-sm ring-1 ring-foreground/10`, padding 16px, footer `bg-muted/50 border-t`.
- **Focus ring (all):** `focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50`; invalid `aria-invalid:border-destructive ring-destructive/20` (dark `/40`).
- **Legacy Radix `new-york-v4`** (still in the registry): button `h-9 px-4 py-2 rounded-md` (sm `h-8 px-3`, lg `h-10 px-6`), input `h-9 rounded-md px-3 py-1 shadow-xs`, card `rounded-xl border py-6 gap-6 shadow-sm` with `px-6` sections, focus `ring-[3px] ring-ring/50`.

## Install

```bash
npx shadcn@latest init          # alias: create. Interactive preset picker
npx shadcn@latest init -d       # next template, base-nova preset
npx shadcn@latest init -b radix -p radix-nova   # Radix primitives instead of Base UI
npx shadcn@latest add button card input
```

Flags: `-t` next | vite | start | react-router | laravel | astro, `-b` base | radix | aria, `-p` preset name, URL or preset code, `--css-variables` / `--no-css-variables`, `--rtl`, `--pointer`, `--monorepo`.

`components.json` notes: `style`, `tailwind.baseColor` and `tailwind.cssVariables` are fixed after init (switching means reinstalling components). `tailwind.config` is blank on Tailwind v4. `aliases.*` map install paths. `registries` adds namespaced registries (`@acme`). The file is only needed for the CLI.

## Limits

- MIT: copying component code is fine; keep the license notice if you redistribute the source. Do not imply a page is made or endorsed by shadcn or Vercel.
- Do not paste whole registry files into answers; install them with the CLI.
- Values here are for neutral + Nova + Base UI. Other styles (vega, maia, lyra, mira, luma, sera, rhea) change sizes and radius; read the project's installed files.
- 미확인: whether `init` itself installs `tw-animate-css` in v4.23 (the docs only show it in an example import; shadcn's own app imports it).
- 미확인: `iconLibrary`, `base` and `menuColor` keys in `components.json` are in the registry schema but not documented on the components.json page.
- 미확인: the registry `DEFAULT_CONFIG` for the web configurator lists `font: "inter"` while the `base-nova` preset used by `init -d` lists Geist. Check the generated layout.
- 미확인: hex equivalents of the OKLCH values; none are published.
