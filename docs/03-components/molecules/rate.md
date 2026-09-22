# Rate

> Star (half-step) or emoji rating, read-only or interactive, with themed fills.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Selection | 1 - Configurable | existing | storybook | `<s-rate>` |

## Anatomy

- icons ×maxStars
- value label

## Props

| Prop | Values / type |
|---|---|
| `value` | number |
| `maxStars` | number |
| `iconStyle` | `star`, `emoji` |
| `theme` | `default`, `secondary`, `danger`, `warning`, `info` |
| `size` | `sm`, `md`, `lg` |
| `readOnly` | boolean |
| `hideValue` | boolean |

## States

- read-only
- interactive
- hover
- focus

## Tokens

- sys.color.warning-primary (stars)
- sys.color.status.*

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Notes and migration

Storybook only: no Figma frame.

## Source in Figma today

_No matching frame in the current Figma library._

## Source in the Twilight Storybook today

### `<s-rate>`

[components-rate](https://dashboard-ui-components.pages.dev/?path=/docs/components-rate) · 9 stories · The s-rate component represents a rating system that allows users to provide or view ratings. It supports two icon styles: `star` (classic half-star capable stars) and `emoji` (5 expressive face icons: angry → confused → neutral → happy → star-face). In emoji mode the value is always a whole number (1–5) and the `rateChanged` payload contains the selected emoji icon class instead of maxStars/totalRate.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `hideValue` | boolean | `true` |  | Hide rate value |
| `iconStyle` | string | `star` | `star`, `emoji` | Icon style for the rating. `star` uses the classic star icons; `emoji` uses expressive face icons (angry → sad → neutral → happy → star-face). |
| `maxStars` | number | `5` |  | Rate max stars |
| `readOnly` | boolean | `false` |  | Enable this if you want to make the rate read only |
| `required` | boolean |  |  |  |
| `size` | string | `md` | `sm`, `md`, `lg` | Rate size, you can choose between `sm`, `md` and `lg |
| `theme` | string | `default` | `default`, `secondary`, `danger`, `warning`, `info` | Rate theme |
| `totalRate` | number | `100` |  | Total rate |
| `value` | number | `3` |  | Rate value |

**Events**

| Event | Description |
|---|---|
| `onRateChanged` | Emitted when the rating value changes. In `star` mode the payload contains `{ value, maxStars, totalRate }`; in `emoji` mode it contains `{ value, emoji }` where `emoji` is the selected HugeIcons class (e.g. `hgi-solid hgi-smile`). |
| `rateChanged` | Emitted when a star or emoji is clicked, providing the new value and mode-specific payload. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-rate--default), [Read Only](https://dashboard-ui-components.pages.dev/?path=/story/components-rate--read-only), [Hide Value](https://dashboard-ui-components.pages.dev/?path=/story/components-rate--hide-value), [Warning Theme](https://dashboard-ui-components.pages.dev/?path=/story/components-rate--warning-theme), [Danger Theme](https://dashboard-ui-components.pages.dev/?path=/story/components-rate--danger-theme), [Large](https://dashboard-ui-components.pages.dev/?path=/story/components-rate--large), [Small](https://dashboard-ui-components.pages.dev/?path=/story/components-rate--small), [Emoji](https://dashboard-ui-components.pages.dev/?path=/story/components-rate--emoji), [Emoji Read Only](https://dashboard-ui-components.pages.dev/?path=/story/components-rate--emoji-read-only)

**Rendered markup (default story)**

```html
<s-rate value="3" theme="default" max-stars="5" total-rate="100" size="md" icon-style="star" class="s-rate s-rate--default s-rate--horizontal ltr md hydrated" id="" name="" layout="horizontal" maxstars="5" totalrate="100" iconstyle="star">
</s-rate>
```


---
_Generated from `catalog/components.json` (id `rate`). Edit the catalog, not this file._
