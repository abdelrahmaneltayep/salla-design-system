# Tabs

> Tab list + panels. Keyboard, roving focus and selection live in useTabs; Tab supplies the visuals.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Navigation | 5 - Headless | existing | `Tabs` |

## Props

| Prop | Values / type |
|---|---|
| `kind` | `primary`, `secondary`, `contained` |
| `value` | string |
| `items` | array |

## How to build it

Build the **logic as a headless hook / controller** (state, keyboard, focus, ARIA) and a thin UI component on top. The hook must be usable with custom UI; document it with examples since it is invisible in Figma.

Headless layer: **useTabs**.

Composes: [Tab](../molecules/tab.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Header Secondary Tabs` | Header | 12 | Language: Arabic, English; state: active, default, hover; Contained: Off, On |
| `Primary Tabs List - Dashboard only` | Header | 2 | Language: Arabic, English |
| `_Table/Tabs Item` | Table | 2 | Active: Off, On |

---
_Generated from `catalog/components.json` (id `tabs`). Edit the catalog, not this file._
