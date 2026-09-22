# BaseField (internal)

> The internal base for every field: label + container (icon-start, control, subtext/unit, translation toggle, info) + helper text. Not exported. Today this role is played by InputWrapper, a 24-variant god component; splitting it into a base and named globals is the main structural change in Text inputs.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `Input (base)` |

## Anatomy

- FieldLabel
- container
- icon-start (slot)
- control (slot)
- subtext / unit
- TranslationToggle
- info icon
- HelperText

## Props

| Prop | Values / type |
|---|---|
| `state` | `default`, `hover`, `pre-active`, `active`, `filled`, `active-filled`, `read-only`, `disabled` |
| `error` | boolean |
| `language` | `ar`, `en` |

## States

- default
- hover
- pre-active
- active
- filled
- active-filled
- read-only
- disabled
- error

## Tokens

- comp.text-field.*
- sys.color.surface-input
- sys.color.outline (#eee)
- sys.color.text.secondary (placeholder #666)
- sys.shape.small

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

## Notes and migration

Eight interaction states is more than a screen reader or CSS needs. Collapse to: enabled, hover, focus, filled, read-only, disabled, plus an orthogonal error flag.

## Source in Figma today

- Figma node: `InputWrapper 4d4e5f6d`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_TextInput` | Inputs | 28 | Language: Arabic, English; state: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True |
| `InputWrapper` | Inputs | 24 | Variant: Search, amount, color picker, dropdown-multiple, dropdown-single, dropdown-single-basic, email, password, phone, texArea, text, upload; Langauge: Arabic, English |
| `_inputLabel` | Inputs | 2 | Language: Arabic, English |
| `_Text-cursor` | Inputs | 2 | State: Not visible, Visible |
| `_inputTip` | Inputs | 10 | Type: Danger, Default, Delete File, Variables, character count; Langauge: Arabic, English |

---
_Generated from `catalog/components.json` (id `base-field`). Edit the catalog, not this file._
