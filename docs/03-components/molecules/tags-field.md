# TagsField

> Free-form tag entry: type a value, press Add, manage the resulting Chips; max limit and validation.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | figma, storybook | `<s-tags>` |

## Anatomy

- input
- add Button
- Chip list

## Props

| Prop | Values / type |
|---|---|
| `value` | string[] |
| `max` | number |
| `buttonLabel` | string |
| `tagTheme` | Tag theme |
| `tagSize` | `sm`, `md` |
| `hasError` | boolean |
| `wide` | boolean |

## States

inherits BaseField

## Tokens

inherits BaseField

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

Composes: [Chip](../atoms/chip.md), [Button](../atoms/button.md).

## Notes and migration

Distinct from MultiSelectField: no option list, values are typed. Twilight tag `s-tags`.

## Source in Figma today

- Variant filter: `Add new value=On`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_dropdown-multiple` | Inputs | 29 | State: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True; Language: Arabic, English; Add new value: Off, On |

## Source in the Twilight Storybook today

### `<s-tags>`

[components-tags-input](https://dashboard-ui-components.pages.dev/?path=/docs/components-tags-input) · 6 stories · A tags input component that allows users to add, remove, and manage multiple tag values. Supports customizable themes, maximum limits, and form validation.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `buttonLabel` | text | `Add` |  | Button label |
| `buttonTheme` | select | `default` | `default`, `secondary`, `danger`, `warning`, `info`, `white`, `transparent`, `feature` | Button theme |
| `disabled` | boolean | `false` |  | Disabled state |
| `hasError` | boolean | `false` |  | Error state |
| `max` | number | `undefined` |  | Maximum number of tags allowed |
| `placeholder` | string | `undefined` |  | Placeholder text |
| `tagSize` | select | `md` | `sm`, `md` | Tag size |
| `tagTheme` | select | `white` | `default`, `secondary`, `success`, `danger`, `warning`, `info`, `white`, `transparent`, `feature` | Tag theme |
| `value` | object | `[]` |  | Array of current tag values |
| `wide` | boolean | `false` |  | Makes the input take full width |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the tags value changes. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-tags-input--default), [Initial Values](https://dashboard-ui-components.pages.dev/?path=/story/components-tags-input--initial-values), [Max Limit](https://dashboard-ui-components.pages.dev/?path=/story/components-tags-input--max-limit), [Wide](https://dashboard-ui-components.pages.dev/?path=/story/components-tags-input--wide), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-tags-input--has-error), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-tags-input--disabled)

**Rendered markup (default story)**

```html
<s-tags id="tags-orxk1uj52" placeholder="Enter a tag and press add" button-label="Add" tag-theme="default" tags-size="sm" class="flex flex-col gap-2 hydrated">
</s-tags>
```


---
_Generated from `catalog/components.json` (id `tags-field`). Edit the catalog, not this file._
