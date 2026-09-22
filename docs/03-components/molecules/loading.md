# Loading

> LoadingIndicator + localised label for block-level loading.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Communication | 3 - Base + Global | existing | `Loader` |

## Props

| Prop | Values / type |
|---|---|
| `label` | string |
| `size` | LoadingIndicator size |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **LoadingIndicator**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Loading` | Loader | 2 | Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `loading`). Edit the catalog, not this file._
