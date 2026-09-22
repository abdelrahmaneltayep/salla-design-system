# DropdownList

> The floating list behind SelectField, MultiSelectField, pickers and menus: one to three layers, accordion, flags, images, checkboxes, descriptions, no-results and create-new states.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Containment | 4 - Slot / Composition | existing | `Dropdown / Select (menu)` |

## Props

| Prop | Values / type |
|---|---|
| `variant` | `one-layer`, `accordion`, `three-layers`, `no-results`, `no-results-with-add` |
| `items` | array |
| `checkbox` | boolean |
| `icon` | boolean |
| `description` | boolean |
| `searchable` | boolean |

## States

- open
- closed
- loading
- empty

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Headless layer: **useListbox / useMenu (structure 5) supplies keyboard navigation, typeahead and selection; DropdownList is the UI.**.

Composes: [ListItem](../molecules/list-item.md), [SearchField](../molecules/search-field.md), [Checkbox](../atoms/checkbox.md), [Flag](../atoms/flag.md), [Avatar](../atoms/avatar.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Drop Down List` | Drop Down List | 34 | Language: Arabic, English; Variant: Accordion, No Results, No Results with add, One Layer, One Layer - Flag, One Layer - Image, Three layers, Two Layers; Checkbox: False, True; Icon: False, True; Description: False, True |
| `_listItem` | Drop Down List | 50 | Language: Arabic, English; Variant: item, item-description, item-flag, item-image; danger: False, True; selected: False, True; disabled: false, true; feature: false, true |
| `_listTitle` | Drop Down List | 8 | Language: Arabic, English; Variant: Category, Search Active, Search Default, Subcategory |

---
_Generated from `catalog/components.json` (id `dropdown-list`). Edit the catalog, not this file._
