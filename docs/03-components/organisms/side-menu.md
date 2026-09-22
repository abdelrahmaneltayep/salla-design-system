# NavigationDrawer

> The dashboard side navigation (Material: navigation drawer) composed of NavigationItems and section headers.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Navigation | 4 - Slot / Composition | existing | figma | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `sections` | array |
| `collapsed` | boolean |
| `disabled` | boolean |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Composes: [NavigationItem](../molecules/side-menu-item.md), [Divider](../atoms/divider.md), [Icon](../atoms/icon.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Side menu` | Side menu | 2 | Status: default, disabled |
| `sidemenu tab` | Side menu | 9 | status: active, default, hover; variant: first, last, middle |

## Source in the Twilight Storybook today

_Not in the Twilight Storybook (dashboard-ui-components.pages.dev)._

---
_Generated from `catalog/components.json` (id `side-menu`). Edit the catalog, not this file._
