# Icon

> A single glyph from the Salla icon set. 4,049 names in Stroke (outline) and Solid (filled) styles; Rounded is the default type.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Communication | 2 - Standalone | existing | figma, storybook | `<s-icon>` |

## Anatomy

- svg 1em box

## Props

| Prop | Values / type |
|---|---|
| `name` | string (e.g. add-01) |
| `style` | `outline`, `filled` |
| `size` | `sm 16`, `md 18`, `lg 20`, `xl 24` |
| `mirrorInRtl` | boolean |

## Tokens

- ref.size.icon.*
- currentColor

## RTL and localisation

Only directional glyphs (arrows, chevrons, undo/redo) set mirrorInRtl. Search, trash, settings never mirror.

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

## Notes and migration

Naming today is `{name}-{outline|filled}` in the Merchant DS while the icon library uses Style/Type variants and the Storybook uses `sicon-*` font classes. Unify on `{name}` + `style` prop; see docs/02-styles/icons.md.

## Source in Figma today

- Library: `Icons DS_V.1`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Icons/Filled` | (top level) | - | - |
| `Icons/Outline` | (top level) | - | - |

## Source in the Twilight Storybook today

### `<s-icon>`

[components-icon](https://dashboard-ui-components.pages.dev/?path=/docs/components-icon) · 1 stories · Use Icon component to display `Hugeicons` or `Sallaicons-light` within a shadowDOM component, such as table, button, uploader, etc when needed.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `icon` | string | `sicon-light-salla` |  | Icon class name representing the icon to be displayed, you can use `Hugeicons` or `Sallaicons-light` like `hgi-stroke hgi-tick-02`, `s-light-tick-02` or `sicon-light-salla |
| `size` | string | `1rem` |  | icon size, you can use rem or px, we prefer rem, default is 1rem |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-icon--default)

**Rendered markup (default story)**

```html
<s-icon icon="sicon-light-salla" size="1rem" class="hydrated">
</s-icon>
```


---
_Generated from `catalog/components.json` (id `icon`). Edit the catalog, not this file._
