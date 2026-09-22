# StepIndicator

> One node of the Stepper: number or check in a circle with a connector.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Navigation | 1 - Configurable | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `state` | `default`, `active`, `success` |
| `last` | boolean |
| `index` | number |

## Tokens

- sys.color.primary
- sys.color.success-primary
- sys.shape.full

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_Step base` | Steps | 8 | Type: Active, Default, Last, Success; Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `step-indicator`). Edit the catalog, not this file._
