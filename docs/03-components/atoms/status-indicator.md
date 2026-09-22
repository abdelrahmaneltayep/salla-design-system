# StatusIndicator

> The 10px coloured dot. Base of Status.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Communication | 1 - Configurable | existing | _not in Storybook_ |

## Anatomy

- dot

## Props

| Prop | Values / type |
|---|---|
| `color` | `success`, `danger`, `warning`, `info`, `neutral` |
| `size` | `xs`, `sm`, `md`, `lg`, `xl`, `2xl` |

## Tokens

- sys.color.status.*.dark (success #008c56, danger #ca4146)
- sys.shape.full

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_Base Status Indicator` | Status | 30 | Color: danger, info, neutral, success, warning; Size: 2xl, lg, md, sm, xl, xs |

---
_Generated from `catalog/components.json` (id `status-indicator`). Edit the catalog, not this file._
