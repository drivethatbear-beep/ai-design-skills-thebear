# Apple HIG theme

> Source: https://developer.apple.com/design/human-interface-guidelines (typography, color, layout, materials, motion, buttons, accessibility, sf-symbols) · https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass · https://developer.apple.com/fonts/ · https://developer.apple.com/sf-symbols/ · https://developer.apple.com/documentation/swiftui/animation · checked 2026-10-29 · License: The HIG is guidance only. SF Pro, SF Compact, SF Mono and New York are licensed under the Apple San Francisco Font License (EA1370), which allows use only to create mock-ups of UI for software on Apple operating systems. Embedding the fonts and using them for non-Apple OS UI are prohibited. SF Symbols carries Apple terms that forbid use in app icons, logos or any trademarked use.

## When to apply

Apply only when the user names Apple HIG, iOS, macOS or Liquid Glass styling, or when the project is a landing page for an app on Apple platforms (an App Store app, Mac app or visionOS app) that should look native. Otherwise keep the base rules from SKILL.md.

## Overrides of base rules

| Base rule (SKILL.md) | This theme |
|---|---|
| B1 fonts: Geist, Manrope, Geist Mono, Poppins | Use the system stack `-apple-system, BlinkMacSystemFont, system-ui, sans-serif`. It renders SF on Apple devices without shipping the font. Never self-host or `@font-face` SF Pro. On non-Apple devices the system falls back to that platform's font. The Helvetica and Arial ban still applies, so do not list them as fallbacks. |
| B1 Tailwind type scale | Use the Apple text styles below (pt maps to CSS px). |
| B1 weight cap (no 900) | Kept. HIG also advises against Ultralight, Thin and Light. |
| B1 button type 16px semibold | Headline or Body emphasized, 17px semibold. |
| B2 spacing set | Kept as the closest web scale. HIG publishes no web spacing scale, so align to safe areas and system margins (iOS values 미확인). |
| B3 Tailwind radius only | Use continuous (squircle-like) corners and concentric nesting. Capsules are used for buttons. Exact radii are 미확인. |
| B4 flat backgrounds | Kept for the content layer. Controls and nav may use translucent material (backdrop blur). This overrides "flat" only for the floating control layer. |
| B4 dark backgrounds limited to six hex values | Use Apple dark semantic backgrounds (values 미확인). `#000000` stays valid. |
| B5 hero heading gradient text | Not an Apple convention. Use solid `label` color. |
| B6 icons: Phosphor, Solar, Iconamoon | SF Symbols only inside Apple-platform contexts (see Icons). On the web, keep the base icon sets in a matching weight. |
| B7 motion curve | Spring-like motion. The SwiftUI default is `spring(duration: 0.5, bounce: 0)`. |

## Typography

SF Pro is the iOS, iPadOS and macOS system font, SF Compact is used on watchOS, and New York (NY) is the serif companion. They ship as variable fonts with dynamic optical sizes, so separate SF Pro Text and SF Pro Display cuts are only needed in tools without variable-font support. Minimum and default sizes: iOS 17/11pt, macOS 13/10pt, visionOS 17/12pt, watchOS 16/12pt, tvOS 29/23pt.

iOS and iPadOS Dynamic Type at the Large (default) size:

| Style | Weight | Size / Leading (pt) | Emphasized |
|---|---|---|---|
| Large Title | Regular | 34 / 41 | Bold |
| Title 1 | Regular | 28 / 34 | Bold |
| Title 2 | Regular | 22 / 28 | Bold |
| Title 3 | Regular | 20 / 25 | Semibold |
| Headline | Semibold | 17 / 22 | Semibold |
| Body | Regular | 17 / 22 | Semibold |
| Callout | Regular | 16 / 21 | Semibold |
| Subheadline | Regular | 15 / 20 | Semibold |
| Footnote | Regular | 13 / 18 | Semibold |
| Caption 1 | Regular | 12 / 16 | Semibold |
| Caption 2 | Regular | 11 / 13 | Semibold |

macOS: Large Title 26/32, Title 1 22/26, Title 2 17/22, Title 3 15/20, Headline 13/16 Bold (emphasized Heavy), Body 13/16, Callout 12/15, Subheadline 11/14, Footnote 10/13, Caption 1 10/13, Caption 2 10/13 Medium. All are Regular unless noted.

Tracking for SF Pro (iOS, iPadOS, visionOS) varies by size, for example: 12pt 0, 13pt -0.08, 15pt -0.23, 17pt -0.43, 20pt -0.45, 22pt -0.26, 28pt +0.38, 34pt +0.40, 48pt +0.35, 80pt and up 0 (pt values). On the web, `-apple-system` applies optical tracking automatically, so do not add `letter-spacing` unless you use a non-system font. For a marketing hero, sizes above Large Title (e.g. 48–80px, Semibold or Bold) are acceptable. Keep line height near 1.1–1.2 (a web approximation, not an HIG value).

## Color tokens

HIG warns that values change between releases. Use them for reference and design. In apps, use the system APIs.

| Color | Light | Dark | Increased contrast light / dark |
|---|---|---|---|
| systemRed | `#FF383C` | `#FF4245` | `#E9152D` / `#FF6165` |
| systemOrange | `#FF8D28` | `#FF9230` | `#C55300` / `#FFA056` |
| systemYellow | `#FFCC00` | `#FFD600` | `#A16A00` / `#FEDF43` |
| systemGreen | `#34C759` | `#30D158` | `#008932` / `#4AD968` |
| systemMint | `#00C8B3` | `#00DAC3` | `#008575` / `#54DFCB` |
| systemTeal | `#00C3D0` | `#00D2E0` | `#008198` / `#3BDDEC` |
| systemCyan | `#00C0E8` | `#3CD3FE` | `#007EAE` / `#6DD9FF` |
| systemBlue | `#0088FF` | `#0091FF` | `#1E6EF4` / `#5CB8FF` |
| systemIndigo | `#6155F5` | `#6D7CFF` | `#564ADE` / `#A7AAFF` |
| systemPurple | `#CB30E0` | `#DB34F2` | `#B02FC2` / `#EA8DFF` |
| systemPink | `#FF2D55` | `#FF375F` | `#E7124D` / `#FF8AC4` |
| systemBrown | `#AC7F5E` | `#B78A66` | `#956D51` / `#DBA679` |
| systemGray | `#8E8E93` | `#8E8E93` | — |
| systemGray2 / 3 | `#AEAEB2` / `#C7C7CC` | `#636366` / `#48484A` | — |
| systemGray4 / 5 / 6 | `#D1D1D6` / `#E5E5EA` / `#F2F2F7` | `#3A3A3C` / `#2C2C2E` / `#1C1C1E` | — |

Semantic roles: `label`, `secondaryLabel`, `tertiaryLabel` and `quaternaryLabel` for text. `systemBackground`, `secondarySystemBackground` and `tertiarySystemBackground`, plus the grouped variants. `separator` (translucent) and `opaqueSeparator`. `link`. Their hex or alpha values are not published in the HIG (미확인). Sample them from Apple Design Resources (iOS 27 UI Kit) instead of guessing. On the web, `color-scheme: light dark` and the CSS system colors (`Canvas`, `CanvasText`, `AccentColor`) adapt natively. Contrast minimums: 4.5:1 up to 17pt, 3:1 at 18pt or bold. Use one accent color for primary actions and do not reuse it for non-interactive text.

## Spacing and layout

- Respect safe areas and system layout margins. On the web, use `env(safe-area-inset-*)` with `viewport-fit=cover`.
- Size classes are compact or regular per axis. Lay out by available space, not device type. HIG gives no web breakpoints, so keep the base container rules.
- Order content top to bottom and leading to trailing. Group with negative space, container shapes or separators.
- The iOS default side margin in pt is 미확인 (HIG gives no number). tvOS insets are 60pt top and bottom and 80pt sides.
- Minimum hit target: 44×44pt on iOS, iPadOS and watchOS (28×28 absolute minimum). 28×28 on macOS. 60×60 on visionOS. 66×66 on tvOS.

## Radius

- Use continuous curvature corners (`RoundedCornerStyle.continuous`). On the web, approximate with `border-radius` plus `corner-shape: squircle` where supported. Otherwise plain `border-radius` is the fallback.
- Liquid Glass era: hardware curvature drives the shape of nested elements. Make inner shapes concentric to their container (`ConcentricRectangle`). Buttons and many controls became rounder. Sheets and list sections have larger radii. The base nested-radius formula (inner = outer − gap) is the web way to achieve concentricity.
- Capsule shape for text buttons and circle for icon-only buttons. The HIG states this for visionOS. That other platforms do the same is 미확인.
- `corner-shape` is a CSS feature, not an Apple value. Check browser support before relying on it.
- Specific corner radius values: 미확인 (not published in the HIG).

## Elevation

Apple does not use an elevation scale. Hierarchy comes from layers. Liquid Glass forms a functional layer for controls and navigation that floats above content. Standard materials (ultraThin, thin, regular, thick) separate areas within the content layer. Shadow values are 미확인.

## Motion

- Purposeful, brief and precise. Motion follows the gesture, can be cancelled, and is optional (provide non-motion feedback).
- Avoid motion on frequent interactions. Avoid sustained oscillation near 0.2Hz (visionOS).
- SwiftUI defaults: `spring(duration: 0.5, bounce: 0)`. Presets: `.smooth` (no bounce), `.snappy` (small bounce), `.bouncy` (more bounce). Their exact parameters are 미확인.
- Web approximation: a 500ms deceleration close to a zero-bounce spring. The base `cubic-bezier(0.22,1,0.36,1)` at 500ms is acceptable. Keep transform and opacity only and honor `prefers-reduced-motion`.

## Icons

SF Symbols (current download: SF Symbols 27) has 9 weights matching SF, 3 scales and 4 rendering modes (monochrome, hierarchical, palette, multicolor), plus gradients and Draw animations in 7 and later. Terms forbid using symbols, or confusingly similar images, in app icons, logos or trademarked uses. Use on websites outside Apple-platform contexts is 미확인 (license text not read). Treat it as not permitted, and on the web use the base icon sets at a weight that matches the text.

## Components

- Button: hit region at least 44×44pt. Use one or two prominent buttons per view, where the accent color fills the background, and differentiate choices by style, not size. Use a verb-first label ("Add to Cart") and always include a pressed state. Liquid Glass: tint the background of prominent buttons, not the label. Keep other controls monochrome.
- Text field: placeholder hint plus a separate label. Size the field to the expected input. Stack fields vertically at consistent widths. Validate at a sensible time and show a trailing clear button on iOS.
- Card or grouped content: use the content layer with a standard material or grouped background, with rounded continuous corners concentric to the container. Do not use Liquid Glass inside content.
- Floating nav or toolbar (web): translucent surface with `backdrop-filter: blur()`. Use the regular variant over most content and the clear variant only over rich media, adding a 35% dark dimming layer if the content is bright. Blur radius values are 미확인.

## Install

No Apple web package exists. Use:

```css
:root { color-scheme: light dark; font-family: -apple-system, BlinkMacSystemFont, system-ui, sans-serif; }
.glass { background: color-mix(in srgb, Canvas 70%, transparent); backdrop-filter: blur(20px) saturate(180%); }
```

The `.glass` numbers are a web approximation, not Apple values. Design files: Apple Design Resources (iOS 27, iPadOS 27 and macOS 27 UI Kits for Figma and Sketch), downloadable by registered developers.

## Limits

- Never use the Apple logo, Apple product names as your own brand, device bezels outside Apple's marketing guidelines, or SF fonts and SF Symbols on non-Apple-platform marketing.
- A landing page "inspired by" the HIG must not pass itself off as an Apple page.
- 미확인: label, background and separator hex or alpha values. iOS layout margin pt values. Concrete corner radii. Liquid Glass blur, opacity and shadow parameters. `.smooth`, `.snappy` and `.bouncy` spring parameters. SF Symbols web-use license text.
