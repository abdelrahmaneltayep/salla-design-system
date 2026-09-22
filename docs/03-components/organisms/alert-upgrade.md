# UpgradeCard

> Plan-upgrade promo card, desktop and mobile. Uses the feature accent.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Communication | 2 - Standalone | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `device` | `desktop`, `mobile` |
| `title` | string |
| `cta` | Button |

## Tokens

- sys.color.feature.*

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Alertbox_Upgrade` | Alertbox | 2 | Device: Desktop, Mobile |

---
_Generated from `catalog/components.json` (id `alert-upgrade`). Edit the catalog, not this file._
