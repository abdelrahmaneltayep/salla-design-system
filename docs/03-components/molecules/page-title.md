# PageTitle

> Page heading row: back / breadcrumb, title, optional status and actions slot. Desktop and mobile layouts.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Navigation | 4 - Slot / Composition | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `title` | string |
| `leading` | slot (Breadcrumb \| back) |
| `meta` | slot (Status) |
| `actions` | slot (Buttons) |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Page Title` | Header | 2 | device: desktop, mobile |

---
_Generated from `catalog/components.json` (id `page-title`). Edit the catalog, not this file._
