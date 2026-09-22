# Checkbox

> Bare selection control with true / false / mixed states in two sizes. The labelled version is CheckboxField.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Selection | 3 - Base + Global | existing | figma, storybook | `<s-checkbox> (single value, no label)` |

## Anatomy

- box
- check / dash glyph

## Props

| Prop | Values / type |
|---|---|
| `checked` | `true`, `false`, `mixed` |
| `size` | `sm (16px)`, `md (20px)` |
| `disabled` | boolean |

## States

- default
- hover
- focus
- disabled

## Tokens

- comp.checkbox.*
- sys.color.primary (checked fill #004956)
- sys.shape.extra-small (4px)
- sys.color.outline

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **self (used by CheckboxField)**.

## Source in Figma today

- Figma node: `12411:21809`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `checkBox` | check Box | 18 | selected: false, mix, true; Status: default, disabled, focus; size: md-20px, sm-16px |

## Source in the Twilight Storybook today

### `<s-checkbox>` — single value, no label

[components-checkbox](https://dashboard-ui-components.pages.dev/?path=/docs/components-checkbox) · 14 stories · A checkbox is a form element that allows users to select one or more options from a list. It is commonly used in forms to gather user preferences or choices.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `checked` | boolean | `false` |  | Checked state |
| `desc` | string |  |  | Checkbox description |
| `direction` | string | `col` |  | Sets the layout direction, col or row, with default col |
| `disabled` | boolean | `false` |  | Disabled state |
| `feature` | boolean | `true` |  | Feature based state |
| `hasError` | boolean | `false` |  | Checkbox error state |
| `indeterminate` | boolean | `false` |  | IF the checkbox is partially selected |
| `items` | text | `[]` |  | Multiple Checkbox value |
| `label` | string |  |  | Checkbox label |
| `loading` | boolean | `false` |  | Replaces every option with a skeleton placeholder so the row height is preserved during data fetches. Per-option loading is supported via `loading: true` on an individual item. |
| `readonly` | boolean | `false` |  | Freezes the value without the disabled styling — the box keeps its normal contrast and the input never receives the `disabled` attribute. |
| `required` | boolean | `false` |  | If the checkbox is required |
| `value` | text |  |  | Single Checkbox value |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the checkbox value changes. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--default), [Checked](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--checked), [Indeterminate](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--indeterminate), [Group Options](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--group-options), [Row Direction](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--row-direction), [Exclusive Option](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--exclusive-option), [Required](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--required), [Feature Based](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--feature-based), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--disabled), [Readonly](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--readonly), [Disabled Item](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--disabled-item), [Loading](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--loading), [Loading Item](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--loading-item), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-checkbox--has-error)

**Rendered markup (default story)**

```html
<s-checkbox label="Accept terms and conditions" desc="I agree to the terms and conditions" direction="col" feature="true" @valuechanged="ev=&gt;console.log(" value="" changed:",ev.detail)"="" class="s-checkbox ltr hydrated">
</s-checkbox>
```


---
_Generated from `catalog/components.json` (id `checkbox`). Edit the catalog, not this file._
