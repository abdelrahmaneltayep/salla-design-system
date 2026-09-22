# Avatar

> Image, text initials, icon or fallback in six sizes, circular or rectangular.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Data display | 1 - Configurable | existing | `Avatar` |

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

---
_Generated from `catalog/components.json` (id `avatar`). Edit the catalog, not this file._
