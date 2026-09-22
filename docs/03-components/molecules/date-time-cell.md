# CalendarCell

> Day, number and time cells used by the date/time picker.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Selection | 1 - Configurable | existing | figma, storybook | `<s-calendar> (inline)` |

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

## Source in the Twilight Storybook today

### `<s-calendar>` — inline

[components-calendar](https://dashboard-ui-components.pages.dev/?path=/docs/components-calendar) · 28 stories · Calendar is a component that provides date or time selection functionality.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `dateFormat` | text | `DD-MM-YYYY` |  | Format used for displaying/parsing dates and disabledDates (e.g. 'DD-MM-YYYY', 'YYYY-MM-DD'). |
| `disabled` | boolean | `false` |  | Disabled state |
| `disabledDates` | object | `[]` |  | Specific dates to disable. Must match the selected dateFormat. Example (DD-MM-YYYY): ['07-09-2025', '10-09-2025'] |
| `disabledDays` | object | `[]` |  | Weekdays to disable selection for. 0 = Sunday, 6 = Saturday. Accepts numbers (0–6) or day names/abbreviations, e.g. ['sun', 'monday'] |
| `hasError` | boolean | `false` |  | Error state |
| `inline` | boolean | `false` |  | Inline calendar |
| `is24Hr` | boolean | `false` |  | Enable 24 hour format |
| `isOpen` | boolean | `false` |  | Open calendar popup on start (only works when inline is false) |
| `layout` | select | `start` | `start`, `end` | Calendar layout |
| `loading` | boolean | `false` |  | Loading state |
| `maxDate` | text | `null` |  | Maximum date selectable |
| `minDate` | text | `null` |  | Minimum date selectable |
| `placeholder` | string | `Select value` |  | Field placeholder |
| `portal` | boolean | `false` |  | If true, appends the calendar dropdown to the body instead of attaching it to the input. Useful for avoiding overflow issues in containers with overflow: hidden. |
| `required` | boolean | `false` |  | Required field |
| `type` | select | `single` | `range`, `time`, `single`, `multiple` | Calendar type, range, time, single or multiple |
| `value` | text | `[]` |  | Current value of the calendar (string or array of strings) for multiple values |

**Events**

| Event | Description |
|---|---|
| `dateRangeChanged` | Emitted when the date range changes. |
| `valueChanged` | Emitted when the calendar value changes. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--default), [Single](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--single), [Multiple](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--multiple), [Range](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--range), [Time](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--time), [Initial Value](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--initial-value), [Multiple Values](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--multiple-values), [Layout End](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--layout-end), [Min Max Date](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--min-max-date), [Hour Format](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--hour-format), [Loading](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--loading), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--has-error), [Required](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--required), [Inline](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--inline), [Disabled Weekends](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-weekends), [Disabled Weekdays](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-weekdays), [Disabled Specific Days](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-specific-days), [Disabled Specific Dates](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-specific-dates), [Disabled Dates Custom Format](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-dates-custom-format), [Disabled Days And Dates Combined](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-days-and-dates-combined), [Disabled Days With Names](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-days-with-names), [Disabled Days With Abbreviations](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-days-with-abbreviations), [Disabled Days Mixed](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-days-mixed), [Disabled Days Inline](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-days-inline), [Disabled Days Range](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-days-range), [Disabled Days Multiple](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--disabled-days-multiple), [Open On Start](https://dashboard-ui-components.pages.dev/?path=/story/components-calendar--open-on-start)

**Rendered markup (default story)**

```html
<s-calendar placeholder="Select value" class="s-calendar date ltr start hydrated">
  <i class="hgi-stroke hgi-calendar-03" slot="start">
  </i>
</s-calendar>
```


---
_Generated from `catalog/components.json` (id `date-time-cell`). Edit the catalog, not this file._
