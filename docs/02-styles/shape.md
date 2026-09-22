# Shape

Corner radii as a Material shape scale. Salla's default corner is **8px**; the system is rounded but not pill-shaped except for status chips, avatars, switches and tags.

## Scale

| Shape role | Token | Value | Figma variable | Observed on |
|---|---|---|---|---|
| None | `sys.shape.none` | 0 | `Radius/Sizes/None` | table cells, full-bleed banners |
| Extra small | `sys.shape.extra-small` | 4px ✓ | `radius/md` | Checkbox, secondary Tab, primary Tab, Tooltip, product image in MenuItem |
| Small | `sys.shape.small` | 8px ✓ | `radius/xl`, `Radius/Sizes/xl` | **Button, fields, Alert, UpgradeCard, NavigationDrawer, MoreMenu, page-size select, video thumbnail** |
| Medium | `sys.shape.medium` | 12px | `Radius/Sizes/2xl` (value not observed) | side sheets |
| Large | `sys.shape.large` | 16px ✓ | `Radius/Sizes/3xl` | LearnMore card, Dialog, BottomSheet top corners |
| Full | `sys.shape.full` | 9999px ✓ | `radius/full`, `Radius/Sizes/Full` | Status, Avatar, Switch, header tag, crown badge |

## Reference scale

`ref.radius.{none 0, sm 2, md 4, lg 6, xl 8, 2xl 12, 3xl 16, 4xl 24, 5xl 32, full}` mirrors Figma `Radius/Sizes/{None, sm, md, lg, xl, 2xl, 3xl, 4xl, 5xl, Full}`. `md`, `xl`, `3xl` and `full` were verified; the rest follow the scale.

## What the Twilight code ships today

The Storybook roundness scale matches the reference scale exactly: `rounded-sm` 2px, `rounded` 4px, `rounded-md` 6px, `rounded-lg` 8px, `rounded-xl` 12px, `rounded-2xl` 16px, `rounded-3xl` 24px, `rounded-4xl` 32px. Note the off-by-one naming against Figma: Tailwind `rounded-lg` (8px) is Figma `radius/xl` (8px) and `sys.shape.small`. The Tailwind preset in this repo exposes the Material names (`rounded-small`) so the mismatch disappears in product code.

## Issues found in Figma

- The old variable **`radius/sm` resolves to 8px** (seen on the header avatar chip and the page-size select) while `radius/xl` is also 8px. `radius/sm` must be re-pointed to 2px or the instances moved to `radius/xl`.
- `Status` hard-codes `30px` and `Radius/Sizes/full` sometimes resolves to `8888px` / `8749px` instead of `9999px` (scaled instances). All map to `sys.shape.full`.
- Header tag uses `radius/xl` overridden to `140px`; map to `sys.shape.full`.

## Rules

- Nested surfaces step down one role (LearnMore large → Button small → Chip extra-small).
- In RTL, start/end corner radii mirror automatically when written with logical properties (`border-start-start-radius`).
- Cut corners and asymmetric shapes are not used, except the MoreMenu sub-menu which squares the corner touching its parent.
