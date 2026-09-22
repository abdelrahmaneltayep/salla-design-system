# PasswordHint

> One requirement line (pending / success / danger) used by PasswordField.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Communication | 1 - Configurable | existing | figma | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `state` | `pending`, `success`, `danger` |
| `text` | string |

## Tokens

- sys.typography.body-xs
- sys.color.status.*

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_passwordHints` | Inputs | 6 | Variant: Pending, danger, success; Langauge: Arabic, English |
| `_passwordValidation` | Inputs | 2 | Language: Arabic, English |

## Source in the Twilight Storybook today

_Not in the Twilight Storybook (dashboard-ui-components.pages.dev)._

---
_Generated from `catalog/components.json` (id `password-hint`). Edit the catalog, not this file._
