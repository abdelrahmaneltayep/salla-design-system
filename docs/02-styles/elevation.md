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

## What the Twilight code ships today

The Storybook's Tailwind config carries its own shadow scale, which does **not** match the Figma effect styles:

| Tailwind class | Value in code | Closest Figma / system token |
|---|---|---|
| `shadow-xs` | `0 1px 2px 0 rgba(18,18,23,.05)` | `sys.elevation.1` |
| `shadow` | `0 2px 4px -1px rgba(18,18,23,.06)` | `sys.elevation.1` |
| `shadow-sm` | `0 2px 4px 0 rgba(0,0,0,.08)` | – (pure black, legacy) |
| `shadow-md` | `0 4px 6px 0 rgba(0,0,0,.12)` | – (pure black, legacy) |
| `shadow-lg` | `0 4px 6px -2px rgba(18,18,23,.05)` | only the second layer of Figma `Shadows/lg` |
| `shadow-xl` | `0 10px 10px -5px rgba(18,18,23,.04)` | `sys.elevation.3` (approx.) |
| `shadow-2xl` | `0 25px 50px -12px rgba(18,18,23,.25)` | `sys.elevation.4` |
| `shadow-smooth` | `0 6px 8px 0 rgba(0,0,0,.02)` | – |
| `shadow-top` / `shadow-bottom` | `0 ∓4px 16px -4px rgba(0,0,0,.15)` | sticky bars (`Table/Footer` mobile) |

Decision: the system scale is the Figma one (`sys.elevation.0-4`); the Tailwind preset in this repo maps `shadow-elevation-*` to it. The legacy pure-black classes should be retired when components move to the preset.

## Rules

- Salla is **flat-first**: containment is shown with `sys.color.outline` borders; elevation is reserved for surfaces that float above the page (menus, tooltips, sheets, dialogs) and for drag states.
- Elevation never changes on hover for cards or rows; hover uses colour (see [interaction-states.md](../01-foundations/interaction-states.md)).
- Scrim under Dialog and BottomSheet: `sys.color.scrim` = `rgb(0 0 0 / .4)` (proposed).
- Tonal elevation (Material's surface tint) is not used; Salla surfaces stay white.

## To do in Figma

- Confirm `Shadows/sm` and `Shadows/xl` exist; if not, add them with the values above.
- Bind `Drop Down List`, `Bottom sheet`, `Table/Bulk Edit Sheet`, `Table/Edit Sheet` and `Action Buttons Type=Float` to a shadow style (they carry none today).
