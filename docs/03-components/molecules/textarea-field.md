# TextareaField

> Multi-line text entry with optional rich-text toolbar.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `Textarea` |

## Props

| Prop | Values / type |
|---|---|
| `rows` | number |
| `richText` | boolean |
| `maxLength` | number |
| `autoResize` | boolean |

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
| `_TextArea` | Inputs | 56 | State: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: Fals, False, True; Language: Arabic, English; Rich text: No, Yes |
| `_Rich-Text-Panel` | Inputs | 2 | Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `textarea-field`). Edit the catalog, not this file._
