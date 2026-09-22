# Dialog

> Centered modal (Storybook: Modal). Overlay, positioning, focus trap and close button; content via slots.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Containment | 4 - Slot / Composition | proposed | `Modal` |

## Props

| Prop | Values / type |
|---|---|
| `open` | boolean |
| `size` | `sm`, `md`, `lg` |
| `header` | slot |
| `body` | slot |
| `footer` | slot (ActionBar) |
| `dismissible` | boolean |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Headless layer: **useDialog (focus trap, escape, scroll lock)**.

## Notes and migration

Present in Storybook, missing from the Figma library. Design it in Figma from this spec.

## Source in Figma today

_No matching frame in the current Figma library._

---
_Generated from `catalog/components.json` (id `dialog`). Edit the catalog, not this file._
