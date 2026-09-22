# Pagination

> Table footer: page size, range label, previous / next and page numbers. Desktop and mobile.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Navigation | 1 - Configurable | existing | `Pagination` |

## Props

| Prop | Values / type |
|---|---|
| `page` | number |
| `pageSize` | number |
| `total` | number |
| `device` | `desktop`, `mobile` |

## RTL and localisation

Previous / next chevrons mirror in RTL.

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Table/Footer` | Table | 2 | Device: Desktop, Mobile |

---
_Generated from `catalog/components.json` (id `pagination`). Edit the catalog, not this file._
