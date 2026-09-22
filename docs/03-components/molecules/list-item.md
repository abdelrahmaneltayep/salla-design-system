# ListItem

> Row inside DropdownList and pickers: plain, with description, with flag, with image; supports checkbox, selected, danger, disabled and 'feature' (upsell) states.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Containment | 4 - Slot / Composition | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `leading` | slot (Flag \| Avatar \| Checkbox) |
| `title` | string |
| `description` | string |
| `trailing` | slot |
| `selected` | boolean |
| `danger` | boolean |
| `disabled` | boolean |
| `feature` | boolean |

## States

- default
- hover
- selected
- disabled

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

## Notes and migration

The PDF names this pattern listItemLayout: a slot-based layout with fixed slots. ListSubheader (_listTitle) is the category / search header variant.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_listItem` | Drop Down List | 50 | Language: Arabic, English; Variant: item, item-description, item-flag, item-image; danger: False, True; selected: False, True; disabled: false, true; feature: false, true |
| `_listTitle` | Drop Down List | 8 | Language: Arabic, English; Variant: Category, Search Active, Search Default, Subcategory |

---
_Generated from `catalog/components.json` (id `list-item`). Edit the catalog, not this file._
