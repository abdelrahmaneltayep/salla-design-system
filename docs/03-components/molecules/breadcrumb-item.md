# BreadcrumbItem

> One breadcrumb node: icon, text or overflow menu trigger.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Navigation | 1 - Configurable | existing | figma, storybook | `<s-breadcrumbs> (items[])` |

## Props

| Prop | Values / type |
|---|---|
| `type` | `icon`, `text`, `more` |
| `current` | boolean |
| `disabled` | boolean |

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_breadcrumbItem` | Bread crumb | 20 | Language: Arabic, English; Status: active, default, disabled, hover, onclick; Type: Icon, More, Separator, Text |

## Source in the Twilight Storybook today

### `<s-breadcrumbs>` — items[]

[components-breadcrumbs](https://dashboard-ui-components.pages.dev/?path=/docs/components-breadcrumbs) · 5 stories · A breadcrumb is a navigation component that allows users to track their location within a website or application.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `isOnClick` | boolean | `false` |  | Specifies if the breadcrumbs are clickable, if true, the breadcrumbClick event will be emitted |
| `items` | string | `[]` |  | Breadcrumbs items |
| `loading` | boolean | `false` |  | Specifies if the breadcrumbs are in a loading state |
| `maxVisibleItems` | number | `5` |  | Maximum number of visible items, the rest will be hidden in a dropdown |

**Events**

| Event | Description |
|---|---|
| `breadcrumbClick` | Emitted when a breadcrumb is clicked. Provides the clicked breadcrumb value. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-breadcrumbs--default), [Array Format](https://dashboard-ui-components.pages.dev/?path=/story/components-breadcrumbs--array-format), [Max Visible Items](https://dashboard-ui-components.pages.dev/?path=/story/components-breadcrumbs--max-visible-items), [Loading](https://dashboard-ui-components.pages.dev/?path=/story/components-breadcrumbs--loading), [With Click Handler](https://dashboard-ui-components.pages.dev/?path=/story/components-breadcrumbs--with-click-handler)

**Rendered markup (default story)**

```html
<s-breadcrumbs items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Home&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Category&quot;,&quot;route&quot;:&quot;/category&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Subcategory&quot;,&quot;route&quot;:&quot;/subcategory&quot;}]" max-visible-items="5" class="s-breadcrumbs ltr hydrated">
</s-breadcrumbs>
```


---
_Generated from `catalog/components.json` (id `breadcrumb-item`). Edit the catalog, not this file._
