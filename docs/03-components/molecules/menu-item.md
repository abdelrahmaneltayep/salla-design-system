# MenuItem

> Row inside MoreMenu: icon or image + label, optional danger tone; separators become Divider.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Containment | 1 - Configurable | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `leading` | `icon`, `image`, `none` |
| `label` | string |
| `danger` | boolean |
| `disabled` | boolean |

## States

- default
- hover
- pressed
- disabled

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_moreItems` | More Menu | 4 | Type: Icon, Image, Sperator; danger: Off, On |

---
_Generated from `catalog/components.json` (id `menu-item`). Edit the catalog, not this file._
