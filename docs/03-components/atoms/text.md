# Text

> Typography primitive exposing the Material type roles (display, headline, title, body, label) that map onto the Figma Bold/Medium/Regular $text-* styles.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Communication | 1 - Configurable | proposed | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `role` | `display-lg`, `headline-lg`, `headline-md`, `title-lg`, `title-md`, `title-sm`, `body-md`, `body-sm`, `body-xs`, `label-md`, `label-sm` |
| `color` | sys.color.text.* |
| `as` | html tag |

## Tokens

- sys.typography.*

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

- Figma styles: `Bold/$text-*, Medium/$text-*, Regular/$text-*`

_No matching frame in the current Figma library._

---
_Generated from `catalog/components.json` (id `text`). Edit the catalog, not this file._
