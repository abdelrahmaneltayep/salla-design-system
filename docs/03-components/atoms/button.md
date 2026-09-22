# Button

> The single action trigger. Seven colour variants x four appearances x three sizes x five states, plus a circular layout for icon-only use.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Actions | 1 - Configurable | existing | figma, storybook | `<s-button>` |

## Anatomy

- container
- icon-start (slot)
- label
- icon-end (slot)

## Props

| Prop | Values / type |
|---|---|
| `variant` | `primary`, `secondary`, `danger`, `success`, `warning`, `info`, `feature` |
| `appearance` | `filled`, `outlined`, `link`, `link-auxiliary` |
| `size` | `sm (32px)`, `md (40px)`, `lg (48px)` |
| `layout` | `default`, `circular` |
| `iconStart` | slot |
| `iconEnd` | slot |
| `loading` | boolean |
| `disabled` | boolean |

## States

- default
- hover
- pressed
- loading
- disabled
- focus-visible

## Tokens

- comp.button.*
- sys.color.primary-container (primary filled fill #a4ffe5)
- sys.color.text.brand (primary label #004956)
- sys.color.status.*.primary (danger #f55157, success #00af6c, warning #ffaf44, info #5196f3)
- sys.color.feature.* (gradient orange 200->300, label orange 800)
- sys.shape.small (8px)
- sys.typography.label-md

## RTL and localisation

iconStart/iconEnd are logical (inline-start / inline-end) and swap automatically under dir=rtl; do not mirror non-directional glyphs.

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Notes and migration

Figma variant values carry a leading `--` (--primary); drop it in code. The 'link' appearance is a Button in Figma but reads as a Link to users; expose it as `Link` (see link.md) built on the same base. `feature` is a non-semantic upsell accent and must stay out of the semantic status palette. Twilight themes add white, transparent and mahally; `outlined`, `wide`, `shadow`, `textAlignment`, `href` are props.

## Source in Figma today

- Figma node: `14526:107536`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Button` | (top level) | - | - |

## Source in the Twilight Storybook today

### `<s-button>`

[components-button](https://dashboard-ui-components.pages.dev/?path=/docs/components-button) · 15 stories · A button is a clickable element that triggers an action when clicked.

Related elements: `<s-icon>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `active` | boolean | `false` |  | Set to true to get an active button state |
| `autoHeight` | boolean | `false` |  | If the button should have auto height instead of pre-defined height, better used with transparent theme if needed |
| `disabled` | boolean | `false` |  | Disable the button |
| `feature` | boolean | `false` |  | Feature based button |
| `href` | text | `null` |  | if applied, the button will behave as a link and will have a href attribute |
| `label` | string | `null` |  | you can dynamically set the label of the button if needed |
| `layout` | select | `default` | `default`, `circular` | Button layout variant, you can default or circular, for circular button, best to use style prop to set the width and height sizes to get a perfect circle |
| `loading` | boolean | `false` |  | Loading state |
| `noPadding` | boolean | `false` |  | Remove button padding |
| `outlined` | boolean | `false` |  | Set to true to get an outlined button |
| `shadow` | boolean | `false` |  | Add shadow to the button |
| `size` | select | `md` | `sm`, `md`, `lg` | Button size |
| `style` | string |  |  |  |
| `target` | select | `_self` | `_blank`, `_self`, `_parent`, `_top` | target attribute for the button if it is a link |
| `textAlignment` | select | `center` | `start`, `center`, `end` | Text alignment within the button |
| `theme` | select | `default` | `default`, `primary`, `secondary`, `danger`, `warning`, `info`, `white`, `transparent`, `feature`, `mahally` | Button theme |
| `type` | select | `button` | `button`, `submit`, `reset` | Button type, you can use button, submit or reset (optional) |
| `wide` | boolean | `false` |  | Make button fill container width |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-button--default), [Theme Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-button--theme-variants), [Size Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-button--size-variants), [Outlined Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-button--outlined-variants), [Loading](https://dashboard-ui-components.pages.dev/?path=/story/components-button--loading), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-button--disabled), [Active](https://dashboard-ui-components.pages.dev/?path=/story/components-button--active), [Wide](https://dashboard-ui-components.pages.dev/?path=/story/components-button--wide), [Text Start](https://dashboard-ui-components.pages.dev/?path=/story/components-button--text-start), [Text End](https://dashboard-ui-components.pages.dev/?path=/story/components-button--text-end), [Has Icons](https://dashboard-ui-components.pages.dev/?path=/story/components-button--has-icons), [Circular](https://dashboard-ui-components.pages.dev/?path=/story/components-button--circular), [Link](https://dashboard-ui-components.pages.dev/?path=/story/components-button--link), [Auto Height](https://dashboard-ui-components.pages.dev/?path=/story/components-button--auto-height), [Feature](https://dashboard-ui-components.pages.dev/?path=/story/components-button--feature)

**Rendered markup (default story)**

```html
<s-button default="" class="s-btn s-btn--default default md ltr hydrated" theme="default" target="_self">Click here to learn more</s-button>
```


---
_Generated from `catalog/components.json` (id `button`). Edit the catalog, not this file._
