# Content and localisation

The dashboard is Arabic-first and fully bilingual. Every component is designed in both languages. This page is Material's *Content design* foundation plus the rules that make RTL automatic.

## Direction

- `dir="rtl"` for Arabic, `dir="ltr"` for English, set on `<html>` and inherited.
- Components use **CSS logical properties** only: `margin-inline-start`, `padding-inline`, `inset-inline-end`, `border-inline-start`, `text-align: start`. No `left` / `right`.
- Props use logical names: `iconStart` / `iconEnd`, `placement="start" | "end"`, `position="start" | "end"` (SwitchField). Figma's `Dir=Left/Right` migrates to `placement`.
- Flex and grid flip automatically; nothing is re-ordered by hand.

Consequence for Figma: `Language=Arabic|English` stops being a variant axis on every component and becomes a **variable mode** applied to the page. Only components with genuinely different Arabic and English layouts keep both frames (typography-heavy ones such as `AlertBanner`, `UpgradeCard`, `LearnMore`).

## Mirroring

| Mirror in RTL | Never mirror |
|---|---|
| arrows, chevrons, back / forward, undo / redo, indent, list bullets, progress direction, `Switch` thumb travel, `Stepper` order, `Breadcrumb` separators, `Pagination` prev / next | search magnifier, trash, settings gear, close ×, check ✓, sort carets (they point up / down), media playback, brand logos, clocks, phone, numbers and units |

`Icon` exposes `mirrorInRtl`; the icon inventory should tag directional glyphs so the default is right.

## Numbers, dates and currency

Follows the live dashboard (s.salla.sa), which does **not** use Arabic-Indic digits:

| Item | Rule | Example |
|---|---|---|
| Digits | Western Arabic (0-9) in both languages | 1,250 |
| Currency | Saudi Riyal symbol glyph (the `Saudi-Riyal` icon in `AmountField`) after the number in Arabic, before in English; two decimals | 1,250.00 ر.س / SAR 1,250.00 |
| Dates | numeric `DD/MM/YYYY` in Arabic UI, `MMM D, YYYY` in English; Hijri available via `DateTimePicker calendar=hijri` | 22/09/2026 |
| Time | 12-hour with locale AM/PM markers | 3:45 م |
| Phone | LTR isolate always (`<bdi>`), country code from `PhoneField` | +966 5X XXX XXXX |
| OTP codes, SKUs, URLs, emails | LTR isolate | |

## Voice and tone

- Address the merchant directly and respectfully: Arabic second person, English "you". No slang.
- Buttons are verbs: `حفظ` / `Save`, `إضافة منتج` / `Add product`. Never "OK" alone on a destructive action.
- Titles are sentence case in English; Arabic has no case.
- Error messages say what happened and what to do: "لم يتم حفظ التغييرات. حاول مرة أخرى." / "Changes were not saved. Try again."
- Empty states (EmptyState) lead with the benefit, then the action.
- Status labels are single nouns or past participles: `تم الشحن` / `Shipped`.

## Typography per language

One family, PingAR+LT, covers both scripts, so type roles do not change per language. Arabic runs ~10% wider at equal size; components size to content (`hug`) so no fixed widths in molecules and atoms.

## Bilingual fields

`TextField bilingual` shows a `TranslationToggle` (EN / AR) at inline-end. The field's `dir` follows the *selected* language, not the page. Storybook name today: `LingualField`.
