# NavigationItem

> One entry of the side navigation (first / middle / last for grouping radius).

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Navigation | 1 - Configurable | existing | figma | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `label` | string |
| `icon` | slot |
| `active` | boolean |
| `position` | `first`, `middle`, `last` |
| `badge` | number |

## States

- default
- hover
- active

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `sidemenu tab` | Side menu | 9 | status: active, default, hover; variant: first, last, middle |

## Source in the Twilight Storybook today

_Not in the Twilight Storybook (dashboard-ui-components.pages.dev)._

---
_Generated from `catalog/components.json` (id `side-menu-item`). Edit the catalog, not this file._
