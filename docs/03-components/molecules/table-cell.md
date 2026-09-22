# TableCell

> Typed cells: name, sub-name, image, products, amount, percentage, status, tags, markets (flag + text), variant, data (text / date-time / dropdown), actions (1-3 icons or toggle), checkbox, chip, disabled, sort and header.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Data display | 2 - Standalone | existing | `Table (cells)` |

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

---
_Generated from `catalog/components.json` (id `table-cell`). Edit the catalog, not this file._
