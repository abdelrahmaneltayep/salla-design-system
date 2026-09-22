# PhoneField

> Phone entry with country-code picker (Flag + code) as leading control.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `Phone` |

## Props

| Prop | Values / type |
|---|---|
| `defaultCountry` | ISO code |
| `countries` | array |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Notes and migration

Figma frame is suffixed V1; the new name drops versions from component names (version lives in the changelog).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_PhoneInputV1` | Inputs | 28 | Language: Arabic, English; state: active, active-filled, default, disabled, filled, hover, preActive, read-only; error: False, True |

---
_Generated from `catalog/components.json` (id `phone-field`). Edit the catalog, not this file._
