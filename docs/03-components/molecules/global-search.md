# GlobalSearch

> Header search: collapsed button-only or full field.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 1 - Configurable | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `variant` | `btn-only`, `full` |

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

Composes: [SearchField](../molecules/search-field.md), [IconButton](../atoms/icon-button.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `searchbar` | (top level) | - | - |

---
_Generated from `catalog/components.json` (id `global-search`). Edit the catalog, not this file._
