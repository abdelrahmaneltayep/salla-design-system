# TextareaField

> Multi-line text entry with optional rich-text toolbar.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | figma, storybook | `<s-textarea>, <s-lingual-field> (type=textarea)` |

## Props

| Prop | Values / type |
|---|---|
| `rows` | number |
| `richText` | boolean |
| `maxLength` | number |
| `autoResize` | boolean |

## States

inherits BaseField

## Tokens

inherits BaseField

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_TextArea` | Inputs | 56 | State: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: Fals, False, True; Language: Arabic, English; Rich text: No, Yes |
| `_Rich-Text-Panel` | Inputs | 2 | Language: Arabic, English |

## Source in the Twilight Storybook today

### `<s-textarea>`

[components-textarea](https://dashboard-ui-components.pages.dev/?path=/docs/components-textarea) · 9 stories · Textarea component is used for multiline text input, allowing users to enter longer text content with various configuration options.

Related elements: `<s-button>`, `<s-icon>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `aiSuggestion` | object | `undefined` |  | AI suggestion config (object or JSON string): { enabled, regenerable, source }. When `enabled`, the textarea gets the Moshammer AI highlight and reveals the `actions` slot (regenerate / dismiss). |
| `desc` | string | `undefined` |  | Textarea description, you can use it to add a description to the textarea |
| `disabled` | boolean | `false` |  | Disabled state |
| `feature` | boolean |  |  |  |
| `fullHeight` | boolean | `false` |  | Make textarea take full height of its container |
| `hasError` | boolean | `false` |  | Error state |
| `hasPreview` | boolean | `false` |  | Enable textarea preview |
| `max` | number | `undefined` |  | Maximum number of characters allowed |
| `multilingual` | boolean | `false` |  | Enables multilingual support, enabled when value is an array of strings |
| `placeholder` | string | `Enter your text here...` |  | Textarea placeholder |
| `required` | boolean | `false` |  | Required state |
| `rows` | number | `4` |  | Number of visible text lines for the textarea |
| `showCount` | boolean | `false` |  | Show a live `current/max` character counter below the field. Requires `max`. Turns danger-red when the field has `has-error`. |
| `value` | string | `Default textarea value...` |  | Textarea value |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the value of the textarea changes. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-textarea--default), [Has Description](https://dashboard-ui-components.pages.dev/?path=/story/components-textarea--has-description), [Has Preview](https://dashboard-ui-components.pages.dev/?path=/story/components-textarea--has-preview), [Multilingual](https://dashboard-ui-components.pages.dev/?path=/story/components-textarea--multilingual), [With Max Length](https://dashboard-ui-components.pages.dev/?path=/story/components-textarea--with-max-length), [With Character Counter](https://dashboard-ui-components.pages.dev/?path=/story/components-textarea--with-character-counter), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-textarea--has-error), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-textarea--disabled), [Ai Suggestion](https://dashboard-ui-components.pages.dev/?path=/story/components-textarea--ai-suggestion)

**Rendered markup (default story)**

```html
<s-textarea value="Default textarea value..." placeholder="Enter your text here..." rows="3" feature="true" class="ltr hydrated">
</s-textarea>
```

### `<s-lingual-field>` — type=textarea

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
_Generated from `catalog/components.json` (id `textarea-field`). Edit the catalog, not this file._
