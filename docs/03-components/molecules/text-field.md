# TextField

> Single-line text entry. Absorbs the four internal Figma frames (plain, with button, with image, with character counter) as slots and props.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `Input / LingualField` |

## Props

| Prop | Values / type |
|---|---|
| `label` | string |
| `placeholder` | string |
| `helperText` | string |
| `maxLength` | number (shows counter) |
| `iconStart` | slot |
| `trailing` | slot (button \| image \| unit) |
| `bilingual` | boolean |
| `error` | string |
| `readOnly` | boolean |
| `disabled` | boolean |

## States

inherits BaseField

## Tokens

inherits BaseField

## RTL and localisation

Text direction follows the field language, not the page; the translation toggle sits inline-end in both directions.

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_TextInput` | Inputs | 28 | Language: Arabic, English; state: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True |
| `_inputWithButton` | Inputs | 28 | Language: Arabic, English; state: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True |
| `_InputWithImage` | Inputs | 28 | Language: Arabic, English; state: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True |
| `_InputCounter` | Inputs | 28 | Language: Arabic, English; state: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True |

---
_Generated from `catalog/components.json` (id `text-field`). Edit the catalog, not this file._
