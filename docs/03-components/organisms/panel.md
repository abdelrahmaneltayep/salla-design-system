# Panel

> Card container with PanelHeader, body and footer slots (Storybook: Panel). Material: card.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Containment | 4 - Slot / Composition | proposed | `Panel` |

## Props

| Prop | Values / type |
|---|---|
| `header` | slot (PanelHeader) |
| `body` | slot |
| `footer` | slot |
| `elevation` | `0`, `1` |

## Tokens

- sys.color.surface
- sys.color.outline
- sys.shape.medium
- sys.elevation.1

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

## Notes and migration

Present in Storybook and production, missing as a top-level frame in Figma.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `previewContainer` | Table | 2 | Type: Blog, Default |
| `_Table/Panel Header` | Table | 2 | Size: Default, Small |

---
_Generated from `catalog/components.json` (id `panel`). Edit the catalog, not this file._
