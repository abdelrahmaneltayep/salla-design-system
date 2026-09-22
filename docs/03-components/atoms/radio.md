# Radio

> Bare single-choice control in two sizes. RadioField, RadioImage and RadioColor build on it.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Selection | 3 - Base + Global | existing | `Radio` |

## Anatomy

- ring
- dot

## Props

| Prop | Values / type |
|---|---|
| `checked` | boolean |
| `size` | `sm`, `md` |
| `disabled` | boolean |

## States

- default
- focus
- disabled

## Tokens

- sys.color.primary
- sys.shape.full
- sys.color.outline

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `radio` | radio Buttton | 12 | Active: Off, On; Status: Default, Disabled, Focus; size: md, sm |

---
_Generated from `catalog/components.json` (id `radio`). Edit the catalog, not this file._
