# Tooltip

> Hover / focus hint on a primary-container surface with a caret. Exists in Figma as a component set (used inside CheckboxField disabled-info) but has no top-level frame on the components page.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Communication | 5 - Headless | existing | figma, storybook | `<s-tooltip>` |

## Props

| Prop | Values / type |
|---|---|
| `content` | string |
| `placement` | `top`, `bottom`, `start`, `end` |

## Tokens

- comp.tooltip.*
- sys.color.primary-container (#a4ffe5)
- sys.color.on-primary-container (#004956)
- sys.typography.body-sm
- sys.elevation.3 (Shadows/lg)
- sys.shape.extra-small

## How to build it

Build the **logic as a headless hook / controller** (state, keyboard, focus, ARIA) and a thin UI component on top. The hook must be usable with custom UI; document it with examples since it is invisible in Figma.

Headless layer: **useTooltip**.

## Notes and migration

Figma guidance on the disabled-info variants: when a control is disabled because of something the merchant can change, keep the label in normal colour and put a link in the tooltip (e.g. "Verify your email to enable notifications. Verify now"). Twilight <s-tooltip> adds themes (default/secondary/white/feature/danger), 12 placements, hover/click toggle, title + action slots.

## Source in Figma today

- Figma node: `1933:1790`
- Variant filter: `--disabled=--disabled-info-tooltip`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `checkboxfield` | check Box | 16 | Language: Arabic, English; disabled: default, disabled, disabled-info, disabled-info-tooltip; selected: False, True |

## Source in the Twilight Storybook today

### `<s-tooltip>`

[components-tooltip](https://dashboard-ui-components.pages.dev/?path=/docs/components-tooltip) · 27 stories · Tooltip component provides contextual information when users hover or click on an element. It displays helpful content in a small overlay positioned relative to the trigger element.

It exposes three slots:

- `toggle`: the trigger element, any element can be used (button, avatar, icon, inline text…).
- `title`: the tooltip heading, it is bolded by the component.
- default: the tooltip body, it accepts any markup, including `<s-tooltip-action>` actions.

Related elements: `<s-button>`, `<s-tooltip-action>`, `<s-icon>`, `<s-avatar>`, `<s-tag>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `layout` | string | `normal` | `tight`, `normal`, `relaxed` | Tooltip layout |
| `placement` | string | `top center` | `bottom`, `bottom-start`, `bottom-end`, `top`, `top-start`, `top-end`, `right`, `right-start`, `right-end` | Tooltip placement |
| `theme` | string | `default` | `default`, `secondary`, `white`, `feature`, `danger` | Tooltip theme |
| `toggleAction` | string | `hover` | `hover`, `click` | Toggle action |
| `width` | string | `300px` |  | Tooltip width |

**Slots**

| Slot | Description |
|---|---|
| `content` | Default slot, raw HTML for the tooltip body. It accepts any markup: paragraphs, lists, media, `s-tooltip-action` or `s-button` actions. |
| `title` | title` slot, the content is rendered inside `<h4 slot="title">` so inline markup such as icons is supported. Leave it empty to render a tooltip without a title. |
| `toggle` | toggle` slot, raw HTML for the trigger element, it must carry `slot="toggle"`. Any element works: `s-button`, `s-avatar`, `s-tag`, an icon or plain inline text. |

**Events**

| Event | Description |
|---|---|
| `onclose` | Emitted when the tooltip is closed. |
| `onopen` | Emitted when the tooltip is opened. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--default), [Secondary](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--secondary), [White](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--white), [Danger](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--danger), [Top Start](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--top-start), [Top End](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--top-end), [Bottom Center](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--bottom-center), [Bottom Start](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--bottom-start), [Bottom End](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--bottom-end), [Center Start](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--center-start), [Center End](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--center-end), [Click Toggle](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--click-toggle), [Tight](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--tight), [Relaxed](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--relaxed), [Custom Width](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--custom-width), [Icon Trigger](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--icon-trigger), [Avatar Trigger](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--avatar-trigger), [Inline Text Trigger](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--inline-text-trigger), [Title With Icon](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--title-with-icon), [Without Title](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--without-title), [List Content](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--list-content), [Key Value Content](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--key-value-content), [Media Content](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--media-content), [Multiple Actions](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--multiple-actions), [Feature Locked](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--feature-locked), [Media Card With Image](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--media-card-with-image), [Media Card With Video](https://dashboard-ui-components.pages.dev/?path=/story/components-tooltip--media-card-with-video)

**Rendered markup (default story)**

```html
<div style="min-height: 30vh;" class="flex items-center justify-center">
  <s-tooltip theme="default" width="300px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
    <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
    <h4 slot="title">Tooltip title</h4>
    <article>
      <p>This is the tooltip content that provides helpful information to users.</p>
      <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
    </article>
  </s-tooltip>
</div>
```


---
_Generated from `catalog/components.json` (id `tooltip`). Edit the catalog, not this file._
