# LoadingIndicator

> Spinner, dots or line progress in nine sizes from 8px to 88px.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Communication | 1 - Configurable | existing | `Loader` |

## Anatomy

- animated shape

## Props

| Prop | Values / type |
|---|---|
| `type` | `spinner`, `dots`, `line` |
| `size` | `xxxxs 8`, `xxxs 16`, `xxs 20`, `xs 24`, `sm 32`, `md 48`, `lg 56`, `xl 64`, `xxl 88` |

## Tokens

- comp.loader.*
- sys.color.primary

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Notes and migration

Nine sizes is more than the rest of the system uses (three to six). Recommend collapsing to xs/sm/md/lg/xl and mapping the rest as aliases.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_LoadingIndicator` | Loader | 27 | Size: lg- 56px, md- 48px, sm- 32px, xl- 64px, xs- 24px, xxl- 88px, xxs- 20px, xxxs- 16px, xxxxs-8px; Type: Dots, Line, Spinner |

---
_Generated from `catalog/components.json` (id `loading-indicator`). Edit the catalog, not this file._
