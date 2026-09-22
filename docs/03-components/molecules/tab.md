# Tab

> One tab, primary (dashboard top nav) or secondary (page sub-nav), contained or plain, with active/hover states.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Navigation | 1 - Configurable | existing | `Tabs (item)` |

## Props

| Prop | Values / type |
|---|---|
| `kind` | `primary`, `secondary` |
| `contained` | boolean |
| `active` | boolean |
| `icon` | slot |
| `count` | number |

## States

- default
- hover
- active
- focus-visible

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Header Secondary Tabs` | Header | 12 | Language: Arabic, English; state: active, default, hover; Contained: Off, On |
| `Primary Tabs List - Dashboard only` | Header | 2 | Language: Arabic, English |
| `_Table/Tabs Item` | Table | 2 | Active: Off, On |
| `Header Primary Tabs` | (top level) | - | - |

---
_Generated from `catalog/components.json` (id `tab`). Edit the catalog, not this file._
