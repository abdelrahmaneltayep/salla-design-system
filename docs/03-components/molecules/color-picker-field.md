# ColorPickerField

> Colour swatch + hex entry with a picker popover.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `Color Picker` |

## Props

| Prop | Values / type |
|---|---|
| `value` | hex |
| `presets` | array |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

- Figma component set: `colorPicker 1d931b4a`

_No matching frame in the current Figma library._

---
_Generated from `catalog/components.json` (id `color-picker-field`). Edit the catalog, not this file._
