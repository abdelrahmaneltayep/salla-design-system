# Switch

> On/off control (Material: Switch). Has a loading state, which is unusual and worth keeping because Salla toggles often trigger a server call.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Selection | 3 - Base + Global | existing | `Toggle` |

## Anatomy

- track
- thumb
- loading spinner (in thumb)

## Props

| Prop | Values / type |
|---|---|
| `checked` | boolean |
| `size` | `sm (16px)`, `default (24px, track 39px)` |
| `loading` | boolean |
| `disabled` | boolean |

## States

- off
- on
- loading
- disabled
- focus-visible

## Tokens

- comp.toggle.*
- sys.color.primary
- sys.shape.full

## RTL and localisation

Thumb travels inline-start -> inline-end; on/off direction mirrors in RTL.

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

## Notes and migration

Figma exports the whole toggle as one SVG per variant; rebuild it from primitives so the track and thumb take tokens. Keep the name Toggle in Storybook for continuity, alias Switch in docs.

## Source in Figma today

- Figma node: `12411:21835`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Toggle` | Toggle | 20 | Language: Arabic, English; selected: false, true; disabled: false, true; loading: false, true; size: default-24px, sm-16px |

---
_Generated from `catalog/components.json` (id `toggle`). Edit the catalog, not this file._
