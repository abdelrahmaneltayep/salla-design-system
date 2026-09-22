# Icon

> A single glyph from the Salla icon set. 4,049 names in Stroke (outline) and Solid (filled) styles; Rounded is the default type.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Communication | 2 - Standalone | existing | `Icons (sicon-* font classes)` |

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

---
_Generated from `catalog/components.json` (id `icon`). Edit the catalog, not this file._
