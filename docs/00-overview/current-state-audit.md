# Current state audit

What Salla's design system contains today and where it diverges from the target structure. Sources: the `Merchant - Storybook DS` Figma library (branch `dnmyqzYKK9dUJjVHuIWMDS`, page *Main Components (Full)*, extracted 2026-09-22), the `Icons DS_V.1` Figma file (exported 2026-07-07), and the Twilight Storybook at `dashboard-ui-components.pages.dev` (37 components / 162 variants as of July 2026, captured in the salla-design-system skill; the host was not reachable from this environment so story names are taken from that capture).

## 1. Inventory

| Source | Size |
|---|---|
| Figma sections | 17 (`Header`, `Bread crumb`, `check Box`, `radio Buttton`, `Toggle`, `Loader`, `Status`, `Avatar`, `Alertbox`, `Inputs`, `Maps`, `Side menu`, `More Menu`, `Drop Down List`, `Table`, `Steps`) + 12 top-level frames outside any section (`Button`, `Icons/Filled`, `Icons/Outline`, `Flag`, `Illustration`, `Illustrations Collection`, `Social media icons`, `Action Buttons`, `searchbar`, `Learn More`, `Products Management`, `Header Primary Tabs`) |
| Figma component frames | 117 (`catalog/figma-inventory.json`) |
| Figma variant symbols | ~10,100 |
| Figma variable collections | `03-Colors` (text / background / border / foreground roles), `04-Token` (Spacing/Sizes, Radius/Sizes). Collections 01 and 02 were not exposed to the MCP search; assumed to be primitives and typography |
| Figma text styles | `Bold`, `Medium`, `Regular` × `$text-xs … $text-9xl` |
| Icon library | 4,049 icon names × Style (Stroke 3,889 · Solid 3,889 · Bulk 5 · Twotone 3 · Duotone 3) × Type (Rounded, Sharp) |
| Storybook components | 37 (Button, Input, LingualField, Textarea, Password, Search, Select, Tags Input, Qty, Checkbox, Radio, Toggle, Loader, Badge/Status, Avatar, AlertBox, Breadcrumb, Tabs, Dropdown, Table, Pagination, Header, Sidebar, Panel, Modal, Tooltip, ButtonsGroup, Steps, Date Picker, File Upload, Color Picker, Phone, Number …) |

Full per-frame variant properties: `catalog/figma-inventory.json`. Classification of every frame: `docs/03-components/README.md`.

## 2. What is working well

- **Role-based colour variables.** `03-Colors` already names colours by role (`text/primary/link`, `background/status/info/lighter`, `border/default`). This maps directly onto Material system tokens.
- **Base + variants pattern is already emergent.** `_TextInput` → `InputWrapper`, `checkBox` → `checkboxfield`, `_Base Status Indicator` → `Status`, `_Step base` → `Steps`, `_listItem` → `Drop Down List`. The `_` prefix for internal frames is a real convention.
- **Bilingual coverage.** Almost every frame has `Language=Arabic|English`, and fields carry a translation toggle.
- **Rich state coverage on fields and buttons.** Hover, pressed, loading, disabled, error and read-only are all designed.
- **Typed table cells.** 18 cell types mirror what the product actually renders.
- **Component descriptions with Arabic and English keywords** on the main component sets (Button, InputWrapper, Toggle, checkBox, Status …), which makes Figma search work in both languages.

## 3. Structural issues

| # | Issue | Evidence | Impact | Fix (target) |
|---|---|---|---|---|
| S1 | **No hierarchy.** Sections are a flat list mixing atoms (`check Box`), molecules (`Status`), organisms (`Table`) and a template (`Products Management`). | 17 sections, 12 orphan frames | Designers cannot tell what composes what; engineers cannot tell what to build first | Sections become `Atoms / Molecules / Organisms / Templates`, sub-grouped by Material category |
| S2 | **God component for inputs.** `InputWrapper` has a `Variant` property with 12 values covering text, search, amount, colour picker, dropdown single/multiple/basic, email, upload … | 24 variants; 27 frames in `Inputs` | Unclear API; any change touches every field | Split into `BaseField` (internal) + 13 named field components (structure type 3) |
| S3 | **Two spacing scales that contradict each other.** `spacing/3xs = 8px` but `Spacing/Sizes/3xs = 2px`; `spacing/2xs = 10px` but `Spacing/Sizes/2xs = 4px`; `spacing/xs = 12px` but `Spacing/Sizes/xs = 6px` | Button, Alertbox, Header use `spacing/*`; fields, Status, Side menu, Table use `Spacing/Sizes/*` | Same pixel value, two names; migrations break | `Spacing/Sizes` becomes the scale; alias table in `docs/02-styles/spacing.md` |
| S4 | **Language and device as variant axes.** `Language=Arabic|English` and `--device=desktop|mobile` double or quadruple every component's variant count | `_passwordInput` has 112 variants; Alertbox 64 | Library size, maintenance cost, and it hides that RTL should be automatic | Language becomes a page-level toggle (Figma variable mode); device stays only where layout truly differs |
| S5 | **Eight interaction states on fields.** `default, hover, preActive, Active, filled, Active-Filled, read-only, disabled` (+ error) | every input frame | Not implementable as CSS states; `preActive` and `Active-Filled` have no DOM equivalent | Material list: enabled, hover, focus, filled, read-only, disabled + orthogonal `error` |
| S6 | **Components missing from Figma but present in Storybook / production.** Modal, Panel, Toast. (Tooltip exists as a component set, node `1933:1790`, but only inside `checkboxfield`; it needs its own frame.) | Storybook has Modal, Panel, Tooltip | Engineers build from code, designers from nothing | Added to catalog as `proposed`; design from the spec |
| S7 | **Components in Figma without a Storybook story.** RadioImage, RadioColor, AvatarStack, Flag, Illustration, Learn More, More Menu layouts, Bulk Edit Sheet, Edit Sheet, mobile table rows, Maps | catalog `storybook: null` | Designed but not shipped | Prioritise in the build order |
| S8 | **Assets stored as components.** `_AvatarplaholderImages`, `_BanksPlaceholderImages`, `Illustrations Collection`, 265 flags as variants | | Bloats the library; not tokenable | Move to `assets/`; keep one `Flag` / `Illustration` component with a `name` prop |
| S9 | **Order-status presets baked into the Table.** `Table/Status` has 9 variants (`wating payment`, `delevery`, `deliverd`, `retrevied` …) | | Business data in the component layer | One `Status` molecule; the mapping order status → semantic type lives in data |
| S10 | **Loader has nine sizes** (8 to 88px) while everything else has three to six | `_LoadingIndicator` | Inconsistent scale | Collapse to five with aliases |
| S11 | **Elevation is only partly defined.** `Shadows/md` and `Shadows/lg` effect styles exist (More Menu, Tooltip, Table/Footer) but DropdownList, Bottom sheet, Bulk/Edit sheets and the floating ActionBar carry no shadow style | `shadow/lg/type-1|2/*` variables | Sheets ship with ad-hoc shadows | Map to `sys.elevation.0-4`, add `Shadows/sm|xl`, bind the remaining surfaces |
| S12 | **Some hard-coded values escape the tokens.** Status pill radius `30px`, Alertbox `gap 4px`, LearnMore `gap 5px`, header tag radius `140px`, legacy `07--light-theme/*` and `spacing-xs/md/lg` variables, `radius/sm` resolving to 8px | design contexts on `Status`, `Alertbox`, `Learn More`, `Header`, `Table/Footer` | Theme changes miss them | Map to `sys.shape.full`, `sys.space.*`, `sys.color.*`; re-point `radius/sm` |

## 4. Naming issues

| Type | Examples (Figma today) | Rule |
|---|---|---|
| Typos | `seconadry`, `Trasnparet`, `Langauge`, `Langugae`, `radio Buttton`, `defaullt`, `Varient`, `Sperator`, `Fals`, `Selceted`, `delevery`, `deliverd`, `in prograss`, `retrevied`, `wating payment`, `bigCalenderItems`, `AvatarplaholderImages`, `Descreptive` | fix at source (they leak into token names such as `background/secondary/seconadry`) |
| Inconsistent casing | `check Box`, `checkBox`, `checkboxfield`, `radiofield`, `toggleField`, `Toggle`, `searchInput`, `searchbar`, `upload input`, `Bread crumb` | PascalCase components, `_` for internals |
| Leading `--` on variant values and some property names | `Variant=--primary`, `--selected=true`, `--device=desktop` | plain values, camelCase props |
| Size vocab varies | `sm-16px`, `md-20px`, `default-24px`, `--md-40px`, `md- 48px`, `compact`, `Small` | `sm / md / lg` (+ `xs`, `xl` where needed), pixel value in the token |
| Two names for one thing | `Toggle` / `toggleField` / `Switch`; `Header` / `Top bar`; `More Menu` / `Dropdown Menu`; `Modal` / `Dialog` | Material name in code, Salla name as documented alias |
| Version in name | `_PhoneInputV1` | no versions in names |

Full old → new mapping: [migration-map.md](migration-map.md).

## 5. Gaps against Material Design

| Material area | Salla today | Action |
|---|---|---|
| Foundations: design tokens (ref / sys / comp) | roles exist, no tiers, no JSON export | `tokens/tokens.json` introduces the tiers |
| Foundations: layout / breakpoints | `desktop` / `mobile` variants only | `docs/01-foundations/layout.md` defines breakpoints and the grid |
| Foundations: interaction states | per-component ad hoc | `docs/01-foundations/interaction-states.md` fixes the list |
| Foundations: accessibility | not documented | `docs/01-foundations/accessibility.md` |
| Styles: elevation | `Shadows/md`, `Shadows/lg` exist; not applied to sheets | mapped to `sys.elevation.*`, gaps listed in elevation.md |
| Styles: motion | absent | proposed durations and easings |
| Styles: shape | `Radius/Sizes` scale exists | mapped to Material shape names |
| Components: snackbar / toast | absent | proposed |
| Components: dialog | Storybook only | proposed spec |
| Components: tooltip | exists (component set `1933:1790`) but has no frame on the components page | catalog entry `existing`, needs its own frame |
| Components: date pickers | cells exist, picker organism not framed | catalog entry with headless plan |
| Components: data table | rich | keep; Material 3 has no table, Salla's is a first-class Data display component |

## 6. Bottom line

The content of the system is in good shape: the colour roles, the base/variant pattern and the bilingual coverage are already Material-like. The work is structural: introduce levels, split the input god component, unify the two spacing scales, take language and device out of the variant matrix, and fill five gaps (full elevation coverage, motion, dialog, toast, breakpoints).
