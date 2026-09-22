# ProgressCircle

> Circular determinate progress (25/50/75/100 in Figma, should accept any value).

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Communication | 1 - Configurable | existing | figma | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `value` | 0-100 |
| `size` | `sm`, `md` |

## Tokens

- sys.color.primary
- sys.color.outline

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_Percentage` | Table | 4 | Type: 100%, 25%, 50%, 75% |

## Source in the Twilight Storybook today

_Not in the Twilight Storybook (dashboard-ui-components.pages.dev)._

---
_Generated from `catalog/components.json` (id `progress-circle`). Edit the catalog, not this file._
