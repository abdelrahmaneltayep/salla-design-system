# Tab

> One tab, primary (dashboard top nav) or secondary (page sub-nav), contained or plain, with active/hover states.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Navigation | 1 - Configurable | existing | figma, storybook | `<s-tabs-group> (<s-tab-head>)` |

## Props

| Prop | Values / type |
|---|---|
| `kind` | `primary`, `secondary` |
| `contained` | boolean |
| `active` | boolean |
| `icon` | slot |
| `count` | number |

## States

- default
- hover
- active
- focus-visible

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Header Secondary Tabs` | Header | 12 | Language: Arabic, English; state: active, default, hover; Contained: Off, On |
| `Primary Tabs List - Dashboard only` | Header | 2 | Language: Arabic, English |
| `_Table/Tabs Item` | Table | 2 | Active: Off, On |
| `Header Primary Tabs` | (top level) | - | - |

## Source in the Twilight Storybook today

### `<s-tabs-group>` — <s-tab-head>

[components-tabs](https://dashboard-ui-components.pages.dev/?path=/docs/components-tabs) · 5 stories · The `s-tabs-group` component represents a group of tabs in a tabbed interface. It handles the display of tab headers and bodies, providing properties for customization, using the `s-tab-head` and `s-tab-body` components. to create a tabbed interface.

Related elements: `<s-tab-head>`, `<s-tab-body>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `id` | string | `''` |  | Tabs group unique identifier |
| `loading` | boolean | `false` |  | Loading state |
| `name` | string | `''` |  | Tabs group unique name |
| `theme` | string | `default` | `default`, `stack`, `buttons`, `underline` | Tabs group theme style, you can choose between 'default', 'stack', 'buttons' and 'underline' |
| `wide` | boolean | `true` |  | Enable full width |

**Events**

| Event | Description |
|---|---|
| `tabChanged` | Emitted when the active tab changes. Provides index, value, and payload information. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-tabs--default), [Stack](https://dashboard-ui-components.pages.dev/?path=/story/components-tabs--stack), [Buttons](https://dashboard-ui-components.pages.dev/?path=/story/components-tabs--buttons), [Underline](https://dashboard-ui-components.pages.dev/?path=/story/components-tabs--underline), [Fit Width](https://dashboard-ui-components.pages.dev/?path=/story/components-tabs--fit-width)

**Rendered markup (default story)**

```html
<div class="flex items-start flex-col gap-4">
  <s-tabs-group id="tabs_group_default" name="Default Tabs Group" theme="default" wide="" class="s-tabs-group s-tabs-group--default w-full ltr hydrated">
    <div slot="head">
      <s-tab-head value="tab_home" active="" class="s-tab-head s-tab-head--default active ltr hydrated">
        <i class="hgi-stroke hgi-home-01">
        </i> Home </s-tab-head>
        <s-tab-head value="tab_products" class="s-tab-head s-tab-head--default ltr hydrated">
          <i class="hgi-stroke hgi-shirt-01">
          </i> Products </s-tab-head>
          <s-tab-head value="tab_orders" class="s-tab-head s-tab-head--default ltr hydrated">
            <i class="hgi-stroke hgi-archive-02">
            </i> Orders </s-tab-head>
          </div>
          <div slot="body">
            <s-tab-body id="tab_home" active="" class="s-tab-body s-tab-body--default active ltr hydrated">
              <article>
                <p>Content for the Home tab.</p>
              </article>
            </s-tab-body>
            <s-tab-body id="tab_products" class="s-tab-body s
<!-- … truncated … -->
```


---
_Generated from `catalog/components.json` (id `tab`). Edit the catalog, not this file._
