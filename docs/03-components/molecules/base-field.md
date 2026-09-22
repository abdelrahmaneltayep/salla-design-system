# BaseField (internal)

> The internal base for every field: label + container (icon-start, control, subtext/unit, translation toggle, info) + helper text. Not exported. Today this role is played by InputWrapper, a 24-variant god component; splitting it into a base and named globals is the main structural change in Text inputs.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | figma, storybook | `<s-input>` |

## Anatomy

- FieldLabel
- container
- icon-start (slot)
- control (slot)
- subtext / unit
- TranslationToggle
- info icon
- HelperText

## Props

| Prop | Values / type |
|---|---|
| `state` | `default`, `hover`, `pre-active`, `active`, `filled`, `active-filled`, `read-only`, `disabled` |
| `error` | boolean |
| `language` | `ar`, `en` |

## States

- default
- hover
- pre-active
- active
- filled
- active-filled
- read-only
- disabled
- error

## Tokens

- comp.text-field.*
- sys.color.surface-input
- sys.color.outline (#eee)
- sys.color.text.secondary (placeholder #666)
- sys.shape.small

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

## Notes and migration

Eight interaction states is more than a screen reader or CSS needs. Collapse to: enabled, hover, focus, filled, read-only, disabled, plus an orthogonal error flag.

## Source in Figma today

- Figma node: `InputWrapper 4d4e5f6d`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_TextInput` | Inputs | 28 | Language: Arabic, English; state: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True |
| `InputWrapper` | Inputs | 24 | Variant: Search, amount, color picker, dropdown-multiple, dropdown-single, dropdown-single-basic, email, password, phone, texArea, text, upload; Langauge: Arabic, English |
| `_inputLabel` | Inputs | 2 | Language: Arabic, English |
| `_Text-cursor` | Inputs | 2 | State: Not visible, Visible |
| `_inputTip` | Inputs | 10 | Type: Danger, Default, Delete File, Variables, character count; Langauge: Arabic, English |

## Source in the Twilight Storybook today

### `<s-input>`

[components-input](https://dashboard-ui-components.pages.dev/?path=/docs/components-input) · 17 stories · Input component is one of the most used components in any application, it is used to get user different types of input in a text field.

Related elements: `<s-icon>`, `<s-dropdown>`, `<s-button>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `aiSuggestion` | object | `undefined` |  | AI suggestion config (object or JSON string): { enabled, regenerable, source }. When `enabled`, the input gets the Moshammer AI highlight and reveals the `actions` slot (regenerate / dismiss). `regenerable` keeps the slot visible without the highlight. |
| `autocomplete` | array |  |  |  |
| `desc` | text | `undefined` |  | Input description, you can use it to add a description to the input |
| `disabled` | boolean | `false` |  | Disabled state |
| `endSlot` | string |  |  |  |
| `hasError` | boolean | `false` |  | Error state |
| `hasPreview` | boolean | `false` |  | Enable input preview |
| `max` | number | `undefined` |  | Input Maximum value |
| `min` | number | `undefined` |  | Input Minimum value |
| `multilingual` | boolean | `false` |  | Enables multilingual support, if true, the input will be able to handle multiple languages, the language will be detected automatically based on merchant supported languages |
| `noBorder` | boolean | `false` |  | Remove input borders, use it in complex component in your app if needed |
| `pattern` | text | `undefined` |  | Regular expression for input validation |
| `placeholder` | string | `Enter your text here...` |  | Input placeholder |
| `shadow` | boolean | `false` |  | Add shadow to the input |
| `size` | string | `md` |  | Input field size |
| `startSlot` | string |  |  |  |
| `step` | number | `undefined` |  | Steps for number inputs only, default is 0 |
| `textAlignment` | string | `start` |  | Text alignment within the input |
| `type` | string | `text` |  | Type of the input |
| `value` | string | `Default input value` |  | Input value |
| `wide` | boolean | `true` |  | Wide input mode |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the input value changes. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-input--default), [Has Preview](https://dashboard-ui-components.pages.dev/?path=/story/components-input--has-preview), [Large Size](https://dashboard-ui-components.pages.dev/?path=/story/components-input--large-size), [Text Alignment Center](https://dashboard-ui-components.pages.dev/?path=/story/components-input--text-alignment-center), [Text Alignment End](https://dashboard-ui-components.pages.dev/?path=/story/components-input--text-alignment-end), [Multilingual](https://dashboard-ui-components.pages.dev/?path=/story/components-input--multilingual), [Border Less](https://dashboard-ui-components.pages.dev/?path=/story/components-input--border-less), [Reg Ex Pattern](https://dashboard-ui-components.pages.dev/?path=/story/components-input--reg-ex-pattern), [Description](https://dashboard-ui-components.pages.dev/?path=/story/components-input--description), [Email](https://dashboard-ui-components.pages.dev/?path=/story/components-input--email), [Auto Complete](https://dashboard-ui-components.pages.dev/?path=/story/components-input--auto-complete), [Password](https://dashboard-ui-components.pages.dev/?path=/story/components-input--password), [Number](https://dashboard-ui-components.pages.dev/?path=/story/components-input--number), [With Slots](https://dashboard-ui-components.pages.dev/?path=/story/components-input--with-slots), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-input--has-error), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-input--disabled), [Ai Suggestion](https://dashboard-ui-components.pages.dev/?path=/story/components-input--ai-suggestion)

**Rendered markup (default story)**

```html
<s-input id="" name="" value="Default input value" type="text" placeholder="Enter your text here..." size="md" text-alignment="start" wide="" class="w-full md ltr hydrated">
  <s-icon slot="start" icon="hgi-stroke hgi-text" class="hydrated">
  </s-icon>
</s-input>
```


---
_Generated from `catalog/components.json` (id `base-field`). Edit the catalog, not this file._
