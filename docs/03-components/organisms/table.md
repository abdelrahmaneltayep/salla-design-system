# DataTable

> The merchant list view: header (title, tabs, search, filters), column headers with sort / select-all, typed cells, sticky action column, row selection with bulk bar, delete, edit sheet, pagination footer, mobile card rows, empty and filter-result states.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Data display | 4 - Slot / Composition | existing | figma, storybook | `<s-table>` |

## Props

| Prop | Values / type |
|---|---|
| `columns` | array of {key, cell: TableCell type, sortable, sticky} |
| `rows` | array |
| `selectable` | boolean |
| `status` | `default`, `selected`, `filter-results`, `no-results`, `scroll`, `actions-scroll`, `tabs`, `title`, `more-menu` |
| `device` | `desktop`, `mobile` |
| `header` | slot (PanelHeader \| Tabs \| FilterResults) |
| `footer` | slot (Pagination) |
| `bulkActions` | slot |

## States

- loading
- empty
- filtered-empty
- selected
- scrolling

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Headless layer: **useDataTable (sorting, selection, pagination state)**.

Composes: [TableCell](../molecules/table-cell.md), [Checkbox](../atoms/checkbox.md), [Chip](../atoms/chip.md), [Status](../molecules/status.md), [MoreMenu](../organisms/more-menu.md), [Pagination](../organisms/pagination.md), [PanelHeader](../molecules/panel-header.md), [Tabs](../organisms/tabs.md), [FilterResults](../molecules/filter-results.md), [EmptyState](../organisms/empty-state.md).

## Notes and migration

Rename Figma's Status=[delevery, deliverd, in prograss, retrevied, wating payment, wating review] presets (typos) to a data mapping in docs/03-components/molecules/status.md.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_Table/Tabs Item` | Table | 2 | Active: Off, On |
| `_Table/Filter Results` | Table | 2 | Type: Close, Default |
| `Table/Header` | Table | 4 | Device: Desktop, Mobile; Selected: Off, On |
| `Table/Status` | Table | 9 | Status: cancelled, deleted, delevery, deliverd, in prograss, retrevied, shipped, wating payment, wating review |
| `Table/Cells` | Table | 32 | Type: Actions Toggle, Actions one icon, Actions three icons, Actions two icons, Bulk Edit, Checkbox, Chips, Date & Time, Drop Down, Image + Text one line, Image + Text two lines, Images, Markets, Percentage, Price, Price with text, Products, Sort, Status, Tags, Text, Text + Flag; Scroll: Off, On; Selected: Off, On |
| `Table` | Table | 18 | Status: Actions Scroll, Default, Filter Results, More Menu, No Results, Scroll Down, Selected, Tabs, Title, Title Scroll; Device: Desktop, Mobile |
| `Table/Footer` | Table | 2 | Device: Desktop, Mobile |
| `previewContainer` | Table | 2 | Type: Blog, Default |
| `Table/Alertbox` | Table | 4 | Hover: Off, On; Device: Desktop, Mobile |
| `Table/Delete` | Table | 2 | Location: Data, Header; Scroll: Off; Selected: Off; Deleted: Off |
| `_Table/Panel Header` | Table | 2 | Size: Default, Small |
| `_Table/Refresh Button` | Table | 2 | Active: Off, On |
| `_Table/Pin` | Table | 2 | Pin: Off, On |

## Source in the Twilight Storybook today

### `<s-table>`

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
_Generated from `catalog/components.json` (id `table`). Edit the catalog, not this file._
