# EditSheet

> Inline edit side sheet for one row (default and minimum-cells layouts).

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Containment | 4 - Slot / Composition | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `open` | boolean |
| `layout` | `default`, `min-cells` |
| `body` | slot |
| `footer` | slot |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Table/Edit Sheet` | Table | 2 | Type: Default, Min Cells |

---
_Generated from `catalog/components.json` (id `edit-sheet`). Edit the catalog, not this file._
