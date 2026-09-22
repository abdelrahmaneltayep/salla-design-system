# IconButton

> Icon-only button. Today this is Button with Layout=--circular and no label; promote it to a named global component so the accessible name is a required prop.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Actions | 3 - Base + Global | proposed | _not in Storybook_ |

## Anatomy

- container (circular)
- icon

## Props

| Prop | Values / type |
|---|---|
| `variant` | same as Button |
| `appearance` | `filled`, `outlined`, `ghost` |
| `size` | `sm`, `md`, `lg` |
| `ariaLabel` | string (required) |

## States

- default
- hover
- pressed
- loading
- disabled
- focus-visible

## Tokens

- comp.button.*
- sys.shape.full

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseButton**.

## Notes and migration

Replaces the ad-hoc icon buttons inside Table (_Table/Refresh Button, _Table/Pin, Table/Cell/Actions icons).

## Source in Figma today

- Variant filter: `Layout=--circular`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Button` | (top level) | - | - |

---
_Generated from `catalog/components.json` (id `icon-button`). Edit the catalog, not this file._
