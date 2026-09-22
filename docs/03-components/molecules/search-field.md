# SearchField

> Search entry with magnifier, clear button, recommendations and no-results states.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | figma, storybook | `<s-input> (type=autocomplete), <s-select> (searchable / autocomplete)` |

## Props

| Prop | Values / type |
|---|---|
| `suggestions` | array |
| `loading` | boolean |
| `onClear` | fn |

## States

- default
- hover
- active
- filled
- active-filled
- recommendation
- no-result

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `searchInput` | Inputs | 16 | State: Active, Active-Filled, Active-Filled-noResult, Active-recommendation, default, filled, hover, preActive; error: False; Language: Arabic, English |

## Source in the Twilight Storybook today

### `<s-input>` — type=autocomplete

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

### `<s-select>` — searchable / autocomplete

[components-select](https://dashboard-ui-components.pages.dev/?path=/docs/components-select) · 29 stories · Select component provides a dropdown interface for choosing from a list of options. It supports single and multiple selection, search functionality, grouping, and various customization options.

Related elements: `<s-button>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `addMissingItem` | boolean | `false` |  | Allow adding new items |
| `allowParentSelect` | boolean | `true` |  | When false and layout is drawer, clicking a parent item opens the drawer/toggles children instead of selecting the parent. When true, parent items remain selectable. |
| `autocomplete` | boolean |  |  | Enables this option to fetch items from server dynamically based on the search query |
| `cancelLabel` | text |  |  | Label of the cancel action. Defaults to the translated "Cancel". |
| `children` | string |  |  |  |
| `confirmLabel` | text |  |  | Label of the confirm action. Defaults to the translated "Save". |
| `confirmable` | boolean |  |  | Buffers the selection behind sticky confirm/cancel actions at the end of the dropdown. No `selectChange` is emitted while the dropdown is open — confirm emits it once (plus `selectConfirm`), cancel emits `selectCancel` and restores the value the dropdown opened with. |
| `disabled` | boolean | `false` |  | Disabled state |
| `endSlot` | text | `undefined` |  | HTML content to render in the end slot |
| `hasError` | boolean |  |  | Error state |
| `hideClearButton` | boolean | `false` |  | Hide the clear button, useful in certain cases |
| `items` | array | `[]` |  | Options for the select |
| `layout` | select | `default` | `default`, `drawer` | Layout mode for the select dropdown |
| `loading` | boolean | `false` |  | Loading state |
| `multiselect` | boolean |  |  | Enables multiple selection mode, you can then choose either tags or count of selected items, count is default |
| `overlayAlignment` | string | `start` | `start`, `end` | Horizontal alignment preference for the dropdown overlay |
| `placeholder` | string |  |  | Placeholder text |
| `readonly` | boolean | `false` |  | The value cannot change, but the component stays usable: the dropdown still opens and closes, and the search box still filters. Selecting, select-all, add-new, drawer navigation, the clear button and tag removal are all locked. Use it for async work that must not be interrupted, or for view-only permissions; unlike `disabled`, it never greys out the whole component or force-closes the overlay. |
| `required` | boolean |  |  | Required state |
| `responsive` | boolean |  |  | Responsive mode |
| `searchPlaceholder` | text | `undefined` |  | Search input placeholder |
| `searchable` | boolean |  |  | Enables search functionality |
| `selectAll` | boolean |  |  | Shows a select-all row in the dropdown. Works only when multiselect is enabled. |
| `sheetTitle` | text |  |  | Optional title shown in the mobile sheet header |
| `size` | select |  | `md`, `lg` | Size of the select component |
| `tags` | boolean |  |  | Display selections as tags |
| `toggleSlot` | text | `undefined` |  | HTML content to render in the toggle slot. When provided, replaces the default input-wrapper. Element should have data-toggle attribute. |
| `value` | string |  |  | Selected value(s) |
| `wide` | boolean |  |  | Full width |

**Events**

| Event | Description |
|---|---|
| `addNewItem` | Emitted when user clicks to add a missing item. Provides value and searchString. |
| `optionsChange` | Emitted when the value of options changes. |
| `searchValueChange` | Emitted when the search value changes in searchable mode. |
| `selectChange` | Emitted when the value of the select component changes. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-select--default), [Searchable](https://dashboard-ui-components.pages.dev/?path=/story/components-select--searchable), [Auto Complete](https://dashboard-ui-components.pages.dev/?path=/story/components-select--auto-complete), [With End Slot](https://dashboard-ui-components.pages.dev/?path=/story/components-select--with-end-slot), [With End Overlay Alignment](https://dashboard-ui-components.pages.dev/?path=/story/components-select--with-end-overlay-alignment), [With Toggle Slot](https://dashboard-ui-components.pages.dev/?path=/story/components-select--with-toggle-slot), [With Groups And Thumbnails](https://dashboard-ui-components.pages.dev/?path=/story/components-select--with-groups-and-thumbnails), [Nested Options](https://dashboard-ui-components.pages.dev/?path=/story/components-select--nested-options), [Drawer Layout](https://dashboard-ui-components.pages.dev/?path=/story/components-select--drawer-layout), [Drawer Layout No Parent Select](https://dashboard-ui-components.pages.dev/?path=/story/components-select--drawer-layout-no-parent-select), [Nested With Child Icons](https://dashboard-ui-components.pages.dev/?path=/story/components-select--nested-with-child-icons), [Multi Select](https://dashboard-ui-components.pages.dev/?path=/story/components-select--multi-select), [Multi Select Tags Layout](https://dashboard-ui-components.pages.dev/?path=/story/components-select--multi-select-tags-layout), [Multi Select With Select All](https://dashboard-ui-components.pages.dev/?path=/story/components-select--multi-select-with-select-all), [Add Missing Item](https://dashboard-ui-components.pages.dev/?path=/story/components-select--add-missing-item), [Hide Clear Button](https://dashboard-ui-components.pages.dev/?path=/story/components-select--hide-clear-button), [Loading](https://dashboard-ui-components.pages.dev/?path=/story/components-select--loading), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-select--has-error), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-select--disabled), [Disabled Item](https://dashboard-ui-components.pages.dev/?path=/story/components-select--disabled-item), [Disabled Nested Item](https://dashboard-ui-components.pages.dev/?path=/story/components-select--disabled-nested-item), [Disabled Item Multiselect](https://dashboard-ui-components.pages.dev/?path=/story/components-select--disabled-item-multiselect), [Readonly](https://dashboard-ui-components.pages.dev/?path=/story/components-select--readonly), [Readonly Searchable](https://dashboard-ui-components.pages.dev/?path=/story/components-select--readonly-searchable), [Readonly Multiselect](https://dashboard-ui-components.pages.dev/?path=/story/components-select--readonly-multiselect), [Readonly Nested](https://dashboard-ui-components.pages.dev/?path=/story/components-select--readonly-nested), [Readonly Drawer](https://dashboard-ui-components.pages.dev/?path=/story/components-select--readonly-drawer), [Readonly While Saving](https://dashboard-ui-components.pages.dev/?path=/story/components-select--readonly-while-saving), [Confirmable Actions](https://dashboard-ui-components.pages.dev/?path=/story/components-select--confirmable-actions)

**Rendered markup (default story)**

```html
<div style="display: contents;">
  <div children="[object Object]" style="overflow: hidden;">
    <s-select class="w-full md ltr hydrated" value="">
    </s-select>
  </div>
</div>
```


---
_Generated from `catalog/components.json` (id `search-field`). Edit the catalog, not this file._
