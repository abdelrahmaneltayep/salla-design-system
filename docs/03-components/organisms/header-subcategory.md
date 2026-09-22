# SecondaryNavBar

> Second-level bar under the TopAppBar carrying secondary Tabs and a help / CTA area.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Navigation | 4 - Slot / Composition | existing | figma | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `tabs` | array |
| `end` | slot |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Composes: [Tab](../molecules/tab.md), [Button](../atoms/button.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Header Subcategory` | Header | 2 | device: desktop, mobile |
| `Header Secondary Tabs` | Header | 12 | Language: Arabic, English; state: active, default, hover; Contained: Off, On |

## Source in the Twilight Storybook today

_Not in the Twilight Storybook (dashboard-ui-components.pages.dev)._

---
_Generated from `catalog/components.json` (id `header-subcategory`). Edit the catalog, not this file._
