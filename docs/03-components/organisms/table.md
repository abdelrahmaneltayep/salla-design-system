# DataTable

> The merchant list view: header (title, tabs, search, filters), column headers with sort / select-all, typed cells, sticky action column, row selection with bulk bar, delete, edit sheet, pagination footer, mobile card rows, empty and filter-result states.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Data display | 4 - Slot / Composition | existing | `Table` |

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

---
_Generated from `catalog/components.json` (id `table`). Edit the catalog, not this file._
