# PhoneField

> Phone entry with country-code picker (Flag + code) as leading control.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | figma, storybook | `<s-tel-input>` |

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

## Source in the Twilight Storybook today

### `<s-tel-input>`

[components-telephone-input](https://dashboard-ui-components.pages.dev/?path=/docs/components-telephone-input) · 4 stories · **Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `disabled` |  | boolean |  |  | Disabled state |
| `hasError` |  | boolean |  |  | Error state |
| `placeholder` | string | text |  |  | Input placeholder |
| `required` |  | boolean |  |  | Required state |
| `size` |  | select |  |  | Input size |
| `value` |  | text |  |  | Input value |
| `wide` | boolean | boolean |  |  | Wide state |

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `disabled` | boolean |  |  | Disabled state |
| `hasError` | boolean |  |  | Error state |
| `placeholder` | string |  |  | Input placeholder |
| `required` | boolean |  |  | Required state |
| `size` | select |  |  | Input size |
| `value` | text |  |  | Input value |
| `wide` | boolean |  |  | Wide state |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the value of the telephone input changes. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-telephone-input--default), [Large](https://dashboard-ui-components.pages.dev/?path=/story/components-telephone-input--large), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-telephone-input--has-error), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-telephone-input--disabled)

**Rendered markup (default story)**

```html
<div class="flex items-start flex-col gap-4 min-h-[400px]">
  <s-tel-input value="" placeholder="Enter phone number" wide="" class="w-full md ltr hydrated" dir="ltr">
  </s-tel-input>
</div>
```


---
_Generated from `catalog/components.json` (id `phone-field`). Edit the catalog, not this file._
