# Link

> Inline text action. Built on BaseButton with the `link` and `link-auxiliary` appearances so it shares focus, disabled and loading logic with Button.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Actions | 3 - Base + Global | existing | figma, storybook | `<s-button> (href + theme=transparent)` |

## Anatomy

- label
- optional icon

## Props

| Prop | Values / type |
|---|---|
| `variant` | `primary`, `secondary`, `danger`, `success`, `warning`, `info` |
| `auxiliary` | boolean |
| `href` | string |
| `external` | boolean |

## States

- default
- hover
- pressed
- disabled
- focus-visible
- visited

## Tokens

- sys.color.text.brand
- sys.typography.label-md

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseButton**.

## Source in Figma today

- Variant filter: `Appearance=--link | --link-auxiliary`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Button` | (top level) | - | - |

## Source in the Twilight Storybook today

### `<s-button>` — href + theme=transparent

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
_Generated from `catalog/components.json` (id `link`). Edit the catalog, not this file._
