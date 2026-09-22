# Illustration

> Spot illustrations for empty states and onboarding, with web and mobile variants.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Communication | 2 - Standalone | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `name` | one of the 20 collection names (add products, no codes, order filters empty ...) |
| `device` | `web`, `mobile` |

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

## Notes and migration

See docs/02-styles/illustrations.md for the full list and usage rules.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Illustrations Collection` | (top level) | - | - |
| `Illustration` | (top level) | - | - |

---
_Generated from `catalog/components.json` (id `illustration`). Edit the catalog, not this file._
