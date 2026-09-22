# Stepper

> Two to five step progress for wizards, desktop and mobile. Step state logic in useStepper, StepIndicator for visuals.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Navigation | 5 - Headless | existing | `Steps` |

## Props

| Prop | Values / type |
|---|---|
| `steps` | array of {label} |
| `current` | number |
| `device` | `desktop`, `mobile` |

## How to build it

Build the **logic as a headless hook / controller** (state, keyboard, focus, ARIA) and a thin UI component on top. The hook must be usable with custom UI; document it with examples since it is invisible in Figma.

Headless layer: **useStepper**.

Composes: [StepIndicator](../atoms/step-indicator.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_Step base` | Steps | 8 | Type: Active, Default, Last, Success; Language: Arabic, English |
| `Steps` | Steps | 16 | Count: 2, 3, 4, 5; Type: Desktop, Mobile; Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `stepper`). Edit the catalog, not this file._
