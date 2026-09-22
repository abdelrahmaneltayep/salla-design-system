# Breadcrumb

> Path navigation with icon, text, more (…) and separator items; collapses past 5 items and on mobile.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Navigation | 4 - Slot / Composition | existing | `Breadcrumb` |

## Props

| Prop | Values / type |
|---|---|
| `items` | array of {label, href, icon} |
| `maxItems` | number |
| `device` | `desktop`, `mobile` |

## States

- item: default, hover, active, disabled, pressed

## RTL and localisation

Separator chevron mirrors in RTL.

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Composes: [BreadcrumbItem](../molecules/breadcrumb-item.md), [Divider](../atoms/divider.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_breadcrumbItem` | Bread crumb | 20 | Language: Arabic, English; Status: active, default, disabled, hover, onclick; Type: Icon, More, Separator, Text |
| `Breadcrumb` | Bread crumb | 12 | Language: Arabic, English; count: 2, 3, >5; device: Desktop, Mobile |

---
_Generated from `catalog/components.json` (id `breadcrumb`). Edit the catalog, not this file._
