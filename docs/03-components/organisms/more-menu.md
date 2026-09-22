# MoreMenu

> Overflow (kebab) menu anchored to a trigger, three layouts, left/right placement.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Containment | 4 - Slot / Composition | existing | `Dropdown Menu` |

## Props

| Prop | Values / type |
|---|---|
| `trigger` | slot (IconButton) |
| `items` | array of MenuItem \| Divider |
| `placement` | `start`, `end` |

## RTL and localisation

Placement uses logical start/end; Figma's Dir=Left/Right becomes placement=end/start under RTL.

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Headless layer: **useMenu**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_moreItems` | More Menu | 4 | Type: Icon, Image, Sperator; danger: Off, On |
| `More Menu` | More Menu | 4 | Type: Type1, Type2, Type3; Dir: Left, Off, Right |

---
_Generated from `catalog/components.json` (id `more-menu`). Edit the catalog, not this file._
