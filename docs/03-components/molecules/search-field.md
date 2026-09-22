# SearchField

> Search entry with magnifier, clear button, recommendations and no-results states.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `Search` |

## Props

| Prop | Values / type |
|---|---|
| `suggestions` | array |
| `loading` | boolean |
| `onClear` | fn |

## States

- default
- hover
- active
- filled
- active-filled
- recommendation
- no-result

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `searchInput` | Inputs | 16 | State: Active, Active-Filled, Active-Filled-noResult, Active-recommendation, default, filled, hover, preActive; error: False; Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `search-field`). Edit the catalog, not this file._
