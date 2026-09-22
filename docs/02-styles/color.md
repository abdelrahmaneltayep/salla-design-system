# Color

Salla's palette as Material colour roles. **Every value below was read from the Figma library on 2026-09-22** (`catalog/figma-tokens-harvest.json`); the Figma variable that produces each role is listed so the two stay diff-able.

## Brand roles

| Role | Token | Value | Figma variable(s) | Use |
|---|---|---|---|---|
| Primary | `sys.color.primary` | `#004956` | `background/primary/primary`, `border/primary` | TopAppBar fill, checked Checkbox / Radio / Switch, active-tab underline, checkbox ring |
| On primary | `sys.color.on-primary` | `#ffffff` | `text/gray/white` | text and icons on the TopAppBar |
| Primary disabled | `sys.color.primary-disabled` | `#95c8d0` | `text/primary/disabled` | disabled outlined-primary label |
| Primary container | `sys.color.primary-container` | `#a4ffe5` | `background/secondary/seconadry` | **primary Button fill**, active primary Tab, Tooltip surface |
| On primary container | `sys.color.on-primary-container` | `#004956` | `text/primary/primary` | primary Button label, Tooltip text |
| Primary container hover | `sys.color.primary-container-hover` | `#dbfff6` | `border/seconadry-hover` | tag outline in the account chip |
| Primary container subtle | `sys.color.primary-container-subtle` | `#e6fff9` | `background/secondary/lighter`, `border/seconadry-disabled` | active NavigationItem, video play button |
| Text brand | `sys.color.text.brand` | `#004956` | `text/primary/link` | links, breadcrumb current item, PageTitle |

Naming note: Figma calls the mint `secondary`, but it is only ever used as the *fill behind primary actions* (primary Button, active primary Tab, Tooltip). Material's name for that role is **primary container**. A true secondary accent is not defined.

## Surfaces, outlines, text

| Role | Token | Value | Figma variable(s) |
|---|---|---|---|
| Surface | `sys.color.surface` | `#ffffff` | `background/default/white`, `background/default/cards` |
| Surface input | `sys.color.surface-input` | `#ffffff` | `background/default/input` |
| Surface neutral | `sys.color.surface-neutral` | `#f4f4f4` | `background/default/neutrals` |
| Surface disabled | `sys.color.surface-disabled` | `#eeeeee` | `background/default/disabled`, `background/default/neutrals-dark` |
| Outline light | `sys.color.outline-light` | `#f4f4f4` | `border/light` (LearnMore card) |
| Outline | `sys.color.outline` | `#eeeeee` | `border/default` |
| Outline hover | `sys.color.outline-hover` | `#dddddd` | `border/hover` (field hover, tab hover underline) |
| Outline strong | `sys.color.outline-strong` | `#737373` | `border/gray-lighter` (disabled-checked checkbox) |
| Outline primary | `sys.color.outline-primary` | `#a4ffe5` | `border/seconadry` (outlined primary Button) |
| Outline primary strong | `sys.color.outline-primary-strong` | `#004956` | `border/primary`, `border/primary-link` |
| Text primary | `sys.color.text.primary` | `#333333` | `text/gray/dark` |
| Text secondary | `sys.color.text.secondary` | `#666666` | `text/gray/light` (placeholder, helper text) |
| Text tertiary | `sys.color.text.tertiary` | `#737373` | `text/gray/lighter` (inactive tab, breadcrumb ancestors, neutral status) |
| Text disabled | `sys.color.text.disabled` | `#bbbbbb` | `text/gray/disabled` |
| Text inverse | `sys.color.text.inverse` | `#ffffff` | `text/gray/white` |

## Status colours

Five statuses × five shades, all observed except where noted.

| Status | lighter (fill) | light (border) | primary | dark (dot) | darker (text) |
|---|---|---|---|---|---|
| Success | `#effbf6` | `#97e7c8` | `#00af6c` | `#008c56` | `#005232` |
| Danger | `#feecec` | `#fbb9bc` | `#f55157` | `#ca4146` | `#7a1f1e` |
| Warning | `#fff9eb` | `#ffe7c7` | `#ffaf44` | `#d18f36` | `#8f5f22` |
| Info | `#ecf3fe` | `#cbe0fb` | `#5196f3` | `#417ac8` | `#204374` |
| Neutral | `#eeeeee` | `#dddddd` | `#bbbbbb` | `#bbbbbb` | `#737373` |

Figma variables per shade: `{status}/{status}-lighter`, `border/status/{status}-light`, `background/status/{status}/primary` (also `{status}/{status}`), `{status}/{status}-dark`, `{status}/{status}-darker` (also `text/status/{status}/darker`). Neutral uses `background/default/neutrals-dark`, `border/hover`, `background/default/neutrals-darkest`, `text/gray/lighter`.

How components use the shades:

| Component | fill | border / accent | dot | text |
|---|---|---|---|---|
| `Button` filled status | `primary` | `primary` (2px) | – | `text.inverse` |
| `Alert` | `lighter` | `light` (3px inline-start) | – | `darker` |
| `Status` subtle | – | – | `dark` | `darker` |
| `Status` strong | `lighter` | – | `dark` | `darker` |
| `Table/Status` | `lighter` | `light` (1px) | `dark` | `darker` |
| `TextField` focus underline | – | `info.primary` (2px) | – | – |
| `TextField` error | – | `danger.primary` | – | `danger.primary` |
| `MenuItem` danger | – | – | – | `danger.primary` |

## Accent roles (non-semantic)

| Role | Token | Values | Figma | Use |
|---|---|---|---|---|
| Feature | `sys.color.feature.*` | gradient `#ffd8c2 → #ffaf83`, text `#883000` | `color/support-non-semantic/orange/200|300`, `background/supporting-colors/orange/darker` | `Button variant=feature`, `ListItem feature` |
| Upgrade | `sys.color.upgrade.*` | lighter `#fffbea`, primary `#ffe895`, dark `#d1b44c`, darker `#554300` | `background/supporting-colors/gold/*`, `border/upgrade/dark`, `text/upgrade/darker` | `UpgradeCard`, crown CTA |

## Reference palette

`ref.palette.{teal, gray, green, red, amber, blue, orange, gold}.{step}` in `tokens/tokens.json`. Steps are named by lightness (50 lightest → 900 darkest); every step listed was observed in Figma.

## Contrast

See [accessibility.md](../01-foundations/accessibility.md#colour-and-contrast). Filled `success`, `warning`, `danger` and `info` Buttons with white labels do not reach AA at 14px; the `dark` shades do (danger 4.8:1) or nearly do (success 4.3:1).

## Dark theme

Not shipped. `tokens/css/tokens.css` includes a `[data-theme="dark"]` block with placeholder values that proves the `sys` tier is theme-able. Legacy variables from the `07--light-theme/*` collection (`color-white-drop-menu`, `color-gray-200`) still appear on a few frames and should be re-pointed to the roles above.
