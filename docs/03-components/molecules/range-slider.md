# RangeSlider

> Slider with a paired numeric input for choosing a value within min / max.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Selection | 3 - Base + Global | existing | storybook | `<s-range-slider>` |

## Anatomy

- track
- fill
- thumb
- numeric input

## Props

| Prop | Values / type |
|---|---|
| `value` | number |
| `min` | number |
| `max` | number |
| `step` | number |
| `theme` | `default`, `secondary` |
| `hasError` | boolean |
| `disabled` | boolean |

## States

- enabled
- dragging
- focus
- disabled
- error

## Tokens

- sys.color.primary
- sys.color.surface-disabled
- sys.shape.full

## RTL and localisation

Track direction mirrors; min sits inline-start.

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Notes and migration

Storybook only: no Figma frame. Material: slider.

## Source in Figma today

_No matching frame in the current Figma library._

## Source in the Twilight Storybook today

### `<s-range-slider>`

[components-range-slider](https://dashboard-ui-components.pages.dev/?path=/docs/components-range-slider) · 5 stories · The s-range-slider component represents a range slider that allows users to select a value within a specified range. It offers a visual slider input and a numerical input for selecting values.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `disabled` | boolean | `false` |  | Disabled state |
| `hasError` | boolean | `false` |  | Error state |
| `max` | number | `200` |  | Slider maximum value |
| `min` | number | `0` |  | Slider minimum value |
| `step` | number | `1` |  | Step value for the range slider |
| `theme` | string | `default` | `default`, `secondary` | Slider theme, you can choose between default and secondary |
| `value` | number | `100` |  | Slider value |

**Events**

| Event | Description |
|---|---|
| `onChange` | Emitted when the value of the range slider changes. |
| `onValueChanged` | Emitted when the value of the range slider changes. Payload includes target, min, max, step, and value. |
| `onchange` | Emitted when the range slider value changes. Provides the new value as a number. |
| `valueChanged` | Emitted when the value of the range slider changes. Provides detailed change information. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-range-slider--default), [Step](https://dashboard-ui-components.pages.dev/?path=/story/components-range-slider--step), [Secondary Theme](https://dashboard-ui-components.pages.dev/?path=/story/components-range-slider--secondary-theme), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-range-slider--has-error), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-range-slider--disabled)

**Rendered markup (default story)**

```html
<s-range-slider value="100" theme="default" max="200" step="1" class="w-full s-range-slider ltr hydrated">
</s-range-slider>
```


---
_Generated from `catalog/components.json` (id `range-slider`). Edit the catalog, not this file._
