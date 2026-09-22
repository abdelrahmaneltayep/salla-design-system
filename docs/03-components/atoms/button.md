# Button

> The single action trigger. Seven colour variants x four appearances x three sizes x five states, plus a circular layout for icon-only use.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Actions | 1 - Configurable | existing | `Button` |

## Anatomy

- container
- icon-start (slot)
- label
- icon-end (slot)

## Props

| Prop | Values / type |
|---|---|
| `variant` | `primary`, `secondary`, `danger`, `success`, `warning`, `info`, `feature` |
| `appearance` | `filled`, `outlined`, `link`, `link-auxiliary` |
| `size` | `sm (32px)`, `md (40px)`, `lg (48px)` |
| `layout` | `default`, `circular` |
| `iconStart` | slot |
| `iconEnd` | slot |
| `loading` | boolean |
| `disabled` | boolean |

## States

- default
- hover
- pressed
- loading
- disabled
- focus-visible

## Tokens

- comp.button.*
- sys.color.primary-container (primary filled fill #a4ffe5)
- sys.color.text.brand (primary label #004956)
- sys.color.status.*.primary (danger #f55157, success #00af6c, warning #ffaf44, info #5196f3)
- sys.color.feature.* (gradient orange 200->300, label orange 800)
- sys.shape.small (8px)
- sys.typography.label-md

## RTL and localisation

iconStart/iconEnd are logical (inline-start / inline-end) and swap automatically under dir=rtl; do not mirror non-directional glyphs.

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Notes and migration

Figma variant values carry a leading `--` (--primary); drop it in code. The 'link' appearance is a Button in Figma but reads as a Link to users; expose it as `Link` (see link.md) built on the same base. `feature` is a non-semantic upsell accent and must stay out of the semantic status palette.

## Source in Figma today

- Figma node: `14526:107536`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Button` | (top level) | - | - |

---
_Generated from `catalog/components.json` (id `button`). Edit the catalog, not this file._
