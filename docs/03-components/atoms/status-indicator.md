# StatusIndicator

> The 10px coloured dot. Base of Status.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Communication | 1 - Configurable | existing | figma, storybook | `<s-tag> (layout=status renders the dot)` |

## Anatomy

- dot

## Props

| Prop | Values / type |
|---|---|
| `color` | `success`, `danger`, `warning`, `info`, `neutral` |
| `size` | `xs`, `sm`, `md`, `lg`, `xl`, `2xl` |

## Tokens

- sys.color.status.*.dark (success #008c56, danger #ca4146)
- sys.shape.full

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_Base Status Indicator` | Status | 30 | Color: danger, info, neutral, success, warning; Size: 2xl, lg, md, sm, xl, xs |

## Source in the Twilight Storybook today

### `<s-tag>` — layout=status renders the dot

[components-tag](https://dashboard-ui-components.pages.dev/?path=/docs/components-tag) · 13 stories · A tag is a visual element used for categorization, labeling, or marking content. Tags can be customized with different themes, sizes, and behaviors.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `closable` | boolean | `false` |  | Enable closable tag |
| `disabled` | boolean | `false` |  | Disabled state |
| `feature` | boolean | `true` |  | Show feature tag for a certain element |
| `label` | string |  |  |  |
| `layout` | select | `default` | `default`, `status` | Tag layout |
| `nowrap` | boolean | `true` |  | Prevent text wrapping inside the tag |
| `outlined` | boolean | `false` |  | Outlined state |
| `size` | select | `md` | `sm`, `md` | Tag size |
| `theme` | select | `default` | `default`, `secondary`, `success`, `danger`, `warning`, `info`, `white`, `transparent`, `feature`, `mahally` | Tag theme |

**Events**

| Event | Description |
|---|---|
| `onclose` | Emitted when the tag is closed. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--default), [Theme Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--theme-variants), [Size Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--size-variants), [Outlined Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--outlined-variants), [Status Layout](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--status-layout), [Closable](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--closable), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--disabled), [Closable Theme Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--closable-theme-variants), [Long Text](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--long-text), [No Wrap](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--no-wrap), [With Feature](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--with-feature), [Disabled Feature](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--disabled-feature), [Mixed Examples](https://dashboard-ui-components.pages.dev/?path=/story/components-tag--mixed-examples)

**Rendered markup (default story)**

```html
<s-tag class="s-tag s-tag--default whitespace-nowrap md ltr hydrated">New</s-tag>
```


---
_Generated from `catalog/components.json` (id `status-indicator`). Edit the catalog, not this file._
