# TopAppBar

> Dark-teal top bar: logo, primary tabs, global search, notifications, account menu. Desktop and mobile.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Navigation | 4 - Slot / Composition | existing | `Header` |

## Props

| Prop | Values / type |
|---|---|
| `device` | `desktop`, `mobile` |
| `start` | slot (logo, drawer toggle) |
| `center` | slot (Tabs) |
| `end` | slot (GlobalSearch, IconButtons, AccountMenuTrigger) |

## Tokens

- sys.color.primary (bar fill #004956)
- sys.color.text.inverse

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Composes: [Tab](../molecules/tab.md), [GlobalSearch](../molecules/global-search.md), [IconButton](../atoms/icon-button.md), [AccountMenuTrigger](../molecules/header-avatar.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Header` | Header | 2 | device: desktop, mobile |
| `Primary Tabs List - Dashboard only` | Header | 2 | Language: Arabic, English |
| `Header Primary Tabs` | (top level) | - | - |

---
_Generated from `catalog/components.json` (id `header`). Edit the catalog, not this file._
