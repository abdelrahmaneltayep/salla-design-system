# Motion

Material's motion system reduced to what the dashboard needs. **No motion tokens exist in Figma today**; these are proposed.

## Tokens

| Token | Value | Use |
|---|---|---|
| `ref.duration.short` | 100ms | state changes: hover, pressed, focus ring, checkbox tick |
| `ref.duration.medium` | 200ms | enter / exit of small surfaces: DropdownList, MoreMenu, Tooltip, Toast |
| `ref.duration.long` | 300ms | enter / exit of large surfaces: Dialog, BottomSheet, side sheets, NavigationDrawer |
| `ref.easing.standard` | `cubic-bezier(0.2, 0, 0, 1)` | everything entering or changing state |
| `ref.easing.emphasized` | `cubic-bezier(0.3, 0, 0.8, 0.15)` | exits (accelerate out) |

## Patterns

| Pattern | Spec |
|---|---|
| Fade | opacity 0 → 1, `medium`, `standard` |
| Fade through | outgoing fades over first 30%, incoming fades in with 4px rise |
| Slide (sheets) | translate 100% → 0 on the inline / block edge, `long`, `standard`; exit `emphasized` |
| Scale (menus) | 0.95 → 1 with fade, `medium`, transform-origin at the trigger |
| Loading | `LoadingIndicator` spinner 1s linear infinite; dots 1.2s; line indeterminate 2s |
| Switch thumb | 100ms `standard` translate; loading spinner fades in inside the thumb |
| Skeleton | shimmer 1.5s linear infinite, disabled under reduced motion |

## Rules

- Animate only `opacity`, `transform`, `color`, `background-color`, `border-color`, `box-shadow`. Never `width`, `height`, `top`, `left`.
- Hover and pressed never move or scale elements.
- Honour `prefers-reduced-motion: reduce`: durations 0, spinners become static, shimmer off.
- RTL: slide directions use logical axes (`translateX` sign flips with `dir`).
