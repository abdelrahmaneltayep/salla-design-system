# HelperText

> Line under a field: hint, error, character count, variables hint or file delete action.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Text inputs | 1 - Configurable | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `type` | `default`, `danger`, `character-count`, `variables`, `delete-file` |
| `text` | string |

## Tokens

- sys.typography.body-xs
- sys.color.text.secondary
- sys.color.status.danger.primary

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_inputTip` | Inputs | 10 | Type: Danger, Default, Delete File, Variables, character count; Langauge: Arabic, English |

---
_Generated from `catalog/components.json` (id `helper-text`). Edit the catalog, not this file._
