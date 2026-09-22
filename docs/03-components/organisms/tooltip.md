# Tooltip

> Hover / focus hint on a primary-container surface with a caret. Exists in Figma as a component set (used inside CheckboxField disabled-info) but has no top-level frame on the components page.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Communication | 5 - Headless | existing | `Tooltip` |

## Props

| Prop | Values / type |
|---|---|
| `content` | string |
| `placement` | `top`, `bottom`, `start`, `end` |

## Tokens

- comp.tooltip.*
- sys.color.primary-container (#a4ffe5)
- sys.color.on-primary-container (#004956)
- sys.typography.body-sm
- sys.elevation.3 (Shadows/lg)
- sys.shape.extra-small

## How to build it

Build the **logic as a headless hook / controller** (state, keyboard, focus, ARIA) and a thin UI component on top. The hook must be usable with custom UI; document it with examples since it is invisible in Figma.

Headless layer: **useTooltip**.

## Notes and migration

Figma guidance on the disabled-info variants: when a control is disabled because of something the merchant can change, keep the label in normal colour and put a link in the tooltip (e.g. "Verify your email to enable notifications. Verify now").

## Source in Figma today

- Figma node: `1933:1790`
- Variant filter: `--disabled=--disabled-info-tooltip`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `checkboxfield` | check Box | 16 | Language: Arabic, English; disabled: default, disabled, disabled-info, disabled-info-tooltip; selected: False, True |

---
_Generated from `catalog/components.json` (id `tooltip`). Edit the catalog, not this file._
