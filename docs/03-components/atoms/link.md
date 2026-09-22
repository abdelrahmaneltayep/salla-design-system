# Link

> Inline text action. Built on BaseButton with the `link` and `link-auxiliary` appearances so it shares focus, disabled and loading logic with Button.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Actions | 3 - Base + Global | proposed | _not in Storybook_ |

## Anatomy

- label
- optional icon

## Props

| Prop | Values / type |
|---|---|
| `variant` | `primary`, `secondary`, `danger`, `success`, `warning`, `info` |
| `auxiliary` | boolean |
| `href` | string |
| `external` | boolean |

## States

- default
- hover
- pressed
- disabled
- focus-visible
- visited

## Tokens

- sys.color.text.brand
- sys.typography.label-md

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseButton**.

## Source in Figma today

- Variant filter: `Appearance=--link | --link-auxiliary`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Button` | (top level) | - | - |

---
_Generated from `catalog/components.json` (id `link`). Edit the catalog, not this file._
