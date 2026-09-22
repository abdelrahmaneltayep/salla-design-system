# Tooltip

> Hover / focus hint. Implied by CheckboxField's disabled-info-tooltip variant but not a component yet.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Communication | 5 - Headless | proposed | `Tooltip` |

## Props

| Prop | Values / type |
|---|---|
| `content` | string |
| `placement` | `top`, `bottom`, `start`, `end` |

## How to build it

Build the **logic as a headless hook / controller** (state, keyboard, focus, ARIA) and a thin UI component on top. The hook must be usable with custom UI; document it with examples since it is invisible in Figma.

Headless layer: **useTooltip**.

## Source in Figma today

- Variant filter: `--disabled=--disabled-info-tooltip`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `checkboxfield` | check Box | 16 | Language: Arabic, English; disabled: default, disabled, disabled-info, disabled-info-tooltip; selected: False, True |

---
_Generated from `catalog/components.json` (id `tooltip`). Edit the catalog, not this file._
