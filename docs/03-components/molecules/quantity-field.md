# QuantityField

> Number entry with StepperButtons, compact and default sizes, and the hot-reload (inline save) variant used in tables.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `Qty` |

## Props

| Prop | Values / type |
|---|---|
| `value` | number |
| `min` | number |
| `max` | number |
| `size` | `compact`, `default` |
| `deleteAtMin` | boolean |
| `inlineSave` | boolean |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Counter` | Inputs | 24 | State: Active, Active-Filled, Active-Filled-with-one, default, disabled, filled, filled-hover, filled-with-one, hover, preActive, read-only, read-only-with-one; error: Fals, False; size: compact, default |
| `_counter-buttons` | Inputs | 6 | variant: left, left-delete, right; disabled: False, True |
| `_quantity-hotreload` | Inputs | 10 | State: Active-Filled, default, filled, hover, preActive; error: False; Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `quantity-field`). Edit the catalog, not this file._
