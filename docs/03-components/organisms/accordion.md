# Accordion

> Collapsible content container (progressive disclosure) with head and body slots, grouped auto-collapse, tight / relaxed layouts and light / transparent / feature themes.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Containment | 4 - Slot / Composition | existing | storybook | `<s-accordion>` |

## Anatomy

- head (slot)
- expand icon
- body (slot, optional maxHeight scroll)

## Props

| Prop | Values / type |
|---|---|
| `theme` | `default`, `light`, `transparent`, `feature` |
| `layout` | `default`, `tight`, `relaxed` |
| `outlined` | boolean |
| `isExpanded` | boolean |
| `autoCollapse` | boolean (group) |
| `loading` | boolean |
| `disabled` | boolean |
| `readonly` | boolean |
| `maxHeight` | css length |

## States

- collapsed
- expanded
- loading
- disabled
- read-only

## Tokens

- sys.color.surface
- sys.color.outline
- sys.shape.small
- sys.typography.title-md

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

Headless layer: **useDisclosure (expanded state, aria-expanded, group coordination)**.

Composes: [Icon](../atoms/icon.md).

## Notes and migration

Storybook only: no Figma frame exists. Design one from this spec (Material: expansion panel).

## Source in Figma today

_No matching frame in the current Figma library._

## Source in the Twilight Storybook today

### `<s-accordion>`

[components-accordion](https://dashboard-ui-components.pages.dev/?path=/docs/components-accordion) · 14 stories · A collapsible content container that provides large amounts of content in a small space through progressive disclosure. Users get the essential details about the core content and can choose to expand this content within the constraints of the accordion.

Related elements: `<s-accordion-group>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `activeTab` | number | `0` |  | Initially active tab index |
| `autoCollapse` | boolean | `true` |  | AutoCollapse other accordions in the same group when one is expanded |
| `disabled` | boolean | `false` |  | Disable accordion |
| `feature` | boolean | `true` |  | Feature based dependency accordion |
| `flatHeader` | boolean | `false` |  | Removes the expand/collapse icon from header, needed in certain cases |
| `headerPadding` | text | `""` |  | Sets custom padding for the accordion header, set value as string like '1rem' or '16px 20px' |
| `isExpanded` | boolean | `false` |  | If you need accordion to be expanded by default |
| `layout` | select | `default` | `default`, `tight`, `relaxed` | You can set accordion layout to tight or relaxed if you have small area |
| `loading` | boolean | `false` |  | Accordion loading state |
| `maxHeight` | text | `auto` |  | You can set max height for accordion body, will be scrollable when content is more than max height, set value as string like '200px' |
| `outlined` | boolean | `false` |  | Adds an outline border to the accordion |
| `readonly` | boolean | `false` |  | Readonly state |
| `theme` | string | `default` | `default`, `light`, `transparent`, `feature` | Accordion theme, you can set theme to light, transparent or feature if you need feature based dependency accordion |

**Events**

| Event | Description |
|---|---|
| `accordionToggle` | Emitted when the accordion is toggled. Provides event object with the state of the accordion. |
| `onchange` | Emitted when the active tab changes. Provides the index of the new active tab. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--default), [Light](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--light), [Transparent](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--transparent), [Feature](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--feature), [Tight](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--tight), [Relaxed](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--relaxed), [Loading](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--loading), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--disabled), [Expanded](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--expanded), [Outlined](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--outlined), [Max Height](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--max-height), [Grouped](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--grouped), [Nested](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--nested), [Read Only](https://dashboard-ui-components.pages.dev/?path=/story/components-accordion--read-only)

**Rendered markup (default story)**

```html
<s-accordion theme="default" outlined="" active-tab="0" class="hydrated">
  <div slot="head">Accordion Title</div>
  <div slot="body">The accordion component provides large amounts of content in a small space through progressive disclosure. Users get the essential details about the core content and can choose to expand this content within the constraints of the accordion.</div>
</s-accordion>
```


---
_Generated from `catalog/components.json` (id `accordion`). Edit the catalog, not this file._
