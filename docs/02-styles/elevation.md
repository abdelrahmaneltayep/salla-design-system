# Elevation

Material's elevation levels, proposed for Salla. **The Figma library has no shadow or elevation styles today**; production surfaces use ad-hoc shadows. These four levels are the proposal to add as effect styles.

| Level | Token | Shadow | Used by |
|---|---|---|---|
| 0 | `sys.elevation.0` | none | page, Panel on surface (Salla's default is flat with an outline) |
| 1 | `sys.elevation.1` | `0 1px 2px rgb(0 0 0 / .06)` | raised Panel, sticky table header, floating help chip |
| 2 | `sys.elevation.2` | `0 4px 12px rgb(0 0 0 / .08)` | DropdownList, MoreMenu, Tooltip, floating ActionBar |
| 3 | `sys.elevation.3` | `0 12px 32px rgb(0 0 0 / .12)` | Dialog, BottomSheet, side sheets, dragged items |

## Rules

- Salla is a **flat-first** system: containment is shown with `sys.color.outline` borders, and elevation is reserved for surfaces that float above the page (menus, sheets, dialogs) and for drag states.
- Elevation never changes on hover for cards or rows; hover uses colour (see [interaction-states.md](../01-foundations/interaction-states.md)).
- Scrims under Dialog and BottomSheet: `rgb(0 0 0 / .4)`.
- Tonal elevation (Material's surface tint) is not used; Salla surfaces stay white.

## To do in Figma

Add four effect styles `Elevation/0-3` and bind `Drop Down List`, `More Menu`, `Bottom sheet`, `Table/Bulk Edit Sheet`, `Table/Edit Sheet` and `Action Buttons Type=Float` to them.
