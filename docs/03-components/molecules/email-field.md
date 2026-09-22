# EmailField

> TextField pre-configured with type=email, mail icon and email validation.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `validate` | boolean |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_emailInput` | Inputs | 28 | State: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True; Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `email-field`). Edit the catalog, not this file._
