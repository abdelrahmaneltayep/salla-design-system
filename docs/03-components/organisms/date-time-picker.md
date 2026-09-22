# DateTimePicker

> Calendar and time picker popover built from CalendarCell. Logic (ranges, locale, Hijri/Gregorian) lives in useCalendar.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Selection | 5 - Headless | existing | `Date Picker` |

## Props

| Prop | Values / type |
|---|---|
| `mode` | `date`, `time`, `datetime`, `range` |
| `calendar` | `gregorian`, `hijri` |
| `min` | date |
| `max` | date |

## How to build it

Build the **logic as a headless hook / controller** (state, keyboard, focus, ARIA) and a thin UI component on top. The hook must be usable with custom UI; document it with examples since it is invisible in Figma.

Headless layer: **useCalendar**.

Composes: [CalendarCell](../molecules/date-time-cell.md), [IconButton](../atoms/icon-button.md), [SelectField](../molecules/select-field.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_Date` | Drop Down List | 4 | Type: Current, Default, Disabled, Selected |
| `_bigCalenderItems` | Drop Down List | 5 | Status: Default, Disable, Select, Variant4; Type: Day, Numbers |
| `_Time` | Drop Down List | 2 | Type: Default, Selceted |
| `Time` | Drop Down List | 3 | Status: Default, Edit, Hover |

---
_Generated from `catalog/components.json` (id `date-time-picker`). Edit the catalog, not this file._
