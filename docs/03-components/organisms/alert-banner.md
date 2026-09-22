# AlertBanner

> Full-width page-level announcement (two layouts). Distinct layout and purpose from Alert, so standalone.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Communication | 2 - Standalone | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `layout` | `1`, `2` |
| `title` | string |
| `action` | slot |
| `dismissible` | boolean |

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Alertbox_Banner` | Alertbox | 2 | Type: Type1, Type2 |

---
_Generated from `catalog/components.json` (id `alert-banner`). Edit the catalog, not this file._
