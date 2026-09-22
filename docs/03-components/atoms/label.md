# FieldLabel

> Label line above a field: text, optional required mark, optional info icon.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Text inputs | 1 - Configurable | existing | figma | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `text` | string |
| `required` | boolean |
| `info` | string (tooltip) |
| `htmlFor` | string |

## Tokens

- sys.typography.label-md
- sys.color.text.primary

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_inputLabel` | Inputs | 2 | Language: Arabic, English |

## Source in the Twilight Storybook today

_Not in the Twilight Storybook (dashboard-ui-components.pages.dev)._

---
_Generated from `catalog/components.json` (id `label`). Edit the catalog, not this file._
