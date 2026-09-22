# Typography

One family, three weights, a Tailwind-shaped size scale, expressed as Material type roles. Values observed in Figma on 2026-09-22 are marked ✓.

## Family

`ref.font.family.base` = **Ping AR + LT** ✓ (Figma `Typography/Family/Font`). One family for Arabic and Latin. Fallback stack: `"Ping AR + LT", "PingAR+LT", "PingARLT", "PT Sans", system-ui, sans-serif`.

Weights ✓: Regular 400, Medium 500, Bold 700. No light or black.

## Scale

| Token | Size | Figma | Line-height token |
|---|---|---|---|
| `ref.font.size.xs` | 12px ✓ | `Typography/Size/xs`, `$text-xs` | `lineHeight.4` = 16px ✓ |
| `ref.font.size.sm` | 14px ✓ | `Typography/Size/sm`, `$text-sm` | `lineHeight.5` = 20px ✓ |
| `ref.font.size.md` | 16px ✓ | `Typography/Size/md`, `$text-base` | `lineHeight.6` = 24px ✓ |
| `ref.font.size.lg` | 18px | `$text-lg` (not observed) | `lineHeight.7` = 28px ✓ |
| `ref.font.size.xl` | 20px ✓ | `Typography/Size/xl`, `$text-xl` | `lineHeight.7` = 28px ✓ |
| `ref.font.size.2xl` | 24px ✓ | `Typography/Size/2xl`, `$text-2xl` | `lineHeight.8` = 32px ✓ |
| `ref.font.size.3xl … 9xl` | 30 … 128px | `$text-3xl … 9xl` (styles exist, values not observed) | |

The Figma line-height variables are named `typography/line-height (Descreptive)/4|5|6|7|8`, i.e. Tailwind's `leading-4 … leading-8`. Rename to `line-height/4 … 8` (typo fix) and keep the numeric names.

## Type roles (Material)

| Role | Token | Figma style | Size / line | Weight | Observed on |
|---|---|---|---|---|---|
| Display large | `sys.typography.display-lg` | `Bold/$text-5xl` | 48 / 1 | 700 | marketing surfaces only |
| Headline large | `headline-lg` | `Bold/$text-2xl` | 24 / 32 ✓ | 700 | PageTitle desktop |
| Headline medium | `headline-md` | `Bold/$text-xl` | 20 / 28 ✓ | 700 | LearnMore title, Dialog title |
| Title large | `title-lg` | `Bold/$text-lg` | 18 / 28 | 700 | PanelHeader |
| Title medium | `title-md` | `Bold/$text-base` | 16 / 24 ✓ | 700 | Alert title, PageTitle mobile, active Tab, active primary Tab |
| Title small | `title-sm` | `Bold/$text-sm` | 14 / 20 ✓ | 700 | pagination numbers, table header |
| Body large | `body-lg` | `Regular/$text-base` | 16 / 24 ✓ | 400 | NavigationItem |
| Body medium | `body-md` | `Regular/$text-sm` | 14 / 20 ✓ | 400 | **default UI text**: field values, placeholders, MenuItem, Alert body, table cells, breadcrumb |
| Body small | `body-sm` | `Regular/$text-xs` | 12 / 16 ✓ | 400 | HelperText, subtext, units, Table/Status, Tooltip |
| Label large | `label-lg` | `Medium/$text-base` | 16 / 24 ✓ | 500 | Tab (inactive / hover), primary Tab, active NavigationItem |
| Label medium | `label-md` | `Medium/$text-sm` | 14 / 20 ✓ | 500 | **Button md / lg label**, FieldLabel, CheckboxField title, UpgradeCard CTA |
| Label small | `label-sm` | `Medium/$text-xs` | 12 / 16 ✓ | 500 | Button sm label, Status label |

Rules:

- Components pick a **role**, never a size + weight pair.
- Letter-spacing is 0 everywhere (Arabic does not track).
- Arabic runs ~10% wider than English at equal size; never fix a text width below organism level.
- Digits are Latin in both languages (see [content-and-localization.md](../01-foundations/content-and-localization.md)).
- Two legacy styles without variables (`Regular/text-sm`, `Medium/text-sm`, line-height 100%) appear on a few frames (Learn More buttons, header name) and should be replaced with `$text-sm` styles.

## Implementation

CSS: `font: var(--sys-type-body-md);` (shorthand-ready values in `tokens/css/tokens.css`).
Tailwind: the preset ships a plugin that emits `.type-{role}` utilities (`type-body-md`, `type-label-md` …).
