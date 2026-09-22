# Color

Salla's palette expressed as Material colour roles. Values marked ✓ were verified from Figma on 2026-09-22; the Figma variable that produces each role is listed so the two stay diff-able.

## Key colours

| Role | Token | Value | Figma variable | Use |
|---|---|---|---|---|
| Primary | `sys.color.primary` | `#004956` ✓ | `background/primary/primary` | TopAppBar fill, checked Checkbox / Radio / Switch, active indicators |
| On primary | `sys.color.on-primary` | `#ffffff` ✓ | `text/gray/white` | text and icons on primary |
| Primary container | `sys.color.primary-container` | `#a4ffe5` ✓ | `background/secondary/seconadry` | **primary Button fill**, focus ring, selected row tint |
| On primary container | `sys.color.on-primary-container` | `#004956` ✓ | `text/primary/primary` | primary Button label |
| Text brand | `sys.color.text.brand` | `#004956` ✓ | `text/primary/link` | links, outlined primary Button label |
| Surface | `sys.color.surface` | `#ffffff` ✓ | `background/default/white` | page, Panel, Dialog |
| Surface input | `sys.color.surface-input` | `#ffffff` ✓ | `background/default/input` | field container |
| Outline | `sys.color.outline` | `#eeeeee` ✓ | `border/default` | field and secondary Button border, dividers, table rules |
| Outline primary | `sys.color.outline-primary` | `#a4ffe5` ✓ | `border/seconadry` | outlined primary Button |
| Text primary | `sys.color.text.primary` | `#333333` ✓ | `text/gray/dark` | body text, secondary Button label |
| Text secondary | `sys.color.text.secondary` | `#666666` ✓ | `text/gray/light` | placeholders, helper text, subtext |
| Text inverse | `sys.color.text.inverse` | `#ffffff` ✓ | `text/gray/white` | labels on filled status buttons |

Note on naming: Figma calls the brand teal `text/primary/primary` *and* `background/primary/primary`, and the mint `background/secondary`. In the new model the mint is the **primary container** (it is the fill of the primary Button, so it belongs to the primary role), not a second brand colour. A true `secondary` role is reserved for a future accent.

## Status colours

Each status has up to five shades. Naming follows the Figma `lighter / light / primary / dark / darker` pattern.

| Status | lighter | light | primary | dark | darker |
|---|---|---|---|---|---|
| Success | – | – | `#00af6c` ✓ | `#008c56` ✓ | `#005232` ✓ |
| Danger | `#feecec` ✓ | – | `#f55157` ✓ | `#ca4146` ✓ | `#7a1f1e` ✓ |
| Warning | – | – | `#ffaf44` ✓ | – | – |
| Info | `#ecf3fe` ✓ | `#cbe0fb` ✓ | `#5196f3` ✓ | – | `#204374` ✓ |
| Neutral | – | – | – | – | – |

Blank cells exist in Figma (the `Status` component has a `neutral` type; `Alertbox` has warning and success surfaces) but were not read in this extraction. Fill them from the `03-Colors` collection.

How components use the shades:

| Component | fill | accent / dot | text |
|---|---|---|---|
| `Button` filled status | `primary` | – | `sys.color.text.inverse` |
| `Alert` | `lighter` | `light` (inline-start border) | `darker` |
| `Status` subtle | – | `dark` (dot) | `darker` |
| `Status` strong | `lighter` | `dark` (dot) | `darker` |
| `HelperText` error, field error outline | – | `primary` | `primary` |

## Feature accent (non-semantic)

For upsell and premium affordances only (`Button variant=feature`, `UpgradeCard`, `ListItem feature`). Never for status.

| Token | Value |
|---|---|
| `sys.color.feature.gradient-start` | `#ffd8c2` ✓ (`color/support-non-semantic/orange/200`) |
| `sys.color.feature.gradient-end` | `#ffaf83` ✓ (`color/support-non-semantic/orange/300`) |
| `sys.color.on-feature` | `#883000` ✓ (`background/supporting-colors/orange/darker`) |

## Reference palette

`ref.palette.{teal,gray,green,red,amber,blue,orange}.{step}` in `tokens/tokens.json`. Only the verified steps are listed; the full 50–900 ramps live in the Figma `01` collection and should be exported to complete the file.

## Contrast

See [accessibility.md](../01-foundations/accessibility.md#colour-and-contrast). Filled `success`, `warning` and `danger` Buttons with white labels do not reach AA at 14px and need a decision.

## Dark theme

Not shipped. `tokens/css/tokens.css` includes a `[data-theme="dark"]` block that re-maps surface and text roles as a proof that the `sys` tier is theme-able; the values are placeholders.
