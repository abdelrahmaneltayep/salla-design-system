# BreadcrumbItem

> One breadcrumb node: icon, text or overflow menu trigger.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Navigation | 1 - Configurable | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `type` | `icon`, `text`, `more` |
| `current` | boolean |
| `disabled` | boolean |

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_breadcrumbItem` | Bread crumb | 20 | Language: Arabic, English; Status: active, default, disabled, hover, onclick; Type: Icon, More, Separator, Text |

---
_Generated from `catalog/components.json` (id `breadcrumb-item`). Edit the catalog, not this file._
