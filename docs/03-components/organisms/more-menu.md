# MoreMenu

> Overflow (kebab) menu anchored to a trigger, three layouts, left/right placement.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Containment | 4 - Slot / Composition | existing | figma, storybook | `<s-dropdown>` |

## Props

| Prop | Values / type |
|---|---|
| `trigger` | slot (IconButton) |
| `items` | array of MenuItem \| Divider |
| `placement` | `start`, `end` |

## RTL and localisation

Placement uses logical start/end; Figma's Dir=Left/Right becomes placement=end/start under RTL.

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Headless layer: **useMenu**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_moreItems` | More Menu | 4 | Type: Icon, Image, Sperator; danger: Off, On |
| `More Menu` | More Menu | 4 | Type: Type1, Type2, Type3; Dir: Left, Off, Right |

## Source in the Twilight Storybook today

### `<s-dropdown>`

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


---
_Generated from `catalog/components.json` (id `more-menu`). Edit the catalog, not this file._
