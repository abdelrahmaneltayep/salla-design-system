# Elevation

Material's elevation levels mapped onto the Figma **`Shadows/*`** effect styles. Two styles were observed on 2026-09-22 (`Shadows/md`, `Shadows/lg`); they follow the Tailwind shadow scale with a cool black `rgb(18 18 23)`, so `sm` and `xl` are filled in on the same scale.

| Level | Token | Figma style | Shadow | Observed on |
|---|---|---|---|---|
| 0 | `sys.elevation.0` | – | none | page, Panel (Salla's default is flat with an outline) |
| 1 | `sys.elevation.1` | `Shadows/sm` (not observed) | `0 1px 2px 0 rgb(18 18 23 / .06)` | raised Panel, sticky table header |
| 2 | `sys.elevation.2` | `Shadows/md` ✓ | `0 4px 6px -1px rgb(18 18 23 / .08), 0 2px 4px -1px rgb(18 18 23 / .05)` | Table/Footer on mobile (sticky bottom bar, shadow flipped upward) |
| 3 | `sys.elevation.3` | `Shadows/lg` ✓ | `0 10px 15px -3px rgb(18 18 23 / .08), 0 4px 6px -2px rgb(18 18 23 / .05)` | MoreMenu, Tooltip, DropdownList |
| 4 | `sys.elevation.4` | `Shadows/xl` (not observed) | `0 20px 25px -5px rgb(18 18 23 / .10), 0 8px 10px -6px rgb(18 18 23 / .05)` | Dialog, BottomSheet, side sheets |

Figma variables behind the styles: `shadow/{size}/type-{1,2}/{position-x, position-y, blur, spread, color}`.

## Rules

- Salla is **flat-first**: containment is shown with `sys.color.outline` borders; elevation is reserved for surfaces that float above the page (menus, tooltips, sheets, dialogs) and for drag states.
- Elevation never changes on hover for cards or rows; hover uses colour (see [interaction-states.md](../01-foundations/interaction-states.md)).
- Scrim under Dialog and BottomSheet: `sys.color.scrim` = `rgb(0 0 0 / .4)` (proposed).
- Tonal elevation (Material's surface tint) is not used; Salla surfaces stay white.

## To do in Figma

- Confirm `Shadows/sm` and `Shadows/xl` exist; if not, add them with the values above.
- Bind `Drop Down List`, `Bottom sheet`, `Table/Bulk Edit Sheet`, `Table/Edit Sheet` and `Action Buttons Type=Float` to a shadow style (they carry none today).
