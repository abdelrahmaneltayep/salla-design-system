# ActionBar

> Confirm / cancel button group, floating or flat, desktop and mobile. Material: bottom app bar / dialog actions.

| Atomic level | Material category | Structure type | Status | Storybook story |
|---|---|---|---|---|
| organism | Actions | 4 - Slot / Composition | existing | `ButtonsGroup` |

## Props

| Prop | Values / type |
|---|---|
| `type` | `float`, `flat` |
| `primary` | slot (Button) |
| `secondary` | slot (Button) |
| `start` | slot (destructive) |

## RTL and localisation

Primary action sits inline-end in both directions.

## How to build it

Build as a **container with named slots**. The component fixes structure, spacing and behaviour of the frame; the parent supplies content. Document every slot and what it accepts.

## Source in Figma today

- Figma component set: `Action Bar/Confirm buttons 02e6c000, buttonsContainer 1eba2b9a`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Action Buttons` | (top level) | - | - |

---
_Generated from `catalog/components.json` (id `action-bar`). Edit the catalog, not this file._
