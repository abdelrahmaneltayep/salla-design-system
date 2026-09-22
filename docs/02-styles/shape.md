# Shape

Corner radii as a Material shape scale. Salla's default corner is **8px**; the system is rounded but not pill-shaped except for status chips, avatars and switches.

## Scale

| Shape role | Token | Value | Figma variable | Used by |
|---|---|---|---|---|
| None | `sys.shape.none` | 0 | `Radius/Sizes/None` | table cells, full-bleed banners |
| Extra small | `sys.shape.extra-small` | 4px ✓ | `radius/md` | Checkbox ✓, chips inside fields, tooltip |
| Small | `sys.shape.small` | 8px ✓ | `radius/xl` | **Button ✓, fields ✓, Alert ✓, MenuItem, ListItem** |
| Medium | `sys.shape.medium` | 12px | `Radius/Sizes/2xl` (assumed) | Panel, DropdownList surface, side sheets |
| Large | `sys.shape.large` | 16px | `Radius/Sizes/3xl` (assumed) | Dialog, BottomSheet top corners |
| Full | `sys.shape.full` | 9999px ✓ | `radius/full` | Status ✓, Avatar circular, Switch, IconButton circular, AvatarStack |

## Reference scale

`ref.radius.{none 0, sm 2, md 4, lg 6, xl 8, 2xl 12, 3xl 16, 4xl 24, 5xl 32, full}` mirrors Figma's `Radius/Sizes/{None, sm, md, lg, xl, 2xl, 3xl, 4xl, 5xl, Full}`. Only `md`, `xl` and `full` were verified; the rest follow the Tailwind scale and must be confirmed.

## Rules

- Nested surfaces step down one shape role (Panel medium → field small → chip extra-small).
- The `Status` component hard-codes `30px`; replace with `sys.shape.full`.
- Cut corners and asymmetric shapes are not used.
- In RTL, start/end corner radii mirror automatically when written with logical properties (`border-start-start-radius`).
