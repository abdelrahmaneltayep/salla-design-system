# Typography

One family, three weights, a Tailwind-shaped size scale, expressed as Material type roles.

## Family

`ref.font.family.base` = **PingAR+LT** (Figma: `Typography/Family/Font`), used for Arabic and Latin. Fallback stack: `"PingAR+LT", "PingARLT", "PT Sans", system-ui, sans-serif`.

Weights ✓: Regular 400, Medium 500, Bold 700. No light or black.

## Scale

| Token | Size | Figma | Line height token |
|---|---|---|---|
| `ref.font.size.xs` | 12px ✓ | `Typography/Size/xs`, `$text-xs` | `lineHeight.4` = 16px ✓ |
| `ref.font.size.sm` | 14px ✓ | `Typography/Size/sm`, `$text-sm` | `lineHeight.5` = 20px ✓ |
| `ref.font.size.md` | 16px ✓ | `Typography/Size/md`, `$text-base` | `lineHeight.6` = 24px ✓ |
| `ref.font.size.lg` | 18px (assumed) | `$text-lg` | `lineHeight.7` = 28px |
| `ref.font.size.xl` | 20px (assumed) | `$text-xl` | `lineHeight.7` = 28px |
| `ref.font.size.2xl` | 24px (assumed) | `$text-2xl` | `lineHeight.8` = 32px |
| `ref.font.size.3xl … 9xl` | 30 … 128px (assumed) | `$text-3xl … 9xl` | |

The Figma line-height variables are named `typography/line-height (Descreptive)/4|5|6`, which is Tailwind's `leading-4/5/6`. Rename to `line-height/4|5|6` (typo fix) and keep the numeric names.

## Type roles (Material)

| Role | Token | Figma style | Size / line | Weight | Used by |
|---|---|---|---|---|---|
| Display large | `sys.typography.display-lg` | `Bold/$text-5xl` | 48 / 1 | 700 | marketing surfaces only |
| Headline large | `headline-lg` | `Bold/$text-2xl` | 24 / 32 | 700 | PageTitle |
| Headline medium | `headline-md` | `Bold/$text-xl` | 20 / 28 | 700 | Dialog title, section headings |
| Title large | `title-lg` | `Bold/$text-lg` | 18 / 28 | 700 | PanelHeader |
| Title medium | `title-md` | `Bold/$text-base` | 16 / 24 ✓ | 700 | Alert title, ListItem title |
| Title small | `title-sm` | `Bold/$text-sm` | 14 / 20 | 700 | table header cells, MenuItem emphasis |
| Body medium | `body-md` | `Regular/$text-base` | 16 / 24 | 400 | long-form body |
| Body small | `body-sm` | `Regular/$text-sm` | 14 / 20 ✓ | 400 | **default UI text**: field values, placeholders, table cells, Alert body |
| Body extra-small | `body-xs` | `Regular/$text-xs` | 12 / 16 ✓ | 400 | HelperText, subtext, units |
| Label medium | `label-md` | `Medium/$text-sm` | 14 / 20 ✓ | 500 | **Button label**, FieldLabel, Tab |
| Label small | `label-sm` | `Medium/$text-xs` | 12 / 16 ✓ | 500 | Status label, Chip, small Button |

Rules:

- Components pick a **role**, never a size + weight pair.
- Letter-spacing is 0 everywhere (Arabic does not track).
- Arabic runs ~10% wider than English at the same size; never fix a text width below organism level.
- Digits are Latin in both languages (see [content-and-localization.md](../01-foundations/content-and-localization.md)).

## Implementation

CSS: `font: var(--sys-type-body-sm);` (shorthand-ready values in `tokens/css/tokens.css`).
Tailwind: role utilities are not in the preset yet; add a plugin that emits `.type-body-sm { font: var(--sys-type-body-sm) }` for each role.
