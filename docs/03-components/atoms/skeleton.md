# Skeleton

> Loading placeholders shaped like the content they replace: inline, list entry, article, table, settings, header and full page layouts.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Communication | 2 - Standalone | existing | storybook | `<s-skeleton>` |

## Anatomy

- shimmer blocks

## Props

| Prop | Values / type |
|---|---|
| `layout` | `inline`, `list-entry`, `article`, `rich-content`, `cart`, `checkout`, `table`, `settings`, `header`, `home-page`, `resource-page`, `sections-page`, `iframe-page` |

## Tokens

- sys.color.surface-neutral
- sys.color.surface-disabled
- sys.shape.extra-small
- motion shimmer 1.5s

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

## Notes and migration

Storybook only: no Figma frame. Each layout is a standalone preset (structure 2); page-level presets belong with templates.

## Source in Figma today

_No matching frame in the current Figma library._

## Source in the Twilight Storybook today

### `<s-skeleton>`

[components-skeleton](https://dashboard-ui-components.pages.dev/?path=/docs/components-skeleton) · 14 stories · The Skeleton component provides loading placeholders that mimic the structure of content while it's being loaded.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `layout` | string | `inline` | `inline`, `list-entry`, `article`, `rich-content`, `cart`, `checkout`, `table`, `settings`, `header`, `home-p` | Skeleton layout |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--default), [Inline](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--inline), [List Entry](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--list-entry), [Article](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--article), [Rich Content](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--rich-content), [Cart Content](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--cart-content), [Checkout](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--checkout), [Table Content](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--table-content), [Settings](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--settings), [Header](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--header), [Home Page](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--home-page), [Resource Page](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--resource-page), [Sections Page](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--sections-page), [Iframe Page](https://dashboard-ui-components.pages.dev/?path=/story/components-skeleton--iframe-page)

**Rendered markup (default story)**

```html
<s-skeleton layout="inline" role="status" class="s-skeleton s-skeleton--inline hydrated">
</s-skeleton>
```


---
_Generated from `catalog/components.json` (id `skeleton`). Edit the catalog, not this file._
