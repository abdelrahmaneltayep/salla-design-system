# RadioField

> Radio + label, used inside a RadioGroup.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Selection | 3 - Base + Global | existing | `Radio` |

## Props

| Prop | Values / type |
|---|---|
| `label` | string |
| `value` | string |
| `disabled` | boolean |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **Radio**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `radiofield` | radio Buttton | 8 | Language: Arabic, English; disabled: false, true; selected: false, true |

---
_Generated from `catalog/components.json` (id `radio-field`). Edit the catalog, not this file._
