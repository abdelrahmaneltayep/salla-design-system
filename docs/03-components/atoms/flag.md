# Flag

> Country flag glyphs, one per ISO 3166 code (265 in Figma).

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Data display | 2 - Standalone | existing | figma | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `code` | ISO 3166-1 alpha-2 |
| `size` | `sm`, `md` |

## Tokens

- ref.size.icon.*

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

## Notes and migration

Ship as a sprite or lazy-loaded SVGs; do not bundle 265 inline SVGs in the base package.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Flag` | (top level) | - | - |

## Source in the Twilight Storybook today

_Not in the Twilight Storybook (dashboard-ui-components.pages.dev)._

---
_Generated from `catalog/components.json` (id `flag`). Edit the catalog, not this file._
