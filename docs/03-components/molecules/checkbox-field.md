# CheckboxField

> Checkbox + label + optional description / info tooltip.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Selection | 3 - Base + Global | existing | `Checkbox` |

## Props

| Prop | Values / type |
|---|---|
| `label` | string |
| `description` | string |
| `info` | string (tooltip) |
| `checked` | boolean \| mixed |
| `disabled` | boolean |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **Checkbox**.

Composes: [Checkbox](../atoms/checkbox.md), [Tooltip](../organisms/tooltip.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `checkboxfield` | check Box | 16 | Language: Arabic, English; disabled: default, disabled, disabled-info, disabled-info-tooltip; selected: False, True |

---
_Generated from `catalog/components.json` (id `checkbox-field`). Edit the catalog, not this file._
