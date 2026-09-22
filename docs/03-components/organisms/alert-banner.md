# AlertBanner

> Full-width page-level announcement (two layouts). Distinct layout and purpose from Alert, so standalone.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Communication | 2 - Standalone | existing | figma, storybook | `<s-alert-box> (horizontal, centerAlign)` |

## Props

| Prop | Values / type |
|---|---|
| `layout` | `1`, `2` |
| `title` | string |
| `action` | slot |
| `dismissible` | boolean |

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Alertbox_Banner` | Alertbox | 2 | Type: Type1, Type2 |

## Source in the Twilight Storybook today

### `<s-alert-box>` — horizontal, centerAlign

[components-alertbox](https://dashboard-ui-components.pages.dev/?path=/docs/components-alertbox) · 11 stories · A message box provides contextual feedback to users. It can be used to display success, warning, error, or info messages.

Related elements: `<s-alert-box-action>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `centerAlign` | boolean |  |  | set to true to center the alert box content |
| `closable` | boolean | `false` |  | Show close button, if you want user to to be able to close the alert box |
| `horizontal` | boolean |  |  | If true, the alert box will be displayed in a horizontal layout. |
| `layout` | string | `default` | `default`, `flat` | Alert box Layout, you can set layout to default or flat |
| `theme` | string | `default` | `default`, `secondary`, `danger`, `warning`, `info`, `feature` | Alert box Theme, you can set theme to default, secondary, danger, warning, info or feature |

**Events**

| Event | Description |
|---|---|
| `onclick` | Emitted when the alert box is clicked. |
| `onclose` | Emitted when the alert box is closed. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-alertbox--default), [Secondary](https://dashboard-ui-components.pages.dev/?path=/story/components-alertbox--secondary), [Danger](https://dashboard-ui-components.pages.dev/?path=/story/components-alertbox--danger), [Warning](https://dashboard-ui-components.pages.dev/?path=/story/components-alertbox--warning), [Info](https://dashboard-ui-components.pages.dev/?path=/story/components-alertbox--info), [Feature](https://dashboard-ui-components.pages.dev/?path=/story/components-alertbox--feature), [Flat](https://dashboard-ui-components.pages.dev/?path=/story/components-alertbox--flat), [Closable](https://dashboard-ui-components.pages.dev/?path=/story/components-alertbox--closable), [Horizontal](https://dashboard-ui-components.pages.dev/?path=/story/components-alertbox--horizontal), [Center Align](https://dashboard-ui-components.pages.dev/?path=/story/components-alertbox--center-align), [Custom Slot](https://dashboard-ui-components.pages.dev/?path=/story/components-alertbox--custom-slot)

**Rendered markup (default story)**

```html
<s-alert-box theme="default" layout="default" class="s-alert-box s-alert-box--default default ltr hydrated">
  <i slot="icon" class="hgi-stroke hgi-alert-02">
  </i>
  <h4 slot="title">AlertBox Title</h4>
  <article slot="desc">
    <p>This is a default alert description.</p>
  </article>
  <div slot="action">
    <s-alert-box-action slot="action" layout="btn" theme="default" href="https://example.com" target="_blank" class="hydrated">Primary Action</s-alert-box-action>
    <s-alert-box-action slot="action" layout="outlined" theme="default" href="https://example.com" target="_blank" class="hydrated">Secondary Action</s-alert-box-action>
  </div>
</s-alert-box>
```


---
_Generated from `catalog/components.json` (id `alert-banner`). Edit the catalog, not this file._
