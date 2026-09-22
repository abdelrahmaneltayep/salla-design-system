# TranslationToggle

> The small EN/AR language switch inside bilingual fields (Storybook: LingualField).

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| atom | Text inputs | 1 - Configurable | existing | `LingualField (inner toggle)` |

## Props

| Prop | Values / type |
|---|---|
| `language` | `ar`, `en` |

## States

- default
- hover
- open

## Tokens

- sys.color.outline
- sys.shape.small
- sys.typography.body-xs

## How to build it

Build as **one component** whose variations are props. Keep the prop list flat and enumerable; if it grows past ~8 props or needs mutually exclusive combinations, split (type 2) or introduce a base (type 3).

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_Translation` | Inputs | 2 | Language: Arabic, English |

---
_Generated from `catalog/components.json` (id `translation-toggle`). Edit the catalog, not this file._
