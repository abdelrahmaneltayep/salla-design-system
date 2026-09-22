# FilterResults

> Applied-filters summary bar above a table with a clear action.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Communication | 1 - Configurable | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `filters` | array of Chip |
| `onClear` | fn |

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

Composes: [Chip](../atoms/chip.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_Table/Filter Results` | Table | 2 | Type: Close, Default |

---
_Generated from `catalog/components.json` (id `filter-results`). Edit the catalog, not this file._
