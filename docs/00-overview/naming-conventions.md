# Naming conventions

Rules for component, prop, token, file and Figma names so the catalog, Figma, Storybook and code all say the same thing.

## Components

| Rule | Do | Don't |
|---|---|---|
| PascalCase, singular noun | `TextField`, `DataTable`, `NavigationItem` | `textfield`, `Tables`, `sidemenu tab` |
| Domain-neutral below page level | `Status`, `ListItem` | `OrderStatus`, `ProductListItem` |
| No version suffix in the name | `PhoneField` | `_PhoneInputV1` |
| Field = control + label + helper | `CheckboxField`, `SwitchField`, `TextField` | `checkboxfield`, `toggleField`, `_TextInput` |
| Internal bases prefixed `Base` in code, `_` in Figma | `BaseField`, `_TextInput` | exporting `InputWrapper` |
| Material names where Material has one, Salla alias kept in docs | `Switch` (alias Toggle), `TopAppBar` (alias Header), `NavigationDrawer` (alias Side menu), `Dialog` (alias Modal) | inventing a third name |
| Typed families use a shared suffix | `NameCell`, `AmountCell`, `StatusCell` | `Table/Cell/Varient`, `Table/Cell/Data` |

## Props and variant properties

| Rule | Do | Don't |
|---|---|---|
| camelCase | `iconStart`, `maxLength` | `icon-start`, `Icon Start` |
| No `--` prefix on values | `variant="primary"` | `Variant=--primary` |
| Booleans are adjectives, no `?`, no `is` | `disabled`, `loading`, `richText` | `Rich text?`, `isDisabled`, `--disabled=true` |
| Enumerations use the same words everywhere | `size: sm \| md \| lg` | `sm-16px`, `md- 48px`, `default-24px`, `compact` |
| Language is a runtime context, not a variant | `dir` / `lang` on the root | `Language=Arabic/English` on every frame |
| Device is a breakpoint, not a variant | responsive CSS; `device` only when layouts truly differ (TopAppBar, DataTable) | `--device=desktop` on Page Title |
| State names are Material's | `enabled, hover, focus, pressed, disabled` (+ `selected`, `activated`, `error`) | `--preActive`, `--Active-Filled`, `--Active-Filled-with-one` |
| Logical directions | `start`, `end`, `inline-start` | `left`, `right`, `Dir=Left` |

Fixed spellings for values seen in Figma today: `secondary` (not `seconadry`), `transparent` (not `Trasnparet`), `language` (not `Langauge` / `Langugae`), `variant` (not `Varient`), `separator` (not `Sperator`), `default` (not `defaullt`), `delivered` / `delivery` / `in-progress` / `retrieved` / `waiting-payment` / `waiting-review` (order statuses), `false` (not `Fals`).

## Tokens

Format: `{tier}.{group}.{role}.{modifier}` in JSON, `--{tier}-{group}-{role}-{modifier}` in CSS.

| Tier | Purpose | Examples |
|---|---|---|
| `ref` | raw values | `ref.palette.teal.900`, `ref.space.5`, `ref.font.size.sm` |
| `sys` | roles | `sys.color.primary`, `sys.color.on-primary`, `sys.color.status.danger.primary`, `sys.space.md`, `sys.shape.small`, `sys.typography.label-md` |
| `comp` | component | `comp.button.height-md`, `comp.alert.accent-width` |

Rules:

- Colour roles follow Material: `primary`, `on-primary`, `primary-container`, `surface`, `outline`, `text.*`, `status.{success|danger|warning|info}.{lighter|light|primary|dark|darker}`.
- The Figma collection `03-Colors` keeps its `text / background / border / foreground` grouping; the mapping to `sys.color.*` is one-to-one and listed in `docs/02-styles/color.md`.
- One spacing scale. `spacing/*` and `Spacing/Sizes/*` (which currently disagree: `spacing/3xs = 8px` but `Spacing/Sizes/3xs = 2px`) both migrate to `sys.space.*`; see `docs/02-styles/spacing.md`.
- Numeric ref scales (`ref.space.1..12`, `ref.palette.teal.100..900`) never appear in product code.

## Files and folders

| Thing | Convention | Example |
|---|---|---|
| Component doc | `docs/03-components/{level}s/{kebab-id}.md` | `docs/03-components/molecules/text-field.md` |
| Catalog id | kebab-case, equals the doc filename | `text-field` |
| Storybook title | `{Level}s / {Category} / {Name}` | `Molecules / Text inputs / TextField` |
| Code folder (future) | `packages/ui/src/{level}s/{Name}/` with `{Name}.tsx`, `{Name}.stories.tsx`, `{Name}.test.tsx`, `index.ts` | `packages/ui/src/molecules/TextField/` |
| Figma section | `{Level}s / {Category}` | `Molecules / Text inputs` |
| Figma component | `{Name}` or `_{Name}` for internal | `TextField`, `_BaseField` |

## Icons

- Name only, no style suffix, in kebab-case: `add-01`, `arrow-down-01`, `information-circle`.
- Style is a prop: `outline` (Figma *Stroke*) or `filled` (Figma *Solid*). Rounded is the only type shipped; Sharp, Bulk, Twotone and Duotone stay in the source library.
- The legacy `sicon-*` font classes map one-to-one and are kept as aliases until the font is retired.
