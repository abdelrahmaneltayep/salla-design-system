# PasswordField

> Masked entry with show/hide toggle and an optional requirements checklist (112 Figma variants collapse to four props).

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `Password` |

## Props

| Prop | Values / type |
|---|---|
| `hidden` | boolean |
| `requirements` | array of {label, met} |
| `showRequirements` | boolean |

## States

inherits BaseField

## Tokens

inherits BaseField

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_passwordInput` | Inputs | 112 | Language: Arabic, English; State: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True; hidden: False, True; requirements: False, True |
| `_passwordHints` | Inputs | 6 | Variant: Pending, danger, success; Langauge: Arabic, English |
| `_passwordValidation` | Inputs | 2 | Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `password-field`). Edit the catalog, not this file._
