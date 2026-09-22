# AccountMenuTrigger

> Avatar + store name + chevron in the top bar that opens the account menu.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Navigation | 1 - Configurable | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `storeName` | string |
| `avatar` | Avatar props |

## States

- default
- hover
- open

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

Composes: [AvatarWithText](../molecules/avatar-with-text.md), [Icon](../atoms/icon.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `header Avatar` | Header | 2 | state: Default, hover |

---
_Generated from `catalog/components.json` (id `header-avatar`). Edit the catalog, not this file._
