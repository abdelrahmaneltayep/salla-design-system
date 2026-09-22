# Migration map

Where every current Figma section, frame and Storybook story goes in the new structure. Use this to rename in Figma and to retitle Storybook stories. The per-frame variant properties are on each component page under *Source in Figma today*.

## Figma sections → new sections

| Figma section today | Frames | New Figma section | Notes |
|---|---|---|---|
| `Header` | header Avatar, Header, Page Title, Header Subcategory, Header Secondary Tabs, Primary Tabs List | `Organisms / Navigation` (TopAppBar, SecondaryNavBar, Tabs) · `Molecules / Navigation` (Tab, PageTitle, AccountMenuTrigger) | Tabs get their own organism with a headless hook |
| `Bread crumb` | Breadcrumb, _breadcrumbItem | `Molecules / Navigation` | Separator variant becomes the `Divider` atom |
| `check Box` | checkBox, checkboxfield | `Atoms / Selection` (Checkbox) · `Molecules / Selection` (CheckboxField) | |
| `radio Buttton` | radio, radiofield, radioImage, radioColor | `Atoms / Selection` (Radio) · `Molecules / Selection` (RadioField, RadioImage, RadioColor) | |
| `Toggle` | Toggle, toggleField | `Atoms / Selection` (Switch, alias Toggle) · `Molecules / Selection` (SwitchField) | |
| `Loader` | _LoadingIndicator, Loading | `Atoms / Communication` (LoadingIndicator) · `Molecules / Communication` (Loading) | |
| `Status` | _Base Status Indicator, Status | `Atoms / Communication` (StatusIndicator) · `Molecules / Communication` (Status) | |
| `Avatar` | Avatar, AvatarWithText, AvatarStack, placeholder image sets | `Atoms / Data display` (Avatar) · `Molecules / Data display` (AvatarWithText, AvatarStack) · placeholder images → `assets/` | |
| `Alertbox` | Alertbox, Alertbox_Banner, Alertbox_Upgrade | `Organisms / Communication` (Alert, AlertBanner, UpgradeCard) · `Molecules / Communication` (InlineAlert) | |
| `Inputs` | 27 frames | `Molecules / Text inputs` (BaseField internal + 13 fields) · `Atoms / Text inputs` (FieldLabel, HelperText, TranslationToggle) · `Atoms / Actions` (StepperButton) · `Atoms / Communication` (PasswordHint) | `InputWrapper` is retired; `_Text-cursor` is dropped (a native caret) |
| `Maps` | Maps | `Organisms / Data display` | |
| `Side menu` | Side menu, sidemenu tab | `Organisms / Navigation` (NavigationDrawer) · `Molecules / Navigation` (NavigationItem) | |
| `More Menu` | More Menu, _moreItems | `Organisms / Containment` (MoreMenu) · `Molecules / Containment` (MenuItem) | |
| `Drop Down List` | Drop Down List, _listItem, _listTitle, _Date, _bigCalenderItems, _Time, Time | `Organisms / Containment` (DropdownList) · `Molecules / Containment` (ListItem) · `Organisms / Selection` (DateTimePicker) · `Molecules / Selection` (CalendarCell) | Calendar cells move out of the dropdown section |
| `Table` | 41 frames | `Organisms / Data display` (DataTable, MobileRow, Pagination) · `Molecules / Data display` (TableCell family) · `Organisms / Containment` (BulkEditSheet, EditSheet, Panel) · `Molecules / Containment` (PanelHeader) · `Molecules / Communication` (FilterResults) | `Table/Status` presets become data; `_Table/Refresh Button`, `_Table/Pin` become IconButton uses |
| `Steps` | Steps, _Step base | `Organisms / Navigation` (Stepper) · `Atoms / Navigation` (StepIndicator) | |
| _(no section)_ `Button` | Button | `Atoms / Actions` (Button, IconButton, Link) | Link and IconButton are exposed as globals on the same base |
| _(no section)_ `Icons/Filled`, `Icons/Outline` | | `Atoms / Communication` (Icon) with the `Icons DS_V.1` library as source | |
| _(no section)_ `Flag`, `Social media icons`, `Illustration`, `Illustrations Collection` | | `Atoms / Data display` (Flag, SocialIcon) · `Atoms / Communication` (Illustration) · collections → `assets/` | |
| _(no section)_ `Action Buttons` | | `Organisms / Actions` (ActionBar) | with `Action Bar/Confirm buttons`, `buttonsContainer` |
| _(no section)_ `searchbar` | | `Molecules / Text inputs` (GlobalSearch) | |
| _(no section)_ `Learn More` | | `Molecules / Communication` (LearnMore) | |
| _(no section)_ `Header Primary Tabs` | | `Molecules / Navigation` (Tab kind=primary) | |
| _(no section)_ `Products Management` | | `Templates` (ListPage) | |

## Frame renames (old → new)

| Old Figma name | New component | Level |
|---|---|---|
| `Button` | `Button` | atom |
| `Button` Layout=--circular | `IconButton` | atom |
| `Button` Appearance=--link / --link-auxiliary | `Link` | atom |
| `checkBox` | `Checkbox` | atom |
| `checkboxfield` | `CheckboxField` | molecule |
| `radio` | `Radio` | atom |
| `radiofield` | `RadioField` | molecule |
| `radioImage` | `RadioImage` | molecule |
| `radioColor` | `RadioColor` | molecule |
| `Toggle` | `Switch` | atom |
| `toggleField` | `SwitchField` | molecule |
| `_LoadingIndicator` | `LoadingIndicator` | atom |
| `Loading` | `Loading` | molecule |
| `_Base Status Indicator` | `StatusIndicator` | atom |
| `Status` | `Status` | molecule |
| `Avatar` | `Avatar` | atom |
| `AvatarWithText`, `header Avatar` | `AvatarWithText`, `AccountMenuTrigger` | molecule |
| `AvatarStack` | `AvatarStack` | molecule |
| `Alertbox` (Type=Default, white) | `Alert` | organism |
| `Alertbox` (Type=Inline) | `InlineAlert` | molecule |
| `Alertbox_Banner` | `AlertBanner` | organism |
| `Alertbox_Upgrade` | `UpgradeCard` | organism |
| `InputWrapper`, `_TextInput`, `_inputLabel`, `_inputTip`, `_Text-cursor` | `_BaseField` (internal) | molecule |
| `_TextInput`, `_inputWithButton`, `_InputWithImage`, `_InputCounter` | `TextField` | molecule |
| `_TextArea`, `_Rich-Text-Panel` | `TextareaField` | molecule |
| `_passwordInput`, `_passwordHints`, `_passwordValidation` | `PasswordField`, `PasswordHint` | molecule, atom |
| `_emailInput` | `EmailField` | molecule |
| `_amountInput` | `AmountField` | molecule |
| `_PhoneInputV1` | `PhoneField` | molecule |
| `searchInput` | `SearchField` | molecule |
| `_SingleDigit` | `OtpField` | molecule |
| `Counter`, `_quantity-hotreload`, `_counter-buttons` | `QuantityField`, `StepperButton` | molecule, atom |
| `_dropdown-single`, `basic-dropdown-single` | `SelectField` | molecule |
| `_dropdown-multiple`, `basic-dropdown-multiple` | `MultiSelectField` | molecule |
| `upload input` | `UploadField` | molecule |
| `colorPicker` | `ColorPickerField` | molecule |
| `_inputLabel` | `FieldLabel` | atom |
| `_inputTip` | `HelperText` | atom |
| `_Translation` | `TranslationToggle` | atom |
| `_breadcrumbItem` | `BreadcrumbItem`, `Divider` | molecule, atom |
| `Breadcrumb` | `Breadcrumb` | molecule |
| `Header Secondary Tabs`, `Header Primary Tabs`, `Primary Tabs List - Dashboard only`, `_Table/Tabs Item` | `Tab` (molecule), `Tabs` (organism) | |
| `Header` | `TopAppBar` | organism |
| `Header Subcategory` | `SecondaryNavBar` | organism |
| `Page Title` | `PageTitle` | molecule |
| `Side menu`, `sidemenu tab` | `NavigationDrawer`, `NavigationItem` | organism, molecule |
| `More Menu`, `_moreItems` | `MoreMenu`, `MenuItem` | organism, molecule |
| `Drop Down List`, `_listItem`, `_listTitle` | `DropdownList`, `ListItem` | organism, molecule |
| `_Date`, `_bigCalenderItems`, `_Time`, `Time` | `CalendarCell`, `DateTimePicker` | molecule, organism |
| `Table`, `Table/Header`, `Table/Cells`, `Table/Delete`, `Table/Alertbox`, `_Table/*` | `DataTable` | organism |
| `Table/Cell/*` (18) | `TableCell` family (`NameCell`, `AmountCell`, `StatusCell` …) | molecule |
| `Table/Cell/Varient` | `VariantCell` | molecule |
| `Table/Cell/Data` | `TextCell` / `DateCell` / `SelectCell` | molecule |
| `Table/Footer` | `Pagination` | organism |
| `Table/mobile *` | `MobileRow` | organism |
| `Table/Bulk Edit Sheet` | `BulkEditSheet` | organism |
| `Table/Edit Sheet` | `EditSheet` | organism |
| `_Table/Panel Header`, `previewContainer` | `PanelHeader`, `Panel` | molecule, organism |
| `_Table/Filter Results` | `FilterResults` | molecule |
| `_Table/Chips`, `Table/Cell/Chip` | `Chip` | atom |
| `_Percentage` | `ProgressCircle` | atom |
| `Steps`, `_Step base` | `Stepper`, `StepIndicator` | organism, atom |
| `Action Buttons`, `Action Bar/Confirm buttons`, `buttonsContainer` | `ActionBar` | organism |
| `Bottom sheet` | `BottomSheet` | organism |
| `searchbar` | `GlobalSearch` | molecule |
| `Learn More` | `LearnMore` | molecule |
| `Maps` | `Map` | organism |
| `Flag` | `Flag` | atom |
| `Social media icons` | `SocialIcon` | atom |
| `Illustration`, `Illustrations Collection` | `Illustration`, `EmptyState` | atom, organism |
| `Icons/Filled`, `Icons/Outline` | `Icon` | atom |
| `Products Management` | `ListPage` | template |

## Storybook story titles (old → new)

| Story today | New title |
|---|---|
| Button | `Atoms / Actions / Button` |
| Input, LingualField | `Molecules / Text inputs / TextField` |
| Textarea | `Molecules / Text inputs / TextareaField` |
| Password | `Molecules / Text inputs / PasswordField` |
| Search | `Molecules / Text inputs / SearchField` |
| Select | `Molecules / Text inputs / SelectField` |
| Tags Input | `Molecules / Text inputs / MultiSelectField` |
| Qty | `Molecules / Text inputs / QuantityField` |
| Phone | `Molecules / Text inputs / PhoneField` |
| Number / Price | `Molecules / Text inputs / AmountField` |
| File Upload | `Molecules / Text inputs / UploadField` |
| Color Picker | `Molecules / Text inputs / ColorPickerField` |
| Checkbox | `Atoms / Selection / Checkbox` and `Molecules / Selection / CheckboxField` |
| Radio | `Atoms / Selection / Radio` and `Molecules / Selection / RadioField` |
| Toggle | `Atoms / Selection / Switch` and `Molecules / Selection / SwitchField` |
| Loader | `Atoms / Communication / LoadingIndicator` and `Molecules / Communication / Loading` |
| Badge / Status | `Molecules / Communication / Status` |
| Avatar | `Atoms / Data display / Avatar` |
| AlertBox | `Organisms / Communication / Alert` and `Molecules / Communication / InlineAlert` |
| Breadcrumb | `Molecules / Navigation / Breadcrumb` |
| Tabs | `Organisms / Navigation / Tabs` |
| Dropdown / Dropdown Menu | `Organisms / Containment / DropdownList`, `Organisms / Containment / MoreMenu` |
| Table | `Organisms / Data display / DataTable` |
| Pagination | `Organisms / Navigation / Pagination` |
| Header | `Organisms / Navigation / TopAppBar` |
| Sidebar | `Organisms / Navigation / NavigationDrawer` |
| Panel | `Organisms / Containment / Panel` |
| Modal | `Organisms / Containment / Dialog` |
| Tooltip | `Organisms / Communication / Tooltip` |
| ButtonsGroup | `Organisms / Actions / ActionBar` |
| Steps | `Organisms / Navigation / Stepper` |
| Date Picker | `Organisms / Selection / DateTimePicker` |

## Token renames (old Figma variable → new)

| Figma variable | New token |
|---|---|
| `text/primary/primary`, `text/primary/link` (#004956) | `sys.color.text.brand` |
| `background/primary/primary` (#004956) | `sys.color.primary` |
| `background/secondary/seconadry`, `border/seconadry` (#a4ffe5) | `sys.color.primary-container`, `sys.color.outline-primary` |
| `text/gray/white`, `background/default/white` | `sys.color.text.inverse`, `sys.color.surface` |
| `background/default/input` | `sys.color.surface-input` |
| `border/default` (#eee) | `sys.color.outline` |
| `text/gray/light` (#666) | `sys.color.text.secondary` |
| `text/gray/dark` (#333) | `sys.color.text.primary` |
| `background/status/{success,danger,warning,info}/primary` | `sys.color.status.{…}.primary` |
| `success/success-dark`, `danger/danger-dark` | `sys.color.status.{…}.dark` |
| `success/success-darker`, `danger/danger-darker`, `text/status/info/darker` | `sys.color.status.{…}.darker` |
| `danger/danger-lighter`, `background/status/info/lighter` | `sys.color.status.{…}.lighter` |
| `border/status/info-light` | `sys.color.status.info.light` |
| `color/support-non-semantic/orange/200|300`, `background/supporting-colors/orange/darker` | `sys.color.feature.gradient-start|end`, `sys.color.feature.on-feature` |
| `spacing/6xs` 2 · `spacing/5xs` 4 · `spacing/3xs` 8 · `spacing/xs` 12 · `spacing/base` 16 · `spacing/2xl` 24 | `sys.space.3xs` · `2xs` · `xs` · `sm` · `md` · `xl` |
| `Spacing/Sizes/3xs` 2 · `Spacing/Sizes/sm` 8 · `Spacing/Sizes/lg` 12 | `sys.space.3xs` · `xs` · `sm` |
| `radius/md` 4 · `radius/xl` 8 · `radius/full` · `Radius/Sizes/*` | `sys.shape.extra-small` · `small` · `full` (see shape.md) |
| `Typography/Family/Font` | `ref.font.family.base` |
| `Typography/Weight/Regular|Medium|Bold` | `ref.font.weight.*` |
| `Typography/Size/xs|sm|md` | `ref.font.size.*` |
| `typography/line-height (Descreptive)/4|5|6` | `ref.font.lineHeight.4|5|6` |
| `Bold/$text-base`, `Regular/$text-sm`, `Medium/$text-xs` … | `sys.typography.title-md`, `body-sm`, `label-sm` … (see typography.md) |

## Suggested order of migration

1. Tokens: add `01-Primitives` values to `tokens.json` (replace `assumed`), add elevation and motion, unify spacing.
2. Figma: create the four level sections and move frames; rename per the table; fix typos in variables.
3. Figma: replace `Language` variants with a variable mode; remove `--device` where layout is responsive.
4. Code: build `BaseButton`, `BaseField`, `Checkbox`, `Radio`, `Switch`, `Icon` first; then the fields; then `DataTable`.
5. Storybook: retitle stories; add Docs pages linking to the catalog.
