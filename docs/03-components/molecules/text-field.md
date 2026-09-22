# TextField

> Single-line text entry. Absorbs the four internal Figma frames (plain, with button, with image, with character counter) as slots and props.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | figma, storybook | `<s-input>, <s-lingual-field> (type=input, bilingual)` |

## Props

| Prop | Values / type |
|---|---|
| `label` | string |
| `placeholder` | string |
| `helperText` | string |
| `maxLength` | number (shows counter) |
| `iconStart` | slot |
| `trailing` | slot (button \| image \| unit) |
| `bilingual` | boolean |
| `error` | string |
| `readOnly` | boolean |
| `disabled` | boolean |

## States

inherits BaseField

## Tokens

inherits BaseField

## RTL and localisation

Text direction follows the field language, not the page; the translation toggle sits inline-end in both directions.

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_TextInput` | Inputs | 28 | Language: Arabic, English; state: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True |
| `_inputWithButton` | Inputs | 28 | Language: Arabic, English; state: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True |
| `_InputWithImage` | Inputs | 28 | Language: Arabic, English; state: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True |
| `_InputCounter` | Inputs | 28 | Language: Arabic, English; state: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: False, True |

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

### `<s-lingual-field>` — type=input, bilingual

[components-lingualfield](https://dashboard-ui-components.pages.dev/?path=/docs/components-lingualfield) · 18 stories · Lingual field component is used to handle multilingual input fields, allowing users to input content in multiple languages with automatic language detection and switching capabilities.

Related elements: `<s-input>`, `<s-icon>`, `<s-dropdown>`, `<s-button>`, `<s-textarea>`, `<s-editor>`, `<s-editor-toolbar>`, `<s-editor-desc>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `aiSuggestion` | object | `undefined` |  | AI suggestion config (object or JSON string): { enabled, source, regenerable, languages }. When active, the field gets the Moshammer AI highlight and reveals the `actions` slot (input/textarea end area, richText overlay). Per-language `languages: { [lang]: { content, status: 'pending' } }` auto-applies suggested content. |
| `desc` | text | `undefined` |  | Input description, you can use it to add a description to the input |
| `disabled` | boolean | `false` |  | Disabled state |
| `endSlot` | text | `undefined` |  | Input end slot, it accepts strings only, such as SAR or USD for example |
| `fullHeight` | boolean | `false` |  | Make the textarea fill its container's height (textarea only). |
| `fullToolbar` | boolean | `false` |  | Show the full rich-text toolbar (richText only). |
| `hasError` | boolean | `false` |  | Error state |
| `hasPreview` | boolean | `false` |  | Enable inline preview panel below the field. |
| `language` | string | `ar` |  | Input current language |
| `languages` | object | `undefined` |  | Languages configuration object with feature flag, supported languages, and current language |
| `max` | number | `undefined` |  | Input Maximum value |
| `min` | number | `undefined` |  | Input Minimum value |
| `noBorder` | boolean | `false` |  | Remove input borders, use it in complex component in your app if needed |
| `placeholder` | string | `Enter your text here...` |  | Input placeholder |
| `required` | boolean | `false` |  | Required state |
| `rows` | number | `3` |  | Row count for `type: 'textarea'`. |
| `showCount` | boolean | `false` |  | Live `current/max` counter under the field (textarea + editor). Requires `max`. Counter follows the document direction so it stays anchored when the editor's per-language RTL flips. Turns danger-red under `has-error`. |
| `size` | string | `md` |  | Input size |
| `startSlot` | string | `undefined` |  | Input start slot, it accepts icon class name from hugeIcons or Sallaicons |
| `toolbar` | array |  |  |  |
| `type` | string | `input` |  | Input type, can be input, textarea or richText |
| `value` | string | `{"en": "Hello", "ar": "مرحبا"}` |  | JSON string mapping languages to their respective values |

**Events**

| Event | Description |
|---|---|
| `languageChanged` | Emitted when the language is changed. |
| `valueChanged` | Emitted when the field value changes. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--default), [Text Area Field](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--text-area-field), [Editor Field](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--editor-field), [Ai Suggestion](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--ai-suggestion), [Ai Suggestion Rich Text](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--ai-suggestion-rich-text), [Multiple Languages](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--multiple-languages), [Large Size](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--large-size), [Min Length](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--min-length), [Max Length](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--max-length), [With Character Counter Textarea](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--with-character-counter-textarea), [With Character Counter Only](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--with-character-counter-only), [With Character Counter Rich Text](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--with-character-counter-rich-text), [Description](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--description), [Border Less](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--border-less), [End Slot](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--end-slot), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--has-error), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--disabled), [Custom Toolbar](https://dashboard-ui-components.pages.dev/?path=/story/components-lingualfield--custom-toolbar)

**Rendered markup (default story)**

```html
<s-lingual-field name="undefined" value="{&quot;en&quot;: &quot;Hello&quot;, &quot;ar&quot;: &quot;مرحبا&quot;}" type="input" placeholder="Enter your text here..." size="md" language="ar" start-slot="hgi-stroke hgi-language-square" languages="{&quot;feature&quot;:true,&quot;supported&quot;:[],&quot;current&quot;:{&quot;id&quot;:0,&quot;label&quot;:&quot;English&quot;,&quot;value&quot;:&quot;en&quot;}}" dir="rtl" class="s-lingual-field s-lingual-field--input rtl w-full relative flex items-start justify-start gap-4 hydrated">
  <!---->
  <s-input class="flex-1 md rtl multilingual ltr hydrated" dir="rtl" value="مرحبا">
    <s-icon slot="start" class="hydrated">
    </s-icon>
    <div slot="end" class="s-lingual-field__actions-end s-lingual-field__actions-end--hidden" data-lingual-field-internal-slot="">
      <div class="s-lingual-field__actions-end__reserve s-lingual-field__actions-end--hidden" aria-hidden="true">
      </div>
    </div>
  </s-input>
  <s-dropdown dir="ltr" class="h-fit end ltr hydrated" overlay-alignment="start">
    <s-button data-toggle="true" slot="dropdown-head" c
<!-- … truncated … -->
```


---
_Generated from `catalog/components.json` (id `text-field`). Edit the catalog, not this file._
