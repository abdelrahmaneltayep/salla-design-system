# OtpField

> Single-digit boxes for verification codes.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `length` | number (default 4-6) |
| `autoSubmit` | boolean |

## RTL and localisation

Code boxes always read left-to-right, even on RTL pages.

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_SingleDigit` | Inputs | 14 | State: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: Fals, False, True; Language: Arabic |

---
_Generated from `catalog/components.json` (id `otp-field`). Edit the catalog, not this file._
