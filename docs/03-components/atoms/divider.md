# Divider

> Horizontal or vertical rule. Exists implicitly as the Separator variants inside Breadcrumb and MoreMenu.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Containment | 1 - Configurable | proposed | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `orientation` | `horizontal`, `vertical` |
| `inset` | boolean |

## Tokens

- sys.color.outline

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

- Variant filter: `Type=Separator | Sperator`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_breadcrumbItem` | Bread crumb | 20 | Language: Arabic, English; Status: active, default, disabled, hover, onclick; Type: Icon, More, Separator, Text |
| `_moreItems` | More Menu | 4 | Type: Icon, Image, Sperator; danger: Off, On |

---
_Generated from `catalog/components.json` (id `divider`). Edit the catalog, not this file._
