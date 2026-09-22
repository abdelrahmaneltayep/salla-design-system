# EmptyState

> Illustration + title + description + action for empty lists and no-results.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Communication | 4 - Slot / Composition | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `illustration` | Illustration name |
| `title` | string |
| `description` | string |
| `action` | slot (Button) |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Composes: [Illustration](../atoms/illustration.md), [Button](../atoms/button.md).

## Source in Figma today

- Related: Table Status=No Results, Drop Down List Variant=No Results

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Illustrations Collection` | (top level) | - | - |

---
_Generated from `catalog/components.json` (id `empty-state`). Edit the catalog, not this file._
