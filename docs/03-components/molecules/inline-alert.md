# InlineAlert

> Compact, non-dismissible alert placed under a field or inside a card (Alertbox Type=Inline).

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Communication | 3 - Base + Global | existing | `AlertBox (inline)` |

## Props

| Prop | Values / type |
|---|---|
| `variant` | `info`, `success`, `warning`, `danger` |
| `text` | string |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseAlert**.

## Source in Figma today

- Variant filter: `Type=Inline`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Alertbox` | Alertbox | 64 | Language: Arabic, English; variant: danger, info, success, warning; Type: Default, Inline, white; Title: Off, On; Trasnparet: Off, On |

---
_Generated from `catalog/components.json` (id `inline-alert`). Edit the catalog, not this file._
