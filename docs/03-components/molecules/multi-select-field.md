# MultiSelectField

> Multi-choice dropdown field rendering selections as Chips (Storybook: Tags Input).

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `Tags Input / Multi Select` |

## Props

| Prop | Values / type |
|---|---|
| `options` | array |
| `searchable` | boolean |
| `allowCreate` | boolean |
| `maxVisibleChips` | number |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

Composes: [DropdownList](../organisms/dropdown-list.md), [Chip](../atoms/chip.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_dropdown-multiple` | Inputs | 29 | State: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True; Language: Arabic, English; Add new value: Off, On |
| `basic-dropdown-multiple` | Inputs | 28 | State: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True; Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `multi-select-field`). Edit the catalog, not this file._
