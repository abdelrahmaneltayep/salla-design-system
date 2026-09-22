# SelectField

> Single-choice dropdown field. The 'basic' Figma variant (no search) is a prop, not a separate component.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `Select` |

## Props

| Prop | Values / type |
|---|---|
| `options` | array |
| `searchable` | boolean |
| `allowCreate` | boolean (Add new value) |
| `placeholder` | string |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

Composes: [DropdownList](../organisms/dropdown-list.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_dropdown-single` | Inputs | 29 | Language: Arabic, English; state: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True; Add new value: Off, On |
| `basic-dropdown-single` | Inputs | 29 | State: Active, Active-Filled, default, disabled, filled, filled-hover, hover, preActive, read-only; error: False, True; Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `select-field`). Edit the catalog, not this file._
