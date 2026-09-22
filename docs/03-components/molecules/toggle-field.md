# SwitchField

> Switch + label with the switch at inline-start or inline-end.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Selection | 3 - Base + Global | existing | `Toggle` |

## Props

| Prop | Values / type |
|---|---|
| `label` | string |
| `description` | string |
| `position` | `start`, `end` |
| `checked` | boolean |
| `loading` | boolean |
| `disabled` | boolean |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **Switch**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `toggleField` | Toggle | 20 | Language: Arabic, English; togglePosition: ending, starting; disabled: false, true; selected: false, true; loading: false, true |

---
_Generated from `catalog/components.json` (id `toggle-field`). Edit the catalog, not this file._
