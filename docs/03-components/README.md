# Components

Every component classified by **atomic level** (how it composes) and **Material category** (how you find it), with its **structure type** (how it is built). Generated from `catalog/components.json`.

| Total | Existing in Figma / Storybook | Proposed (gap) | Page references |
|---|---|---|---|
| 92 | 79 | 10 | 3 |

## By atomic level

### Atoms (23)

Atoms are the smallest usable UI units: a button, an icon, a checkbox. They do one thing, take tokens directly and never know about product data.

| Component | Material category | Structure | Status | What it is |
|---|---|---|---|---|
| [Button](atoms/button.md) | Actions | 1 | existing | The single action trigger. |
| [IconButton](atoms/icon-button.md) | Actions | 3 | proposed | Icon-only button. |
| [Link](atoms/link.md) | Actions | 3 | proposed | Inline text action. |
| [Icon](atoms/icon.md) | Communication | 2 | existing | A single glyph from the Salla icon set. |
| [Checkbox](atoms/checkbox.md) | Selection | 3 | existing | Bare selection control with true / false / mixed states in two sizes. |
| [Radio](atoms/radio.md) | Selection | 3 | existing | Bare single-choice control in two sizes. |
| [Switch](atoms/toggle.md) | Selection | 3 | existing | On/off control (Material: Switch). |
| [LoadingIndicator](atoms/loading-indicator.md) | Communication | 1 | existing | Spinner, dots or line progress in nine sizes from 8px to 88px. |
| [StatusIndicator](atoms/status-indicator.md) | Communication | 1 | existing | The 10px coloured dot. |
| [Avatar](atoms/avatar.md) | Data display | 1 | existing | Image, text initials, icon or fallback in six sizes, circular or rectangular. |
| [Chip](atoms/chip.md) | Selection | 1 | existing | Compact tag used in table cells and multi-select fields. |
| [Flag](atoms/flag.md) | Data display | 2 | existing | Country flag glyphs, one per ISO 3166 code (265 in Figma). |
| [SocialIcon](atoms/social-icon.md) | Data display | 2 | existing | Brand logos (Facebook, Google, Google Ads, Meta, Snapchat, TikTok, YouTube, Instagram, X). |
| [Illustration](atoms/illustration.md) | Communication | 2 | existing | Spot illustrations for empty states and onboarding, with web and mobile variants. |
| [FieldLabel](atoms/label.md) | Text inputs | 1 | existing | Label line above a field: text, optional required mark, optional info icon. |
| [HelperText](atoms/helper-text.md) | Text inputs | 1 | existing | Line under a field: hint, error, character count, variables hint or file delete action. |
| [PasswordHint](atoms/password-hint.md) | Communication | 1 | existing | One requirement line (pending / success / danger) used by PasswordField. |
| [StepperButton](atoms/stepper-button.md) | Actions | 1 | existing | The +/- buttons flanking QuantityField, including the delete-at-one variant. |
| [TranslationToggle](atoms/translation-toggle.md) | Text inputs | 1 | existing | The small EN/AR language switch inside bilingual fields (Storybook: LingualField). |
| [ProgressCircle](atoms/progress-circle.md) | Communication | 1 | existing | Circular determinate progress (25/50/75/100 in Figma, should accept any value). |
| [StepIndicator](atoms/step-indicator.md) | Navigation | 1 | existing | One node of the Stepper: number or check in a circle with a connector. |
| [Divider](atoms/divider.md) | Containment | 1 | proposed | Horizontal or vertical rule. |
| [Text](atoms/text.md) | Communication | 1 | proposed | Typography primitive exposing the Material type roles (display, headline, title, body, label) that map onto the Figma Bold/Medium/Regular $text-* styles. |

### Molecules (38)

Molecules are small groups of atoms working as a unit: a labelled field, a status pill, a breadcrumb. They own a single, clear responsibility.

| Component | Material category | Structure | Status | What it is |
|---|---|---|---|---|
| [BaseField (internal)](molecules/base-field.md) | Text inputs | 3 | existing | The internal base for every field: label + container (icon-start, control, subtext/unit, translation toggle, info) + helper text. |
| [TextField](molecules/text-field.md) | Text inputs | 3 | existing | Single-line text entry. |
| [TextareaField](molecules/textarea-field.md) | Text inputs | 3 | existing | Multi-line text entry with optional rich-text toolbar. |
| [PasswordField](molecules/password-field.md) | Text inputs | 3 | existing | Masked entry with show/hide toggle and an optional requirements checklist (112 Figma variants collapse to four props). |
| [EmailField](molecules/email-field.md) | Text inputs | 3 | existing | TextField pre-configured with type=email, mail icon and email validation. |
| [AmountField](molecules/amount-field.md) | Text inputs | 3 | existing | Numeric / currency entry with the Saudi Riyal symbol as trailing unit. |
| [PhoneField](molecules/phone-field.md) | Text inputs | 3 | existing | Phone entry with country-code picker (Flag + code) as leading control. |
| [SearchField](molecules/search-field.md) | Text inputs | 3 | existing | Search entry with magnifier, clear button, recommendations and no-results states. |
| [OtpField](molecules/otp-field.md) | Text inputs | 3 | existing | Single-digit boxes for verification codes. |
| [QuantityField](molecules/quantity-field.md) | Text inputs | 3 | existing | Number entry with StepperButtons, compact and default sizes, and the hot-reload (inline save) variant used in tables. |
| [SelectField](molecules/select-field.md) | Text inputs | 3 | existing | Single-choice dropdown field. |
| [MultiSelectField](molecules/multi-select-field.md) | Text inputs | 3 | existing | Multi-choice dropdown field rendering selections as Chips (Storybook: Tags Input). |
| [UploadField](molecules/upload-field.md) | Text inputs | 3 | existing | File picker with drag and drop: inline, single image, single video, multiple (row or column). |
| [ColorPickerField](molecules/color-picker-field.md) | Text inputs | 3 | existing | Colour swatch + hex entry with a picker popover. |
| [CheckboxField](molecules/checkbox-field.md) | Selection | 3 | existing | Checkbox + label + optional description / info tooltip. |
| [RadioField](molecules/radio-field.md) | Selection | 3 | existing | Radio + label, used inside a RadioGroup. |
| [RadioImage](molecules/radio-image.md) | Selection | 2 | existing | Selectable image card (visual radio) for templates, themes, layouts. |
| [RadioColor](molecules/radio-color.md) | Selection | 2 | existing | Selectable colour swatch (visual radio) for product colour variants. |
| [SwitchField](molecules/toggle-field.md) | Selection | 3 | existing | Switch + label with the switch at inline-start or inline-end. |
| [Status](molecules/status.md) | Communication | 3 | existing | StatusIndicator + label in subtle (dot + text) or strong (pill) appearance. |
| [Loading](molecules/loading.md) | Communication | 3 | existing | LoadingIndicator + localised label for block-level loading. |
| [AvatarWithText](molecules/avatar-with-text.md) | Data display | 4 | existing | Avatar + primary and secondary text lines (customer, product, staff rows). |
| [AvatarStack](molecules/avatar-stack.md) | Data display | 1 | existing | Overlapping or spaced row of Avatars with +N overflow. |
| [Breadcrumb](molecules/breadcrumb.md) | Navigation | 4 | existing | Path navigation with icon, text, more (…) and separator items; collapses past 5 items and on mobile. |
| [BreadcrumbItem](molecules/breadcrumb-item.md) | Navigation | 1 | existing | One breadcrumb node: icon, text or overflow menu trigger. |
| [Tab](molecules/tab.md) | Navigation | 1 | existing | One tab, primary (dashboard top nav) or secondary (page sub-nav), contained or plain, with active/hover states. |
| [NavigationItem](molecules/side-menu-item.md) | Navigation | 1 | existing | One entry of the side navigation (first / middle / last for grouping radius). |
| [MenuItem](molecules/menu-item.md) | Containment | 1 | existing | Row inside MoreMenu: icon or image + label, optional danger tone; separators become Divider. |
| [ListItem](molecules/list-item.md) | Containment | 4 | existing | Row inside DropdownList and pickers: plain, with description, with flag, with image; supports checkbox, selected, danger, disabled and 'feature' (upsell) states. |
| [TableCell](molecules/table-cell.md) | Data display | 2 | existing | Typed cells: name, sub-name, image, products, amount, percentage, status, tags, markets (flag + text), variant, data (text / date-time / dropdown), actions (1-3 icons or toggle), checkbox, chip, disabled, sort and header. |
| [CalendarCell](molecules/date-time-cell.md) | Selection | 1 | existing | Day, number and time cells used by the date/time picker. |
| [AccountMenuTrigger](molecules/header-avatar.md) | Navigation | 1 | existing | Avatar + store name + chevron in the top bar that opens the account menu. |
| [PageTitle](molecules/page-title.md) | Navigation | 4 | existing | Page heading row: back / breadcrumb, title, optional status and actions slot. |
| [LearnMore](molecules/learn-more.md) | Communication | 1 | existing | Help card linking to documentation, default and small sizes, desktop and mobile. |
| [GlobalSearch](molecules/global-search.md) | Text inputs | 1 | existing | Header search: collapsed button-only or full field. |
| [FilterResults](molecules/filter-results.md) | Communication | 1 | existing | Applied-filters summary bar above a table with a clear action. |
| [PanelHeader](molecules/panel-header.md) | Containment | 4 | existing | Title + actions row for Panel / Table containers, default and small. |
| [InlineAlert](molecules/inline-alert.md) | Communication | 3 | existing | Compact, non-dismissible alert placed under a field or inside a card (Alertbox Type=Inline). |

### Organisms (24)

Organisms are complex sections built from molecules and atoms: the data table, the top app bar, the dropdown list. They usually manage state or layout.

| Component | Material category | Structure | Status | What it is |
|---|---|---|---|---|
| [Alert](organisms/alert.md) | Communication | 1 | existing | Contextual message with icon, optional title, body, optional button and close. |
| [AlertBanner](organisms/alert-banner.md) | Communication | 2 | existing | Full-width page-level announcement (two layouts). |
| [UpgradeCard](organisms/alert-upgrade.md) | Communication | 2 | existing | Plan-upgrade promo card, desktop and mobile. |
| [DropdownList](organisms/dropdown-list.md) | Containment | 4 | existing | The floating list behind SelectField, MultiSelectField, pickers and menus: one to three layers, accordion, flags, images, checkboxes, descriptions, no-results and create-new states. |
| [DateTimePicker](organisms/date-time-picker.md) | Selection | 5 | existing | Calendar and time picker popover built from CalendarCell. |
| [MoreMenu](organisms/more-menu.md) | Containment | 4 | existing | Overflow (kebab) menu anchored to a trigger, three layouts, left/right placement. |
| [NavigationDrawer](organisms/side-menu.md) | Navigation | 4 | existing | The dashboard side navigation (Material: navigation drawer) composed of NavigationItems and section headers. |
| [TopAppBar](organisms/header.md) | Navigation | 4 | existing | Dark-teal top bar: logo, primary tabs, global search, notifications, account menu. |
| [SecondaryNavBar](organisms/header-subcategory.md) | Navigation | 4 | existing | Second-level bar under the TopAppBar carrying secondary Tabs and a help / CTA area. |
| [Tabs](organisms/tabs.md) | Navigation | 5 | existing | Tab list + panels. |
| [DataTable](organisms/table.md) | Data display | 4 | existing | The merchant list view: header (title, tabs, search, filters), column headers with sort / select-all, typed cells, sticky action column, row selection with bulk bar, delete, edit sheet, pagination footer, mobile card rows, empty and filter-result states. |
| [MobileRow](organisms/table-row-mobile.md) | Data display | 2 | existing | Card-style row for phones: order, product, customer and default layouts. |
| [BulkEditSheet](organisms/bulk-edit-sheet.md) | Containment | 4 | existing | Side sheet opened from the DataTable bulk bar to edit selected rows. |
| [EditSheet](organisms/edit-sheet.md) | Containment | 4 | existing | Inline edit side sheet for one row (default and minimum-cells layouts). |
| [Stepper](organisms/stepper.md) | Navigation | 5 | existing | Two to five step progress for wizards, desktop and mobile. |
| [ActionBar](organisms/action-bar.md) | Actions | 4 | existing | Confirm / cancel button group, floating or flat, desktop and mobile. |
| [BottomSheet](organisms/bottom-sheet.md) | Containment | 4 | existing | Mobile modal surface sliding from the bottom. |
| [Dialog](organisms/dialog.md) | Containment | 4 | proposed | Centered modal (Storybook: Modal). |
| [Panel](organisms/panel.md) | Containment | 4 | proposed | Card container with PanelHeader, body and footer slots (Storybook: Panel). |
| [Tooltip](organisms/tooltip.md) | Communication | 5 | existing | Hover / focus hint on a primary-container surface with a caret. |
| [Toast](organisms/toast.md) | Communication | 1 | proposed | Transient bottom notification (Material: snackbar). |
| [EmptyState](organisms/empty-state.md) | Communication | 4 | existing | Illustration + title + description + action for empty lists and no-results. |
| [Pagination](organisms/pagination.md) | Navigation | 1 | existing | Table footer: page size, range label, previous / next and page numbers. |
| [Map](organisms/map.md) | Data display | 2 | existing | Embedded map for addresses and branches. |

### Templates (4)

Templates are page-level layouts with slots and no real content. They fix where organisms go.

| Component | Material category | Structure | Status | What it is |
|---|---|---|---|---|
| [ListPage](templates/list-page.md) | Containment | 4 | existing | TopAppBar + SecondaryNavBar + PageTitle + DataTable in a Panel. |
| [ListDetailPage](templates/list-detail.md) | Containment | 4 | proposed | Two-pane layout used by Orders: list on one side, detail on the other, collapsing to stacked on mobile. |
| [FormPage](templates/form-page.md) | Containment | 4 | proposed | PageTitle + one or more Panels of fields + sticky ActionBar. |
| [WizardPage](templates/wizard-page.md) | Navigation | 4 | proposed | Stepper + step content + ActionBar for onboarding and multi-step flows. |

### Pages (3)

Pages are templates filled with real merchant data. They are documented as references to production, not built in the library.

| Component | Material category | Structure | Status | What it is |
|---|---|---|---|---|
| [Orders list](pages/orders-list.md) | Data display | 4 | reference | s. |
| [Products list](pages/products-list.md) | Data display | 4 | reference | s. |
| [Order details](pages/order-details.md) | Containment | 4 | reference | s. |

## By Material category

### Actions (5)

| Component | Atomic level | Structure | Status |
|---|---|---|---|
| [Button](atoms/button.md) | atom | 1 | existing |
| [IconButton](atoms/icon-button.md) | atom | 3 | proposed |
| [Link](atoms/link.md) | atom | 3 | proposed |
| [StepperButton](atoms/stepper-button.md) | atom | 1 | existing |
| [ActionBar](organisms/action-bar.md) | organism | 4 | existing |

### Communication (18)

| Component | Atomic level | Structure | Status |
|---|---|---|---|
| [Icon](atoms/icon.md) | atom | 2 | existing |
| [LoadingIndicator](atoms/loading-indicator.md) | atom | 1 | existing |
| [StatusIndicator](atoms/status-indicator.md) | atom | 1 | existing |
| [Illustration](atoms/illustration.md) | atom | 2 | existing |
| [PasswordHint](atoms/password-hint.md) | atom | 1 | existing |
| [ProgressCircle](atoms/progress-circle.md) | atom | 1 | existing |
| [Text](atoms/text.md) | atom | 1 | proposed |
| [Status](molecules/status.md) | molecule | 3 | existing |
| [Loading](molecules/loading.md) | molecule | 3 | existing |
| [LearnMore](molecules/learn-more.md) | molecule | 1 | existing |
| [FilterResults](molecules/filter-results.md) | molecule | 1 | existing |
| [InlineAlert](molecules/inline-alert.md) | molecule | 3 | existing |
| [Alert](organisms/alert.md) | organism | 1 | existing |
| [AlertBanner](organisms/alert-banner.md) | organism | 2 | existing |
| [UpgradeCard](organisms/alert-upgrade.md) | organism | 2 | existing |
| [Tooltip](organisms/tooltip.md) | organism | 5 | existing |
| [Toast](organisms/toast.md) | organism | 1 | proposed |
| [EmptyState](organisms/empty-state.md) | organism | 4 | existing |

### Containment (15)

| Component | Atomic level | Structure | Status |
|---|---|---|---|
| [Divider](atoms/divider.md) | atom | 1 | proposed |
| [MenuItem](molecules/menu-item.md) | molecule | 1 | existing |
| [ListItem](molecules/list-item.md) | molecule | 4 | existing |
| [PanelHeader](molecules/panel-header.md) | molecule | 4 | existing |
| [DropdownList](organisms/dropdown-list.md) | organism | 4 | existing |
| [MoreMenu](organisms/more-menu.md) | organism | 4 | existing |
| [BulkEditSheet](organisms/bulk-edit-sheet.md) | organism | 4 | existing |
| [EditSheet](organisms/edit-sheet.md) | organism | 4 | existing |
| [BottomSheet](organisms/bottom-sheet.md) | organism | 4 | existing |
| [Dialog](organisms/dialog.md) | organism | 4 | proposed |
| [Panel](organisms/panel.md) | organism | 4 | proposed |
| [ListPage](templates/list-page.md) | template | 4 | existing |
| [ListDetailPage](templates/list-detail.md) | template | 4 | proposed |
| [FormPage](templates/form-page.md) | template | 4 | proposed |
| [Order details](pages/order-details.md) | page | 4 | reference |

### Navigation (14)

| Component | Atomic level | Structure | Status |
|---|---|---|---|
| [StepIndicator](atoms/step-indicator.md) | atom | 1 | existing |
| [Breadcrumb](molecules/breadcrumb.md) | molecule | 4 | existing |
| [BreadcrumbItem](molecules/breadcrumb-item.md) | molecule | 1 | existing |
| [Tab](molecules/tab.md) | molecule | 1 | existing |
| [NavigationItem](molecules/side-menu-item.md) | molecule | 1 | existing |
| [AccountMenuTrigger](molecules/header-avatar.md) | molecule | 1 | existing |
| [PageTitle](molecules/page-title.md) | molecule | 4 | existing |
| [NavigationDrawer](organisms/side-menu.md) | organism | 4 | existing |
| [TopAppBar](organisms/header.md) | organism | 4 | existing |
| [SecondaryNavBar](organisms/header-subcategory.md) | organism | 4 | existing |
| [Tabs](organisms/tabs.md) | organism | 5 | existing |
| [Stepper](organisms/stepper.md) | organism | 5 | existing |
| [Pagination](organisms/pagination.md) | organism | 1 | existing |
| [WizardPage](templates/wizard-page.md) | template | 4 | proposed |

### Selection (11)

| Component | Atomic level | Structure | Status |
|---|---|---|---|
| [Checkbox](atoms/checkbox.md) | atom | 3 | existing |
| [Radio](atoms/radio.md) | atom | 3 | existing |
| [Switch](atoms/toggle.md) | atom | 3 | existing |
| [Chip](atoms/chip.md) | atom | 1 | existing |
| [CheckboxField](molecules/checkbox-field.md) | molecule | 3 | existing |
| [RadioField](molecules/radio-field.md) | molecule | 3 | existing |
| [RadioImage](molecules/radio-image.md) | molecule | 2 | existing |
| [RadioColor](molecules/radio-color.md) | molecule | 2 | existing |
| [SwitchField](molecules/toggle-field.md) | molecule | 3 | existing |
| [CalendarCell](molecules/date-time-cell.md) | molecule | 1 | existing |
| [DateTimePicker](organisms/date-time-picker.md) | organism | 5 | existing |

### Text inputs (18)

| Component | Atomic level | Structure | Status |
|---|---|---|---|
| [FieldLabel](atoms/label.md) | atom | 1 | existing |
| [HelperText](atoms/helper-text.md) | atom | 1 | existing |
| [TranslationToggle](atoms/translation-toggle.md) | atom | 1 | existing |
| [BaseField (internal)](molecules/base-field.md) | molecule | 3 | existing |
| [TextField](molecules/text-field.md) | molecule | 3 | existing |
| [TextareaField](molecules/textarea-field.md) | molecule | 3 | existing |
| [PasswordField](molecules/password-field.md) | molecule | 3 | existing |
| [EmailField](molecules/email-field.md) | molecule | 3 | existing |
| [AmountField](molecules/amount-field.md) | molecule | 3 | existing |
| [PhoneField](molecules/phone-field.md) | molecule | 3 | existing |
| [SearchField](molecules/search-field.md) | molecule | 3 | existing |
| [OtpField](molecules/otp-field.md) | molecule | 3 | existing |
| [QuantityField](molecules/quantity-field.md) | molecule | 3 | existing |
| [SelectField](molecules/select-field.md) | molecule | 3 | existing |
| [MultiSelectField](molecules/multi-select-field.md) | molecule | 3 | existing |
| [UploadField](molecules/upload-field.md) | molecule | 3 | existing |
| [ColorPickerField](molecules/color-picker-field.md) | molecule | 3 | existing |
| [GlobalSearch](molecules/global-search.md) | molecule | 1 | existing |

### Data display (11)

| Component | Atomic level | Structure | Status |
|---|---|---|---|
| [Avatar](atoms/avatar.md) | atom | 1 | existing |
| [Flag](atoms/flag.md) | atom | 2 | existing |
| [SocialIcon](atoms/social-icon.md) | atom | 2 | existing |
| [AvatarWithText](molecules/avatar-with-text.md) | molecule | 4 | existing |
| [AvatarStack](molecules/avatar-stack.md) | molecule | 1 | existing |
| [TableCell](molecules/table-cell.md) | molecule | 2 | existing |
| [DataTable](organisms/table.md) | organism | 4 | existing |
| [MobileRow](organisms/table-row-mobile.md) | organism | 2 | existing |
| [Map](organisms/map.md) | organism | 2 | existing |
| [Orders list](pages/orders-list.md) | page | 4 | reference |
| [Products list](pages/products-list.md) | page | 4 | reference |

## Structure types legend

| # | Pattern |
|---|---|
| 1 | Configurable (single component, variations via props) |
| 2 | Standalone (separate, explicitly named components) |
| 3 | Base + Global (internal base component, public pre-configured components) |
| 4 | Slot / Composition (container with named slots) |
| 5 | Headless (logic only, UI supplied separately) |

See [component-structure-types.md](../00-overview/component-structure-types.md) for when to use each.
