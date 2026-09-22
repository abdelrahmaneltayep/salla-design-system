# Accessibility

Baseline: **WCAG 2.2 AA** for the merchant dashboard. Base components (structure type 3 and 5) own these behaviours so that global components inherit them.

## Colour and contrast

Ratios computed with the WCAG 2.x relative-luminance formula from the verified token values.

| Pairing | Ratio | Status |
|---|---|---|
| `sys.color.text.primary` #333 on `sys.color.surface` #fff | 12.6:1 | pass |
| `sys.color.text.secondary` #666 on #fff | 5.7:1 | pass (AA text) |
| `sys.color.text.brand` #004956 on `sys.color.primary-container` #a4ffe5 (primary Button) | 8.6:1 | pass |
| `sys.color.text.inverse` #fff on `sys.color.primary` #004956 (TopAppBar) | 10.1:1 | pass |
| `sys.color.text.inverse` #fff on `sys.color.status.danger.primary` #f55157 (danger Button) | 3.4:1 | **fails AA for 14px text** (needs 4.5:1) |
| #fff on `sys.color.status.success.primary` #00af6c (success Button) | 2.9:1 | **fails** |
| #fff on `sys.color.status.warning.primary` #ffaf44 (warning Button) | 1.8:1 | **fails** |
| #fff on `sys.color.status.info.primary` #5196f3 (info Button, Alert action) | 3.0:1 | **fails** |
| #fff on `sys.color.status.danger.dark` #ca4146 | 4.8:1 | pass, candidate fill for the danger Button |
| #fff on `sys.color.status.success.dark` #008c56 | 4.3:1 | passes only for large text; success needs `darker` #005232 (9.3:1 on white) or a dark label |
| `sys.color.text.primary` #333 on #ffaf44 | 6.9:1 | pass, candidate label colour for the warning Button |
| `sys.color.status.info.darker` #204374 on `sys.color.status.info.lighter` #ecf3fe (Alert) | 8.9:1 | pass |
| `sys.color.status.danger.darker` #7a1f1e on `sys.color.status.danger.lighter` #feecec (Status strong) | 9.0:1 | pass |
| `sys.color.on-feature` #883000 on feature gradient #ffd8c2 → #ffaf83 | 6.4:1 → 4.7:1 | pass across the gradient |

Action: all four filled status Buttons (`danger`, `success`, `warning`, `info`) with white labels fail AA at 14px. Options: use the `dark` shade as fill (danger passes at 4.8:1), use a dark label on warning (6.9:1), or reserve filled status buttons for 18px+ large text. Tracked as an open item in the audit.

Colour is never the only signal: `Status` pairs a dot colour with a label; `Alert` pairs colour with an icon; `Switch` pairs colour with thumb position.

## Focus

- Every interactive element shows `sys.focus.ring` on `:focus-visible`. It is never suppressed.
- Focus order follows reading order, which follows `dir`.
- `Dialog`, `BottomSheet`, `MoreMenu`, `DropdownList` trap focus while open and return it to the trigger on close (`useDialog`, `useMenu`).

## Keyboard

| Component | Keys |
|---|---|
| Button, Link, IconButton | Enter / Space |
| Checkbox, Switch | Space |
| Radio group | Arrow keys move selection |
| Tabs | Arrow keys move focus, Enter / Space activate (roving tabindex) |
| DropdownList / SelectField / MoreMenu | Arrow keys, Home / End, type-ahead, Enter select, Escape close |
| DataTable | Tab to interactive cells, Space to select row, Shift+Space range |
| Dialog / BottomSheet | Escape closes (unless blocking) |
| Stepper | steps are links or buttons, no custom keys |

## Semantics

- Icon-only controls (`IconButton`, `ActionsCell` icons, close buttons) require `ariaLabel`. The catalog marks it required.
- `FieldLabel` is a `<label for>`; `HelperText` is linked with `aria-describedby`; errors set `aria-invalid` and are announced.
- `Status` uses text, not just colour; `LoadingIndicator` sets `aria-busy` on the region it covers.
- `Alert` uses `role="status"` for info/success and `role="alert"` for warning/danger.
- `Toast` is a `role="status"` live region.

## Target size

Interactive targets are at least **24×24 CSS px** (WCAG 2.2 2.5.8) and, on compact screens, **40×40**. `Checkbox sm` (16px) and `Switch sm` (16px) get an invisible hit area to reach the minimum.

## Motion

Respect `prefers-reduced-motion`: durations drop to 0 and loaders use a static state.

## Language

`lang` and `dir` are set on the root and on any field whose language differs from the page (bilingual `TextField`), so screen readers switch voice correctly.
