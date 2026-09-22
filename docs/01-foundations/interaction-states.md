# Interaction states

One fixed vocabulary of states for every interactive component, following Material's *Interaction states*. Components document these and no others.

## The list

| State | Trigger | Visual rule | CSS / ARIA |
|---|---|---|---|
| **Enabled** | default | as designed | – |
| **Hover** | pointer over | surface darkens ~4–8%; outlined and link variants gain a tinted background | `:hover` |
| **Focus** | keyboard focus | 2px ring `sys.focus.ring-color` (#a4ffe5) offset 2px; never removed | `:focus-visible` |
| **Pressed** | pointer down / Enter | surface darkens ~12%; no scale transforms | `:active` |
| **Dragged** | drag in progress (UploadField, sortable rows) | elevation 3, 90% opacity | `[data-dragging]` |
| **Disabled** | `disabled` | 38% opacity on content, no hover/pressed, `cursor: not-allowed` | `:disabled`, `aria-disabled` |
| **Loading** | `loading` | content replaced or overlaid by `LoadingIndicator`, width preserved, pointer events off | `aria-busy` |
| **Selected** | on/checked (Checkbox, Radio, Switch, Chip, Tab, ListItem, table row) | primary fill or primary outline | `aria-checked` / `aria-selected` |
| **Activated** | current navigation target (NavigationItem, Tab, BreadcrumbItem) | primary text + indicator | `aria-current` |
| **Error** | validation failed (fields) | outline and helper text `sys.color.status.danger.primary`; orthogonal to the states above | `aria-invalid` |
| **Read-only** | `readOnly` (fields) | no outline change on focus, text selectable | `readonly` |

## Fields specifically

The Figma library today designs eight field states: `default, hover, preActive, Active, filled, Active-Filled, read-only, disabled`. They map as follows:

| Figma state | New state | Note |
|---|---|---|
| default | enabled (empty) | |
| hover | hover | |
| preActive | focus (empty) | "pre-active" is focus before typing |
| Active | focus (typing) | same visual as focus |
| filled | enabled (has value) | value presence is content, not a state |
| Active-Filled | focus (has value) | |
| read-only | read-only | |
| disabled | disabled | |
| `--error=True` | error flag | combinable with any of the above |

Net: fields have **enabled, hover, focus, read-only, disabled** plus the **error** flag, and the value (empty / filled) is a content condition. This is what CSS can express and what a screen reader announces.

## Priority when states overlap

`disabled` > `loading` > `error` styling > `pressed` > `focus` > `hover` > `selected/activated` > `enabled`.

## Motion

State changes animate colour and elevation over `ref.duration.short` (100ms) with `ref.easing.standard`. Nothing animates size or position on hover. See `docs/02-styles/motion.md`.
