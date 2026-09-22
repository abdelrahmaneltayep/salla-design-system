# InlineAlert

> Compact, non-dismissible alert placed under a field or inside a card (Alertbox Type=Inline).

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Communication | 3 - Base + Global | existing | figma, storybook | `<s-alert-box> (layout=flat)` |

## Props

| Prop | Values / type |
|---|---|
| `variant` | `info`, `success`, `warning`, `danger` |
| `text` | string |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseAlert**.

## Source in Figma today

- Variant filter: `Type=Inline`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Alertbox` | Alertbox | 64 | Language: Arabic, English; variant: danger, info, success, warning; Type: Default, Inline, white; Title: Off, On; Trasnparet: Off, On |

## Source in the Twilight Storybook today

### `<s-alert-box>` — layout=flat

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
_Generated from `catalog/components.json` (id `inline-alert`). Edit the catalog, not this file._
