# ActionBar

> Confirm / cancel button group, floating or flat, desktop and mobile. Material: bottom app bar / dialog actions.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Actions | 4 - Slot / Composition | existing | figma, storybook | `<s-buttons-group>` |

## Props

| Prop | Values / type |
|---|---|
| `type` | `float`, `flat` |
| `primary` | slot (Button) |
| `secondary` | slot (Button) |
| `start` | slot (destructive) |

## RTL and localisation

Primary action sits inline-end in both directions.

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

## Source in Figma today

- Figma component set: `Action Bar/Confirm buttons 02e6c000, buttonsContainer 1eba2b9a`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Action Buttons` | (top level) | - | - |

## Source in the Twilight Storybook today

### `<s-buttons-group>`

[components-buttonsgroup](https://dashboard-ui-components.pages.dev/?path=/docs/components-buttonsgroup) · 7 stories · A buttons group is a container that groups related buttons together, providing visual cohesion and proper spacing.

Related elements: `<s-button>`, `<s-dropdown>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `layout` | select | `horizontal` | `horizontal` | Layout direction of the buttons group, currently only horizontal is supported.. vertical will be supported soon |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-buttonsgroup--default), [Button Count Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-buttonsgroup--button-count-variants), [Theme Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-buttonsgroup--theme-variants), [With Dropdown](https://dashboard-ui-components.pages.dev/?path=/story/components-buttonsgroup--with-dropdown), [Dropdown In Middle](https://dashboard-ui-components.pages.dev/?path=/story/components-buttonsgroup--dropdown-in-middle), [Buttons With Icons](https://dashboard-ui-components.pages.dev/?path=/story/components-buttonsgroup--buttons-with-icons), [With Disabled States](https://dashboard-ui-components.pages.dev/?path=/story/components-buttonsgroup--with-disabled-states)

**Rendered markup (default story)**

```html
<s-buttons-group class="s-btn-group s-btn-group--horizontal hydrated">
  <s-button theme="white" outlined="" class="s-btn s-btn--white default md outlined ltr hydrated s-btn-group-item s-btn-group-item--start" target="_self">First Button</s-button>
  <s-button theme="white" outlined="" class="s-btn s-btn--white default md outlined ltr hydrated s-btn-group-item s-btn-group-item--end" target="_self">Second Button</s-button>
</s-buttons-group>
```


---
_Generated from `catalog/components.json` (id `action-bar`). Edit the catalog, not this file._
