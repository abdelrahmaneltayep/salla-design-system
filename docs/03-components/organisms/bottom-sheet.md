# BottomSheet

> Mobile modal surface sliding from the bottom.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Containment | 4 - Slot / Composition | existing | figma, storybook | `<s-dropdown> (mobile sheet (sheetTitle)), <s-select> (mobile sheet (sheetTitle))` |

## Props

| Prop | Values / type |
|---|---|
| `open` | boolean |
| `header` | slot |
| `body` | slot |
| `footer` | slot |
| `snapPoints` | array |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

## Source in Figma today

- Figma component set: `Bottom sheet e90621fb`

_No matching frame in the current Figma library._

## Source in the Twilight Storybook today

### `<s-dropdown>` — mobile sheet (sheetTitle)

[components-dropdown](https://dashboard-ui-components.pages.dev/?path=/docs/components-dropdown) · 13 stories · A dropdown component that displays a list of selectable items. It supports various states, search functionality, and different toggle elements.

Related elements: `<s-button>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `active` | boolean | `false` |  | Active state of the dropdown |
| `autoComplete` | boolean | `false` |  | Enables autocomplete functionality |
| `children` | string |  |  |  |
| `disabled` | boolean | `false` |  | Disabled state |
| `isOnClick` | boolean | `false` |  | Enables click event handling |
| `items` | array | `[]` |  | Items for the dropdown menu |
| `layout` | select | `start` | `start`, `end`, `expanded` | Dropdown layout |
| `loading` | boolean | `false` |  | Loading state |
| `multiselect` | boolean | `false` |  | Enables multiple item selection |
| `overlayAlignment` | select | `start` | `start`, `end` | Horizontal alignment preference for the dropdown overlay |
| `searchPlaceholder` | text | `undefined` |  | Placeholder text for the search input |
| `searchQuery` | text | `undefined` |  | Initial search query |
| `searchable` | boolean | `false` |  | Enables search functionality |
| `selectable` | boolean | `false` |  | Enables item selection |
| `sheetTitle` | text |  |  | Optional title shown in the mobile sheet header |

**Events**

| Event | Description |
|---|---|
| `itemClick` | Event emitted when an item in the dropdown is clicked. Provides the item's route or identifier. |
| `onclick` | Event emitted when the dropdown toggle button is clicked. This is the main click event for opening/closing the dropdown. |
| `onclose` | Event emitted when the dropdown menu is closed. Useful for tracking dropdown visibility state and cleanup operations. |
| `onopen` | Event emitted when the dropdown menu is opened. Useful for tracking dropdown visibility state. |
| `onselected` | Event emitted when an item is selected in the dropdown. Provides comprehensive information about the selected item including id, label, value, and icon. |
| `searchValueChange` | Event emitted when the search input value changes (only when searchable or autocomplete is enabled). Useful for implementing custom search logic or autocomplete functionality. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--default), [Selectable](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--selectable), [Searchable](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--searchable), [Layout Start](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--layout-start), [Layout End](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--layout-end), [Overlay Alignment End](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--overlay-alignment-end), [Layout Expanded](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--layout-expanded), [Multiselect](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--multiselect), [With Images](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--with-images), [With Descriptions](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--with-descriptions), [Custom Toggle](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--custom-toggle), [Loading](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--loading), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-dropdown--disabled)

**Rendered markup (default story)**

```html
<s-dropdown layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="start ltr hydrated">
  <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
    <i class="hgi-stroke h
<!-- … truncated … -->
```

### `<s-select>` — mobile sheet (sheetTitle)

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
_Generated from `catalog/components.json` (id `bottom-sheet`). Edit the catalog, not this file._
