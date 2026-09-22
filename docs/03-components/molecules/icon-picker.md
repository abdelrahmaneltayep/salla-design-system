# IconPicker

> Trigger button opening a searchable, paginated icon grid (Hugeicons or Salla icons) inside a dropdown.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Selection | 3 - Base + Global | existing | storybook | `<s-icon-picker>` |

## Anatomy

- trigger (current icon)
- search input
- icon grid
- error message

## Props

| Prop | Values / type |
|---|---|
| `source` | `hugeicons`, `sicon` |
| `value` | icon token |
| `searchable` | boolean |
| `iconCellSize` | css length |
| `wide` | boolean |
| `feature` | boolean (gate) |
| `hasError` | boolean |
| `required` | boolean |

## States

- closed
- open
- disabled
- error
- feature-locked

## Tokens

- sys.shape.small
- sys.color.outline
- sys.elevation.3

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

Composes: [DropdownList](../organisms/dropdown-list.md), [Icon](../atoms/icon.md), [SearchField](../molecules/search-field.md).

## Notes and migration

Storybook only: no Figma frame.

## Source in Figma today

_No matching frame in the current Figma library._

## Source in the Twilight Storybook today

### `<s-icon-picker>`

[components-iconpicker](https://dashboard-ui-components.pages.dev/?path=/docs/components-iconpicker) · 12 stories · Searchable, paginated icon grid rendered inside a built-in dropdown. Renders the currently-picked icon in a trigger button; the grid opens on click.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `disabled` | boolean |  |  | Disables the picker — trigger becomes non-interactive and the dropdown won't open. |
| `errorMessage` | text |  |  | Optional error message shown under the trigger when `hasError` is true. |
| `feature` | boolean | `true` |  | Feature-flag guard. When locked, the trigger won't open and clicks reroute to the upgrade flow. |
| `hasError` | boolean |  |  | Renders the trigger in an error state (danger border/text). |
| `iconCellSize` | text | `2.5rem` |  | Height / width of each grid tile. |
| `iconSize` | text | `1.25rem` |  | Font size of icons inside grid cells. |
| `minWidth` | text | `10rem` |  | Minimum width of the trigger button. Any CSS length. Ignored when `wide` is set. |
| `name` | text |  |  | Form field name (participates in native `<form>` submission). |
| `placeholder` | text |  |  | Search-input placeholder. |
| `required` | boolean |  |  | Marks the field as required for native form validity. |
| `searchable` | boolean | `true` |  | Show the search input above the grid. |
| `source` | string | `hugeicons` | `hugeicons`, `sicon` | Icon library — `hugeicons` (prefixed) or `sicon`. |
| `value` | text |  |  | Selected icon name / class token. |
| `wide` | boolean |  |  | Stretch the trigger to fill its container; the panel widens to match. Takes precedence over `min-width`. |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when an icon is picked. `event.detail.payload.value` carries the token. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--default), [With Value](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--with-value), [Salla Icons](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--salla-icons), [No Search](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--no-search), [Custom Sizing](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--custom-sizing), [Wide](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--wide), [Feature Locked](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--feature-locked), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--disabled), [With Error](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--with-error), [Required](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--required), [With Value Display](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--with-value-display), [Shared Cache](https://dashboard-ui-components.pages.dev/?path=/story/components-iconpicker--shared-cache)

**Rendered markup (default story)**

```html
<s-icon-picker source="hugeicons" class="s-icon-picker hydrated" style="--picker-min-width: 10rem; --picker-cell-size: 2.5rem; --picker-overlay-width: calc(2.5rem * 5 + 6rem); --picker-trigger-width: 1252px;">
</s-icon-picker>
```


---
_Generated from `catalog/components.json` (id `icon-picker`). Edit the catalog, not this file._
