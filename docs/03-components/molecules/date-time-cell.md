# CalendarCell

> Day, number and time cells used by the date/time picker.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Selection | 1 - Configurable | existing | _not in Storybook_ |

## Props

| Prop | Values / type |
|---|---|
| `kind` | `day`, `number`, `time` |
| `state` | `default`, `current`, `selected`, `disabled` |

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_Date` | Drop Down List | 4 | Type: Current, Default, Disabled, Selected |
| `_bigCalenderItems` | Drop Down List | 5 | Status: Default, Disable, Select, Variant4; Type: Day, Numbers |
| `_Time` | Drop Down List | 2 | Type: Default, Selceted |
| `Time` | Drop Down List | 3 | Status: Default, Edit, Hover |

---
_Generated from `catalog/components.json` (id `date-time-cell`). Edit the catalog, not this file._
