# Toast

> Transient bottom notification (Material: snackbar). Missing from both Figma and Storybook; production uses ad-hoc notifications.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Communication | 1 - Configurable | proposed | none yet | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `variant` | `info`, `success`, `warning`, `danger` |
| `action` | slot |
| `duration` | ms |

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Notes and migration

Missing from both Figma and Storybook; the dashboard uses react-toastify (see --toastify-z-index in the Twilight root variables). Specify it as a component.

## Source in Figma today

_No matching frame in the current Figma library._

## Source in the Twilight Storybook today

_Not in the Twilight Storybook (dashboard-ui-components.pages.dev)._

---
_Generated from `catalog/components.json` (id `toast`). Edit the catalog, not this file._
