# RichTextEditor

> Quill-based rich text editor with configurable toolbar, html / text / json output, character limits, preview, product embeds, image picker and AI suggestion.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Text inputs | 3 - Base + Global | existing | figma, storybook | `<s-editor>` |

## Anatomy

- toolbar (slot end for language)
- content area (start slot icon)
- counter / description
- AI actions overlay

## Props

| Prop | Values / type |
|---|---|
| `toolbar` | array config |
| `fullToolbar` | boolean |
| `hideToolbar` | boolean |
| `format` | `html`, `text`, `json` |
| `min / max` | number |
| `showCount` | boolean |
| `hasPreview` | boolean |
| `multilingual` | boolean |
| `productEmbed` | config |
| `aiSuggestion` | config |

## States

- enabled
- focus
- disabled
- error
- loading

## Tokens

- comp.text-field.*
- sys.color.outline
- sys.shape.small

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Notes and migration

Figma models this as TextareaField with Rich text?=Yes plus the _Rich-Text-Panel toolbar; Twilight ships it as a standalone Editor. Treat it as the third global on BaseField.

## Source in Figma today

- Variant filter: `Rich text?=Yes`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_TextArea` | Inputs | 56 | State: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: Fals, False, True; Language: Arabic, English; Rich text: No, Yes |
| `_Rich-Text-Panel` | Inputs | 2 | Language: Arabic, English |

## Source in the Twilight Storybook today

### `<s-editor>`

[components-editor](https://dashboard-ui-components.pages.dev/?path=/docs/components-editor) · 12 stories · A rich text editor component that provides a comprehensive toolbar for content creation and editing. It supports various formats, multilingual content, and preview functionality.

Related elements: `<s-editor-toolbar>`, `<s-dropdown>`, `<s-button>`, `<s-icon>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `aiSuggestion` | object | `undefined` |  | AI suggestion config (object or JSON string): { enabled, regenerable, source }. When `enabled`, the editor gets the Moshammer AI highlight and overlays the `actions` slot (regenerate / dismiss) at the top of the content area. |
| `demoImagePicker` | boolean | `undefined (native file picker)` |  | Story-only. Wires a stub `imagePicker` so the toolbar image button opens it instead of the native file picker. `imagePicker` itself is a function prop and has no Storybook control. |
| `desc` | text | `undefined` |  | Description text for the editor |
| `disabled` | boolean | `false` |  | Disabled state |
| `format` | select | `html` | `html`, `text`, `json` | Output format of the editor content |
| `fullToolbar` | boolean | `false` |  | Editor full toolbar |
| `hasError` | boolean | `false` |  | Error state |
| `hasPreview` | boolean | `false` |  | Enable editor preview |
| `hideToolbar` | boolean | `false` |  | Render the editor without its toolbar. Also moves the `end` slot in flow, since there is no toolbar row left to overlay. |
| `max` | number | `undefined` |  | Maximum Characters |
| `min` | number | `undefined` |  | Minimum Characters |
| `multilingual` | boolean | `false` |  | Enables multilingual support, if true, the editor will be able to handle multiple languages, the language will be detected automatically based on merchant supported languages |
| `placeholder` | string | `Editor placeholder` |  | Editor placeholder |
| `productEmbed` | object | `undefined (disabled)` |  | Enable product embeds in the editor. Pass true for the default products API, or an object with endpoint (and optional searchParam / transform). |
| `required` | boolean | `false` |  | Required state |
| `server` | object | `Default server config with type: 'products'` |  | Server configuration including upload type (crucial for each app context) |
| `showCount` | boolean | `false` |  | Show a live `current/max` character counter below the editor. Requires `max`. Counter follows the document direction so it stays anchored when the editor's own dir flips for per-language RTL. Turns danger-red under `has-error`. |
| `toolbar` | array | `[["bold","italic","underline","strike"],[{"direction":"rtl"},{"align":[]},{"list":"ordered"},{"list":"bullet"}],[{"header":1},{"header":2},{"header":3}],[{"indent":"-1"},{"indent":"+1"}],[{"color":[]},{"background":[]}],["image","video","link"],["clean"],["blockquote","code-block"]]` |  | Custom toolbar configuration for the editor |
| `value` | string | `Editor value` |  | Editor value |

**Slots**

| Slot | Description |
|---|---|
| `endSlot` | HTML projected into the `end` slot — trailing chrome such as a language dropdown. Overlaid on the toolbar's trailing edge, or in flow at the end of the body when `hideToolbar` is set. Set `multilingual` (or let the component detect the slot) to reserve the strip it sits over. |
| `startSlot` | HTML projected into the `start` slot — a leading icon beside the editor body. Same contract as s-input / s-textarea: pass the element itself (no wrapper), and the component supplies `text-xl text-dark-100`. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--default), [Has Preview](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--has-preview), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--disabled), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--has-error), [Has Character Limits 50](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--has-character-limits-50), [With Character Counter](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--with-character-counter), [With Slots](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--with-slots), [With Slots No Toolbar](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--with-slots-no-toolbar), [Custom Toolbar](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--custom-toolbar), [Ai Suggestion](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--ai-suggestion), [With Product Embed](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--with-product-embed), [With Image Picker](https://dashboard-ui-components.pages.dev/?path=/story/components-editor--with-image-picker)

**Rendered markup (default story)**

```html
<s-editor value="Default editor content..." placeholder="Enter your content here..." full-toolbar="" class="s-editor ltr hydrated">
  <!---->
  <div class="s-editor__wrapper">
    <s-editor-toolbar class="hydrated">
      <div id="toolbar" class="s-editor__toolbar ql-toolbar ql-snow" role="toolbar" aria-label="Editor toolbar">
        <span class="ql-formats" role="group" aria-label="Formatting options group">
          <button type="button" class="ql-bold" title="Bold" aria-label="Bold" aria-pressed="false">
            <svg viewBox="0 0 18 18">
              <path class="ql-stroke" d="M5,4H9.5A2.5,2.5,0,0,1,12,6.5v0A2.5,2.5,0,0,1,9.5,9H5A0,0,0,0,1,5,9V4A0,0,0,0,1,5,4Z">
              </path>
              <path class="ql-stroke" d="M5,9h5.5A2.5,2.5,0,0,1,13,11.5v0A2.5,2.5,0,0,1,10.5,14H5a0,0,0,0,1,0,0V9A0,0,0,0,1,5,9Z">
              </path>
            </svg>
          </button>
          <button type="button" class="ql-italic" title="Italic" aria-label="Italic" aria-pressed="false">
            <svg viewBox="0 0 18 18">
              <line class="ql-stroke" x1="7" x2="13" y1="4" 
<!-- … truncated … -->
```


---
_Generated from `catalog/components.json` (id `rich-text-editor`). Edit the catalog, not this file._
