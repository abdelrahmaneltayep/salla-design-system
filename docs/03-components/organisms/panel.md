# Panel

> Card container with PanelHeader, body and footer slots (Storybook: Panel). Material: card.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Containment | 4 - Slot / Composition | existing | figma, storybook | `<s-panel>` |

## Props

| Prop | Values / type |
|---|---|
| `header` | slot (PanelHeader) |
| `body` | slot |
| `footer` | slot |
| `elevation` | `0`, `1` |

## Tokens

- sys.color.surface
- sys.color.outline
- sys.shape.small (8px, as NavigationDrawer and LearnMore use)
- sys.elevation.0

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

## Notes and migration

Twilight ships <s-panel> with <s-panel-head> (title + actions slots) and <s-panel-body>, collapsable, compact/relaxed layouts, noPadding for tables. Missing as a top-level Figma frame.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `previewContainer` | Table | 2 | Type: Blog, Default |
| `_Table/Panel Header` | Table | 2 | Size: Default, Small |

## Source in the Twilight Storybook today

### `<s-panel>`

[components-panel](https://dashboard-ui-components.pages.dev/?path=/docs/components-panel) · 6 stories · The content wrapper component

Related elements: `<s-panel-head>`, `<s-panel-body>`, `<s-table>`, `<s-button>`, `<s-dropdown>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `actions` | string |  |  |  |
| `collapsable` | boolean | `false` |  | Make panel collapsable |
| `collapsed` | boolean | `true` |  | Set collapse prop |
| `content` | string |  |  | Panel content, use the `<s-panel-body />` to add all your content inside this slot |
| `layout` | string | `relaxed` |  | for some scenarions, you may need a compact layout for panel |
| `noPadding` | boolean |  |  | Remove panel body padding, useful for full width panels with tables inside panel body |
| `overflowHidden` | boolean |  |  | overflow hidden for panel body |
| `title` | string |  |  | Panel title, you can add the title via `<s-panel-head />` and use the `title` slot |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-panel--default), [No Padding](https://dashboard-ui-components.pages.dev/?path=/story/components-panel--no-padding), [Collapsable](https://dashboard-ui-components.pages.dev/?path=/story/components-panel--collapsable), [Header Actions Slot](https://dashboard-ui-components.pages.dev/?path=/story/components-panel--header-actions-slot), [Compact Layout](https://dashboard-ui-components.pages.dev/?path=/story/components-panel--compact-layout), [Headless Panel](https://dashboard-ui-components.pages.dev/?path=/story/components-panel--headless-panel)

**Rendered markup (default story)**

```html
<s-panel collapsed="" layout="relaxed" class="s-panel ltr hydrated">
  <s-panel-head data-collapsed="true" class="hydrated">
    <div slot="title">Panel Title</div>
  </s-panel-head>
  <s-panel-body class="hydrated"> Panel content, you can add any content here inside this slot </s-panel-body>
</s-panel>
```


---
_Generated from `catalog/components.json` (id `panel`). Edit the catalog, not this file._
