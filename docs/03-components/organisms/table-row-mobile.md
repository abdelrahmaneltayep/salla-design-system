# MobileRow

> Card-style row for phones: order, product, customer and default layouts.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Data display | 2 - Standalone | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `kind` | `default`, `order`, `product`, `customer` |
| `selected` | boolean |

## States

- default
- hover
- focus
- selected

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Table/mobile Order` | Table | 6 | Type: Default, Focus, Hover; Selected: Off, On; Deleted: Off |
| `Table/mobile Default` | Table | 6 | Type: Default, Focus, Hover; Selected: Off, On; Deleted: Off |
| `Table/mobile Product` | Table | 6 | Type: Default, Focus, Hover; Selected: Off, On; Deleted: Off |
| `Table/mobile Customer` | Table | 6 | Type: Default, Focus, Hover; Selected: Off, On; Deleted: Off |

---
_Generated from `catalog/components.json` (id `table-row-mobile`). Edit the catalog, not this file._
