# Loading

> LoadingIndicator + localised label for block-level loading.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Communication | 3 - Base + Global | existing | figma, storybook | `<s-loader>` |

## Props

| Prop | Values / type |
|---|---|
| `label` | string |
| `size` | LoadingIndicator size |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **LoadingIndicator**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Loading` | Loader | 2 | Language: Arabic, English |

## Source in the Twilight Storybook today

### `<s-loader>`

[components-loader](https://dashboard-ui-components.pages.dev/?path=/docs/components-loader) · 1 stories · Loader component to show loading state.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `size` | string | `md` | `xs`, `sm`, `md`, `lg`, `xlg` | Loader size |
| `theme` | string | `default` | `default`, `default-force`, `light`, `dark` | Loader theme |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-loader--default)

**Rendered markup (default story)**

```html
<s-loader theme="default" size="md" role="status" class="s-loader s-loader--default md hydrated">
</s-loader>
```


---
_Generated from `catalog/components.json` (id `loading`). Edit the catalog, not this file._
