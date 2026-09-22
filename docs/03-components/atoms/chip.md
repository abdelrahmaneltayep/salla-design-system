# Chip

> Compact tag used in table cells and multi-select fields. Material: assist / filter / input chip.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Selection | 1 - Configurable | existing | `Tags Input (chips inside)` |

## Anatomy

- container
- label
- optional remove icon

## Props

| Prop | Values / type |
|---|---|
| `kind` | `assist`, `filter`, `input` |
| `selected` | boolean |
| `removable` | boolean |
| `color` | `neutral`, `primary` |

## States

- default
- hover
- pressed
- selected
- disabled

## Tokens

- sys.shape.full
- sys.color.outline
- sys.typography.label-sm

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Table/Cell/Chip` | Table | 6 | Count: Multi, One; Status: Default, Hover, press |
| `_Table/Chips` | Table | 1 | Status: Gray |

---
_Generated from `catalog/components.json` (id `chip`). Edit the catalog, not this file._
