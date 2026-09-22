# AvatarStack

> Overlapping or spaced row of Avatars with +N overflow.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Data display | 1 - Configurable | existing | figma | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `items` | array |
| `max` | number |
| `overlapping` | boolean |
| `size` | `compact`, `default` |

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

Composes: [Avatar](../atoms/avatar.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `AvatarStack` | Avatar | 8 | overlapping: false, true; size: compact, default; Language: Arabic, English |

## Source in the Twilight Storybook today

_Not in the Twilight Storybook (dashboard-ui-components.pages.dev)._

---
_Generated from `catalog/components.json` (id `avatar-stack`). Edit the catalog, not this file._
