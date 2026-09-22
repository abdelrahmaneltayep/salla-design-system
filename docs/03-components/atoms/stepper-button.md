# StepperButton

> The +/- buttons flanking QuantityField, including the delete-at-one variant.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Actions | 1 - Configurable | existing | figma, storybook | `<s-qty> (increase / decrease buttons)` |

## Props

| Prop | Values / type |
|---|---|
| `action` | `increment`, `decrement`, `delete` |
| `disabled` | boolean |

## States

- default
- hover
- disabled

## Tokens

- sys.color.outline
- sys.shape.small

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_counter-buttons` | Inputs | 6 | variant: left, left-delete, right; disabled: False, True |

## Source in the Twilight Storybook today

### `<s-qty>` — increase / decrease buttons

[components-qty](https://dashboard-ui-components.pages.dev/?path=/docs/components-qty) · 9 stories · The Qty component represents a quantity input field. It allows users to input numeric quantities and provides buttons to increment or decrement the value.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `deletable` | boolean | `false` |  | Enable this to show delete button instead of minus button when value is 1 an event will be emitted with the following payload { payload: { target, min, max, value, leastValue, deletable } } |
| `disabled` | boolean | `false` |  | Disabled state |
| `hasError` | boolean | `false` |  | Error state |
| `layout` | string | `sides` |  | Field layout, you can choose between sides and end |
| `max` | number | `100` |  | Field maximum value |
| `min` | number | `0` |  | Field minimum value |
| `placeholder` | string | `Enter the required quantity` |  | Field placeholder |
| `required` | boolean | `false` |  | Required state |
| `step` | number | `1` |  | Field step, it's the value to increment or decrement when clicking the buttons. Default is 1. |
| `theme` | string | `default` |  | Field theme, you can choose between default and circular |
| `value` | number | `1` |  | Field value |
| `wide` | boolean | `false` |  | Wide state |

**Events**

| Event | Description |
|---|---|
| `decreaseClicked` | Emitted when the decrease button is clicked. |
| `increaseClicked` | Emitted when the increase button is clicked. |
| `valueChanged` | Emitted when the quantity input field value changes. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-qty--default), [Circular](https://dashboard-ui-components.pages.dev/?path=/story/components-qty--circular), [Wide](https://dashboard-ui-components.pages.dev/?path=/story/components-qty--wide), [Min Max Values](https://dashboard-ui-components.pages.dev/?path=/story/components-qty--min-max-values), [Step](https://dashboard-ui-components.pages.dev/?path=/story/components-qty--step), [Deletable](https://dashboard-ui-components.pages.dev/?path=/story/components-qty--deletable), [Layout End](https://dashboard-ui-components.pages.dev/?path=/story/components-qty--layout-end), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-qty--has-error), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-qty--disabled)

**Rendered markup (default story)**

```html
<s-qty value="1" theme="default" layout="sides" min="1" max="100" step="1" placeholder="Enter Qty" class="s-qty s-qty--default ltr hydrated">
</s-qty>
```


---
_Generated from `catalog/components.json` (id `stepper-button`). Edit the catalog, not this file._
