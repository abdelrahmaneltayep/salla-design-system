# Spacing

The scale is the Figma **`Spacing/Sizes`** collection (`04-Token`), adopted verbatim. Values were read from Figma on 2026-09-22; the older `spacing/*` variables that some frames still use are mapped below.

## The scale

| Token | Value | Figma `Spacing/Sizes` | Older `spacing/*` alias | Observed use |
|---|---|---|---|---|
| `ref.space.none` | 0 | `none` ✓ | – | |
| `ref.space.3xs` | 2px | `3xs` ✓ | `spacing/6xs` ✓ | Checkbox inner padding, TranslationToggle gap, Alert icon offset |
| `ref.space.2xs` | 4px | `2xs` ✓ | `spacing/5xs` ✓ | Button icon–label gap, Status dot–label gap, Alert title–body gap, Button sm vertical padding |
| `ref.space.xs` | 6px | `xs` ✓ | `spacing/4xs` ✓ | Table/Status vertical padding, Loader padding |
| `ref.space.sm` | 8px | `sm` ✓ | `spacing/3xs` ✓ | Button / field vertical padding, field gap, Status horizontal padding, Tab vertical padding, Alert gap |
| `ref.space.md` | 10px | `md` ✓ | `spacing/2xs` ✓ | UpgradeCard CTA vertical padding, page-size select, primary Tabs gap |
| `ref.space.lg` | 12px | `lg` ✓ | `spacing/xs` ✓ | Button / field horizontal padding, MenuItem padding, label–field gap, Tooltip padding |
| `ref.space.xl` | 14px | `xl` ✓ | – | mobile gutters (PageTitle, Table/Footer) |
| `ref.space.2xl` | 16px | `2xl` ✓ | `spacing/base` ✓ | card padding, TopAppBar vertical padding, Alert vertical padding, NavigationItem padding, primary Tab horizontal padding |
| `ref.space.3xl` | 20px | `3xl` ✓ | – | TopAppBar gap |
| `ref.space.4xl` | 24px | `4xl` ✓ | `spacing/2xl` ✓ | Alert horizontal padding, Pagination gap, SecondaryNavBar gap |
| `ref.space.5xl` | 26px | `5xl` ✓ | – | Table/Footer desktop horizontal padding (off-grid, see below) |
| `ref.space.6xl` | 32px | `6xl` | – | not observed |
| `ref.space.7xl` | 40px | `7xl` | – | not observed |
| `ref.space.8xl` | 48px | `8xl` | – | not observed |
| `ref.space.9xl` | 56px | `9xl` ✓ | `spacing/7xl` ✓ | **desktop page gutter** (TopAppBar, SecondaryNavBar, PageTitle, Breadcrumb) |

## Semantic aliases

Components use role names so intent reads in the CSS:

| Alias | → | Use |
|---|---|---|
| `sys.space.hairline` | `3xs` 2px | inner padding of tiny controls |
| `sys.space.tight` | `2xs` 4px | icon ↔ label |
| `sys.space.compact` | `sm` 8px | control vertical padding, sibling gaps in a row |
| `sys.space.default` | `lg` 12px | control horizontal padding, list item padding |
| `sys.space.comfortable` | `2xl` 16px | card / bar padding |
| `sys.space.loose` | `3xl` 20px | bar item gap |
| `sys.space.section` | `4xl` 24px | between sections, alert side padding |
| `sys.space.gutter` | `9xl` 56px | page side gutter (desktop) |

## The two-scale problem, resolved

Figma still carries two variable sets with **the same names for different values**:

| Name | `spacing/*` (older) | `Spacing/Sizes/*` (04-Token) |
|---|---|---|
| `3xs` | 8px | 2px |
| `2xs` | 10px | 4px |
| `xs` | 12px | 6px |
| `2xl` | 24px | 16px |

`Button`, `Alertbox`, `Page Title` and `Header` use the older set; `_TextInput`, `checkBox`, `Status`, `Side menu`, `More Menu`, `Table/*` use `Spacing/Sizes`. The value is always the same physical pixel; only the name differs. **Decision: `Spacing/Sizes` is the scale**, because it is the newer collection, it is complete (`none … 9xl`), and most component frames already use it. Re-point the older `spacing/*` variables per the alias column above, then delete them.

Two values are off the 4px grid and worth a design decision: `xl` = 14px (used as the mobile gutter) and `5xl` = 26px (Table/Footer). Recommend 16px and 24px.

## Rules

- Padding inside atoms and molecules comes from `comp.*` tokens that alias `ref.space.*`.
- Gaps between siblings use the semantic aliases.
- No values outside the scale; legacy hard-coded `gap-[5px]`, `p-[10px]` seen on a few frames are migration targets.
