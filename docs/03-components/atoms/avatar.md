# Avatar

> Image, text initials, icon or fallback in six sizes, circular or rectangular.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Data display | 1 - Configurable | existing | figma, storybook | `<s-avatar>` |

## Anatomy

- container
- image | initials | icon

## Props

| Prop | Values / type |
|---|---|
| `variant` | `image`, `text`, `icon`, `avatar-fallback`, `image-fallback` |
| `size` | `xs`, `sm`, `md`, `lg`, `xl`, `2xl` |
| `shape` | `circular`, `rectangular` |

## Tokens

- sys.shape.full | sys.shape.small
- sys.color.primary-container

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Notes and migration

Placeholder image sets (_AvatarplaholderImages, _BanksPlaceholderImages) are assets, not components; move them to assets/.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Avatar` | Avatar | 60 | Variant: avatar, avatar-fallback, icon, image-fallback, text; Size: 2xl, lg, md, sm, xl, xs; radius: circular, rectangular |
| `_AvatarplaholderImages` | Avatar | 10 | Image: 1, 2, 3, 4, 5, 6, 7, 8, 9, arabic-male |
| `_BanksPlaceholderImages` | Avatar | 1 | Image: Alarjhi |

## Source in the Twilight Storybook today

### `<s-avatar>`

[components-avatar](https://dashboard-ui-components.pages.dev/?path=/docs/components-avatar) · 16 stories · An avatar is a graphical representation of a user, typically a photo or icon, used to represent a person or entity in a user interface.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `desc` | string |  |  | Description displayed below avatar label |
| `icon` | text |  |  | If you want to show an icon instead of an image, we are using huge icons, so you can use icons classes here like `hgi-stroke hgi-user-multiple-02 |
| `iconSize` | text | `md` |  | Custom icon size |
| `imageFit` | select | `cover` | `cover`, `contain`, `fit` | Image fit type, cover, contain, fit |
| `initials` | boolean | `false` |  | If you want to show initials instead of an image, you can use this property |
| `initialsLabel` | text | `undefined` |  | Custom text to extract initials from when initials=true. If not provided, will use the label prop. Supports 1-2 characters for direct display or longer text for auto-extraction. |
| `isActive` | boolean | `false` |  | adds an active indicator to the avatar image to show that the user is active |
| `label` | string |  |  | Label displayed next to avatar image |
| `layout` | string | `circular` | `circular`, `rounded` | Layout variant, you can use either circular, rounded |
| `loading` | boolean | `false` |  | Shows loading state for the avatar |
| `outlined` | boolean | `false` |  | You can also add outline to the avatar image |
| `responsive` | boolean | `false` |  | If set to true, label and description will be hidden on mobile only avatar image will be visible |
| `shadow` | boolean | `false` |  | You can add shadow to the avatar image |
| `size` | string | `md` | `xs`, `sm`, `md`, `lg` | Avatar size |
| `status` | select | `undefined` | `None`, `info`, `success`, `warning`, `danger` | Predefined status badge shown on the avatar thumbnail. Adds a colored icon badge and a matching border to the thumb. |
| `url` | string |  |  | Image URL |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--default), [Circular](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--circular), [Rounded](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--rounded), [Initials](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--initials), [Icons](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--icons), [Icon Size Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--icon-size-variants), [Shadow And Outline](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--shadow-and-outline), [Image Cover Fit](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--image-cover-fit), [Image Contain Fit](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--image-contain-fit), [Size Variations](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--size-variations), [Loading State](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--loading-state), [Active State](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--active-state), [Responsive](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--responsive), [Without Thumbnail](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--without-thumbnail), [Status Badge](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--status-badge), [Status Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-avatar--status-variants)

**Rendered markup (default story)**

```html
<s-avatar label="James Bond" desc="Special agent 007" layout="circular" size="md" url="https://i.pravatar.cc/100" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated">
</s-avatar>
```


---
_Generated from `catalog/components.json` (id `avatar`). Edit the catalog, not this file._
