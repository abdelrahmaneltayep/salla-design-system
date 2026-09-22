# BulkEditSheet

> Side sheet opened from the DataTable bulk bar to edit selected rows.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Containment | 4 - Slot / Composition | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `open` | boolean |
| `header` | slot |
| `body` | slot |
| `footer` | slot (ActionBar) |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Table/Bulk Edit Sheet` | Table | 2 | Open: Off, On |

---
_Generated from `catalog/components.json` (id `bulk-edit-sheet`). Edit the catalog, not this file._
