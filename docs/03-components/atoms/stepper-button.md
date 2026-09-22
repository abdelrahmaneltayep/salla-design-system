# StepperButton

> The +/- buttons flanking QuantityField, including the delete-at-one variant.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Actions | 1 - Configurable | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `action` | `increment`, `decrement`, `delete` |
| `disabled` | boolean |

## States

- default
- hover
- disabled

## Tokens

- sys.color.outline
- sys.shape.small

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_counter-buttons` | Inputs | 6 | variant: left, left-delete, right; disabled: False, True |

---
_Generated from `catalog/components.json` (id `stepper-button`). Edit the catalog, not this file._
