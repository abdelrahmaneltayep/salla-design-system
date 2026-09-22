# Toast

> Transient bottom notification (Material: snackbar). Missing from both Figma and Storybook; production uses ad-hoc notifications.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Communication | 1 - Configurable | proposed | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `variant` | `info`, `success`, `warning`, `danger` |
| `action` | slot |
| `duration` | ms |

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

_No matching frame in the current Figma library._

---
_Generated from `catalog/components.json` (id `toast`). Edit the catalog, not this file._
