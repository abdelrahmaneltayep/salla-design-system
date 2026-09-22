# Layout and adaptive design

How screens are structured and how they adapt. Material's *Adaptive design* and *Layout* foundations applied to the merchant dashboard, which is desktop-first with a full mobile experience.

## Grid

- Base unit **4px** (`ref.space.*`). All spacing, sizes and radii are multiples of 4, with 2px allowed only for hairline gaps (`sys.space.3xs`).
- Page gutter: `sys.space.md` (16px) on phones, `sys.space.xl` (24px) from tablet up.
- Content max width: 1536px (the Figma desktop frames are 1536 wide inside a 1576 artboard), centred.

## Breakpoints (window size classes)

Material 3 window size classes, with Salla's Tailwind names:

| Class | Width | Tailwind | Layout behaviour |
|---|---|---|---|
| Compact | < 600 | `sm` and below | Single column. `TopAppBar` mobile, `NavigationDrawer` modal, `DataTable` renders `MobileRow`, `ActionBar` floats bottom, `BottomSheet` replaces `Dialog` |
| Medium | 600 – 839 | `md` | Single column with wider gutters. Drawer modal. Tables scroll horizontally |
| Expanded | 840 – 1199 | `lg` | Drawer standard (persistent). `ListDetailPage` shows two panes |
| Large / Extra-large | ≥ 1200 | `xl`, `2xl` | Full desktop; content capped at 1536 |

Components with genuinely different layouts per class declare a `device` prop in the catalog (`TopAppBar`, `PageTitle`, `DataTable`, `Breadcrumb`, `Stepper`, `Pagination`). Everything else adapts with CSS.

## App shell

```
┌──────────────────────────────────────────────────────────┐
│ TopAppBar (sys.color.primary, 64px)                      │
│  logo · primary Tabs · GlobalSearch · icons · account    │
├──────────────────────────────────────────────────────────┤
│ SecondaryNavBar (secondary Tabs · help · CTA)            │
├────────────┬─────────────────────────────────────────────┤
│ Navigation │ PageTitle                                    │
│ Drawer     │ ┌──────────────────────────────────────────┐ │
│ (expanded+)│ │ Panel / DataTable / form sections        │ │
│            │ └──────────────────────────────────────────┘ │
│            │                              [floating help] │
└────────────┴─────────────────────────────────────────────┘
```

Templates (`ListPage`, `ListDetailPage`, `FormPage`, `WizardPage`) fix which organisms sit in the content region. See `docs/03-components/templates/`.

## Panes

- **List pane** min 320px, **detail pane** takes the rest (`ListDetailPage`).
- Side sheets (`BulkEditSheet`, `EditSheet`) are 400 – 480px wide on expanded, full-width on compact.
- Dropdown surfaces (`DropdownList`, `MoreMenu`) match the trigger width, min 240px, max 400px.

## Density

Two densities exist in the library: **default** and **compact** (`QuantityField size=compact`, `AvatarStack size=compact`, `PanelHeader size=small`, `Button size=sm`). Compact is used inside `DataTable` cells and dense forms only.

## Direction

The dashboard runs in Arabic (RTL) and English (LTR). Layout is written with CSS logical properties so it mirrors automatically. Details: [content-and-localization.md](content-and-localization.md).
