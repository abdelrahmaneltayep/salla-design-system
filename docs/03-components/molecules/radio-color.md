# RadioColor

> Selectable colour swatch (visual radio) for product colour variants.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Selection | 2 - Standalone | existing | figma, storybook | `<s-radio> (layout=color)` |

## Props

| Prop | Values / type |
|---|---|
| `color` | hex |
| `label` | string |
| `selected` | boolean |

## States

- default
- hover
- selected

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

Composes: [Radio](../atoms/radio.md).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `radioColor` | radio Buttton | 3 | state: default, hover, selected |

## Source in the Twilight Storybook today

### `<s-radio>` — layout=color

[components-radio](https://dashboard-ui-components.pages.dev/?path=/docs/components-radio) · 15 stories · A radio button is a form element that allows users to select one option from a list of mutually exclusive choices. It is commonly used in forms where only one selection is allowed.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `autoHeight` | boolean | `false` |  | If the text radio should fill the available height. Applies when layout is "text". |
| `checked` | boolean | `false` |  | Radio checked state |
| `desc` | string |  |  | Radio description |
| `direction` | string | `col` |  | Radio direction, you can choose between col (vertical) or row (horizontal) |
| `disabled` | boolean | `false` |  | Boolean indicating whether the radio is disabled |
| `feature` | boolean | `true` |  | Feature based state |
| `hasError` | boolean | `false` |  | Boolean indicating whether the radio has an error |
| `items` | text | `[]` |  | Multiple Radio value |
| `label` | string |  |  | Radio label |
| `layout` | string | `default` |  | Radio layout style, you can choose between default, text, image, color |
| `loading` | boolean | `false` |  | Replaces every option with a skeleton placeholder shaped like the current layout. Per-option loading is also supported via `loading: true` on an individual item. |
| `required` | boolean | `false` |  | If the radio is required |
| `value` | text |  |  | Single Radio value |
| `wide` | boolean | `false` |  | Boolean indicating whether the radio occupies full width |

**Events**

| Event | Description |
|---|---|
| `onChange` | Emitted when the radio selection changes (native change event). |
| `onInput` | Emitted when the radio input is modified (native input event). |
| `onValueChanged` | Emitted when the radio value changes. Payload includes value, checked state, and all options. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--default), [Checked](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--checked), [Group Options](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--group-options), [Row Direction](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--row-direction), [Text Layout](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--text-layout), [Text Layout Auto Height](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--text-layout-auto-height), [Color Layout](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--color-layout), [Image Layout](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--image-layout), [Required](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--required), [Feature Based](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--feature-based), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--disabled), [Disabled Item](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--disabled-item), [Loading](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--loading), [Loading Item](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--loading-item), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-radio--has-error)

**Rendered markup (default story)**

```html
<s-radio label="Select your preferred option" desc="Choose one option from the list below" layout="default" direction="col" class="s-radio s-radio--default ltr hydrated">
</s-radio>
```


---
_Generated from `catalog/components.json` (id `radio-color`). Edit the catalog, not this file._
