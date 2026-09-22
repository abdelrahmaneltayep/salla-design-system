# Alert

> Contextual message with icon, optional title, body, optional button and close. Four semantic variants, default / white / transparent surfaces. Also the Table-embedded variant.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Communication | 1 - Configurable | existing | `AlertBox` |

## Anatomy

- icon-start
- title
- body
- action (Button size sm)
- close icon
- inline-start accent border 3px

## Props

| Prop | Values / type |
|---|---|
| `variant` | `info`, `success`, `warning`, `danger` |
| `type` | `default`, `white` |
| `transparent` | boolean |
| `title` | string |
| `closable` | boolean |
| `action` | slot |

## States

- visible
- dismissed

## Tokens

- comp.alert.*
- sys.color.info-lighter (#ecf3fe fill)
- sys.color.info-light (#cbe0fb accent)
- sys.color.info-darker (#204374 text)
- sys.shape.small
- sys.typography.title-md / body-sm

## RTL and localisation

Accent border is border-inline-start; icon-start / close swap sides automatically.

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Notes and migration

Figma prop 'Trasnparet' -> transparent.

## Source in Figma today

- Figma node: `18843:88067 (info, default, title on)`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Alertbox` | Alertbox | 64 | Language: Arabic, English; variant: danger, info, success, warning; Type: Default, Inline, white; Title: Off, On; Trasnparet: Off, On |
| `Table/Alertbox` | Table | 4 | Hover: Off, On; Device: Desktop, Mobile |

---
_Generated from `catalog/components.json` (id `alert`). Edit the catalog, not this file._
