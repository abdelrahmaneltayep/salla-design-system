# Methodology: Atomic Design × Material Design

Salla's design system uses two frameworks together. **Atomic Design** answers *how components compose*. **Material Design 3** answers *how the system is organised, named and tokenised*. Neither alone is enough: Atomic Design says nothing about tokens or categories, and Material's flat component list says nothing about which components are built from which.

## 1. What we take from Material Design

Material 3 organises its documentation into three top-level groups and we mirror them one-to-one.

| Material group | Material contents | Salla folder | What lives there |
|---|---|---|---|
| **Foundations** | Accessibility, Adaptive design, Content design, Customization, Design tokens, Interaction states, Layout | `docs/01-foundations/` | The rules that apply to everything: token model, layout grid and breakpoints, interaction states, accessibility, Arabic/English content and RTL |
| **Styles** | Color, Elevation, Icons, Motion, Shape, Typography | `docs/02-styles/` | The visual vocabulary. Each style page owns one token family. Salla adds *Spacing* (Material folds it into Layout) and *Illustrations* |
| **Components** | Grouped by category: Actions, Communication, Containment, Navigation, Selection, Text inputs | `docs/03-components/` | The parts. We keep Material's six categories and add **Data display** for tables, avatars, flags and status, which Material 3 does not cover but the merchant dashboard is built on |

We also adopt Material's **three-tier token model**:

```
ref.*   reference tokens   raw values, no meaning        ref.palette.teal.900 = #004956
sys.*   system tokens      roles, theme-able             sys.color.primary = {ref.palette.teal.900}
comp.*  component tokens   per-component overrides only  comp.button.height-md = {ref.size.control.md}
```

Product code and components use `sys.*`. Only the token build touches `ref.*`. `comp.*` exists only where a component needs a value that is not a plain system token. This is exactly how Material's `md.ref.*` / `md.sys.*` / `md.comp.*` tokens work, and it lets Salla theme (dark mode, white-label, partner apps) by re-mapping the `sys` tier without touching a component.

Other Material conventions we adopt:

- **Color roles, not color names**: `primary`, `on-primary`, `primary-container`, `surface`, `outline`. The Figma library already names colours by role (`text/primary`, `background/status/info`), so this is an alignment, not a rewrite.
- **Type roles**: display / headline / title / body / label, each mapping to an existing `Bold|Medium|Regular / $text-*` Figma style.
- **Shape scale**: none / extra-small / small / medium / large / full instead of raw radii.
- **Interaction states** as a fixed list: enabled, hover, focus, pressed, dragged, disabled (plus selected / activated where relevant). Every stateful component documents these and no others.
- **Component anatomy** diagrams with numbered parts, and a props table per component.

## 2. What we take from Atomic Design

Material lists ~35 components flat. Salla has 117 Figma frames and ~90 public components, many of which are built from each other (`_TextInput` → `TextField` → `DataTable`). Atomic Design gives us the vertical axis:

| Level | Definition for Salla | Examples | Rule of thumb |
|---|---|---|---|
| **Atom** | Cannot be broken down further and still be useful. Takes tokens directly. No product data. | Button, Icon, Checkbox, Switch, Avatar, LoadingIndicator, StatusIndicator, Chip, Flag | If it needs another component to make sense, it is not an atom |
| **Molecule** | A few atoms with one job. | TextField (label + input + helper), Status (dot + label), CheckboxField, Breadcrumb, Tab, ListItem, TableCell | Should be describable in one sentence without "and" |
| **Organism** | A distinct section of the interface. Often stateful. Composed of molecules and atoms. | DataTable, TopAppBar, NavigationDrawer, DropdownList, Alert, Stepper, Dialog | Could appear on its own in a Storybook story with realistic data |
| **Template** | Page skeleton with slots and placeholder content. | ListPage, ListDetailPage, FormPage, WizardPage | No real strings, no real data |
| **Page** | Template + real content. | Orders list, Products list, Order details | Lives in the product, documented here as reference |

Naming stays domain-neutral at atom and molecule level (`Button`, not `SaveButton`) and becomes domain-aware only at page level.

## 3. How the two axes combine

Every component gets a coordinate on both axes. Material category is the **folder a designer opens**; atomic level is the **folder an engineer opens**. Storybook titles use both:

```
Atoms / Actions / Button
Molecules / Text inputs / TextField
Organisms / Data display / DataTable
Templates / ListPage
```

The catalog (`catalog/components.json`) is the single place where the coordinate is declared, and `docs/03-components/README.md` renders the matrix both ways.

## 4. The third axis: structure type

The internal *Component Structure Types* document defines five build patterns. They are orthogonal to level and category and answer *how the engineer should implement it*:

| # | Pattern | Typical level | Salla examples |
|---|---|---|---|
| 1 | Configurable | atom | Button, LoadingIndicator, Chip, Alert |
| 2 | Standalone | atom / molecule | Icon, Flag, RadioImage, TableCell types, MobileRow |
| 3 | Base + Global | molecule | BaseField → TextField / PasswordField / SearchField …; Checkbox → CheckboxField |
| 4 | Slot / Composition | organism / template | DataTable, TopAppBar, Dialog, Panel, ListPage |
| 5 | Headless | organism | Tabs (useTabs), DropdownList (useListbox), Stepper (useStepper), Tooltip |

Details and decision rules: [component-structure-types.md](component-structure-types.md).

## 5. Principles

1. **Tokens before components.** No hard-coded value in a component; if a value is missing, add a token first.
2. **One source of truth per fact.** A component's props live in the catalog; its colours live in tokens; its Figma frame is linked, not copied.
3. **Bilingual by default.** Every component is designed in Arabic and English and uses logical properties (`inline-start`, not `left`).
4. **Accessible by construction.** Base components own focus, keyboard and ARIA so globals inherit it.
5. **Small public API.** Prefer named globals (`PasswordField`) over a god component with a `variant` that changes behaviour.
6. **Figma mirrors code.** Frame names, variant property names and token names match the catalog after migration.
