# Checkbox

> Bare selection control with true / false / mixed states in two sizes. The labelled version is CheckboxField.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Selection | 3 - Base + Global | existing | `Checkbox` |

## Anatomy

- box
- check / dash glyph

## Props

| Prop | Values / type |
|---|---|
| `checked` | `true`, `false`, `mixed` |
| `size` | `sm (16px)`, `md (20px)` |
| `disabled` | boolean |

## States

- default
- hover
- focus
- disabled

## Tokens

- comp.checkbox.*
- sys.color.primary (checked fill #004956)
- sys.shape.extra-small (4px)
- sys.color.outline

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **self (used by CheckboxField)**.

## Source in Figma today

- Figma node: `12411:21809`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `checkBox` | check Box | 18 | selected: false, mix, true; Status: default, disabled, focus; size: md-20px, sm-16px |

---
_Generated from `catalog/components.json` (id `checkbox`). Edit the catalog, not this file._
