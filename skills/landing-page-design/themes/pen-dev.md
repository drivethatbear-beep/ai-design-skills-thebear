# pen.dev design kits

> Source: design libraries bundled with the pen.dev (Pencil) desktop app, read 2026-10-29 · License: pen.dev assets, governed by pen.dev's terms. This page summarizes each kit's character and key tokens. Full token sets are not redistributed here.

## When to apply

Apply when the user names one of these kits ("Lunaris로", "Halo 토큰으로"), or when the design is being made on the pen.dev canvas with that library imported. Each kit is a complete shadcn style token set (`--background`, `--primary`, `--border`, and so on, with Light and Dark modes) plus about 80 to 100 reusable components.

## Where the full values come from

Use the first source that is available:

1. **On the pen.dev canvas.** Import the library (`pencil:<kit>.lib.pen`) and read it with `Print(GetVariables())` through the pen.dev MCP `execute` tool.
2. **Local token dump.** Read `themes/local/pen-<kit>.tokens.json` if it exists. This folder is git ignored and holds the full variables, theme axes, and component names for this machine only.
3. **Neither.** Use the key tokens below, and say that the remaining values are approximated.

## The kits

| Kit | Library | Character | Primary | Fonts | Radius |
|---|---|---|---|---|---|
| **Halo** | `pencil:halo.lib.pen` | Soft and rounded, violet accent, navy tinted dark mode | `#5749F4` | Inter / Inter | xs 6, m 24, l 40, pill 999 |
| **Lunaris** | `pencil:lunaris.lib.pen` | Warm off white, orange accent, technical mono headings | `#FF8400` (text on it `#111111`) | JetBrains Mono (primary), Geist (secondary) | m 16, pill 999 |
| **Nitro** | `pencil:nitro.lib.pen` | Square and dense, blue accent, data tables included | `#0F5FFE` | Roboto / Roboto Mono | none 0 (default), xs 2, pill 999 |
| **shadcn** | `pencil:shadcn.lib.pen` | shadcn/ui with three theme axes: Mode, Base (Neutral, Gray, Stone, Zinc, Slate), Accent (Default plus 7 colors) | Neutral `#171717`, Dark `#e5e5e5` | Set per project | Set per project |
| **HeroUI** | demo file `pencil-heroui.pen` (not a library) | HeroUI style kit: 379 variables across semantic, primitives, and typography | accent `#0485F7` | Inter / JetBrains Mono | xs 2 to 4xl 32, field 12, full 9999 |

### Key surface tokens

| Token | Halo L / D | Lunaris L / D | Nitro L / D | HeroUI L / D |
|---|---|---|---|---|
| background | `#FFFFFF` / `#131124` | `#F2F3F0` / `#111111` | `#F5F5F5` / `#252629` | `#F5F5F5` / `#060607` |
| foreground | `#2A2933` / `#E8E8EA` | `#111111` / `#FFFFFF` | `#333333` / `#F5F5F5` | `#18181B` / `#FCFCFC` |
| card | `#FFFFFF` / `#1A182E` | `#FFFFFF` / `#1A1A1A` | `#FFFFFF` / `#1F1F1F` | see local dump |
| border | `#C5C5CB` / `#2B283D` | `#CBCCC9` / `#2E2E2E` | `#E1E2E5` / `#2E2E2E` | see local dump |
| muted foreground | `#616167` / `#888799` | `#666666` / `#B8B9B6` | `#5B5F66` / `#A0A6B2` | `#71717A` / `#A1A1AA` |
| destructive | `#CC3314` | `#D93C15` / `#FF5C33` | `#A62911` | danger `#FF383C` / `#DB3B3E` |

Halo, Lunaris, and Nitro also define `--color-success`, `--color-warning`, `--color-error`, and `--color-info`, each with a `-foreground` pair, as tinted backgrounds with dark text.

## Overrides of base rules

| Base rule (SKILL.md) | This theme |
|---|---|
| B1 fonts: Inter and Roboto banned | Halo (Inter), Nitro (Roboto), and HeroUI (Inter) keep their fonts **only when the user picked the kit**. For Korean pages, swap the sans face for Pretendard and keep the mono face |
| B1 one typeface | Lunaris pairs JetBrains Mono and Geist by design |
| B3 Tailwind radius only | Use the kit's radius tokens (Halo 24 and 40 are intentional) |
| B4 dark backgrounds list | Use the kit's dark `--background` and `--card` |
| B5 hero heading gradient | Not part of any kit. Use solid `--foreground` |
| B6 icons | pen.dev ships Lucide, Phosphor, Feather, and Material Symbols. Prefer Phosphor to stay within B6 |
| B7 motion | Kits define no motion tokens. Keep B7 |

Spacing is not tokenized in Halo, Lunaris, or Nitro; components sit on a 4px and 8px rhythm, so B2 holds. HeroUI defines a `spacing` group, available in the local dump.

## Components

All three libraries carry the same core set: Button and Icon Button (Default, Secondary, Destructive, Outline, Ghost, each in regular and Large), Input, Select, Textarea, and OTP groups, Checkbox, Radio, Switch, Tabs, Accordion, Alert (Info, Success, Warning, Error), Avatar, Breadcrumb, Card (plain, image, action), Dialog and Modal, Dropdown, Tooltip, Progress, Pagination, and Sidebar. Nitro adds Data Table, Table Row, and Table Cell. Lunaris adds Search Box and Icon Label. Exact names are in the local dump.

Text sizes across the kits are mostly 14px for UI and 16px for large controls, at weights 400 and 500. On a landing page, apply the A and B11 hierarchy above that UI base.

## Style archetypes (`get_style`)

pen.dev also ships about 60 visual style archetypes, loaded with the pen.dev MCP tool `get_style({ name })`. They provide fonts, colors, and imagery direction, not component libraries. Use them only when the user has **no brand direction**, and never on top of TBNC or a named theme.

Families: Aerial, Anchored Ribbon Grid, Annotated Lookbook, Artisan Editorial, Blueprint Technical, Brutalist (Console, Editorial, Lattice, Poster, Spine), Calligraphic Atelier, Centered (Device Cascade, Serif List), Ceramic Console, Cinematic (Alternating, Device Column), Color Block Stack, Dark Centered Platform, Editorial (Landscape Stack, Scientific), Elegant (Bento, Couture, Editorial, Serene), Gradient (Aurora, Bubble, Editorial, Halftone, Haze, Prompt Stack), Illustrated (Ribbon Stack, Warm), Inline Friendly, Minimalistic (Atrium, Hairline, Monolith, Mosaic, Panel, Swiss), Modular Bento Showcase, Monumental Editorial, Narrative Illustrated, Optical Glass, Playful, Post Internet Archive, Prismatic Cinema, Product Data Grid, Product Demo, Saturated Code Bridge, Soft Bento, Spatial Plus, Split Inverse Showcase, Swiss Type Atlas, Technical (Blueprint, Console, Dispatch, Phosphor, Terminal), Visual (Cinematic, Editorial, Soft), Zigzag Bold Split.

Call `get_style()` for the current list with one line descriptions, since pen.dev updates it.

## Limits

- These kits belong to pen.dev. Do not publish the full token dumps or library files. The local folder is git ignored for that reason.
- Gradient styles conflict with B4. Use them only on explicit request, and keep reading surfaces flat.
- HeroUI here is pen.dev's demo file. For code, install HeroUI itself and follow its own tokens.
