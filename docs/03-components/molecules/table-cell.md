# TableCell

> Typed cells: name, sub-name, image, products, amount, percentage, status, tags, markets (flag + text), variant, data (text / date-time / dropdown), actions (1-3 icons or toggle), checkbox, chip, disabled, sort and header.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Data display | 2 - Standalone | existing | figma, storybook | `<s-table> (headers[] + items[]; custom slots for typed cells)` |

## Props

| Prop | Values / type |
|---|---|
| `type` | one cell component per type: TextCell, NameCell, ImageCell, AmountCell, PercentageCell, StatusCell, TagsCell, MarketCell, DateCell, ActionsCell, CheckboxCell, ChipCell, HeaderCell |
| `status` | `default`, `hover`, `focus`, `edit` |
| `twoLines` | boolean |
| `empty` | boolean |

## States

- default
- hover
- focus
- edit

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

## Notes and migration

Standalone per type (structure 2) so each cell has a tiny API; they share a CellLayout base for padding and alignment. Rename Varient -> VariantCell, Data -> DateCell / TextCell / SelectCell.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Table/Cell/Flag_with_text` | Table | 3 | Type: Text + Flag; Status: Default, Edit, Hover |
| `Table/Cell/Markets` | Table | 3 | Type: Text + Flag; Status: Default, Edit, Hover |
| `Table/Cell/Actions` | Table | 12 | Type: Actions Toggle, Actions one icon, Actions three icons, Actions two icons; Status: Default, Focus, Hover |
| `Table/Cell/Status` | Table | 3 | Status: Default, Focus, Hover |
| `Table/Cell/Tags` | Table | 3 | Status: Default, Focus, Hover |
| `Table/Cell/Products` | Table | 3 | Status: Default, Focus, Hover; Hover: Off |
| `Table/Cell/Image` | Table | 6 | Status: Default, Focus, Hover; Hover: Off; Empty: Off, On |
| `Table/Cell/Amount` | Table | 6 | Status: Default, Focus, Hover; Type: Default, price with text |
| `Table/Cell/Name` | Table | 6 | Status: Default, Focus, Hover; Two Lines: Off, On |
| `Table/Cell/Varient` | Table | 3 | Status: Default, Focus, Hover |
| `Table/Cell/Percentage` | Table | 3 | Status: Default, Focus, Hover |
| `Table/Cell/SubName` | Table | 6 | Status: Default, Focus, Hover; Two Lines: Off, On |
| `Table/Cell/Data` | Table | 9 | Type: Date & Time, Dropdown, Text; Status: Default, Edit, Hover |
| `Table/Cell/Sort` | Table | 3 | Type: Text; Status: Default, Hover, press |
| `Table/Cell/Checkbox` | Table | 3 | Type: Text; Status: Default, Hover, press |
| `Table/Cell/Disabled` | Table | 1 | Type: Text; Status: Default |
| `Table/Cell/Chip` | Table | 6 | Count: Multi, One; Status: Default, Hover, press |
| `Table/Cell/Header` | Table | 6 | Scroll: Off; Type: Default, End, Start; Status: Default, Hover |
| `Table/Cells` | Table | 32 | Type: Actions Toggle, Actions one icon, Actions three icons, Actions two icons, Bulk Edit, Checkbox, Chips, Date & Time, Drop Down, Image + Text one line, Image + Text two lines, Images, Markets, Percentage, Price, Price with text, Products, Sort, Status, Tags, Text, Text + Flag; Scroll: Off, On; Selected: Off, On |
| `_Table/Product Image` | Table | 2 | Active: Off, On |
| `Image` | Table | 2 | Hover: Off, On |

## Source in the Twilight Storybook today

### `<s-table>` — headers[] + items[]; custom slots for typed cells

[components-table](https://dashboard-ui-components.pages.dev/?path=/docs/components-table) · 9 stories · The table component is a customizable table that provides functionalities for sorting, pagination, and filtering.

Related elements: `<s-panel>`, `<s-panel-head>`, `<s-panel-body>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `children` | string |  |  |  |
| `emptyPlaceholderDesc` | text | `undefined` |  | Description to display when there's no data |
| `emptyPlaceholderIcon` | text | `undefined` |  | Icon to display when there's no data |
| `emptyPlaceholderLabel` | text | `undefined` |  | Label to display when there's no data |
| `fetchUrl` | text | `undefined` |  | Table data source url |
| `hasNextPage` | boolean | `false` |  | Indicates if there is a next page available |
| `hasPrevPage` | boolean | `false` |  | Indicates if there is a previous page available |
| `headers` | array | `["Name", "Age", "Visits", "Progress"]` |  | Table headers |
| `items` | array | `TABLE_ITEMS` |  | Table data |
| `itemsPerPage` | string | `["10", "20", "30", "40", "50"]` |  | Items per page |
| `layout` | string | `scroll` |  | Table layout, scroll or responsive, default is scroll |
| `loading` | boolean | `false` |  | Loading state |
| `pagination` | boolean | `true` |  | Table pagination |
| `searchPlaceholder` | string | `Search...` |  | Table search placeholder |
| `searchable` | boolean | `false` |  | Enable table search |
| `selectable` | boolean | `false` |  | Enable table row selection |
| `sortBy` | object | `undefined` |  | Sorting configuration for columns in the table |
| `sortable` | boolean | `false` |  | Enable table sorting |
| `transform` | object | `undefined` |  | Transform data before passing to the component |

**Events**

| Event | Description |
|---|---|
| `onNextButtonClicked` | Event emitted when next page button is clicked |
| `onPrevButtonClicked` | Event emitted when previous page button is clicked |
| `onSelect` | Event emitted when single or all rows are selected |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-table--default), [With Search](https://dashboard-ui-components.pages.dev/?path=/story/components-table--with-search), [Sorting](https://dashboard-ui-components.pages.dev/?path=/story/components-table--sorting), [Selection](https://dashboard-ui-components.pages.dev/?path=/story/components-table--selection), [Custom Pagination](https://dashboard-ui-components.pages.dev/?path=/story/components-table--custom-pagination), [Empty State](https://dashboard-ui-components.pages.dev/?path=/story/components-table--empty-state), [Responsive Layout](https://dashboard-ui-components.pages.dev/?path=/story/components-table--responsive-layout), [Custom Slots](https://dashboard-ui-components.pages.dev/?path=/story/components-table--custom-slots), [All Features](https://dashboard-ui-components.pages.dev/?path=/story/components-table--all-features)

**Rendered markup (default story)**

```html
<s-panel no-padding="" class="s-panel no-padding ltr">
  <s-panel-head data-collapsed="true" class="hydrated">
    <h2 slot="title">Table Component</h2>
  </s-panel-head>
  <s-panel-body>
    <s-table items="[{&quot;name&quot;:&quot;John Wick&quot;,&quot;age&quot;:&quot;24&quot;,&quot;visits&quot;:&quot;100&quot;,&quot;progress&quot;:&quot;54&quot;},{&quot;name&quot;:&quot;James Bond&quot;,&quot;age&quot;:&quot;24&quot;,&quot;visits&quot;:&quot;100&quot;,&quot;progress&quot;:&quot;54&quot;},{&quot;name&quot;:&quot;Joe&quot;,&quot;age&quot;:&quot;45&quot;,&quot;visits&quot;:&quot;20&quot;,&quot;progress&quot;:&quot;68&quot;,&quot;options&quot;:&quot;&quot;},{&quot;name&quot;:&quot;Joe&quot;,&quot;age&quot;:&quot;45&quot;,&quot;visits&quot;:&quot;20&quot;,&quot;progress&quot;:&quot;68&quot;,&quot;options&quot;:&quot;&quot;},{&quot;name&quot;:&quot;Joe&quot;,&quot;age&quot;:&quot;45&quot;,&quot;visits&quot;:&quot;20&quot;,&quot;progress&quot;:&quot;68&quot;,&quot;options&quot;:&quot;&quot;},{&quot;name&quot;:&quot;Joe&quot;,&quot;age&quot;:&quot;45&quot;,&quot;visits&quot;:&quot;20&quot
<!-- … truncated … -->
```


---
_Generated from `catalog/components.json` (id `table-cell`). Edit the catalog, not this file._
