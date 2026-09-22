# Pagination

> Table footer: page size, range label, previous / next and page numbers. Desktop and mobile.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Navigation | 1 - Configurable | existing | figma, storybook | `<s-table> (pagination, itemsPerPage, hasNext/PrevPage)` |

## Props

| Prop | Values / type |
|---|---|
| `page` | number |
| `pageSize` | number |
| `total` | number |
| `device` | `desktop`, `mobile` |

## RTL and localisation

Previous / next chevrons mirror in RTL.

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Table/Footer` | Table | 2 | Device: Desktop, Mobile |

## Source in the Twilight Storybook today

### `<s-table>` — pagination, itemsPerPage, hasNext/PrevPage

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
_Generated from `catalog/components.json` (id `pagination`). Edit the catalog, not this file._
