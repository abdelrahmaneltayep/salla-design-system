# Component structure types

Five architectural patterns for building components, from the internal *Component Structure Types* document (Product Design, 2025-07-06), with the decision rules and the mapping to Salla components. Every entry in `catalog/components.json` declares one of these in its `structure` field.

## Decision tree

```
Does the component render UI?
├─ No  → 5 Headless (hook / controller)
└─ Yes
   Is its main job to frame content supplied by the parent?
   ├─ Yes → 4 Slot / Composition
   └─ No
      Do the variants differ in layout, behaviour or meaning (not just colour/size)?
      ├─ Yes
      │   Do they share significant logic or styling?
      │   ├─ Yes → 3 Base + Global
      │   └─ No  → 2 Standalone
      └─ No  → 1 Configurable
```

## 1. Configurable (single component with internal logic)

All variations are props. Use when variations are small and visual (colour, size, icon), structure and interaction are the same, and the prop list stays readable.

- **Salla examples:** `Button` (variant × appearance × size × layout), `LoadingIndicator`, `StatusIndicator`, `Avatar`, `Chip`, `Alert`, `HelperText`, `Pagination`.
- **Pros:** one import, all variants discoverable from props, logic in one place.
- **Cons:** becomes a god component if props pile up; unclear which combinations are valid.
- **Salla rule:** more than ~8 props, or any prop that changes *behaviour* rather than *look*, is the signal to split. `InputWrapper` in Figma (24 variants covering text, dropdown, amount, upload, colour picker …) is the cautionary example; it is being split under pattern 3.

## 2. Standalone (separate components with different names)

Each significant variant is its own named component. Use when variants have distinct functions, layouts or semantics, when one component would need many mutually exclusive props, or when variants evolve independently.

- **Salla examples:** `Icon` (one per glyph), `Flag`, `SocialIcon`, `Illustration`, `RadioImage` and `RadioColor`, the `TableCell` family (`NameCell`, `AmountCell`, `StatusCell`, `ActionsCell` …), `MobileRow` kinds, `AlertBanner` and `UpgradeCard` (distinct from `Alert`).
- **Pros:** small APIs, clear separation, explicit choice by name.
- **Cons:** possible duplication, more files.
- **Salla rule:** standalone components that share look share it through tokens and a tiny private layout helper (e.g. `CellLayout`), never by copy-pasting CSS.

## 3. Base + Global (inheritance / composition)

A private base component holds shared logic and minimal styling; public "global" components configure it. Use when several components share significant logic but must be exposed as distinct entities, or when you want to control which configurations exist.

- **Salla examples:**
  - `BaseField` → `TextField`, `TextareaField`, `PasswordField`, `EmailField`, `AmountField`, `PhoneField`, `SearchField`, `OtpField`, `QuantityField`, `SelectField`, `MultiSelectField`, `UploadField`, `ColorPickerField`. This is the Figma `Inputs` section (27 frames) resolved into one base and thirteen globals.
  - `BaseButton` → `Button`, `IconButton`, `Link`.
  - `Checkbox` → `CheckboxField`; `Radio` → `RadioField`; `Switch` → `SwitchField`.
  - `StatusIndicator` → `Status`; `LoadingIndicator` → `Loading`.
  - `BaseAlert` → `Alert`, `InlineAlert`.
- **Pros:** shared logic fixed once, controlled complexity, sensible defaults.
- **Cons:** abstraction overhead; needs planning.
- **Salla rule:** the base is never exported from the package index and never appears in Storybook navigation (it appears in Figma with the `_` prefix, which we keep for internal frames).

## 4. Slot-based / composition

The component defines a frame and named slots; the parent supplies content. Use when the component's job is layout or wrapping, when content is application-specific, or when maximum flexibility is needed.

- **Salla examples:** `DataTable` (header, footer, bulk-actions, cells), `TopAppBar` (start / center / end), `NavigationDrawer`, `Dialog` and `BottomSheet` (header / body / footer), `Panel`, `PageTitle` (leading / meta / actions), `ActionBar` (primary / secondary / start), `ListItem` (leading / title / description / trailing, the PDF's `listItemLayout`), `AvatarWithText`, `EmptyState`, all templates.
- **Pros:** flexible, reusable, decoupled content, readable usage.
- **Cons:** needs slot documentation; easy to over-use.
- **Salla rule:** every slot is documented with what it accepts (component types) and a default. A component with one slot and no layout responsibility is a prop, not a slot component.

## 5. Functional / headless (logic only)

Behaviour, state and accessibility without rendering. Exposed as hooks or controllers. Use when logic must be reusable across different UIs or when consumers need full control over markup.

- **Salla examples:** `useTabs` (Tabs), `useListbox` / `useMenu` (DropdownList, MoreMenu, SelectField), `useStepper` (Stepper), `useCalendar` (DateTimePicker), `useDialog` (Dialog, BottomSheet), `useTooltip`, `useDataTable` (sorting, selection, pagination).
- **Pros:** full control over presentation, reusable logic, clean separation, easy re-theming.
- **Cons:** more setup, not visible in Figma, needs strong documentation and examples.
- **Salla rule:** every headless hook ships with a default UI component in the same folder (`Tabs` uses `useTabs`) so designers still have a Figma-visible counterpart, and with a usage example in Storybook's *Docs* tab.

## Mapping summary

| Structure | Count in catalog | Levels where it appears |
|---|---|---|
| 1 Configurable | see `docs/03-components/README.md` | mostly atoms, some molecules |
| 2 Standalone | " | atoms, molecules, a few organisms |
| 3 Base + Global | " | molecules (fields, selection controls) |
| 4 Slot / Composition | " | organisms, templates, pages |
| 5 Headless | " | organisms with keyboard / focus behaviour |

The exact list is generated in [`docs/03-components/README.md`](../03-components/README.md).
