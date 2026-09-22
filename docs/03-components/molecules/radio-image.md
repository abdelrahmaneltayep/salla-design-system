# RadioImage

> Selectable image card (visual radio) for templates, themes, layouts.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Selection | 2 - Standalone | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `image` | src |
| `label` | string |
| `selected` | boolean |

## States

- default
- hover
- selected

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

Composes: [Radio](../atoms/radio.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `radioImage` | radio Buttton | 3 | state: defaullt, hover, selected |

---
_Generated from `catalog/components.json` (id `radio-image`). Edit the catalog, not this file._
