# UploadField

> File picker with drag and drop: inline, single image, single video, multiple (row or column).

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | `File Upload` |

## Props

| Prop | Values / type |
|---|---|
| `variant` | `inline`, `single-image`, `single-video`, `multiple`, `multiple-vertical` |
| `accept` | string |
| `maxSize` | number |
| `maxFiles` | number |

## States

- default
- filled
- dragging
- uploading
- error

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `upload input` | Inputs | 17 | Langugae: Arabic, English; variant: inline, multiple, multiple vertical, single-image, single-video; state: default, filled; error: false, true |

---
_Generated from `catalog/components.json` (id `upload-field`). Edit the catalog, not this file._
