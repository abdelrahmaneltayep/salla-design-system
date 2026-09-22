# Status

> StatusIndicator + label in subtle (dot + text) or strong (pill) appearance. Material: badge / chip.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Communication | 3 - Base + Global | existing | figma, storybook | `<s-tag> (layout=status)` |

## Props

| Prop | Values / type |
|---|---|
| `type` | `success`, `danger`, `warning`, `info`, `neutral` |
| `appearance` | `subtle`, `strong` |
| `label` | string |

## Tokens

- comp.status.*
- sys.color.status.*.dark (dot)
- sys.color.status.*.darker (label)
- sys.color.status.*.lighter (strong background)
- sys.typography.label-sm

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **StatusIndicator**.

## Notes and migration

Table/Status carries nine order-status presets (waiting payment, in progress, shipped, delivered ...). Model those as a data mapping (order status -> Status type), not as extra variants. Twilight renders this as <s-tag layout="status">; `Status` stays the design-system name.

## Source in Figma today

- Figma node: `15342:59936`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Status` | Status | 20 | Language: Arabic, English; Type: danger, info, neutral, success, warning; Appearance: strong, subtle |

## Source in the Twilight Storybook today

### `<s-tag>` — layout=status

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
_Generated from `catalog/components.json` (id `status`). Edit the catalog, not this file._
