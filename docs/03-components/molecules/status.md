# Status

> StatusIndicator + label in subtle (dot + text) or strong (pill) appearance. Material: badge / chip.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Communication | 3 - Base + Global | existing | `Badge / Status` |

## Props

| Prop | Values / type |
|---|---|
| `type` | `success`, `danger`, `warning`, `info`, `neutral` |
| `appearance` | `subtle`, `strong` |
| `label` | string |

## Tokens

- comp.status.*
- sys.color.status.*.dark (dot)
- sys.color.status.*.darker (label)
- sys.color.status.*.lighter (strong background)
- sys.typography.label-sm

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **StatusIndicator**.

## Notes and migration

Table/Status carries nine order-status presets (waiting payment, in progress, shipped, delivered ...). Model those as a data mapping (order status -> Status type), not as extra variants.

## Source in Figma today

- Figma node: `15342:59936`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Status` | Status | 20 | Language: Arabic, English; Type: danger, info, neutral, success, warning; Appearance: strong, subtle |

---
_Generated from `catalog/components.json` (id `status`). Edit the catalog, not this file._
