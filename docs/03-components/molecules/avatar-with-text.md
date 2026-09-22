# AvatarWithText

> Avatar + primary and secondary text lines (customer, product, staff rows).

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Data display | 4 - Slot / Composition | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `avatar` | Avatar props |
| `title` | slot |
| `subtitle` | slot |
| `trailing` | slot |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Composes: [Avatar](../atoms/avatar.md), [Text](../atoms/text.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `header Avatar` | Header | 2 | state: Default, hover |
| `AvatarWithText` | Avatar | 2 | Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `avatar-with-text`). Edit the catalog, not this file._
