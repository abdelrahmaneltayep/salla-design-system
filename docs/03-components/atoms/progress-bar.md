# ProgressBar

> Linear determinate progress with label, description, percentage and an optional secondary percentage.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Communication | 1 - Configurable | existing | storybook | `<s-progress-bar>` |

## Anatomy

- label
- track
- fill (+ secondary fill)
- percentage

## Props

| Prop | Values / type |
|---|---|
| `percentage` | 0-100 |
| `secondaryPercentage` | 0-100 |
| `theme` | `default`, `secondary` |
| `size` | `sm`, `md`, `lg` |
| `showPercentage` | boolean |
| `shortLabel` | boolean |

## Tokens

- sys.color.primary
- sys.color.primary-container
- sys.color.surface-disabled
- sys.shape.full

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Notes and migration

Storybook only: no Figma frame. Pairs with ProgressCircle (_Percentage) which exists only in Figma; both are Material 'progress indicators'.

## Source in Figma today

_No matching frame in the current Figma library._

## Source in the Twilight Storybook today

### `<s-progress-bar>`

[components-progress-bar](https://dashboard-ui-components.pages.dev/?path=/docs/components-progress-bar) · 6 stories · A progress bar component, helping you adding a graphical element to your app. It supports various states, loading, and different toggle elements.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `desc` | string | `This is a progress bar description` |  | Progress bar description |
| `label` | string | `This is a progress bar label` |  | Progress bar label |
| `percentage` | number | `25` |  | Progress bar percentage |
| `secondaryPercentage` | number | `undefined` |  | You can add a secondary percentage to the progress bar if needed |
| `shortLabel` | boolean | `false` |  | If you need to make the label shorter, you can use this prop |
| `showPercentage` | boolean | `true` |  | Show or hide the percentage value on the progress bar |
| `size` | string | `md` |  | Progress bar size |
| `theme` | string | `default` |  | Progress bar theme, default or secondary |

**Events**

| Event | Description |
|---|---|
| `onchange` | Emitted when the progress bar value changes. |
| `onclick` | Emitted when the progress bar is clicked. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-progress-bar--default), [Short Label](https://dashboard-ui-components.pages.dev/?path=/story/components-progress-bar--short-label), [Secondary Theme](https://dashboard-ui-components.pages.dev/?path=/story/components-progress-bar--secondary-theme), [Secondary Percentage](https://dashboard-ui-components.pages.dev/?path=/story/components-progress-bar--secondary-percentage), [Large](https://dashboard-ui-components.pages.dev/?path=/story/components-progress-bar--large), [Small](https://dashboard-ui-components.pages.dev/?path=/story/components-progress-bar--small)

**Rendered markup (default story)**

```html
<s-progress-bar label="This is a progress bar label" desc="This is a progress bar description" theme="default" size="md" percentage="25" show-percentage="true" class="w-full s-progress-bar flex flex-col gap-2 default md ltr hydrated">
</s-progress-bar>
```


---
_Generated from `catalog/components.json` (id `progress-bar`). Edit the catalog, not this file._
