# Dialog

> Centered modal (Storybook: Modal). Overlay, positioning, focus trap and close button; content via slots.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Containment | 4 - Slot / Composition | existing | storybook | `<s-modal>` |

## Props

| Prop | Values / type |
|---|---|
| `open` | boolean |
| `size` | `sm`, `md`, `lg` |
| `header` | slot |
| `body` | slot |
| `footer` | slot (ActionBar) |
| `dismissible` | boolean |

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Headless layer: **useDialog (focus trap, escape, scroll lock)**.

## Notes and migration

Twilight ships <s-modal> with <s-modal-head|body|footer> slots (sizes sm/md/lg/xlg, theme default/light). Missing from the Figma library: design it from the Storybook.

## Source in Figma today

_No matching frame in the current Figma library._

## Source in the Twilight Storybook today

### `<s-modal>`

[components-modal](https://dashboard-ui-components.pages.dev/?path=/docs/components-modal) · 1 stories · A modal component that displays a list of selectable items. It supports various states, search functionality, and different toggle elements.

Related elements: `<s-button>`, `<s-modal-head>`, `<s-modal-body>`, `<s-modal-footer>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `closable` | boolean | `false` |  | Backdrop clickable to close the modal |
| `size` | string | `md` |  | Modal size, sm, md, lg, xlg |
| `theme` | string | `default` |  | Modal theme, default or light |

**Events**

| Event | Description |
|---|---|
| `onclose` | Emitted when the modal closes. |
| `onopen` | Emitted when the modal opens. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-modal--default)

**Rendered markup (default story)**

```html
<div class="relative w-full h-full min-h-[600px] flex items-center justify-center">
  <s-button id="s_modal_toggle_s_modal" class="s-btn s-btn--default default md ltr hydrated" theme="default" target="_self">Show Modal</s-button>
  <s-modal id="s_modal" name="" size="md" theme="default" class="s-modal s-modal--default md hydrated" role="dialog" data-scrollable="" scrollable="">
    <s-modal-head class="hydrated">
      <h4 class="text-base font-bold">Modal Title</h4>
      <s-button size="sm" theme="danger" outlined="" data-modal-close="" class="s-btn s-btn--danger default sm outlined ltr hydrated" target="_self">
        <i class="hgi-stroke hgi-cancel-01">
        </i>
      </s-button>
    </s-modal-head>
    <s-modal-body class="hydrated">
      <div class="flex flex-col w-full gap-4">
        <article class="text-sm leading-[1.5]">
          <h4 class="block font-bold mb-2">Sample Content</h4>
          <p>This is the default modal content. You can customize it using the content control.</p>
        </article>
      </div>
    </s-modal-body>
    <s-modal-footer class="hydrated"
<!-- … truncated … -->
```


---
_Generated from `catalog/components.json` (id `dialog`). Edit the catalog, not this file._
