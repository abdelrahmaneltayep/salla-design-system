# AmountField

> Numeric / currency entry with the Saudi Riyal symbol as trailing unit.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `Number / Price` |

## Props

| Prop | Values / type |
|---|---|
| `currency` | string (default SAR) |
| `min` | number |
| `max` | number |
| `step` | number |
| `decimals` | number |

## RTL and localisation

Digits stay Latin (0-9) per live dashboard convention; the currency glyph sits inline-end.

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_amountInput` | Inputs | 28 | State: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True; Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `amount-field`). Edit the catalog, not this file._
