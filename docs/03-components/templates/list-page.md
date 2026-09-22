# ListPage

> TopAppBar + SecondaryNavBar + PageTitle + DataTable in a Panel. Figma's 'Products Management' frame is this template.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| template | Containment | 4 - Slot / Composition | existing | figma | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `header` | slot |
| `pageTitle` | slot |
| `content` | slot |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Composes: [TopAppBar](../organisms/header.md), [SecondaryNavBar](../organisms/header-subcategory.md), [PageTitle](../molecules/page-title.md), [DataTable](../organisms/table.md), [Panel](../organisms/panel.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Products Management` | (top level) | - | - |

## Source in the Twilight Storybook today

_Not in the Twilight Storybook (dashboard-ui-components.pages.dev)._

---
_Generated from `catalog/components.json` (id `list-page`). Edit the catalog, not this file._
