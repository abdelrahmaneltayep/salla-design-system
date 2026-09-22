# EmptyState

> Illustration + title + description + action for empty lists and no-results.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Communication | 4 - Slot / Composition | existing | figma, storybook | `<s-placeholder>` |

## Props

| Prop | Values / type |
|---|---|
| `illustration` | Illustration name |
| `title` | string |
| `description` | string |
| `action` | slot (Button) |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Composes: [Illustration](../atoms/illustration.md), [Button](../atoms/button.md).

## Notes and migration

Twilight ships this as <s-placeholder> (icon, label, desc, actions slot, sizes sm/md/lg) and DataTable uses it for emptyPlaceholder*. Rename in code to EmptyState or keep Placeholder as alias.

## Source in Figma today

- Related: Table Status=No Results, Drop Down List Variant=No Results

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Illustrations Collection` | (top level) | - | - |

## Source in the Twilight Storybook today

### `<s-placeholder>`

[components-placeholder](https://dashboard-ui-components.pages.dev/?path=/docs/components-placeholder) · 3 stories · Placeholder component is used to display a placeholder for a component or page.

Related elements: `<s-icon>`, `<s-button>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `actions` | text | `Upgrade now & learn more buttons` |  | Actions slot content - insert your action buttons in the `actions` slot |
| `desc` | string | `You can select specific details such as name, price, and more…` |  | Placeholder description (optional) |
| `icon` | string | `hgi-stroke hgi-package-open` |  | Hugeicons class name rendered in the `icon` slot |
| `label` | string | `Add a template to customize the export with only the information you need!` |  | Placeholder label |
| `size` | string | `md` |  | Placeholder size |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-placeholder--default), [Small](https://dashboard-ui-components.pages.dev/?path=/story/components-placeholder--small), [Large](https://dashboard-ui-components.pages.dev/?path=/story/components-placeholder--large)

**Rendered markup (default story)**

```html
<s-placeholder label="Add a template to customize the export with only the information you need!" desc="You can select specific details such as name, price, and more…" size="md" class="s-placeholder md hydrated">
  <div slot="icon">
    <s-icon icon="hgi-stroke hgi-package-open" size="4rem" class="hydrated">
    </s-icon>
  </div>
  <div slot="actions">
    <s-button outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">Upgrade now</s-button>
    <s-button theme="transparent" no-padding="true" class="text-primary underline s-btn s-btn--transparent default md ltr hydrated" target="_self">learn more</s-button>
  </div>
</s-placeholder>
```


---
_Generated from `catalog/components.json` (id `empty-state`). Edit the catalog, not this file._
