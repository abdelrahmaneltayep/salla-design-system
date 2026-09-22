# Salla Twilight — Dashboard UI Components

> Full extract of the component Storybook at <https://dashboard-ui-components.pages.dev>.
> Captured 2026-09-22 · Storybook index v5 · 408 stories across 41 entries.

This file is a machine-readable reference of the design system: tokens, every component, every prop, slot, event, story, and the real rendered markup. Components are Stencil web components with an `s-` prefix, styled with Tailwind classes backed by CSS variables.

**Conventions**

- Every component is a custom element, e.g. `<s-button theme="default">`.
- Props are set as HTML attributes (kebab-case) or JS properties (camelCase).
- Colors are CSS variables holding bare HSL channels — use as `hsl(var(--primary))`, or the Tailwind class `bg-primary`.
- Font family is **PingARLT**; the UI is bilingual (Arabic RTL + English LTR).

---

## 1. Design tokens

### 1.1 Color palette

**Primary**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `primary` | `bg-primary` | `--primary` | `hsl(189 100% 17%)` | `#004A57` | rgb(0, 74, 87) |
| `primary-force` | `bg-primary-force` | `--primary-force` | `hsl(189 100% 17%)` | `#004A57` | rgb(0, 74, 87) |
| `primary-100` | `bg-primary-100` | `--primary-100` | `hsl(187 40% 96%)` | `#F1F8F9` | rgb(241, 248, 249) |
| `primary-200` | `bg-primary-200` | `--primary-200` | `hsl(188 39% 70%)` | `#95C8D0` | rgb(149, 200, 208) |
| `primary-300` | `bg-primary-300` | `--primary-300` | `hsl(188 38% 54%)` | `#5DAAB6` | rgb(93, 170, 182) |
| `primary-400` | `bg-primary-400` | `--primary-400` | `hsl(189 50% 41%)` | `#348D9D` | rgb(52, 141, 157) |
| `primary-500` | `bg-primary-500` | `--primary-500` | `hsl(189 100% 18%)` | `#004E5C` | rgb(0, 78, 92) |
| `primary-600` | `bg-primary-600` | `--primary-600` | `hsl(189 100% 15%)` | `#00414D` | rgb(0, 65, 77) |
| `primary-700` | `bg-primary-700` | `--primary-700` | `hsl(191 76% 16%)` | `#0A3C48` | rgb(10, 60, 72) |

**Secondary**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `secondary` | `bg-secondary` | `--secondary` | `hsl(163 100% 82%)` | `#A3FFE5` | rgb(163, 255, 229) |
| `secondary-100` | `bg-secondary-100` | `--secondary-100` | `hsl(163 100% 97%)` | `#F0FFFB` | rgb(240, 255, 251) |
| `secondary-200` | `bg-secondary-200` | `--secondary-200` | `hsl(166 100% 95%)` | `#E5FFF9` | rgb(230, 255, 249) |
| `secondary-300` | `bg-secondary-300` | `--secondary-300` | `hsl(165 100% 93%)` | `#DBFFF6` | rgb(219, 255, 246) |
| `secondary-400` | `bg-secondary-400` | `--secondary-400` | `hsl(164 96% 72%)` | `#73FCD8` | rgb(115, 252, 216) |
| `secondary-500` | `bg-secondary-500` | `--secondary-500` | `hsl(164 89% 63%)` | `#4DF5C8` | rgb(77, 245, 200) |
| `secondary-600` | `bg-secondary-600` | `--secondary-600` | `hsl(164 83% 55%)` | `#2DEBB9` | rgb(45, 235, 185) |
| `secondary-700` | `bg-secondary-700` | `--secondary-700` | `hsl(163 78% 52%)` | `#25E4AE` | rgb(37, 228, 174) |

**Success**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `success` | `bg-success` | `--success` | `hsl(157 100% 34%)` | `#00AD6B` | rgb(0, 173, 107) |
| `success-100` | `bg-success-100` | `--success-100` | `hsl(155 60% 96%)` | `#EFFBF6` | rgb(239, 251, 246) |
| `success-200` | `bg-success-200` | `--success-200` | `hsl(157 63% 75%)` | `#97E7C9` | rgb(151, 231, 201) |
| `success-300` | `bg-success-300` | `--success-300` | `hsl(157 59% 69%)` | `#81DFBB` | rgb(129, 223, 187) |
| `success-400` | `bg-success-400` | `--success-400` | `hsl(157 56% 57%)` | `#54CFA0` | rgb(84, 207, 160) |
| `success-500` | `bg-success-500` | `--success-500` | `hsl(157 63% 46%)` | `#2BBF87` | rgb(43, 191, 135) |
| `success-600` | `bg-success-600` | `--success-600` | `hsl(157 100% 27%)` | `#008A55` | rgb(0, 138, 85) |
| `success-700` | `bg-success-700` | `--success-700` | `hsl(157 100% 21%)` | `#006B42` | rgb(0, 107, 66) |
| `success-800` | `bg-success-800` | `--success-800` | `hsl(157 100% 16%)` | `#005232` | rgb(0, 82, 50) |

**Info**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `info` | `bg-info` | `--info` | `hsl(214 87% 64%)` | `#5399F3` | rgb(83, 153, 243) |
| `info-100` | `bg-info-100` | `--info-100` | `hsl(217 90% 96%)` | `#ECF3FE` | rgb(236, 243, 254) |
| `info-200` | `bg-info-200` | `--info-200` | `hsl(214 86% 89%)` | `#CBE0FB` | rgb(203, 224, 251) |
| `info-300` | `bg-info-300` | `--info-300` | `hsl(214 87% 85%)` | `#B7D4FA` | rgb(183, 212, 250) |
| `info-400` | `bg-info-400` | `--info-400` | `hsl(215 87% 78%)` | `#96BFF8` | rgb(150, 191, 248) |
| `info-500` | `bg-info-500` | `--info-500` | `hsl(214 87% 71%)` | `#75ACF5` | rgb(117, 172, 245) |
| `info-600` | `bg-info-600` | `--info-600` | `hsl(215 55% 52%)` | `#4179C8` | rgb(65, 121, 200) |
| `info-700` | `bg-info-700` | `--info-700` | `hsl(214 52% 40%)` | `#315F9B` | rgb(49, 95, 155) |
| `info-800` | `bg-info-800` | `--info-800` | `hsl(215 57% 29%)` | `#204374` | rgb(32, 67, 116) |

**Warning**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `warning` | `bg-warning` | `--warning` | `hsl(34 100% 63%)` | `#FFAD42` | rgb(255, 173, 66) |
| `warning-100` | `bg-warning-100` | `--warning-100` | `hsl(33 100% 96%)` | `#FFF6EB` | rgb(255, 246, 235) |
| `warning-200` | `bg-warning-200` | `--warning-200` | `hsl(34 100% 89%)` | `#FFE7C7` | rgb(255, 231, 199) |
| `warning-300` | `bg-warning-300` | `--warning-300` | `hsl(34 100% 85%)` | `#FFDEB3` | rgb(255, 222, 179) |
| `warning-400` | `bg-warning-400` | `--warning-400` | `hsl(34 100% 78%)` | `#FFCE8F` | rgb(255, 206, 143) |
| `warning-500` | `bg-warning-500` | `--warning-500` | `hsl(34 100% 71%)` | `#FFBF6B` | rgb(255, 191, 107) |
| `warning-600` | `bg-warning-600` | `--warning-600` | `hsl(34 63% 52%)` | `#D28F37` | rgb(210, 143, 55) |
| `warning-700` | `bg-warning-700` | `--warning-700` | `hsl(34 60% 40%)` | `#A36E29` | rgb(163, 110, 41) |
| `warning-800` | `bg-warning-800` | `--warning-800` | `hsl(34 62% 35%)` | `#916122` | rgb(145, 97, 34) |

**Danger**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `danger` | `bg-danger` | `--danger` | `hsl(358 89% 64%)` | `#F55157` | rgb(245, 81, 87) |
| `danger-100` | `bg-danger-100` | `--danger-100` | `hsl(0 90% 96%)` | `#FEECEC` | rgb(254, 236, 236) |
| `danger-200` | `bg-danger-200` | `--danger-200` | `hsl(358 89% 89%)` | `#FCCACC` | rgb(252, 202, 204) |
| `danger-300` | `bg-danger-300` | `--danger-300` | `hsl(357 89% 85%)` | `#FBB7BA` | rgb(251, 183, 186) |
| `danger-400` | `bg-danger-400` | `--danger-400` | `hsl(358 89% 78%)` | `#F99598` | rgb(249, 149, 152) |
| `danger-500` | `bg-danger-500` | `--danger-500` | `hsl(358 89% 71%)` | `#F77378` | rgb(247, 115, 120) |
| `danger-600` | `bg-danger-600` | `--danger-600` | `hsl(358 56% 52%)` | `#C94045` | rgb(201, 64, 69) |
| `danger-700` | `bg-danger-700` | `--danger-700` | `hsl(358 53% 41%)` | `#A03135` | rgb(160, 49, 53) |
| `danger-800` | `bg-danger-800` | `--danger-800` | `hsl(1 61% 30%)` | `#7B1F1E` | rgb(123, 31, 30) |

**Gray**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `gray` | `bg-gray` | `--gray` | `hsl(0 0% 73%)` | `#BABABA` | rgb(186, 186, 186) |
| `gray-100` | `bg-gray-100` | `--gray-100` | `hsl(0 0% 99%)` | `#FCFCFC` | rgb(252, 252, 252) |
| `gray-200` | `bg-gray-200` | `--gray-200` | `hsl(0 0% 97%)` | `#F7F7F7` | rgb(247, 247, 247) |
| `gray-250` | `bg-gray-250` | `--gray-250` | `hsl(0 0% 96%)` | `#F5F5F5` | rgb(245, 245, 245) |
| `gray-300` | `bg-gray-300` | `--gray-300` | `hsl(0 0% 96%)` | `#F5F5F5` | rgb(245, 245, 245) |
| `gray-400` | `bg-gray-400` | `--gray-400` | `hsl(0 0% 93%)` | `#EDEDED` | rgb(237, 237, 237) |
| `gray-500` | `bg-gray-500` | `--gray-500` | `hsl(0 0% 87%)` | `#DEDEDE` | rgb(222, 222, 222) |

**Dark**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `dark` | `bg-dark` | `--dark` | `hsl(0 0% 20%)` | `#333333` | rgb(51, 51, 51) |
| `dark-100` | `bg-dark-100` | `--dark-100` | `hsl(0 0% 45%)` | `#737373` | rgb(115, 115, 115) |
| `dark-200` | `bg-dark-200` | `--dark-200` | `hsl(0 0% 40%)` | `#666666` | rgb(102, 102, 102) |
| `dark-300` | `bg-dark-300` | `--dark-300` | `hsl(0 0% 33%)` | `#545454` | rgb(84, 84, 84) |
| `dark-400` | `bg-dark-400` | `--dark-400` | `hsl(0 0% 27%)` | `#454545` | rgb(69, 69, 69) |

**White**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `white` | `bg-white` | `--white` | `hsl(0 0% 100%)` | `#FFFFFF` | rgb(255, 255, 255) |
| `white-100` | `bg-white-100` | `--white-100` | `hsl(0 0% 100%)` | `#FFFFFF` | rgb(255, 255, 255) |
| `white-200` | `bg-white-200` | `--white-200` | `hsl(0 0% 100%)` | `#FFFFFF` | rgb(255, 255, 255) |
| `white-300` | `bg-white-300` | `--white-300` | `hsl(0 0% 100%)` | `#FFFFFF` | rgb(255, 255, 255) |

**Black**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `black` | `bg-black` | `--black` | `hsl(0 0% 0%)` | `#000000` | rgb(0, 0, 0) |
| `black-force` | `bg-black-force` | `--black-force` | `hsl(0 0% 0%)` | `#000000` | rgb(0, 0, 0) |

**Mahally**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `mahally` | `bg-mahally` | `--mahally` | `hsl(11 100% 58%)` | `#FF5029` | rgb(255, 80, 41) |
| `mahally-100` | `bg-mahally-100` | `--mahally-100` | `hsl(11 100% 98%)` | `#FFF7F5` | rgb(255, 247, 245) |
| `mahally-200` | `bg-mahally-200` | `--mahally-200` | `hsl(11 100% 93%)` | `#FFE2DB` | rgb(255, 226, 219) |
| `mahally-300` | `bg-mahally-300` | `--mahally-300` | `hsl(11 100% 86%)` | `#FFC5B8` | rgb(255, 197, 184) |
| `mahally-400` | `bg-mahally-400` | `--mahally-400` | `hsl(11 100% 75%)` | `#FF9780` | rgb(255, 151, 128) |
| `mahally-500` | `bg-mahally-500` | `--mahally-500` | `hsl(11 100% 66%)` | `#FF7152` | rgb(255, 113, 82) |
| `mahally-600` | `bg-mahally-600` | `--mahally-600` | `hsl(11 73% 46%)` | `#CB3F20` | rgb(203, 63, 32) |
| `mahally-700` | `bg-mahally-700` | `--mahally-700` | `hsl(11 73% 35%)` | `#9A3018` | rgb(154, 48, 24) |

**Gold**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `gold` | `bg-gold` | `--gold` | `hsl(47 100% 79%)` | `#FFE894` | rgb(255, 232, 148) |
| `gold-100` | `bg-gold-100` | `--gold-100` | `hsl(49 100% 96%)` | `#FFFBEB` | rgb(255, 251, 235) |
| `gold-200` | `bg-gold-200` | `--gold-200` | `hsl(46 100% 90%)` | `#FFF3CC` | rgb(255, 243, 204) |
| `gold-300` | `bg-gold-300` | `--gold-300` | `hsl(47 59% 56%)` | `#D1B44D` | rgb(209, 180, 77) |
| `gold-400` | `bg-gold-400` | `--gold-400` | `hsl(47 100% 17%)` | `#574400` | rgb(87, 68, 0) |

**Orange**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `orange` | `bg-orange` | `--orange` | `hsl(21 100% 76%)` | `#FFAF85` | rgb(255, 175, 133) |
| `orange-100` | `bg-orange-100` | `--orange-100` | `hsl(21 81% 96%)` | `#FDF2ED` | rgb(253, 242, 237) |
| `orange-200` | `bg-orange-200` | `--orange-200` | `hsl(22 100% 88%)` | `#FFD8C2` | rgb(255, 216, 194) |
| `orange-300` | `bg-orange-300` | `--orange-300` | `hsl(21 85% 60%)` | `#F07F42` | rgb(240, 127, 66) |
| `orange-400` | `bg-orange-400` | `--orange-400` | `hsl(21 100% 27%)` | `#8A3000` | rgb(138, 48, 0) |

**Blue**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `blue` | `bg-blue` | `--blue` | `hsl(188 100% 79%)` | `#94F1FF` | rgb(148, 241, 255) |
| `blue-100` | `bg-blue-100` | `--blue-100` | `hsl(193 64% 96%)` | `#EEF8FB` | rgb(238, 248, 251) |
| `blue-200` | `bg-blue-200` | `--blue-200` | `hsl(195 100% 87%)` | `#BDEEFF` | rgb(189, 238, 255) |
| `blue-300` | `bg-blue-300` | `--blue-300` | `hsl(188 100% 41%)` | `#00B5D1` | rgb(0, 181, 209) |
| `blue-400` | `bg-blue-400` | `--blue-400` | `hsl(188 100% 21%)` | `#005D6B` | rgb(0, 93, 107) |

**Pink**

| Token | Tailwind | CSS variable | HSL | Hex | Computed |
|---|---|---|---|---|---|
| `pink` | `bg-pink` | `--pink` | `hsl(348 100% 78%)` | `#FF8FA5` | rgb(255, 143, 165) |
| `pink-100` | `bg-pink-100` | `--pink-100` | `hsl(345 100% 96%)` | `#FFEBF0` | rgb(255, 235, 240) |
| `pink-200` | `bg-pink-200` | `--pink-200` | `hsl(348 100% 88%)` | `#FFC2CE` | rgb(255, 194, 206) |
| `pink-300` | `bg-pink-300` | `--pink-300` | `hsl(348 81% 63%)` | `#ED5473` | rgb(237, 84, 115) |
| `pink-400` | `bg-pink-400` | `--pink-400` | `hsl(348 79% 32%)` | `#92112B` | rgb(146, 17, 43) |

### 1.2 Typography

**Font Family** — The admin UI uses PingARLT as the primary interface font.

| Class | Value |
|---|---|
| `font-sans` |  |
| `font-regular` |  |

**Font Sizes** — Tailwind text tokens backed by @salla.sa/ui-merchant-styles.

| Class | Value |
|---|---|
| `text-3xs` |  |
| `text-2xs` |  |
| `text-xs` |  |
| `text-sm` |  |
| `text-base` |  |
| `text-md` |  |
| `text-lg` |  |
| `text-xl` |  |
| `text-2xl` |  |
| `text-3xl` |  |
| `text-4xl` |  |
| `text-5xl` |  |
| `text-6xl` |  |
| `text-7xl` |  |
| `text-8xl` |  |
| `text-9xl` |  |

### 1.3 Roundness

Border-radius tokens for surfaces, cards, inputs, and panels.

| Class | Value |
|---|---|
| `rounded` | 0.25rem |
| `rounded-sm` | 0.125rem |
| `rounded-md` | 0.375rem |
| `rounded-lg` | 0.5rem |
| `rounded-xl` | 0.75rem |
| `rounded-2xl` | 1rem |
| `rounded-3xl` | 1.5rem |
| `rounded-4xl` | 2rem |

### 1.4 Shadows

Elevation tokens for layered UI, floating surfaces, and sticky areas.

| Class | Value |
|---|---|
| `shadow` | 0px 2px 4px -1px rgba(18, 18, 23, 0.06) |
| `shadow-xs` | 0px 1px 2px 0px rgba(18, 18, 23, 0.05) |
| `shadow-sm` | 0 2px 4px 0 rgba(0, 0, 0, 0.08) |
| `shadow-md` | 0 4px 6px 0 rgba(0, 0, 0, 0.12) |
| `shadow-lg` | 0px 4px 6px -2px rgba(18, 18, 23, 0.05) |
| `shadow-xl` | 0px 10px 10px -5px rgba(18, 18, 23, 0.04) |
| `shadow-2xl` | 0px 25px 50px -12px rgba(18, 18, 23, 0.25) |
| `shadow-smooth` | 0 6px 8px 0 rgba(0, 0, 0, 0.02) |
| `shadow-top` | 0px -4px 16px -4px rgba(0,0,0,0.15) |
| `shadow-bottom` | 0px 4px 16px -4px rgba(0,0,0,0.15) |

### 1.5 Global CSS variables

125 custom properties declared on `:root`.

| Variable | Value |
|---|---|
| `--action-bar-height` | `79px` |
| `--base-font-size` | `var(--font-base)` |
| `--black` | `0 0% 0%` |
| `--black-force` | `0 0% 0%` |
| `--blue` | `188 100% 79%` |
| `--blue-100` | `193 64% 96%` |
| `--blue-200` | `195 100% 87%` |
| `--blue-300` | `188 100% 41%` |
| `--blue-400` | `188 100% 21%` |
| `--breakpoint-2xl` | `1400px` |
| `--breakpoint-lg` | `1024px` |
| `--breakpoint-md` | `768px` |
| `--breakpoint-sm` | `639px` |
| `--breakpoint-xl` | `1279px` |
| `--chart-bars` | `#348d9c` |
| `--chart-bars-empty` | `#92c3cb` |
| `--chart-bars-hover` | `#ffaf44` |
| `--danger` | `358 89% 64%` |
| `--danger-100` | `0 90% 96%` |
| `--danger-200` | `358 89% 89%` |
| `--danger-300` | `357 89% 85%` |
| `--danger-400` | `358 89% 78%` |
| `--danger-500` | `358 89% 71%` |
| `--danger-600` | `358 56% 52%` |
| `--danger-700` | `358 53% 41%` |
| `--danger-800` | `1 61% 30%` |
| `--dark` | `0 0% 20%` |
| `--dark-100` | `0 0% 45%` |
| `--dark-200` | `0 0% 40%` |
| `--dark-300` | `0 0% 33%` |
| `--dark-400` | `0 0% 27%` |
| `--font-base` | `14px` |
| `--font-main` | `"PingARLT"` |
| `--gold` | `47 100% 79%` |
| `--gold-100` | `49 100% 96%` |
| `--gold-200` | `46 100% 90%` |
| `--gold-300` | `47 59% 56%` |
| `--gold-400` | `47 100% 17%` |
| `--gray` | `0 0% 73%` |
| `--gray-100` | `0 0% 99%` |
| `--gray-200` | `0 0% 97%` |
| `--gray-250` | `0 0% 96%` |
| `--gray-300` | `0 0% 96%` |
| `--gray-400` | `0 0% 93%` |
| `--gray-500` | `0 0% 87%` |
| `--info` | `214 87% 64%` |
| `--info-100` | `217 90% 96%` |
| `--info-200` | `214 86% 89%` |
| `--info-300` | `214 87% 85%` |
| `--info-400` | `215 87% 78%` |
| `--info-500` | `214 87% 71%` |
| `--info-600` | `215 55% 52%` |
| `--info-700` | `214 52% 40%` |
| `--info-800` | `215 57% 29%` |
| `--lg-height` | `3rem` |
| `--mahally` | `11 100% 58%` |
| `--mahally-100` | `11 100% 98%` |
| `--mahally-200` | `11 100% 93%` |
| `--mahally-300` | `11 100% 86%` |
| `--mahally-400` | `11 100% 75%` |
| `--mahally-500` | `11 100% 66%` |
| `--mahally-600` | `11 73% 46%` |
| `--mahally-700` | `11 73% 35%` |
| `--md-height` | `2.5rem` |
| `--moshammer` | `188 100% 79%` |
| `--moshammer-100` | `193 64% 96%` |
| `--moshammer-200` | `195 100% 87%` |
| `--moshammer-300` | `188 100% 41%` |
| `--moshammer-400` | `188 100% 21%` |
| `--moshammer-gradient` | `linear-gradient(     90deg,     #ffe894,     #ffaf85 25%,     #e4bd90 50%,     #2cf2c7 75%,     #94f1ff   )` |
| `--nav-height` | `4.5rem` |
| `--orange` | `21 100% 76%` |
| `--orange-100` | `21 81% 96%` |
| `--orange-200` | `22 100% 88%` |
| `--orange-300` | `21 85% 60%` |
| `--orange-400` | `21 100% 27%` |
| `--pink` | `348 100% 78%` |
| `--pink-100` | `345 100% 96%` |
| `--pink-200` | `348 100% 88%` |
| `--pink-300` | `348 81% 63%` |
| `--pink-400` | `348 79% 32%` |
| `--primary` | `189 100% 17%` |
| `--primary-100` | `187 40% 96%` |
| `--primary-200` | `188 39% 70%` |
| `--primary-300` | `188 38% 54%` |
| `--primary-400` | `189 50% 41%` |
| `--primary-500` | `189 100% 18%` |
| `--primary-600` | `189 100% 15%` |
| `--primary-700` | `191 76% 16%` |
| `--primary-force` | `189 100% 17%` |
| `--secondary` | `163 100% 82%` |
| `--secondary-100` | `163 100% 97%` |
| `--secondary-200` | `166 100% 95%` |
| `--secondary-300` | `165 100% 93%` |
| `--secondary-400` | `164 96% 72%` |
| `--secondary-500` | `164 89% 63%` |
| `--secondary-600` | `164 83% 55%` |
| `--secondary-700` | `163 78% 52%` |
| `--sm-height` | `2rem` |
| `--success` | `157 100% 34%` |
| `--success-100` | `155 60% 96%` |
| `--success-200` | `157 63% 75%` |
| `--success-300` | `157 59% 69%` |
| `--success-400` | `157 56% 57%` |
| `--success-500` | `157 63% 46%` |
| `--success-600` | `157 100% 27%` |
| `--success-700` | `157 100% 21%` |
| `--success-800` | `157 100% 16%` |
| `--toastify-z-index` | `2147483647` |
| `--transition-duration` | `250ms` |
| `--tw-bg-opacity` | `1` |
| `--tw-text-opacity` | `1` |
| `--warning` | `34 100% 63%` |
| `--warning-100` | `33 100% 96%` |
| `--warning-200` | `34 100% 89%` |
| `--warning-300` | `34 100% 85%` |
| `--warning-400` | `34 100% 78%` |
| `--warning-500` | `34 100% 71%` |
| `--warning-600` | `34 63% 52%` |
| `--warning-700` | `34 60% 40%` |
| `--warning-800` | `34 62% 35%` |
| `--white` | `0 0% 100%` |
| `--white-100` | `0 0% 100%` |
| `--white-200` | `0 0% 100%` |
| `--white-300` | `0 0% 100%` |

---

## 2. Components

| # | Component | Tag | Stories | Props |
|---|---|---|---|---|
| 1 | Accordion | `<s-accordion>` | 14 | 13 |
| 2 | AlertBox | `<s-alert-box>` | 11 | 5 |
| 3 | Avatar | `<s-avatar>` | 16 | 16 |
| 4 | Breadcrumbs | `<s-breadcrumbs>` | 5 | 4 |
| 5 | Button | `<s-button>` | 15 | 18 |
| 6 | ButtonsGroup | `<s-buttons-group>` | 7 | 1 |
| 7 | Calendar | `<s-calendar>` | 28 | 17 |
| 8 | Checkbox | `<s-checkbox>` | 14 | 13 |
| 9 | ColorPicker | `<s-color-picker>` | 6 | 6 |
| 10 | Dropdown | `<s-dropdown>` | 13 | 15 |
| 11 | Editor | `<s-editor>` | 12 | 19 |
| 12 | Icon | `<s-icon>` | 1 | 2 |
| 13 | IconPicker | `<s-icon-picker>` | 12 | 14 |
| 14 | Input | `<s-input>` | 17 | 21 |
| 15 | Item | `<s-list-item>` | 1 | 1 |
| 16 | LingualField | `<s-lingual-field>` | 18 | 22 |
| 17 | Loader | `<s-loader>` | 1 | 2 |
| 18 | Maps | `<s-maps>` | 4 | 6 |
| 19 | Modal | `<s-modal>` | 1 | 3 |
| 20 | OTP | `<s-otp>` | 8 | 6 |
| 21 | Panel | `<s-panel>` | 6 | 8 |
| 22 | Placeholder | `<s-placeholder>` | 3 | 5 |
| 23 | Progress Bar | `<s-progress-bar>` | 6 | 8 |
| 24 | Qty | `<s-qty>` | 9 | 12 |
| 25 | Radio | `<s-radio>` | 15 | 14 |
| 26 | Range Slider | `<s-range-slider>` | 5 | 7 |
| 27 | Rate | `<s-rate>` | 9 | 9 |
| 28 | Select | `<s-select>` | 29 | 29 |
| 29 | Skeleton | `<s-skeleton>` | 14 | 1 |
| 30 | Table | `<s-table>` | 9 | 19 |
| 31 | Tabs | `<s-tabs-group>` | 5 | 5 |
| 32 | Tag | `<s-tag>` | 13 | 9 |
| 33 | Tags Input | `<s-tags>` | 6 | 10 |
| 34 | Telephone Input | `<s-tel-input>` | 4 | 7 |
| 35 | Textarea | `<s-textarea>` | 9 | 14 |
| 36 | Toggle | `<s-toggle>` | 11 | 12 |
| 37 | Tooltip | `<s-tooltip>` | 27 | 5 |
| 38 | Uploader | `<s-uploader>` | 21 | 33 |

---

### 2.1 Accordion

**Tag:** `<s-accordion>`  ·  **Related elements:** `<s-accordion-group>`  
**Storybook:** `components-accordion` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-accordion>

A collapsible content container that provides large amounts of content in a small space through progressive disclosure. Users get the essential details about the core content and can choose to expand this content within the constraints of the accordion.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `activeTab` | number | number | `0` |  | Initially active tab index |
| `autoCollapse` |  | boolean | `true` |  | AutoCollapse other accordions in the same group when one is expanded |
| `disabled` | boolean | boolean | `false` |  | Disable accordion |
| `feature` |  | boolean | `true` |  | Feature based dependency accordion |
| `flatHeader` |  | boolean | `false` |  | Removes the expand/collapse icon from header, needed in certain cases |
| `headerPadding` |  | text | `""` |  | Sets custom padding for the accordion header, set value as string like '1rem' or '16px 20px' |
| `isExpanded` |  | boolean | `false` |  | If you need accordion to be expanded by default |
| `layout` |  | select | `default` | default, tight, relaxed | You can set accordion layout to tight or relaxed if you have small area |
| `loading` | boolean | boolean | `false` |  | Accordion loading state |
| `maxHeight` |  | text | `auto` |  | You can set max height for accordion body, will be scrollable when content is more than max height, set value as string like '200px' |
| `outlined` | boolean | boolean | `false` |  | Adds an outline border to the accordion |
| `readonly` |  | boolean | `false` |  | Readonly state |
| `theme` | string | select | `default` | default, light, transparent, feature | Accordion theme, you can set theme to light, transparent or feature if you need feature based dependency accordion |

**Events**

| Event | Description |
|---|---|
| `accordionToggle` | Emitted when the accordion is toggled. Provides event object with the state of the accordion. |
| `onchange` | Emitted when the active tab changes. Provides the index of the new active tab. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-accordion--default` | theme="default", outlined=true, loading=false, disabled=false, activeTab=0 |
| Light | `components-accordion--light` | theme="light", outlined=false, loading=false, disabled=false, activeTab=0 |
| Transparent | `components-accordion--transparent` | theme="transparent", outlined=false, loading=false, disabled=false, activeTab=0 |
| Feature | `components-accordion--feature` | theme="feature", outlined=true, loading=false, disabled=false, activeTab=0 |
| Tight | `components-accordion--tight` | theme="default", outlined=true, loading=false, disabled=false, activeTab=0 |
| Relaxed | `components-accordion--relaxed` | theme="default", outlined=true, loading=false, disabled=false, activeTab=0 |
| Loading | `components-accordion--loading` | theme="default", outlined=true, loading=true, disabled=false, activeTab=0 |
| Disabled | `components-accordion--disabled` | theme="default", outlined=true, loading=false, disabled=true, activeTab=0 |
| Expanded | `components-accordion--expanded` | theme="default", outlined=true, loading=false, disabled=false, activeTab=0 |
| Outlined | `components-accordion--outlined` | theme="default", outlined=true, loading=false, disabled=false, activeTab=0 |
| Max Height | `components-accordion--max-height` |  |
| Grouped | `components-accordion--grouped` |  |
| Nested | `components-accordion--nested` |  |
| Read Only | `components-accordion--read-only` |  |

**Rendered markup — “Default”**

```html
<s-accordion theme="default" outlined="" active-tab="0" class="hydrated">
  <div slot="head">Accordion Title</div>
  <div slot="body">The accordion component provides large amounts of content in a small space through progressive disclosure. Users get the essential details about the core content and can choose to expand this content within the constraints of the accordion.</div>
</s-accordion>
```

---

### 2.2 AlertBox

**Tag:** `<s-alert-box>`  ·  **Related elements:** `<s-alert-box-action>`  
**Storybook:** `components-alertbox` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-alertbox>

A message box provides contextual feedback to users. It can be used to display success, warning, error, or info messages.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `centerAlign` |  | boolean |  |  | set to true to center the alert box content |
| `closable` | boolean | boolean | `false` |  | Show close button, if you want user to to be able to close the alert box |
| `horizontal` |  | boolean |  |  | If true, the alert box will be displayed in a horizontal layout. |
| `layout` | string | select | `default` | default, flat | Alert box Layout, you can set layout to default or flat |
| `theme` | string | select | `default` | default, secondary, danger, warning, info, feature | Alert box Theme, you can set theme to default, secondary, danger, warning, info or feature |

**Events**

| Event | Description |
|---|---|
| `onclick` | Emitted when the alert box is clicked. |
| `onclose` | Emitted when the alert box is closed. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-alertbox--default` | theme="default", layout="default", closable=false |
| Secondary | `components-alertbox--secondary` | theme="secondary", layout="default", closable=false |
| Danger | `components-alertbox--danger` | theme="danger", layout="default", closable=false |
| Warning | `components-alertbox--warning` | theme="warning", layout="default", closable=false |
| Info | `components-alertbox--info` | theme="info", layout="default", closable=false |
| Feature | `components-alertbox--feature` | theme="feature", layout="default", closable=false |
| Flat | `components-alertbox--flat` | theme="default", layout="flat", closable=false |
| Closable | `components-alertbox--closable` | theme="default", layout="default", closable=true |
| Horizontal | `components-alertbox--horizontal` | horizontal=true |
| Center Align | `components-alertbox--center-align` | centerAlign=true |
| Custom Slot | `components-alertbox--custom-slot` |  |

**Rendered markup — “Default”**

```html
<s-alert-box theme="default" layout="default" class="s-alert-box s-alert-box--default default ltr hydrated">
  <i slot="icon" class="hgi-stroke hgi-alert-02">
  </i>
  <h4 slot="title">AlertBox Title</h4>
  <article slot="desc">
    <p>This is a default alert description.</p>
  </article>
  <div slot="action">
    <s-alert-box-action slot="action" layout="btn" theme="default" href="https://example.com" target="_blank" class="hydrated">Primary Action</s-alert-box-action>
    <s-alert-box-action slot="action" layout="outlined" theme="default" href="https://example.com" target="_blank" class="hydrated">Secondary Action</s-alert-box-action>
  </div>
</s-alert-box>
```

---

### 2.3 Avatar

**Tag:** `<s-avatar>`  
**Storybook:** `components-avatar` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-avatar>

An avatar is a graphical representation of a user, typically a photo or icon, used to represent a person or entity in a user interface.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `desc` | string | text |  |  | Description displayed below avatar label |
| `icon` |  | text |  |  | If you want to show an icon instead of an image, we are using huge icons, so you can use icons classes here like `hgi-stroke hgi-user-multiple-02` |
| `iconSize` |  | text | `md` |  | Custom icon size |
| `imageFit` |  | select | `cover` | cover, contain, fit | Image fit type, cover, contain, fit |
| `initials` |  | boolean | `false` |  | If you want to show initials instead of an image, you can use this property |
| `initialsLabel` |  | text | `undefined` |  | Custom text to extract initials from when initials=true. If not provided, will use the label prop. Supports 1-2 characters for direct display or longer text for auto-extraction. |
| `isActive` |  | boolean | `false` |  | adds an active indicator to the avatar image to show that the user is active |
| `label` | string | text |  |  | Label displayed next to avatar image |
| `layout` | string | select | `circular` | circular, rounded | Layout variant, you can use either circular, rounded |
| `loading` | boolean | boolean | `false` |  | Shows loading state for the avatar |
| `outlined` | boolean | boolean | `false` |  | You can also add outline to the avatar image |
| `responsive` |  | boolean | `false` |  | If set to true, label and description will be hidden on mobile only avatar image will be visible |
| `shadow` | boolean | boolean | `false` |  | You can add shadow to the avatar image |
| `size` | string | select | `md` | xs, sm, md, lg | Avatar size |
| `status` |  | select | `undefined` | None, info, success, warning, danger | Predefined status badge shown on the avatar thumbnail. Adds a colored icon badge and a matching border to the thumb. |
| `url` | string | text |  |  | Image URL |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-avatar--default` | url="https://i.pravatar.cc/100", label="James Bond", desc="Special agent 007", layout="circular", size="md" |
| Circular | `components-avatar--circular` | url="https://i.pravatar.cc/100", label="James Bond", desc="Special agent 007", layout="circular", size="md" |
| Rounded | `components-avatar--rounded` | url="https://i.pravatar.cc/100", label="James Bond", desc="Special agent 007", layout="rounded", size="md" |
| Initials | `components-avatar--initials` |  |
| Icons | `components-avatar--icons` | label="James Bond", desc="Special agent 007", icon="hgi-stroke hgi-store-verified-01", iconSize="md", size="md" |
| Icon Size Variants | `components-avatar--icon-size-variants` | label="James Bond", desc="Special agent 007", icon="hgi-stroke hgi-store-verified-01" |
| Shadow And Outline | `components-avatar--shadow-and-outline` |  |
| Image Cover Fit | `components-avatar--image-cover-fit` | url="https://i.pravatar.cc/100", label="James Bond", desc="Special agent 007", layout="rounded", size="md" |
| Image Contain Fit | `components-avatar--image-contain-fit` | url="https://i.pravatar.cc/100", label="James Bond", desc="Special agent 007", layout="rounded", size="md" |
| Size Variations | `components-avatar--size-variations` |  |
| Loading State | `components-avatar--loading-state` | url="https://i.pravatar.cc/100", label="James Bond", desc="Special agent 007", layout="rounded", size="md" |
| Active State | `components-avatar--active-state` |  |
| Responsive | `components-avatar--responsive` | url="https://i.pravatar.cc/100", label="James Bond", desc="Special agent 007", layout="rounded", size="md" |
| Without Thumbnail | `components-avatar--without-thumbnail` | label="James Bond", desc="Special agent 007" |
| Status Badge | `components-avatar--status-badge` | url="https://i.pravatar.cc/100", label="James Bond", desc="Special agent 007", layout="circular", size="md" |
| Status Variants | `components-avatar--status-variants` |  |

**Rendered markup — “Default”**

```html
<s-avatar label="James Bond" desc="Special agent 007" layout="circular" size="md" url="https://i.pravatar.cc/100" class="s-avatar s-avatar--circular s-avatar--horizontal ltr md hydrated">
</s-avatar>
```

---

### 2.4 Breadcrumbs

**Tag:** `<s-breadcrumbs>`  
**Storybook:** `components-breadcrumbs` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-breadcrumbs>

A breadcrumb is a navigation component that allows users to track their location within a website or application.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `isOnClick` | boolean | boolean | `false` |  | Specifies if the breadcrumbs are clickable, if true, the breadcrumbClick event will be emitted |
| `items` | string | text | `[]` |  | Breadcrumbs items |
| `loading` | boolean | boolean | `false` |  | Specifies if the breadcrumbs are in a loading state |
| `maxVisibleItems` | number | number | `5` |  | Maximum number of visible items, the rest will be hidden in a dropdown |

**Events**

| Event | Description |
|---|---|
| `breadcrumbClick` | Emitted when a breadcrumb is clicked. Provides the clicked breadcrumb value. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-breadcrumbs--default` | items="[{\"id\":0,\"label\":\"Home\",\"route\", loading=false, maxVisibleItems=5, isOnClick=false |
| Array Format | `components-breadcrumbs--array-format` | items=[{"id": 0, "label": "Home", "route": "/", loading=false, maxVisibleItems=5, isOnClick=false |
| Max Visible Items | `components-breadcrumbs--max-visible-items` | items="[{\"id\":0,\"label\":\"Home\",\"route\", maxVisibleItems=3, loading=false, isOnClick=false |
| Loading | `components-breadcrumbs--loading` | items="[{\"id\":0,\"label\":\"Home\",\"route\", loading=true, maxVisibleItems=5, isOnClick=false |
| With Click Handler | `components-breadcrumbs--with-click-handler` | items="[{\"id\":0,\"label\":\"Home\",\"route\", isOnClick=true, loading=false, maxVisibleItems=5 |

**Rendered markup — “Default”**

```html
<s-breadcrumbs items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Home&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Category&quot;,&quot;route&quot;:&quot;/category&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Subcategory&quot;,&quot;route&quot;:&quot;/subcategory&quot;}]" max-visible-items="5" class="s-breadcrumbs ltr hydrated">
</s-breadcrumbs>
```

---

### 2.5 Button

**Tag:** `<s-button>`  ·  **Related elements:** `<s-icon>`  
**Storybook:** `components-button` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-button>

A button is a clickable element that triggers an action when clicked.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `active` |  | boolean | `false` |  | Set to true to get an active button state |
| `autoHeight` |  | boolean | `false` |  | If the button should have auto height instead of pre-defined height, better used with transparent theme if needed |
| `disabled` |  | boolean | `false` |  | Disable the button |
| `feature` |  | boolean | `false` |  | Feature based button |
| `href` |  | text | `null` |  | if applied, the button will behave as a link and will have a href attribute |
| `label` | string | text | `null` |  | you can dynamically set the label of the button if needed |
| `layout` |  | select | `default` | default, circular | Button layout variant, you can default or circular, for circular button, best to use style prop to set the width and height sizes to get a perfect circle |
| `loading` |  | boolean | `false` |  | Loading state |
| `noPadding` |  | boolean | `false` |  | Remove button padding |
| `outlined` |  | boolean | `false` |  | Set to true to get an outlined button |
| `shadow` |  | boolean | `false` |  | Add shadow to the button |
| `size` |  | select | `md` | sm, md, lg | Button size |
| `style` | string | text |  |  |  |
| `target` |  | select | `_self` | _blank, _self, _parent, _top | target attribute for the button if it is a link |
| `textAlignment` |  | select | `center` | start, center, end | Text alignment within the button |
| `theme` |  | select | `default` | default, primary, secondary, danger, warning, info, white, transparent, feature, mahally,  | Button theme |
| `type` |  | select | `button` | button, submit, reset | Button type, you can use button, submit or reset (optional) |
| `wide` |  | boolean | `false` |  | Make button fill container width |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-button--default` | label="Click here to learn more" |
| Theme Variants | `components-button--theme-variants` | label="Click here to learn more" |
| Size Variants | `components-button--size-variants` | label="Click here to learn more" |
| Outlined Variants | `components-button--outlined-variants` | label="Click here to learn more" |
| Loading | `components-button--loading` | label="Click here to learn more", style="width: 3.75rem;", loading=true |
| Disabled | `components-button--disabled` | label="Click here to learn more", disabled=true |
| Active | `components-button--active` | label="Click here to learn more", active=true |
| Wide | `components-button--wide` | label="Click here to learn more", wide=true |
| Text Start | `components-button--text-start` | label="Click here to learn more", wide=true, textAlignment="start" |
| Text End | `components-button--text-end` | label="Click here to learn more", wide=true, textAlignment="end" |
| Has Icons | `components-button--has-icons` | label="<s-icon icon=\"hgi-stroke hgi-user\"></ |
| Circular | `components-button--circular` | label="<s-icon icon=\"hgi-stroke hgi-help-circ, style="width: 3.75rem; height: 3.75rem;", layout="circular" |
| Link | `components-button--link` | label="Click here to learn more", href="https://www.salla.com", target="_blank" |
| Auto Height | `components-button--auto-height` | label="Click here to learn more", theme="transparent", autoHeight=true |
| Feature | `components-button--feature` | label="Click here to learn more", theme="feature" |

**Rendered markup — “Default”**

```html
<s-button default="" class="s-btn s-btn--default default md ltr hydrated" theme="default" target="_self">Click here to learn more</s-button>
```

---

### 2.6 ButtonsGroup

**Tag:** `<s-buttons-group>`  ·  **Related elements:** `<s-button>`, `<s-dropdown>`  
**Storybook:** `components-buttonsgroup` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-buttonsgroup>

A buttons group is a container that groups related buttons together, providing visual cohesion and proper spacing.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `layout` |  | select | `horizontal` | horizontal | Layout direction of the buttons group, currently only horizontal is supported.. vertical will be supported soon |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-buttonsgroup--default` |  |
| Button Count Variants | `components-buttonsgroup--button-count-variants` |  |
| Theme Variants | `components-buttonsgroup--theme-variants` |  |
| With Dropdown | `components-buttonsgroup--with-dropdown` |  |
| Dropdown In Middle | `components-buttonsgroup--dropdown-in-middle` |  |
| Buttons With Icons | `components-buttonsgroup--buttons-with-icons` |  |
| With Disabled States | `components-buttonsgroup--with-disabled-states` |  |

**Rendered markup — “Default”**

```html
<s-buttons-group class="s-btn-group s-btn-group--horizontal hydrated">
  <s-button theme="white" outlined="" class="s-btn s-btn--white default md outlined ltr hydrated s-btn-group-item s-btn-group-item--start" target="_self">First Button</s-button>
  <s-button theme="white" outlined="" class="s-btn s-btn--white default md outlined ltr hydrated s-btn-group-item s-btn-group-item--end" target="_self">Second Button</s-button>
</s-buttons-group>
```

---

### 2.7 Calendar

**Tag:** `<s-calendar>`  
**Storybook:** `components-calendar` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-calendar>

Calendar is a component that provides date or time selection functionality.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `dateFormat` |  | text | `DD-MM-YYYY` |  | Format used for displaying/parsing dates and disabledDates (e.g. 'DD-MM-YYYY', 'YYYY-MM-DD'). |
| `disabled` |  | boolean | `false` |  | Disabled state |
| `disabledDates` |  | object | `[]` |  | Specific dates to disable. Must match the selected dateFormat. Example (DD-MM-YYYY): ['07-09-2025', '10-09-2025'] |
| `disabledDays` |  | object | `[]` |  | Weekdays to disable selection for. 0 = Sunday, 6 = Saturday. Accepts numbers (0–6) or day names/abbreviations, e.g. ['sun', 'monday'] |
| `hasError` |  | boolean | `false` |  | Error state |
| `inline` |  | boolean | `false` |  | Inline calendar |
| `is24Hr` |  | boolean | `false` |  | Enable 24 hour format |
| `isOpen` |  | boolean | `false` |  | Open calendar popup on start (only works when inline is false) |
| `layout` |  | select | `start` | start, end | Calendar layout |
| `loading` |  | boolean | `false` |  | Loading state |
| `maxDate` |  | text | `null` |  | Maximum date selectable |
| `minDate` |  | text | `null` |  | Minimum date selectable |
| `placeholder` | string | text | `Select value` |  | Field placeholder |
| `portal` |  | boolean | `false` |  | If true, appends the calendar dropdown to the body instead of attaching it to the input. Useful for avoiding overflow issues in containers with overflow: hidden. |
| `required` |  | boolean | `false` |  | Required field |
| `type` |  | select | `single` | range, time, single, multiple | Calendar type, range, time, single or multiple |
| `value` |  | text | `[]` |  | Current value of the calendar (string or array of strings) for multiple values |

**Events**

| Event | Description |
|---|---|
| `dateRangeChanged` | Emitted when the date range changes. |
| `valueChanged` | Emitted when the calendar value changes. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-calendar--default` | placeholder="Select value" |
| Single | `components-calendar--single` | placeholder="Select a single date", type="single" |
| Multiple | `components-calendar--multiple` | placeholder="Select multiple dates", type="multiple" |
| Range | `components-calendar--range` | placeholder="Select date range", type="range" |
| Time | `components-calendar--time` | placeholder="Select time", type="time" |
| Initial Value | `components-calendar--initial-value` | placeholder="Select value", value="2023-12-15" |
| Multiple Values | `components-calendar--multiple-values` | placeholder="Select value", type="multiple", value=["2023-12-15", "2023-12-20"] |
| Layout End | `components-calendar--layout-end` | placeholder="Select value", layout="end" |
| Min Max Date | `components-calendar--min-max-date` | placeholder="Select value", minDate="2025-07-28", maxDate="2025-08-28" |
| Hour Format | `components-calendar--hour-format` | placeholder="Select value", is24Hr=true |
| Loading | `components-calendar--loading` | placeholder="Loading...", loading=true |
| Disabled | `components-calendar--disabled` | placeholder="Select value", disabled=true |
| Has Error | `components-calendar--has-error` | placeholder="Select value", hasError=true |
| Required | `components-calendar--required` | placeholder="Select value", required=true |
| Inline | `components-calendar--inline` | placeholder="Select value", inline=true |
| Disabled Weekends | `components-calendar--disabled-weekends` | placeholder="Select value (Weekends disabled)", disabledDays=[0, 6] |
| Disabled Weekdays | `components-calendar--disabled-weekdays` | placeholder="Select value (Weekdays disabled)", disabledDays=[1, 2, 3, 4, 5] |
| Disabled Specific Days | `components-calendar--disabled-specific-days` | placeholder="Select value (Wed, Fri disabled)", disabledDays=[3, 5] |
| Disabled Specific Dates | `components-calendar--disabled-specific-dates` | placeholder="Select value (Specific dates disabled)", dateFormat="DD-MM-YYYY", disabledDates=["07-09-2025", "10-09-2025"] |
| Disabled Dates Custom Format | `components-calendar--disabled-dates-custom-format` | placeholder="Select value (Custom format & disabled , dateFormat="YYYY-MM-DD", disabledDates=["2025-09-07", "2025-09-10"] |
| Disabled Days And Dates Combined | `components-calendar--disabled-days-and-dates-combined` | placeholder="Weekends + specific dates disabled", disabledDays=[0, 6], dateFormat="DD-MM-YYYY", disabledDates=["15-09-2025"] |
| Disabled Days With Names | `components-calendar--disabled-days-with-names` | placeholder="Select value (Sun, Mon disabled)", disabledDays=["sunday", "monday"] |
| Disabled Days With Abbreviations | `components-calendar--disabled-days-with-abbreviations` | placeholder="Select value (Tue, Thu disabled)", disabledDays=["tue", "thu"] |
| Disabled Days Mixed | `components-calendar--disabled-days-mixed` | placeholder="Select value (Mixed format)", disabledDays=[0, "wednesday", "fri"] |
| Disabled Days Inline | `components-calendar--disabled-days-inline` | placeholder="Select value", inline=true, disabledDays=[0, 6] |
| Disabled Days Range | `components-calendar--disabled-days-range` | placeholder="Select date range (Weekends disabled)", type="range", disabledDays=[0, 6] |
| Disabled Days Multiple | `components-calendar--disabled-days-multiple` | placeholder="Select multiple dates (Wed, Fri disable, type="multiple", disabledDays=[3, 5] |
| Open On Start | `components-calendar--open-on-start` | placeholder="Calendar opens on start", isOpen=true |

**Rendered markup — “Default”**

```html
<s-calendar placeholder="Select value" class="s-calendar date ltr start hydrated">
  <i class="hgi-stroke hgi-calendar-03" slot="start">
  </i>
</s-calendar>
```

---

### 2.8 Checkbox

**Tag:** `<s-checkbox>`  
**Storybook:** `components-checkbox` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-checkbox>

A checkbox is a form element that allows users to select one or more options from a list. It is commonly used in forms to gather user preferences or choices.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `checked` | boolean | boolean | `false` |  | Checked state |
| `desc` | string | text |  |  | Checkbox description |
| `direction` | string | select | `col` |  | Sets the layout direction, col or row, with default col |
| `disabled` | boolean | boolean | `false` |  | Disabled state |
| `feature` | boolean | boolean | `true` |  | Feature based state |
| `hasError` | boolean | boolean | `false` |  | Checkbox error state |
| `indeterminate` |  | boolean | `false` |  | IF the checkbox is partially selected |
| `items` |  | text | `[]` |  | Multiple Checkbox value |
| `label` | string | text |  |  | Checkbox label |
| `loading` |  | boolean | `false` |  | Replaces every option with a skeleton placeholder so the row height is preserved during data fetches. Per-option loading is supported via `loading: true` on an individual item. |
| `readonly` | boolean | boolean | `false` |  | Freezes the value without the disabled styling — the box keeps its normal contrast and the input never receives the `disabled` attribute. |
| `required` | boolean | boolean | `false` |  | If the checkbox is required |
| `value` |  | text |  |  | Single Checkbox value |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the checkbox value changes. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-checkbox--default` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=false, disabled=false, readonly=false |
| Checked | `components-checkbox--checked` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=false, disabled=false, readonly=false |
| Indeterminate | `components-checkbox--indeterminate` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=false, disabled=false, readonly=false |
| Group Options | `components-checkbox--group-options` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=true, disabled=false, readonly=false |
| Row Direction | `components-checkbox--row-direction` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=true, disabled=false, readonly=false |
| Exclusive Option | `components-checkbox--exclusive-option` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=false, disabled=false, readonly=false |
| Required | `components-checkbox--required` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=true, disabled=false, readonly=false |
| Feature Based | `components-checkbox--feature-based` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=false, disabled=false, readonly=false |
| Disabled | `components-checkbox--disabled` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=false, disabled=true, readonly=false |
| Readonly | `components-checkbox--readonly` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=false, disabled=false, readonly=true |
| Disabled Item | `components-checkbox--disabled-item` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=false, disabled=false, readonly=false |
| Loading | `components-checkbox--loading` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=false, disabled=false, readonly=false |
| Loading Item | `components-checkbox--loading-item` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=false, disabled=false, readonly=false |
| Has Error | `components-checkbox--has-error` | label="Accept terms and conditions", desc="I agree to the terms and conditions", required=false, disabled=false, readonly=false |

**Rendered markup — “Default”**

```html
<s-checkbox label="Accept terms and conditions" desc="I agree to the terms and conditions" direction="col" feature="true" @valuechanged="ev=&gt;console.log(" value="" changed:",ev.detail)"="" class="s-checkbox ltr hydrated">
</s-checkbox>
```

---

### 2.9 ColorPicker

**Tag:** `<s-color-picker>`  ·  **Related elements:** `<s-icon>`  
**Storybook:** `components-colorpicker` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-colorpicker>

A color picker field component that allows users to select colors using a color input. It supports various states and configurations for different use cases.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `disabled` |  | boolean | `false` |  | Disabled state |
| `hasError` |  | boolean | `false` |  | Error state |
| `noBorder` |  | boolean | `false` |  | Border-less field ( required in certain cases) |
| `noLabel` |  | boolean | `false` |  | Label-less field ( required in certain cases) |
| `required` |  | boolean | `false` |  | Required state |
| `value` | string | color | `#000000` |  | Field value |

**Events**

| Event | Description |
|---|---|
| `colorChanged` | Emitted when the color changes. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-colorpicker--default` | value="#000000" |
| Initial Value | `components-colorpicker--initial-value` | value="#ab1c1c" |
| Has Error | `components-colorpicker--has-error` | value="#000000", hasError=true |
| Label Less | `components-colorpicker--label-less` | value="#000000", noLabel=true |
| Border Less | `components-colorpicker--border-less` | value="#000000", noBorder=true |
| Disabled | `components-colorpicker--disabled` | value="#000000", disabled=true |

**Rendered markup — “Default”**

```html
<s-color-picker value="#000000" @colorchanged="ev=&gt;console.log(" color="" changed:",ev.detail)"="" class="ltr hydrated">
  <s-icon icon="hgi-stroke hgi-color-picker" slot="start" class="hydrated">
  </s-icon>
</s-color-picker>
```

---

### 2.10 Dropdown

**Tag:** `<s-dropdown>`  ·  **Related elements:** `<s-button>`  
**Storybook:** `components-dropdown` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-dropdown>

A dropdown component that displays a list of selectable items. It supports various states, search functionality, and different toggle elements.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `active` |  | boolean | `false` |  | Active state of the dropdown |
| `autoComplete` |  | boolean | `false` |  | Enables autocomplete functionality |
| `children` | string | text |  |  |  |
| `disabled` |  | boolean | `false` |  | Disabled state |
| `isOnClick` |  | boolean | `false` |  | Enables click event handling |
| `items` | array | object | `[]` |  | Items for the dropdown menu |
| `layout` |  | select | `start` | start, end, expanded | Dropdown layout |
| `loading` |  | boolean | `false` |  | Loading state |
| `multiselect` |  | boolean | `false` |  | Enables multiple item selection |
| `overlayAlignment` |  | select | `start` | start, end | Horizontal alignment preference for the dropdown overlay |
| `searchPlaceholder` |  | text | `undefined` |  | Placeholder text for the search input |
| `searchQuery` |  | text | `undefined` |  | Initial search query |
| `searchable` |  | boolean | `false` |  | Enables search functionality |
| `selectable` |  | boolean | `false` |  | Enables item selection |
| `sheetTitle` |  | text |  |  | Optional title shown in the mobile sheet header |

**Events**

| Event | Description |
|---|---|
| `itemClick` | Event emitted when an item in the dropdown is clicked. Provides the item's route or identifier. |
| `onclick` | Event emitted when the dropdown toggle button is clicked. This is the main click event for opening/closing the dropdown. |
| `onclose` | Event emitted when the dropdown menu is closed. Useful for tracking dropdown visibility state and cleanup operations. |
| `onopen` | Event emitted when the dropdown menu is opened. Useful for tracking dropdown visibility state. |
| `onselected` | Event emitted when an item is selected in the dropdown. Provides comprehensive information about the selected item including id, label, value, and icon. |
| `searchValueChange` | Event emitted when the search input value changes (only when searchable or autocomplete is enabled). Useful for implementing custom search logic or autocomplete functionality. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-dropdown--default` | items=[{"id": 0, "label": "Sort Items", "value |
| Selectable | `components-dropdown--selectable` | items=[{"id": 0, "label": "Sort Items", "value, selectable=true |
| Searchable | `components-dropdown--searchable` | items=[{"id": 0, "label": "Sort Items", "value, searchable=true, searchPlaceholder="Search for items..." |
| Layout Start | `components-dropdown--layout-start` | items=[{"id": 0, "label": "Sort Items", "value, layout="start" |
| Layout End | `components-dropdown--layout-end` | items=[{"id": 0, "label": "Sort Items", "value, layout="end" |
| Overlay Alignment End | `components-dropdown--overlay-alignment-end` | items=[{"id": 0, "label": "Sort Items", "value, overlayAlignment="end", searchable=true |
| Layout Expanded | `components-dropdown--layout-expanded` | items=[{"id": 0, "label": "Sort Items", "value, layout="expanded" |
| Multiselect | `components-dropdown--multiselect` | items=[{"id": 0, "label": "Sort Items", "value, multiselect=true |
| With Images | `components-dropdown--with-images` | selectable=true, items=[{"id": 0, "label": "Avatar (s-avatar)", |
| With Descriptions | `components-dropdown--with-descriptions` | selectable=true, sheetTitle="Add file", items=[{"id": 0, "label": "Upload file", "desc |
| Custom Toggle | `components-dropdown--custom-toggle` | items=[{"id": 0, "label": "Sort Items", "value, children="\n      <span data-toggle=\"true\" slot |
| Loading | `components-dropdown--loading` | items=[{"id": 0, "label": "Sort Items", "value, loading=true |
| Disabled | `components-dropdown--disabled` | items=[{"id": 0, "label": "Sort Items", "value, disabled=true |

**Rendered markup — “Default”**

```html
<s-dropdown layout="start" items="[{&quot;id&quot;:0,&quot;label&quot;:&quot;Sort Items&quot;,&quot;value&quot;:&quot;sort&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-sorting-01&quot;},{&quot;id&quot;:1,&quot;label&quot;:&quot;Copy Items&quot;,&quot;value&quot;:&quot;copy&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-copy-01&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:2,&quot;label&quot;:&quot;Export Items&quot;,&quot;value&quot;:&quot;export&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-share-05&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:3,&quot;label&quot;:&quot;Delete Items&quot;,&quot;value&quot;:&quot;delete&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-delete-02&quot;,&quot;route&quot;:&quot;/&quot;},{&quot;id&quot;:4,&quot;label&quot;:&quot;Settings&quot;,&quot;value&quot;:&quot;settings&quot;,&quot;icon&quot;:&quot;hgi-stroke hgi-settings-01&quot;}]" class="start ltr hydrated">
  <s-button data-toggle="true" slot="dropdown-head" outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">
    <i class="hgi-stroke h
<!-- … truncated … -->
```

---

### 2.11 Editor

**Tag:** `<s-editor>`  ·  **Related elements:** `<s-editor-toolbar>`, `<s-dropdown>`, `<s-button>`, `<s-icon>`  
**Storybook:** `components-editor` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-editor>

A rich text editor component that provides a comprehensive toolbar for content creation and editing. It supports various formats, multilingual content, and preview functionality.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `aiSuggestion` |  | object | `undefined` |  | AI suggestion config (object or JSON string): { enabled, regenerable, source }. When `enabled`, the editor gets the Moshammer AI highlight and overlays the `actions` slot (regenerate / dismiss) at the top of the content area. |
| `demoImagePicker` |  | boolean | `undefined (native file picker)` |  | Story-only. Wires a stub `imagePicker` so the toolbar image button opens it instead of the native file picker. `imagePicker` itself is a function prop and has no Storybook control. |
| `desc` |  | text | `undefined` |  | Description text for the editor |
| `disabled` |  | boolean | `false` |  | Disabled state |
| `format` |  | select | `html` | html, text, json | Output format of the editor content |
| `fullToolbar` | boolean | boolean | `false` |  | Editor full toolbar |
| `hasError` |  | boolean | `false` |  | Error state |
| `hasPreview` |  | boolean | `false` |  | Enable editor preview |
| `hideToolbar` |  | boolean | `false` |  | Render the editor without its toolbar. Also moves the `end` slot in flow, since there is no toolbar row left to overlay. |
| `max` |  | number | `undefined` |  | Maximum Characters |
| `min` |  | number | `undefined` |  | Minimum Characters |
| `multilingual` |  | boolean | `false` |  | Enables multilingual support, if true, the editor will be able to handle multiple languages, the language will be detected automatically based on merchant supported languages |
| `placeholder` | string | text | `Editor placeholder` |  | Editor placeholder |
| `productEmbed` |  | object | `undefined (disabled)` |  | Enable product embeds in the editor. Pass true for the default products API, or an object with endpoint (and optional searchParam / transform). |
| `required` |  | boolean | `false` |  | Required state |
| `server` | object | object | `Default server config with type: 'products'` |  | Server configuration including upload type (crucial for each app context) |
| `showCount` |  | boolean | `false` |  | Show a live `current/max` character counter below the editor. Requires `max`. Counter follows the document direction so it stays anchored when the editor's own dir flips for per-language RTL. Turns danger-red under `has-error`. |
| `toolbar` | array | object | `[["bold","italic","underline","strike"],[{"direction":"rtl"},{"align":[]},{"list":"ordered"},{"list":"bullet"}],[{"header":1},{"header":2},{"header":3}],[{"indent":"-1"},{"indent":"+1"}],[{"color":[]},{"background":[]}],["image","video","link"],["clean"],["blockquote","code-block"]]` |  | Custom toolbar configuration for the editor |
| `value` | string | text | `Editor value` |  | Editor value |

**Slots**

| Slot | Description |
|---|---|
| `endSlot` | HTML projected into the `end` slot — trailing chrome such as a language dropdown. Overlaid on the toolbar's trailing edge, or in flow at the end of the body when `hideToolbar` is set. Set `multilingual` (or let the component detect the slot) to reserve the strip it sits over. |
| `startSlot` | HTML projected into the `start` slot — a leading icon beside the editor body. Same contract as s-input / s-textarea: pass the element itself (no wrapper), and the component supplies `text-xl text-dark-100`. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-editor--default` | value="Default editor content...", placeholder="Enter your content here...", toolbar=[["bold", "italic", "underline", "strike, fullToolbar=true, server={"url": "https://api.salla.dev/admin/v2/ |
| Has Preview | `components-editor--has-preview` | value="Default editor content...", placeholder="Enter your content here...", toolbar=[["bold", "italic", "underline", "strike, fullToolbar=true, server={"url": "https://api.salla.dev/admin/v2/ |
| Disabled | `components-editor--disabled` | value="Default editor content...", placeholder="Enter your content here...", toolbar=[["bold", "italic", "underline", "strike, fullToolbar=true, server={"url": "https://api.salla.dev/admin/v2/ |
| Has Error | `components-editor--has-error` | value="Default editor content...", placeholder="Enter your content here...", toolbar=[["bold", "italic", "underline", "strike, fullToolbar=true, server={"url": "https://api.salla.dev/admin/v2/ |
| Has Character Limits 50 | `components-editor--has-character-limits-50` | value="Default editor content...", placeholder="Enter your content here...", toolbar=[["bold", "italic", "underline", "strike, fullToolbar=true, server={"url": "https://api.salla.dev/admin/v2/ |
| With Character Counter | `components-editor--with-character-counter` | value="<p>Try typing to watch the counter tick, placeholder="Enter your content here...", toolbar=[["bold", "italic", "underline", "strike, fullToolbar=true, server={"url": "https://api.salla.dev/admin/v2/ |
| With Slots | `components-editor--with-slots` | value="<p>The globe icon lines up with this fi, placeholder="Editor with start and end slots...", toolbar=[["bold", "italic", "underline", "strike, fullToolbar=true, server={"url": "https://api.salla.dev/admin/v2/ |
| With Slots No Toolbar | `components-editor--with-slots-no-toolbar` | value="<p>With no toolbar, the end control sit, placeholder="hide-toolbar: the end slot stays in flo, toolbar=[["bold", "italic", "underline", "strike, fullToolbar=true, server={"url": "https://api.salla.dev/admin/v2/ |
| Custom Toolbar | `components-editor--custom-toolbar` | value="Default editor content...", placeholder="Enter your content here...", toolbar=[["bold", "italic", "underline"]], fullToolbar=false, server={"url": "https://api.salla.dev/admin/v2/ |
| Ai Suggestion | `components-editor--ai-suggestion` | value="AI generated content...", placeholder="Enter your content here...", toolbar=[["bold", "italic", "underline", "strike, fullToolbar=true, server={"url": "https://api.salla.dev/admin/v2/ |
| With Product Embed | `components-editor--with-product-embed` | value="Default editor content...", placeholder="Enter your content here...", toolbar=[["bold", "italic", "underline", "strike, fullToolbar=true, server={"url": "https://api.salla.dev/admin/v2/ |
| With Image Picker | `components-editor--with-image-picker` | value="Place the cursor somewhere, then press , placeholder="Enter your content here...", toolbar=[["bold", "italic", "underline", "strike, fullToolbar=true, server={"url": "https://api.salla.dev/admin/v2/ |

**Rendered markup — “Default”**

```html
<s-editor value="Default editor content..." placeholder="Enter your content here..." full-toolbar="" class="s-editor ltr hydrated">
  <!---->
  <div class="s-editor__wrapper">
    <s-editor-toolbar class="hydrated">
      <div id="toolbar" class="s-editor__toolbar ql-toolbar ql-snow" role="toolbar" aria-label="Editor toolbar">
        <span class="ql-formats" role="group" aria-label="Formatting options group">
          <button type="button" class="ql-bold" title="Bold" aria-label="Bold" aria-pressed="false">
            <svg viewBox="0 0 18 18">
              <path class="ql-stroke" d="M5,4H9.5A2.5,2.5,0,0,1,12,6.5v0A2.5,2.5,0,0,1,9.5,9H5A0,0,0,0,1,5,9V4A0,0,0,0,1,5,4Z">
              </path>
              <path class="ql-stroke" d="M5,9h5.5A2.5,2.5,0,0,1,13,11.5v0A2.5,2.5,0,0,1,10.5,14H5a0,0,0,0,1,0,0V9A0,0,0,0,1,5,9Z">
              </path>
            </svg>
          </button>
          <button type="button" class="ql-italic" title="Italic" aria-label="Italic" aria-pressed="false">
            <svg viewBox="0 0 18 18">
              <line class="ql-stroke" x1="7" x2="13" y1="4" 
<!-- … truncated … -->
```

---

### 2.12 Icon

**Tag:** `<s-icon>`  
**Storybook:** `components-icon` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-icon>

Use Icon component to display `Hugeicons` or `Sallaicons-light` within a shadowDOM component, such as table, button, uploader, etc when needed.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `icon` | string | text | `sicon-light-salla` |  | Icon class name representing the icon to be displayed, you can use `Hugeicons` or `Sallaicons-light` like `hgi-stroke hgi-tick-02`, `s-light-tick-02` or `sicon-light-salla` |
| `size` | string | text | `1rem` |  | icon size, you can use rem or px, we prefer rem, default is 1rem |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-icon--default` | icon="sicon-light-salla", size="1rem" |

**Rendered markup — “Default”**

```html
<s-icon icon="sicon-light-salla" size="1rem" class="hydrated">
</s-icon>
```

---

### 2.13 IconPicker

**Tag:** `<s-icon-picker>`  
**Storybook:** `components-iconpicker` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-iconpicker>

Searchable, paginated icon grid rendered inside a built-in dropdown. Renders the currently-picked icon in a trigger button; the grid opens on click.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `disabled` |  | boolean |  |  | Disables the picker — trigger becomes non-interactive and the dropdown won't open. |
| `errorMessage` |  | text |  |  | Optional error message shown under the trigger when `hasError` is true. |
| `feature` |  | boolean | `true` |  | Feature-flag guard. When locked, the trigger won't open and clicks reroute to the upgrade flow. |
| `hasError` |  | boolean |  |  | Renders the trigger in an error state (danger border/text). |
| `iconCellSize` |  | text | `2.5rem` |  | Height / width of each grid tile. |
| `iconSize` |  | text | `1.25rem` |  | Font size of icons inside grid cells. |
| `minWidth` |  | text | `10rem` |  | Minimum width of the trigger button. Any CSS length. Ignored when `wide` is set. |
| `name` |  | text |  |  | Form field name (participates in native `<form>` submission). |
| `placeholder` |  | text |  |  | Search-input placeholder. |
| `required` |  | boolean |  |  | Marks the field as required for native form validity. |
| `searchable` |  | boolean | `true` |  | Show the search input above the grid. |
| `source` | string | select | `hugeicons` | hugeicons, sicon | Icon library — `hugeicons` (prefixed) or `sicon`. |
| `value` |  | text |  |  | Selected icon name / class token. |
| `wide` |  | boolean |  |  | Stretch the trigger to fill its container; the panel widens to match. Takes precedence over `min-width`. |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when an icon is picked. `event.detail.payload.value` carries the token. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-iconpicker--default` | source="hugeicons" |
| With Value | `components-iconpicker--with-value` | source="hugeicons", value="home-01" |
| Salla Icons | `components-iconpicker--salla-icons` | source="sicon", value="sicon-cart" |
| No Search | `components-iconpicker--no-search` | source="hugeicons", searchable=false |
| Custom Sizing | `components-iconpicker--custom-sizing` | source="hugeicons", minWidth="14rem", iconCellSize="3rem", iconSize="1.25rem" |
| Wide | `components-iconpicker--wide` | source="hugeicons", wide=true, value="home-01" |
| Feature Locked | `components-iconpicker--feature-locked` | source="hugeicons", value="home-01", feature=false |
| Disabled | `components-iconpicker--disabled` | source="hugeicons", value="home-01", disabled=true |
| With Error | `components-iconpicker--with-error` | source="hugeicons", hasError=true, errorMessage="Please pick an icon before saving." |
| Required | `components-iconpicker--required` | source="hugeicons", name="category_icon", required=true |
| With Value Display | `components-iconpicker--with-value-display` | source="hugeicons", value="home-01" |
| Shared Cache | `components-iconpicker--shared-cache` | source="hugeicons" |

**Rendered markup — “Default”**

```html
<s-icon-picker source="hugeicons" class="s-icon-picker hydrated" style="--picker-min-width: 10rem; --picker-cell-size: 2.5rem; --picker-overlay-width: calc(2.5rem * 5 + 6rem); --picker-trigger-width: 1252px;">
</s-icon-picker>
```

---

### 2.14 Input

**Tag:** `<s-input>`  ·  **Related elements:** `<s-icon>`, `<s-dropdown>`, `<s-button>`  
**Storybook:** `components-input` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-input>

Input component is one of the most used components in any application, it is used to get user different types of input in a text field.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `aiSuggestion` |  | object | `undefined` |  | AI suggestion config (object or JSON string): { enabled, regenerable, source }. When `enabled`, the input gets the Moshammer AI highlight and reveals the `actions` slot (regenerate / dismiss). `regenerable` keeps the slot visible without the highlight. |
| `autocomplete` | array | object |  |  |  |
| `desc` |  | text | `undefined` |  | Input description, you can use it to add a description to the input |
| `disabled` | boolean | boolean | `false` |  | Disabled state |
| `endSlot` | string | text |  |  |  |
| `hasError` | boolean | boolean | `false` |  | Error state |
| `hasPreview` | boolean | boolean | `false` |  | Enable input preview |
| `max` |  | number | `undefined` |  | Input Maximum value |
| `min` |  | number | `undefined` |  | Input Minimum value |
| `multilingual` | boolean | boolean | `false` |  | Enables multilingual support, if true, the input will be able to handle multiple languages, the language will be detected automatically based on merchant supported languages |
| `noBorder` | boolean | boolean | `false` |  | Remove input borders, use it in complex component in your app if needed |
| `pattern` |  | text | `undefined` |  | Regular expression for input validation |
| `placeholder` | string | text | `Enter your text here...` |  | Input placeholder |
| `shadow` | boolean | boolean | `false` |  | Add shadow to the input |
| `size` | string | select | `md` |  | Input field size |
| `startSlot` | string | text |  |  |  |
| `step` |  | number | `undefined` |  | Steps for number inputs only, default is 0 |
| `textAlignment` | string | select | `start` |  | Text alignment within the input |
| `type` | string | select | `text` |  | Type of the input |
| `value` | string | text | `Default input value` |  | Input value |
| `wide` | boolean | boolean | `true` |  | Wide input mode |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the input value changes. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-input--default` | value="Default input value", placeholder="Enter your text here...", type="text", size="md", disabled=false |
| Has Preview | `components-input--has-preview` | value="Default input value", placeholder="Enter your text here...", type="text", size="md", disabled=false |
| Large Size | `components-input--large-size` | value="Default input value", placeholder="Enter your text here...", type="text", size="lg", disabled=false |
| Text Alignment Center | `components-input--text-alignment-center` | value="Default input value", placeholder="Enter your text here...", type="text", size="md", disabled=false |
| Text Alignment End | `components-input--text-alignment-end` | value="Default input value", placeholder="Enter your text here...", type="text", size="md", disabled=false |
| Multilingual | `components-input--multilingual` | value="Default input value", placeholder="Enter your text here...", type="text", size="md", disabled=false |
| Border Less | `components-input--border-less` | value="Default input value", placeholder="Enter your text here...", type="text", size="md", disabled=false |
| Reg Ex Pattern | `components-input--reg-ex-pattern` | value="Default input value", placeholder="Enter 3 letters...", type="text", size="md", disabled=false |
| Description | `components-input--description` | value="Default input value", placeholder="Enter your text here...", type="text", size="md", disabled=false |
| Email | `components-input--email` | value="user@example.com", placeholder="Enter your email...", type="email", size="md", disabled=false |
| Auto Complete | `components-input--auto-complete` | value="Default input value", placeholder="Enter to search...", type="autocomplete", size="md", disabled=false |
| Password | `components-input--password` | value="", placeholder="Enter your password...", type="password", size="md", disabled=false |
| Number | `components-input--number` | value="12345", placeholder="Enter a number...", type="number", size="md", disabled=false |
| With Slots | `components-input--with-slots` | value="Default input value", placeholder="Input with start and end slots...", type="text", size="md", disabled=false |
| Has Error | `components-input--has-error` | value="Default input value", placeholder="Enter your text here...", type="text", size="md", disabled=false |
| Disabled | `components-input--disabled` | value="Default input value", placeholder="Enter your text here...", type="text", size="md", disabled=true |
| Ai Suggestion | `components-input--ai-suggestion` | value="AI generated product name", placeholder="Enter your text here...", type="text", size="md", disabled=false |

**Rendered markup — “Default”**

```html
<s-input id="" name="" value="Default input value" type="text" placeholder="Enter your text here..." size="md" text-alignment="start" wide="" class="w-full md ltr hydrated">
  <s-icon slot="start" icon="hgi-stroke hgi-text" class="hydrated">
  </s-icon>
</s-input>
```

---

### 2.15 Item

**Tag:** `<s-list-item>`  ·  **Related elements:** `<s-icon>`  
**Storybook:** `components-item` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-item>

Items are elements that can contain text, icons, avatars, images, inputs, and any other native or custom elements. Items should only be used as rows in a List with other items.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `clickable` | boolean | boolean |  |  |  |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-item--default` | clickable=false |

**Rendered markup — “Default”**

```html
<div style="display: contents;">
  <s-list-item role="listitem" class="hydrated">List Item <s-icon slot="end" class="hydrated">
  </s-icon>
</s-list-item>
</div>
```

---

### 2.16 LingualField

**Tag:** `<s-lingual-field>`  ·  **Related elements:** `<s-input>`, `<s-icon>`, `<s-dropdown>`, `<s-button>`, `<s-textarea>`, `<s-editor>`, `<s-editor-toolbar>`, `<s-editor-desc>`  
**Storybook:** `components-lingualfield` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-lingualfield>

Lingual field component is used to handle multilingual input fields, allowing users to input content in multiple languages with automatic language detection and switching capabilities.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `aiSuggestion` |  | object | `undefined` |  | AI suggestion config (object or JSON string): { enabled, source, regenerable, languages }. When active, the field gets the Moshammer AI highlight and reveals the `actions` slot (input/textarea end area, richText overlay). Per-language `languages: { [lang]: { content, status: 'pending' } }` auto-applies suggested content. |
| `desc` |  | text | `undefined` |  | Input description, you can use it to add a description to the input |
| `disabled` | boolean | boolean | `false` |  | Disabled state |
| `endSlot` |  | text | `undefined` |  | Input end slot, it accepts strings only, such as SAR or USD for example |
| `fullHeight` |  | boolean | `false` |  | Make the textarea fill its container's height (textarea only). |
| `fullToolbar` |  | boolean | `false` |  | Show the full rich-text toolbar (richText only). |
| `hasError` | boolean | boolean | `false` |  | Error state |
| `hasPreview` |  | boolean | `false` |  | Enable inline preview panel below the field. |
| `language` | string | text | `ar` |  | Input current language |
| `languages` | object | object | `undefined` |  | Languages configuration object with feature flag, supported languages, and current language |
| `max` |  | number | `undefined` |  | Input Maximum value |
| `min` |  | number | `undefined` |  | Input Minimum value |
| `noBorder` | boolean | boolean | `false` |  | Remove input borders, use it in complex component in your app if needed |
| `placeholder` | string | text | `Enter your text here...` |  | Input placeholder |
| `required` | boolean | boolean | `false` |  | Required state |
| `rows` |  | number | `3` |  | Row count for `type: 'textarea'`. |
| `showCount` |  | boolean | `false` |  | Live `current/max` counter under the field (textarea + editor). Requires `max`. Counter follows the document direction so it stays anchored when the editor's per-language RTL flips. Turns danger-red under `has-error`. |
| `size` | string | select | `md` |  | Input size |
| `startSlot` | string | text | `undefined` |  | Input start slot, it accepts icon class name from hugeIcons or Sallaicons |
| `toolbar` | array | object |  |  |  |
| `type` | string | select | `input` |  | Input type, can be input, textarea or richText |
| `value` | string | object | `{"en": "Hello", "ar": "مرحبا"}` |  | JSON string mapping languages to their respective values |

**Events**

| Event | Description |
|---|---|
| `languageChanged` | Emitted when the language is changed. |
| `valueChanged` | Emitted when the field value changes. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-lingualfield--default` | value="{\"en\": \"Hello\", \"ar\": \"\u0645\u0, type="input", placeholder="Enter your text here...", size="md", required=false |
| Text Area Field | `components-lingualfield--text-area-field` | value="{\"en\": \"This is a longer text for te, type="textarea", placeholder="Enter your text here...", size="md", required=false |
| Editor Field | `components-lingualfield--editor-field` | value="{\"en\": \"Rich text content\", \"ar\":, type="richText", placeholder="Enter your text here...", size="md", required=false |
| Ai Suggestion | `components-lingualfield--ai-suggestion` | value="{\"en\": \"AI generated name\", \"ar\":, type="input", placeholder="Enter your text here...", size="md", required=false |
| Ai Suggestion Rich Text | `components-lingualfield--ai-suggestion-rich-text` | value="{\"en\": \"AI generated content\", \"ar, type="richText", placeholder="Enter your text here...", size="md", required=false |
| Multiple Languages | `components-lingualfield--multiple-languages` | value="{\"en\": \"Hello\", \"ar\": \"\u0645\u0, type="input", placeholder="Enter your text here...", size="md", required=false |
| Large Size | `components-lingualfield--large-size` | value="{\"en\": \"Hello\", \"ar\": \"\u0645\u0, type="input", placeholder="Enter your text here...", size="lg", required=false |
| Min Length | `components-lingualfield--min-length` | value="{\"en\": \"Hello\", \"ar\": \"\u0645\u0, type="input", placeholder="Enter your text here...", size="md", required=false |
| Max Length | `components-lingualfield--max-length` | value="{\"en\": \"Hello\", \"ar\": \"\u0645\u0, type="input", placeholder="Enter your text here...", size="md", required=false |
| With Character Counter Textarea | `components-lingualfield--with-character-counter-textarea` | value="{\"en\": \"Sample English phrase \u2014, type="textarea", placeholder="Enter your text here...", size="md", required=false |
| With Character Counter Only | `components-lingualfield--with-character-counter-only` | value="{\"en\": \"Counter without desc \u2014 , type="textarea", placeholder="Enter your text here...", size="md", required=false |
| With Character Counter Rich Text | `components-lingualfield--with-character-counter-rich-text` | value="{\"en\": \"<p>Editable rich text \u2014, type="richText", placeholder="Enter your text here...", size="md", required=false |
| Description | `components-lingualfield--description` | value="{\"en\": \"Hello\", \"ar\": \"\u0645\u0, type="input", placeholder="Enter your text here...", size="md", required=false |
| Border Less | `components-lingualfield--border-less` | value="{\"en\": \"Hello\", \"ar\": \"\u0645\u0, type="input", placeholder="Enter your text here...", size="md", required=false |
| End Slot | `components-lingualfield--end-slot` | value="{\"en\": \"Hello\", \"ar\": \"\u0645\u0, type="input", placeholder="Lingual field with start and end slots., size="md", required=false |
| Has Error | `components-lingualfield--has-error` | value="{\"en\": \"Hello\", \"ar\": \"\u0645\u0, type="input", placeholder="Enter your text here...", size="md", required=false |
| Disabled | `components-lingualfield--disabled` | value="{\"en\": \"Hello\", \"ar\": \"\u0645\u0, type="input", placeholder="Enter your text here...", size="md", required=false |
| Custom Toolbar | `components-lingualfield--custom-toolbar` | value="{\"en\": \"Hello\", \"ar\": \"\u0645\u0, type="richText", placeholder="Enter your text here...", size="md", required=false |

**Rendered markup — “Default”**

```html
<s-lingual-field name="undefined" value="{&quot;en&quot;: &quot;Hello&quot;, &quot;ar&quot;: &quot;مرحبا&quot;}" type="input" placeholder="Enter your text here..." size="md" language="ar" start-slot="hgi-stroke hgi-language-square" languages="{&quot;feature&quot;:true,&quot;supported&quot;:[],&quot;current&quot;:{&quot;id&quot;:0,&quot;label&quot;:&quot;English&quot;,&quot;value&quot;:&quot;en&quot;}}" dir="rtl" class="s-lingual-field s-lingual-field--input rtl w-full relative flex items-start justify-start gap-4 hydrated">
  <!---->
  <s-input class="flex-1 md rtl multilingual ltr hydrated" dir="rtl" value="مرحبا">
    <s-icon slot="start" class="hydrated">
    </s-icon>
    <div slot="end" class="s-lingual-field__actions-end s-lingual-field__actions-end--hidden" data-lingual-field-internal-slot="">
      <div class="s-lingual-field__actions-end__reserve s-lingual-field__actions-end--hidden" aria-hidden="true">
      </div>
    </div>
  </s-input>
  <s-dropdown dir="ltr" class="h-fit end ltr hydrated" overlay-alignment="start">
    <s-button data-toggle="true" slot="dropdown-head" c
<!-- … truncated … -->
```

---

### 2.17 Loader

**Tag:** `<s-loader>`  
**Storybook:** `components-loader` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-loader>

Loader component to show loading state.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `size` | string | select | `md` | xs, sm, md, lg, xlg | Loader size |
| `theme` | string | select | `default` | default, default-force, light, dark | Loader theme |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-loader--default` | theme="default", size="md" |

**Rendered markup — “Default”**

```html
<s-loader theme="default" size="md" role="status" class="s-loader s-loader--default md hydrated">
</s-loader>
```

---

### 2.18 Maps

**Tag:** `<s-maps>`  
**Storybook:** `components-maps` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-maps>

Maps component provides an interactive map interface with search functionality and location services.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `apiKey` | string | text |  |  | Google Maps API Key. |
| `hasCurrentLocationButton` | boolean | boolean | `false` |  | Show or hide the 'Go to current location' button. |
| `height` | string | text | `300px` |  | Map wrapper height. Accepts CSS height property values. |
| `latitude` | number | number | `21.4255186` |  | The latitude coordinate of the map's center |
| `longitude` | number | number | `39.7858435` |  | The longitude coordinate of the map's center |
| `searchPlaceholder` | string | text | `Search...` |  | Search input placeholder. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-maps--default` | apiKey="", hasCurrentLocationButton=false, latitude=21.4255186, longitude=39.7858435, searchPlaceholder="Search..." |
| With Current Location Button | `components-maps--with-current-location-button` | apiKey="", hasCurrentLocationButton=true, latitude=21.4255186, longitude=39.7858435, searchPlaceholder="Search for a place" |
| Custom Coordinates | `components-maps--custom-coordinates` | apiKey="", hasCurrentLocationButton=false, latitude=34.052235, longitude=-118.243683, searchPlaceholder="Search..." |
| Custom Height | `components-maps--custom-height` | apiKey="", hasCurrentLocationButton=false, latitude=21.4255186, longitude=39.7858435, searchPlaceholder="Search..." |

**Rendered markup — “Default”**

```html
<s-maps api-key="" has-current-location-button="false" latitude="21.4255186" longitude="39.7858435" height="300px" search-placeholder="Search..." value="21.4255186,39.7858435" class="w-full relative rounded hydrated" style="height: 300px; position: relative; overflow: hidden;">
  <div style="height: 100%; width: 100%; position: absolute; top: 0px; left: 0px; background-color: rgb(229, 227, 223);">
    <div tabindex="0" aria-label="الخريطة" aria-roledescription="خريطة" role="region" aria-describedby="0F3C4CA7-351C-4968-9FE8-DC637B4C546B" style="position: absolute; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px; left: 0px; top: 0px;">
      <div id="0F3C4CA7-351C-4968-9FE8-DC637B4C546B" style="display: none;">
      </div>
    </div>
    <div class="gm-style" style="position: absolute; z-index: 0; left: 0px; top: 0px; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px;">
      <div style="position: absolute; z-index: 0; left: 0px; top: 0px; height: 100%; width: 100%; padding: 0px; border-width: 0px; margin: 0px; cursor: url(&quot;https://ma
<!-- … truncated … -->
```

---

### 2.19 Modal

**Tag:** `<s-modal>`  ·  **Related elements:** `<s-button>`, `<s-modal-head>`, `<s-modal-body>`, `<s-modal-footer>`  
**Storybook:** `components-modal` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-modal>

A modal component that displays a list of selectable items. It supports various states, search functionality, and different toggle elements.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `closable` | boolean | boolean | `false` |  | Backdrop clickable to close the modal |
| `size` | string | select | `md` |  | Modal size, sm, md, lg, xlg |
| `theme` | string | select | `default` |  | Modal theme, default or light |

**Events**

| Event | Description |
|---|---|
| `onclose` | Emitted when the modal closes. |
| `onopen` | Emitted when the modal opens. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-modal--default` | size="md", theme="default", closable=false |

**Rendered markup — “Default”**

```html
<div class="relative w-full h-full min-h-[600px] flex items-center justify-center">
  <s-button id="s_modal_toggle_s_modal" class="s-btn s-btn--default default md ltr hydrated" theme="default" target="_self">Show Modal</s-button>
  <s-modal id="s_modal" name="" size="md" theme="default" class="s-modal s-modal--default md hydrated" role="dialog" data-scrollable="" scrollable="">
    <s-modal-head class="hydrated">
      <h4 class="text-base font-bold">Modal Title</h4>
      <s-button size="sm" theme="danger" outlined="" data-modal-close="" class="s-btn s-btn--danger default sm outlined ltr hydrated" target="_self">
        <i class="hgi-stroke hgi-cancel-01">
        </i>
      </s-button>
    </s-modal-head>
    <s-modal-body class="hydrated">
      <div class="flex flex-col w-full gap-4">
        <article class="text-sm leading-[1.5]">
          <h4 class="block font-bold mb-2">Sample Content</h4>
          <p>This is the default modal content. You can customize it using the content control.</p>
        </article>
      </div>
    </s-modal-body>
    <s-modal-footer class="hydrated"
<!-- … truncated … -->
```

---

### 2.20 OTP

**Tag:** `<s-otp>`  
**Storybook:** `components-otp` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-otp>

OTP (One-Time Password) component provides a user-friendly interface for entering and validating OTP codes. It supports configurable number of fields, timer functionality, and various sizes.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `fields` | number | number | `4` |  | OTP fields number |
| `hasError` | boolean | boolean | `false` |  | Error state |
| `hasTimer` | boolean | boolean | `true` |  | Enable countdown state |
| `resendLabel` | string | text | `Resend Code` |  | Resend button label |
| `size` | string | select | `md` | md, lg | Fields siz |
| `timer` | number | number | `60000` |  | Timer duration (in milliseconds) |

**Events**

| Event | Description |
|---|---|
| `canSend` | Emitted when the timer expires and user can resend OTP |
| `fieldUpdated` | Emitted when any OTP field value is updated |
| `otpComplete` | Emitted when all OTP fields are filled with complete values |
| `resendRequest` | Emitted when the resend button is clicked |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-otp--default` | fields=4, hasTimer=true, timer=60000, size="md", resendLabel="Resend Code" |
| Size Variants | `components-otp--size-variants` | fields=4, hasTimer=true, timer=60000, size="md", resendLabel="Resend Code" |
| Field Variants | `components-otp--field-variants` | fields=4, hasTimer=true, timer=60000, size="md", resendLabel="Resend Code" |
| Six Fields | `components-otp--six-fields` | fields=6, hasTimer=true, timer=60000, size="md", resendLabel="Resend Code" |
| No Timer | `components-otp--no-timer` | fields=4, size="md", resendLabel="Resend Code", hasError=false, hasTimer=false |
| Short Timer | `components-otp--short-timer` | fields=4, hasTimer=true, timer=10000, size="md", resendLabel="Resend Code" |
| Custom Resend Label | `components-otp--custom-resend-label` | fields=4, hasTimer=true, timer=60000, size="md", resendLabel="Send Again" |
| Has Error | `components-otp--has-error` | fields=4, hasTimer=true, timer=60000, size="md", resendLabel="Resend Code" |

**Rendered markup — “Default”**

```html
<s-otp size="md" fields="4" has-timer="true" timer="60000" resend-label="Resend Code" class="flex flex-col items-center justify-center gap-6 hydrated">
</s-otp>
```

---

### 2.21 Panel

**Tag:** `<s-panel>`  ·  **Related elements:** `<s-panel-head>`, `<s-panel-body>`, `<s-table>`, `<s-button>`, `<s-dropdown>`  
**Storybook:** `components-panel` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-panel>

The content wrapper component

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `actions` | string | text |  |  |  |
| `collapsable` | boolean | boolean | `false` |  | Make panel collapsable |
| `collapsed` | boolean | boolean | `true` |  | Set collapse prop |
| `content` | string | text |  |  | Panel content, use the `<s-panel-body />` to add all your content inside this slot |
| `layout` | string | select | `relaxed` |  | for some scenarions, you may need a compact layout for panel |
| `noPadding` | boolean | boolean |  |  | Remove panel body padding, useful for full width panels with tables inside panel body |
| `overflowHidden` | boolean | boolean |  |  | overflow hidden for panel body |
| `title` | string | text |  |  | Panel title, you can add the title via `<s-panel-head />` and use the `title` slot |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-panel--default` | noPadding=false, overflowHidden=false, collapsable=false, collapsed=true, layout="relaxed" |
| No Padding | `components-panel--no-padding` | noPadding=true, overflowHidden=false, collapsable=false, collapsed=true, layout="relaxed" |
| Collapsable | `components-panel--collapsable` | noPadding=false, overflowHidden=false, collapsable=true, collapsed=true, layout="relaxed" |
| Header Actions Slot | `components-panel--header-actions-slot` | noPadding=false, overflowHidden=false, collapsable=false, collapsed=true, layout="relaxed" |
| Compact Layout | `components-panel--compact-layout` | noPadding=false, overflowHidden=false, collapsable=false, collapsed=true, layout="compact" |
| Headless Panel | `components-panel--headless-panel` | noPadding=false, overflowHidden=false, collapsable=false, collapsed=true, layout="relaxed" |

**Rendered markup — “Default”**

```html
<s-panel collapsed="" layout="relaxed" class="s-panel ltr hydrated">
  <s-panel-head data-collapsed="true" class="hydrated">
    <div slot="title">Panel Title</div>
  </s-panel-head>
  <s-panel-body class="hydrated"> Panel content, you can add any content here inside this slot </s-panel-body>
</s-panel>
```

---

### 2.22 Placeholder

**Tag:** `<s-placeholder>`  ·  **Related elements:** `<s-icon>`, `<s-button>`  
**Storybook:** `components-placeholder` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-placeholder>

Placeholder component is used to display a placeholder for a component or page.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `actions` |  | text | `Upgrade now & learn more buttons` |  | Actions slot content - insert your action buttons in the `actions` slot |
| `desc` | string | text | `You can select specific details such as name, price, and more…` |  | Placeholder description (optional) |
| `icon` | string | text | `hgi-stroke hgi-package-open` |  | Hugeicons class name rendered in the `icon` slot |
| `label` | string | text | `Add a template to customize the export with only the information you need!` |  | Placeholder label |
| `size` | string | select | `md` |  | Placeholder size |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-placeholder--default` | label="Add a template to customize the export , desc="You can select specific details such as, size="md", icon="hgi-stroke hgi-package-open" |
| Small | `components-placeholder--small` | label="Add a template to customize the export , desc="You can select specific details such as, size="sm", icon="hgi-stroke hgi-package-open" |
| Large | `components-placeholder--large` | label="Add a template to customize the export , desc="You can select specific details such as, size="lg", icon="hgi-stroke hgi-package-open" |

**Rendered markup — “Default”**

```html
<s-placeholder label="Add a template to customize the export with only the information you need!" desc="You can select specific details such as name, price, and more…" size="md" class="s-placeholder md hydrated">
  <div slot="icon">
    <s-icon icon="hgi-stroke hgi-package-open" size="4rem" class="hydrated">
    </s-icon>
  </div>
  <div slot="actions">
    <s-button outlined="" class="s-btn s-btn--default default md outlined ltr hydrated" theme="default" target="_self">Upgrade now</s-button>
    <s-button theme="transparent" no-padding="true" class="text-primary underline s-btn s-btn--transparent default md ltr hydrated" target="_self">learn more</s-button>
  </div>
</s-placeholder>
```

---

### 2.23 Progress Bar

**Tag:** `<s-progress-bar>`  
**Storybook:** `components-progress-bar` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-progress-bar>

A progress bar component, helping you adding a graphical element to your app. It supports various states, loading, and different toggle elements.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `desc` | string | text | `This is a progress bar description` |  | Progress bar description |
| `label` | string | text | `This is a progress bar label` |  | Progress bar label |
| `percentage` | number | number | `25` |  | Progress bar percentage |
| `secondaryPercentage` |  | number | `undefined` |  | You can add a secondary percentage to the progress bar if needed |
| `shortLabel` | boolean | boolean | `false` |  | If you need to make the label shorter, you can use this prop |
| `showPercentage` | boolean | boolean | `true` |  | Show or hide the percentage value on the progress bar |
| `size` | string | select | `md` |  | Progress bar size |
| `theme` | string | select | `default` |  | Progress bar theme, default or secondary |

**Events**

| Event | Description |
|---|---|
| `onchange` | Emitted when the progress bar value changes. |
| `onclick` | Emitted when the progress bar is clicked. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-progress-bar--default` | label="This is a progress bar label", desc="This is a progress bar description", theme="default", size="md", percentage=25 |
| Short Label | `components-progress-bar--short-label` | label="This is a progress bar label", desc="This is a progress bar description", theme="default", size="md", percentage=25 |
| Secondary Theme | `components-progress-bar--secondary-theme` | label="This is a progress bar label", desc="This is a progress bar description", theme="secondary", size="md", percentage=25 |
| Secondary Percentage | `components-progress-bar--secondary-percentage` | label="This is a progress bar label", desc="This is a progress bar description", theme="default", size="md", percentage=25 |
| Large | `components-progress-bar--large` | label="This is a progress bar label", desc="This is a progress bar description", theme="default", size="lg", percentage=25 |
| Small | `components-progress-bar--small` | label="This is a progress bar label", desc="This is a progress bar description", theme="default", size="sm", percentage=25 |

**Rendered markup — “Default”**

```html
<s-progress-bar label="This is a progress bar label" desc="This is a progress bar description" theme="default" size="md" percentage="25" show-percentage="true" class="w-full s-progress-bar flex flex-col gap-2 default md ltr hydrated">
</s-progress-bar>
```

---

### 2.24 Qty

**Tag:** `<s-qty>`  
**Storybook:** `components-qty` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-qty>

The Qty component represents a quantity input field. It allows users to input numeric quantities and provides buttons to increment or decrement the value.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `deletable` | boolean | boolean | `false` |  | Enable this to show delete button instead of minus button when value is 1 an event will be emitted with the following payload { payload: { target, min, max, value, leastValue, deletable } } |
| `disabled` | boolean | boolean | `false` |  | Disabled state |
| `hasError` | boolean | boolean | `false` |  | Error state |
| `layout` | string | select | `sides` |  | Field layout, you can choose between sides and end |
| `max` | number | number | `100` |  | Field maximum value |
| `min` | number | number | `0` |  | Field minimum value |
| `placeholder` | string | text | `Enter the required quantity` |  | Field placeholder |
| `required` | boolean | boolean | `false` |  | Required state |
| `step` | number | number | `1` |  | Field step, it's the value to increment or decrement when clicking the buttons. Default is 1. |
| `theme` | string | select | `default` |  | Field theme, you can choose between default and circular |
| `value` | number | number | `1` |  | Field value |
| `wide` | boolean | boolean | `false` |  | Wide state |

**Events**

| Event | Description |
|---|---|
| `decreaseClicked` | Emitted when the decrease button is clicked. |
| `increaseClicked` | Emitted when the increase button is clicked. |
| `valueChanged` | Emitted when the quantity input field value changes. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-qty--default` | value=1, theme="default", layout="sides", min=1, max=100 |
| Circular | `components-qty--circular` | value=1, theme="circular", layout="sides", min=1, max=100 |
| Wide | `components-qty--wide` | value=1, theme="default", layout="sides", min=1, max=100 |
| Min Max Values | `components-qty--min-max-values` | value=8, theme="default", layout="sides", min=5, max=10 |
| Step | `components-qty--step` | value=10, theme="default", layout="sides", min=0, max=50 |
| Deletable | `components-qty--deletable` | value=1, theme="default", layout="sides", min=1, max=1 |
| Layout End | `components-qty--layout-end` | value=1, theme="default", layout="end", min=1, max=100 |
| Has Error | `components-qty--has-error` | value=1, theme="default", layout="sides", min=1, max=100 |
| Disabled | `components-qty--disabled` | value=1, theme="default", layout="sides", min=1, max=100 |

**Rendered markup — “Default”**

```html
<s-qty value="1" theme="default" layout="sides" min="1" max="100" step="1" placeholder="Enter Qty" class="s-qty s-qty--default ltr hydrated">
</s-qty>
```

---

### 2.25 Radio

**Tag:** `<s-radio>`  
**Storybook:** `components-radio` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-radio>

A radio button is a form element that allows users to select one option from a list of mutually exclusive choices. It is commonly used in forms where only one selection is allowed.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `autoHeight` |  | boolean | `false` |  | If the text radio should fill the available height. Applies when layout is "text". |
| `checked` | boolean | boolean | `false` |  | Radio checked state |
| `desc` | string | text |  |  | Radio description |
| `direction` | string | select | `col` |  | Radio direction, you can choose between col (vertical) or row (horizontal) |
| `disabled` | boolean | boolean | `false` |  | Boolean indicating whether the radio is disabled |
| `feature` |  | boolean | `true` |  | Feature based state |
| `hasError` | boolean | boolean | `false` |  | Boolean indicating whether the radio has an error |
| `items` |  | text | `[]` |  | Multiple Radio value |
| `label` | string | text |  |  | Radio label |
| `layout` | string | select | `default` |  | Radio layout style, you can choose between default, text, image, color |
| `loading` |  | boolean | `false` |  | Replaces every option with a skeleton placeholder shaped like the current layout. Per-option loading is also supported via `loading: true` on an individual item. |
| `required` | boolean | boolean | `false` |  | If the radio is required |
| `value` |  | text |  |  | Single Radio value |
| `wide` | boolean | boolean | `false` |  | Boolean indicating whether the radio occupies full width |

**Events**

| Event | Description |
|---|---|
| `onChange` | Emitted when the radio selection changes (native change event). |
| `onInput` | Emitted when the radio input is modified (native input event). |
| `onValueChanged` | Emitted when the radio value changes. Payload includes value, checked state, and all options. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-radio--default` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=false, hasError=false |
| Checked | `components-radio--checked` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=false, hasError=false |
| Group Options | `components-radio--group-options` | label="Select your preferred option", desc="Choose one option from the list below", required=true, disabled=false, hasError=false |
| Row Direction | `components-radio--row-direction` | label="Select your preferred option", desc="Choose one option from the list below", required=true, disabled=false, hasError=false |
| Text Layout | `components-radio--text-layout` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=false, hasError=false |
| Text Layout Auto Height | `components-radio--text-layout-auto-height` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=false, hasError=false |
| Color Layout | `components-radio--color-layout` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=false, hasError=false |
| Image Layout | `components-radio--image-layout` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=false, hasError=false |
| Required | `components-radio--required` | label="Select your preferred option", desc="Choose one option from the list below", required=true, disabled=false, hasError=false |
| Feature Based | `components-radio--feature-based` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=false, hasError=false |
| Disabled | `components-radio--disabled` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=true, hasError=false |
| Disabled Item | `components-radio--disabled-item` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=false, hasError=false |
| Loading | `components-radio--loading` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=false, hasError=false |
| Loading Item | `components-radio--loading-item` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=false, hasError=false |
| Has Error | `components-radio--has-error` | label="Select your preferred option", desc="Choose one option from the list below", required=false, disabled=false, hasError=true |

**Rendered markup — “Default”**

```html
<s-radio label="Select your preferred option" desc="Choose one option from the list below" layout="default" direction="col" class="s-radio s-radio--default ltr hydrated">
</s-radio>
```

---

### 2.26 Range Slider

**Tag:** `<s-range-slider>`  
**Storybook:** `components-range-slider` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-range-slider>

The s-range-slider component represents a range slider that allows users to select a value within a specified range. It offers a visual slider input and a numerical input for selecting values.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `disabled` | boolean | boolean | `false` |  | Disabled state |
| `hasError` | boolean | boolean | `false` |  | Error state |
| `max` | number | number | `200` |  | Slider maximum value |
| `min` | number | number | `0` |  | Slider minimum value |
| `step` | number | number | `1` |  | Step value for the range slider |
| `theme` | string | select | `default` | default, secondary | Slider theme, you can choose between default and secondary |
| `value` | number | number | `100` |  | Slider value |

**Events**

| Event | Description |
|---|---|
| `onChange` | Emitted when the value of the range slider changes. |
| `onValueChanged` | Emitted when the value of the range slider changes. Payload includes target, min, max, step, and value. |
| `onchange` | Emitted when the range slider value changes. Provides the new value as a number. |
| `valueChanged` | Emitted when the value of the range slider changes. Provides detailed change information. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-range-slider--default` | value=100, theme="default", min=0, max=200, step=1 |
| Step | `components-range-slider--step` | value=100, theme="default", min=0, max=200, step=10 |
| Secondary Theme | `components-range-slider--secondary-theme` | value=100, theme="secondary", min=0, max=200, step=1 |
| Has Error | `components-range-slider--has-error` | value=100, theme="default", min=0, max=200, step=1 |
| Disabled | `components-range-slider--disabled` | value=100, theme="default", min=0, max=200, step=1 |

**Rendered markup — “Default”**

```html
<s-range-slider value="100" theme="default" max="200" step="1" class="w-full s-range-slider ltr hydrated">
</s-range-slider>
```

---

### 2.27 Rate

**Tag:** `<s-rate>`  
**Storybook:** `components-rate` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-rate>

The s-rate component represents a rating system that allows users to provide or view ratings. It supports two icon styles: `star` (classic half-star capable stars) and `emoji` (5 expressive face icons: angry → confused → neutral → happy → star-face). In emoji mode the value is always a whole number (1–5) and the `rateChanged` payload contains the selected emoji icon class instead of maxStars/totalRate.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `hideValue` | boolean | boolean | `true` |  | Hide rate value |
| `iconStyle` | string | select | `star` | star, emoji | Icon style for the rating. `star` uses the classic star icons; `emoji` uses expressive face icons (angry → sad → neutral → happy → star-face). |
| `maxStars` | number | number | `5` |  | Rate max stars |
| `readOnly` | boolean | boolean | `false` |  | Enable this if you want to make the rate read only |
| `required` | boolean | boolean |  |  |  |
| `size` | string | select | `md` | sm, md, lg | Rate size, you can choose between `sm`, `md` and `lg` |
| `theme` | string | select | `default` | default, secondary, danger, warning, info | Rate theme |
| `totalRate` | number | number | `100` |  | Total rate |
| `value` | number | number | `3` |  | Rate value |

**Events**

| Event | Description |
|---|---|
| `onRateChanged` | Emitted when the rating value changes. In `star` mode the payload contains `{ value, maxStars, totalRate }`; in `emoji` mode it contains `{ value, emoji }` where `emoji` is the selected HugeIcons class (e.g. `hgi-solid hgi-smile`). |
| `rateChanged` | Emitted when a star or emoji is clicked, providing the new value and mode-specific payload. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-rate--default` | value=3, theme="default", hideValue=false, maxStars=5, totalRate=100 |
| Read Only | `components-rate--read-only` | value=3, theme="default", hideValue=false, maxStars=5, totalRate=100 |
| Hide Value | `components-rate--hide-value` | value=3, theme="default", hideValue=true, maxStars=5, totalRate=100 |
| Warning Theme | `components-rate--warning-theme` | value=3, theme="warning", hideValue=false, maxStars=5, totalRate=100 |
| Danger Theme | `components-rate--danger-theme` | value=3, theme="danger", hideValue=false, maxStars=5, totalRate=100 |
| Large | `components-rate--large` | value=3, theme="default", hideValue=false, maxStars=5, totalRate=100 |
| Small | `components-rate--small` | value=3, theme="default", hideValue=false, maxStars=5, totalRate=100 |
| Emoji | `components-rate--emoji` | iconStyle="emoji", value=4, theme="default", size="md", hideValue=false |
| Emoji Read Only | `components-rate--emoji-read-only` | iconStyle="emoji", value=3, theme="default", size="md", hideValue=false |

**Rendered markup — “Default”**

```html
<s-rate value="3" theme="default" max-stars="5" total-rate="100" size="md" icon-style="star" class="s-rate s-rate--default s-rate--horizontal ltr md hydrated" id="" name="" layout="horizontal" maxstars="5" totalrate="100" iconstyle="star">
</s-rate>
```

---

### 2.28 Select

**Tag:** `<s-select>`  ·  **Related elements:** `<s-button>`  
**Storybook:** `components-select` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-select>

Select component provides a dropdown interface for choosing from a list of options. It supports single and multiple selection, search functionality, grouping, and various customization options.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `addMissingItem` | boolean | boolean | `false` |  | Allow adding new items |
| `allowParentSelect` |  | boolean | `true` |  | When false and layout is drawer, clicking a parent item opens the drawer/toggles children instead of selecting the parent. When true, parent items remain selectable. |
| `autocomplete` | boolean | boolean |  |  | Enables this option to fetch items from server dynamically based on the search query |
| `cancelLabel` |  | text |  |  | Label of the cancel action. Defaults to the translated "Cancel". |
| `children` | string | text |  |  |  |
| `confirmLabel` |  | text |  |  | Label of the confirm action. Defaults to the translated "Save". |
| `confirmable` | boolean | boolean |  |  | Buffers the selection behind sticky confirm/cancel actions at the end of the dropdown. No `selectChange` is emitted while the dropdown is open — confirm emits it once (plus `selectConfirm`), cancel emits `selectCancel` and restores the value the dropdown opened with. |
| `disabled` | boolean | boolean | `false` |  | Disabled state |
| `endSlot` |  | text | `undefined` |  | HTML content to render in the end slot |
| `hasError` | boolean | boolean |  |  | Error state |
| `hideClearButton` | boolean | boolean | `false` |  | Hide the clear button, useful in certain cases |
| `items` | array | text | `[]` |  | Options for the select |
| `layout` |  | select | `default` | default, drawer | Layout mode for the select dropdown |
| `loading` | boolean | boolean | `false` |  | Loading state |
| `multiselect` | boolean | boolean |  |  | Enables multiple selection mode, you can then choose either tags or count of selected items, count is default |
| `overlayAlignment` | string | select | `start` | start, end | Horizontal alignment preference for the dropdown overlay |
| `placeholder` | string | text |  |  | Placeholder text |
| `readonly` | boolean | boolean | `false` |  | The value cannot change, but the component stays usable: the dropdown still opens and closes, and the search box still filters. Selecting, select-all, add-new, drawer navigation, the clear button and tag removal are all locked. Use it for async work that must not be interrupted, or for view-only permissions; unlike `disabled`, it never greys out the whole component or force-closes the overlay. |
| `required` | boolean | boolean |  |  | Required state |
| `responsive` |  | boolean |  |  | Responsive mode |
| `searchPlaceholder` |  | text | `undefined` |  | Search input placeholder |
| `searchable` | boolean | boolean |  |  | Enables search functionality |
| `selectAll` | boolean | boolean |  |  | Shows a select-all row in the dropdown. Works only when multiselect is enabled. |
| `sheetTitle` |  | text |  |  | Optional title shown in the mobile sheet header |
| `size` |  | select |  | md, lg | Size of the select component |
| `tags` | boolean | boolean |  |  | Display selections as tags |
| `toggleSlot` |  | text | `undefined` |  | HTML content to render in the toggle slot. When provided, replaces the default input-wrapper. Element should have data-toggle attribute. |
| `value` | string | text |  |  | Selected value(s) |
| `wide` |  | boolean |  |  | Full width |

**Events**

| Event | Description |
|---|---|
| `addNewItem` | Emitted when user clicks to add a missing item. Provides value and searchString. |
| `optionsChange` | Emitted when the value of options changes. |
| `searchValueChange` | Emitted when the search value changes in searchable mode. |
| `selectChange` | Emitted when the value of the select component changes. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-select--default` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Searchable | `components-select--searchable` | placeholder="Select an option...", value="", required=false, searchable=true, autocomplete=false |
| Auto Complete | `components-select--auto-complete` | placeholder="Select an option...", value="", required=false, searchable=true, autocomplete=true |
| With End Slot | `components-select--with-end-slot` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| With End Overlay Alignment | `components-select--with-end-overlay-alignment` | placeholder="Open me near viewport edge", value="", required=false, searchable=true, autocomplete=false |
| With Toggle Slot | `components-select--with-toggle-slot` | placeholder="Select an option...", value="", required=false, searchable=true, autocomplete=false |
| With Groups And Thumbnails | `components-select--with-groups-and-thumbnails` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Nested Options | `components-select--nested-options` | placeholder="Select categories", value=["laptops", "kitchen"], required=false, searchable=true, autocomplete=false |
| Drawer Layout | `components-select--drawer-layout` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Drawer Layout No Parent Select | `components-select--drawer-layout-no-parent-select` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Nested With Child Icons | `components-select--nested-with-child-icons` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Multi Select | `components-select--multi-select` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Multi Select Tags Layout | `components-select--multi-select-tags-layout` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Multi Select With Select All | `components-select--multi-select-with-select-all` | placeholder="Select multiple options", value="", required=false, searchable=true, autocomplete=false |
| Add Missing Item | `components-select--add-missing-item` | placeholder="Select an option...", value="", required=false, searchable=true, autocomplete=false |
| Hide Clear Button | `components-select--hide-clear-button` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Loading | `components-select--loading` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Has Error | `components-select--has-error` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Disabled | `components-select--disabled` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Disabled Item | `components-select--disabled-item` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Disabled Nested Item | `components-select--disabled-nested-item` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Disabled Item Multiselect | `components-select--disabled-item-multiselect` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Readonly | `components-select--readonly` | placeholder="Open me \u2014 the list is locked", value="", required=false, searchable=false, autocomplete=false |
| Readonly Searchable | `components-select--readonly-searchable` | placeholder="Searchable + locked list", value="", required=false, searchable=true, autocomplete=false |
| Readonly Multiselect | `components-select--readonly-multiselect` | placeholder="Select an option...", value=["m-1"], required=false, searchable=true, autocomplete=false |
| Readonly Nested | `components-select--readonly-nested` | placeholder="Nested options \u2014 locked", value="", required=false, searchable=false, autocomplete=false |
| Readonly Drawer | `components-select--readonly-drawer` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Readonly While Saving | `components-select--readonly-while-saving` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |
| Confirmable Actions | `components-select--confirmable-actions` | placeholder="Select an option...", value="", required=false, searchable=false, autocomplete=false |

**Rendered markup — “Default”**

```html
<div style="display: contents;">
  <div children="[object Object]" style="overflow: hidden;">
    <s-select class="w-full md ltr hydrated" value="">
    </s-select>
  </div>
</div>
```

---

### 2.29 Skeleton

**Tag:** `<s-skeleton>`  
**Storybook:** `components-skeleton` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-skeleton>

The Skeleton component provides loading placeholders that mimic the structure of content while it's being loaded.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `layout` | string | select | `inline` | inline, list-entry, article, rich-content, cart, checkout, table, settings, header, home-p | Skeleton layout |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-skeleton--default` | layout="inline" |
| Inline | `components-skeleton--inline` | layout="inline" |
| List Entry | `components-skeleton--list-entry` | layout="list-entry" |
| Article | `components-skeleton--article` | layout="article" |
| Rich Content | `components-skeleton--rich-content` | layout="rich-content" |
| Cart Content | `components-skeleton--cart-content` | layout="cart" |
| Checkout | `components-skeleton--checkout` | layout="checkout" |
| Table Content | `components-skeleton--table-content` | layout="table" |
| Settings | `components-skeleton--settings` | layout="settings" |
| Header | `components-skeleton--header` | layout="header" |
| Home Page | `components-skeleton--home-page` | layout="home-page" |
| Resource Page | `components-skeleton--resource-page` | layout="resource-page" |
| Sections Page | `components-skeleton--sections-page` | layout="sections-page" |
| Iframe Page | `components-skeleton--iframe-page` | layout="iframe-page" |

**Rendered markup — “Default”**

```html
<s-skeleton layout="inline" role="status" class="s-skeleton s-skeleton--inline hydrated">
</s-skeleton>
```

---

### 2.30 Table

**Tag:** `<s-table>`  ·  **Related elements:** `<s-panel>`, `<s-panel-head>`, `<s-panel-body>`  
**Storybook:** `components-table` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-table>

The table component is a customizable table that provides functionalities for sorting, pagination, and filtering.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `children` | string | text |  |  |  |
| `emptyPlaceholderDesc` |  | text | `undefined` |  | Description to display when there's no data |
| `emptyPlaceholderIcon` |  | text | `undefined` |  | Icon to display when there's no data |
| `emptyPlaceholderLabel` |  | text | `undefined` |  | Label to display when there's no data |
| `fetchUrl` |  | text | `undefined` |  | Table data source url |
| `hasNextPage` |  | boolean | `false` |  | Indicates if there is a next page available |
| `hasPrevPage` |  | boolean | `false` |  | Indicates if there is a previous page available |
| `headers` | array | object | `["Name", "Age", "Visits", "Progress"]` |  | Table headers |
| `items` | array | object | `TABLE_ITEMS` |  | Table data |
| `itemsPerPage` | string | object | `["10", "20", "30", "40", "50"]` |  | Items per page |
| `layout` | string | select | `scroll` |  | Table layout, scroll or responsive, default is scroll |
| `loading` | boolean | boolean | `false` |  | Loading state |
| `pagination` | boolean | boolean | `true` |  | Table pagination |
| `searchPlaceholder` | string | text | `Search...` |  | Table search placeholder |
| `searchable` | boolean | boolean | `false` |  | Enable table search |
| `selectable` | boolean | boolean | `false` |  | Enable table row selection |
| `sortBy` |  | object | `undefined` |  | Sorting configuration for columns in the table |
| `sortable` | boolean | boolean | `false` |  | Enable table sorting |
| `transform` |  | object | `undefined` |  | Transform data before passing to the component |

**Events**

| Event | Description |
|---|---|
| `onNextButtonClicked` | Event emitted when next page button is clicked |
| `onPrevButtonClicked` | Event emitted when previous page button is clicked |
| `onSelect` | Event emitted when single or all rows are selected |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-table--default` | items=[{"name": "John Wick", "age": "24", "vis, headers=["Name", "Age", "Visits", "Progress"], searchable=false, sortable=false, pagination=true |
| With Search | `components-table--with-search` | items=[{"name": "John Wick", "age": "24", "vis, headers=["Name", "Age", "Visits", "Progress"], searchable=true, sortable=false, pagination=true |
| Sorting | `components-table--sorting` | items=[{"name": "John Wick", "age": "24", "vis, headers=["Name", "Age", "Visits", "Progress"], searchable=false, sortable=true, pagination=true |
| Selection | `components-table--selection` | items=[{"name": "John Wick", "age": "24", "vis, headers=["Name", "Age", "Visits", "Progress"], searchable=false, sortable=false, pagination=true |
| Custom Pagination | `components-table--custom-pagination` | items=[{"name": "John Wick", "age": "24", "vis, headers=["Name", "Age", "Visits", "Progress"], searchable=false, sortable=false, pagination=true |
| Empty State | `components-table--empty-state` | items=[], headers=["Name", "Age", "Visits", "Progress"], searchable=false, sortable=false, pagination=true |
| Responsive Layout | `components-table--responsive-layout` | items=[{"name": "John Wick", "age": "24", "vis, headers=["Name", "Age", "Visits", "Progress"], searchable=false, sortable=false, pagination=true |
| Custom Slots | `components-table--custom-slots` | items=[{"name": "John Wick", "age": "24", "vis, headers=["Name", "Age", "Visits", "Progress"], searchable=false, sortable=false, pagination=true |
| All Features | `components-table--all-features` | items=[{"name": "John Wick", "age": "24", "vis, headers=["Name", "Age", "Visits", "Progress"], searchable=true, sortable=true, pagination=true |

**Rendered markup — “Default”**

```html
<s-panel no-padding="" class="s-panel no-padding ltr">
  <s-panel-head data-collapsed="true" class="hydrated">
    <h2 slot="title">Table Component</h2>
  </s-panel-head>
  <s-panel-body>
    <s-table items="[{&quot;name&quot;:&quot;John Wick&quot;,&quot;age&quot;:&quot;24&quot;,&quot;visits&quot;:&quot;100&quot;,&quot;progress&quot;:&quot;54&quot;},{&quot;name&quot;:&quot;James Bond&quot;,&quot;age&quot;:&quot;24&quot;,&quot;visits&quot;:&quot;100&quot;,&quot;progress&quot;:&quot;54&quot;},{&quot;name&quot;:&quot;Joe&quot;,&quot;age&quot;:&quot;45&quot;,&quot;visits&quot;:&quot;20&quot;,&quot;progress&quot;:&quot;68&quot;,&quot;options&quot;:&quot;&quot;},{&quot;name&quot;:&quot;Joe&quot;,&quot;age&quot;:&quot;45&quot;,&quot;visits&quot;:&quot;20&quot;,&quot;progress&quot;:&quot;68&quot;,&quot;options&quot;:&quot;&quot;},{&quot;name&quot;:&quot;Joe&quot;,&quot;age&quot;:&quot;45&quot;,&quot;visits&quot;:&quot;20&quot;,&quot;progress&quot;:&quot;68&quot;,&quot;options&quot;:&quot;&quot;},{&quot;name&quot;:&quot;Joe&quot;,&quot;age&quot;:&quot;45&quot;,&quot;visits&quot;:&quot;20&quot
<!-- … truncated … -->
```

---

### 2.31 Tabs

**Tag:** `<s-tabs-group>`  ·  **Related elements:** `<s-tab-head>`, `<s-tab-body>`  
**Storybook:** `components-tabs` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-tabs>

The `s-tabs-group` component represents a group of tabs in a tabbed interface. It handles the display of tab headers and bodies, providing properties for customization, using the `s-tab-head` and `s-tab-body` components. to create a tabbed interface.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `id` | string | text | `''` |  | Tabs group unique identifier |
| `loading` | boolean | boolean | `false` |  | Loading state |
| `name` | string | text | `''` |  | Tabs group unique name |
| `theme` | string | select | `default` | default, stack, buttons, underline | Tabs group theme style, you can choose between 'default', 'stack', 'buttons' and 'underline' |
| `wide` | boolean | boolean | `true` |  | Enable full width |

**Events**

| Event | Description |
|---|---|
| `tabChanged` | Emitted when the active tab changes. Provides index, value, and payload information. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-tabs--default` | id="tabs_group_default", name="Default Tabs Group", theme="default", wide=true, loading=false |
| Stack | `components-tabs--stack` | id="tabs_group_stack", name="Stack Tabs Group", theme="stack", wide=true, loading=false |
| Buttons | `components-tabs--buttons` | id="tabs_group_buttons", name="Buttons Tabs Group", theme="buttons", wide=true, loading=false |
| Underline | `components-tabs--underline` | id="tabs_group_underline", name="Underline Tabs Group", theme="underline", wide=true, loading=false |
| Fit Width | `components-tabs--fit-width` | id="tabs_group_narrow", name="Narrow Tabs Group", theme="default", wide=false, loading=false |

**Rendered markup — “Default”**

```html
<div class="flex items-start flex-col gap-4">
  <s-tabs-group id="tabs_group_default" name="Default Tabs Group" theme="default" wide="" class="s-tabs-group s-tabs-group--default w-full ltr hydrated">
    <div slot="head">
      <s-tab-head value="tab_home" active="" class="s-tab-head s-tab-head--default active ltr hydrated">
        <i class="hgi-stroke hgi-home-01">
        </i> Home </s-tab-head>
        <s-tab-head value="tab_products" class="s-tab-head s-tab-head--default ltr hydrated">
          <i class="hgi-stroke hgi-shirt-01">
          </i> Products </s-tab-head>
          <s-tab-head value="tab_orders" class="s-tab-head s-tab-head--default ltr hydrated">
            <i class="hgi-stroke hgi-archive-02">
            </i> Orders </s-tab-head>
          </div>
          <div slot="body">
            <s-tab-body id="tab_home" active="" class="s-tab-body s-tab-body--default active ltr hydrated">
              <article>
                <p>Content for the Home tab.</p>
              </article>
            </s-tab-body>
            <s-tab-body id="tab_products" class="s-tab-body s
<!-- … truncated … -->
```

---

### 2.32 Tag

**Tag:** `<s-tag>`  
**Storybook:** `components-tag` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-tag>

A tag is a visual element used for categorization, labeling, or marking content. Tags can be customized with different themes, sizes, and behaviors.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `closable` |  | boolean | `false` |  | Enable closable tag |
| `disabled` |  | boolean | `false` |  | Disabled state |
| `feature` |  | boolean | `true` |  | Show feature tag for a certain element |
| `label` | string | text |  |  |  |
| `layout` |  | select | `default` | default, status | Tag layout |
| `nowrap` |  | boolean | `true` |  | Prevent text wrapping inside the tag |
| `outlined` |  | boolean | `false` |  | Outlined state |
| `size` |  | select | `md` | sm, md | Tag size |
| `theme` |  | select | `default` | default, secondary, success, danger, warning, info, white, transparent, feature, mahally | Tag theme |

**Events**

| Event | Description |
|---|---|
| `onclose` | Emitted when the tag is closed. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-tag--default` | label="New" |
| Theme Variants | `components-tag--theme-variants` | label="Sample Tag" |
| Size Variants | `components-tag--size-variants` | label="Sample Tag" |
| Outlined Variants | `components-tag--outlined-variants` | label="Sample Tag" |
| Status Layout | `components-tag--status-layout` | label="Status Tag", layout="status" |
| Closable | `components-tag--closable` | label="Closable Tag", closable=true |
| Disabled | `components-tag--disabled` | label="Disabled Tag", disabled=true |
| Closable Theme Variants | `components-tag--closable-theme-variants` | label="Closable" |
| Long Text | `components-tag--long-text` | label="This is a very long tag text that might, nowrap=false |
| No Wrap | `components-tag--no-wrap` | label="This is a very long tag text that shoul, nowrap=true |
| With Feature | `components-tag--with-feature` | label="Feature Tag", theme="feature", feature=true |
| Disabled Feature | `components-tag--disabled-feature` | label="Disabled Feature", theme="feature", feature=false |
| Mixed Examples | `components-tag--mixed-examples` | label="Mixed" |

**Rendered markup — “Default”**

```html
<s-tag class="s-tag s-tag--default whitespace-nowrap md ltr hydrated">New</s-tag>
```

---

### 2.33 Tags Input

**Tag:** `<s-tags>`  
**Storybook:** `components-tags-input` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-tags-input>

A tags input component that allows users to add, remove, and manage multiple tag values. Supports customizable themes, maximum limits, and form validation.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `buttonLabel` |  | text | `Add` |  | Button label |
| `buttonTheme` |  | select | `default` | default, secondary, danger, warning, info, white, transparent, feature | Button theme |
| `disabled` |  | boolean | `false` |  | Disabled state |
| `hasError` |  | boolean | `false` |  | Error state |
| `max` |  | number | `undefined` |  | Maximum number of tags allowed |
| `placeholder` | string | text | `undefined` |  | Placeholder text |
| `tagSize` |  | select | `md` | sm, md | Tag size |
| `tagTheme` |  | select | `white` | default, secondary, success, danger, warning, info, white, transparent, feature | Tag theme |
| `value` |  | object | `[]` |  | Array of current tag values |
| `wide` |  | boolean | `false` |  | Makes the input take full width |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the tags value changes. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-tags-input--default` | placeholder="Enter a tag and press add" |
| Initial Values | `components-tags-input--initial-values` | value=["React", "TypeScript", "Stencil"], placeholder="Enter a tag and press add" |
| Max Limit | `components-tags-input--max-limit` | max=3, placeholder="Enter a tag and press add" |
| Wide | `components-tags-input--wide` | placeholder="Enter a tag and press add", wide=true |
| Has Error | `components-tags-input--has-error` | placeholder="Enter a tag and press add", hasError=true |
| Disabled | `components-tags-input--disabled` | placeholder="Enter a tag and press add", disabled=true |

**Rendered markup — “Default”**

```html
<s-tags id="tags-orxk1uj52" placeholder="Enter a tag and press add" button-label="Add" tag-theme="default" tags-size="sm" class="flex flex-col gap-2 hydrated">
</s-tags>
```

---

### 2.34 Telephone Input

**Tag:** `<s-tel-input>`  
**Storybook:** `components-telephone-input` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-telephone-input>

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `disabled` |  | boolean |  |  | Disabled state |
| `hasError` |  | boolean |  |  | Error state |
| `placeholder` | string | text |  |  | Input placeholder |
| `required` |  | boolean |  |  | Required state |
| `size` |  | select |  |  | Input size |
| `value` |  | text |  |  | Input value |
| `wide` | boolean | boolean |  |  | Wide state |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the value of the telephone input changes. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-telephone-input--default` | placeholder="Enter phone number", wide=true |
| Large | `components-telephone-input--large` | placeholder="Enter phone number", wide=true, size="lg" |
| Has Error | `components-telephone-input--has-error` | placeholder="Enter phone number", wide=true, hasError=true |
| Disabled | `components-telephone-input--disabled` | placeholder="Enter phone number", wide=true, disabled=true |

**Rendered markup — “Default”**

```html
<div class="flex items-start flex-col gap-4 min-h-[400px]">
  <s-tel-input value="" placeholder="Enter phone number" wide="" class="w-full md ltr hydrated" dir="ltr">
  </s-tel-input>
</div>
```

---

### 2.35 Textarea

**Tag:** `<s-textarea>`  ·  **Related elements:** `<s-button>`, `<s-icon>`  
**Storybook:** `components-textarea` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-textarea>

Textarea component is used for multiline text input, allowing users to enter longer text content with various configuration options.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `aiSuggestion` |  | object | `undefined` |  | AI suggestion config (object or JSON string): { enabled, regenerable, source }. When `enabled`, the textarea gets the Moshammer AI highlight and reveals the `actions` slot (regenerate / dismiss). |
| `desc` | string | text | `undefined` |  | Textarea description, you can use it to add a description to the textarea |
| `disabled` | boolean | boolean | `false` |  | Disabled state |
| `feature` | boolean | boolean |  |  |  |
| `fullHeight` | boolean | boolean | `false` |  | Make textarea take full height of its container |
| `hasError` | boolean | boolean | `false` |  | Error state |
| `hasPreview` | boolean | boolean | `false` |  | Enable textarea preview |
| `max` |  | number | `undefined` |  | Maximum number of characters allowed |
| `multilingual` | boolean | boolean | `false` |  | Enables multilingual support, enabled when value is an array of strings |
| `placeholder` | string | text | `Enter your text here...` |  | Textarea placeholder |
| `required` | boolean | boolean | `false` |  | Required state |
| `rows` | number | number | `4` |  | Number of visible text lines for the textarea |
| `showCount` | boolean | boolean | `false` |  | Show a live `current/max` character counter below the field. Requires `max`. Turns danger-red when the field has `has-error`. |
| `value` | string | text | `Default textarea value...` |  | Textarea value |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the value of the textarea changes. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-textarea--default` | value="Default textarea value...", placeholder="Enter your text here...", disabled=false, hasError=false, hasPreview=false |
| Has Description | `components-textarea--has-description` | value="Default textarea value...", placeholder="Enter your text here...", disabled=false, hasError=false, hasPreview=false |
| Has Preview | `components-textarea--has-preview` | value="Default textarea value...", placeholder="Enter your text here...", disabled=false, hasError=false, hasPreview=true |
| Multilingual | `components-textarea--multilingual` | value="Default textarea value...", placeholder="Enter your text here...", disabled=false, hasError=false, hasPreview=false |
| With Max Length | `components-textarea--with-max-length` | value="This textarea has a maximum character l, placeholder="Enter your text here...", disabled=false, hasError=false, hasPreview=false |
| With Character Counter | `components-textarea--with-character-counter` | value="Sample text \u2014 try typing to watch , placeholder="Enter your text here...", disabled=false, hasError=false, hasPreview=false |
| Has Error | `components-textarea--has-error` | value="Default textarea value...", placeholder="Enter your text here...", disabled=false, hasError=true, hasPreview=false |
| Disabled | `components-textarea--disabled` | value="Default textarea value...", placeholder="Enter your text here...", disabled=true, hasError=false, hasPreview=false |
| Ai Suggestion | `components-textarea--ai-suggestion` | value="AI generated product description...", placeholder="Enter your text here...", disabled=false, hasError=false, hasPreview=false |

**Rendered markup — “Default”**

```html
<s-textarea value="Default textarea value..." placeholder="Enter your text here..." rows="3" feature="true" class="ltr hydrated">
</s-textarea>
```

---

### 2.36 Toggle

**Tag:** `<s-toggle>`  
**Storybook:** `components-toggle` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-toggle>

Toggle component is used to switch between two states, typically on/off or enabled/disabled. It provides a clear visual indication of the current state and allows users to toggle between states with a single interaction.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `checked` | boolean | boolean | `false` |  | Checked state |
| `desc` | string | text |  |  | Toggle description |
| `disabled` | boolean | boolean | `false` |  | Disabled state |
| `feature` |  | text | `true (omitted in HTML when unset)` |  | Feature guard: `true` (default), `false` to show gated UI + tag, a flag key string, or JSON for structured state (same as the `feature` attribute on the component). |
| `hasError` | boolean | boolean | `false` |  | Error state |
| `ischecked` | boolean | boolean | `false` |  | Checked state (deprecated, and will be removed soon) |
| `label` | string | text | `Toggle option` |  | Toggle label |
| `layout` | string | select | `start` |  | Layout position, start or end |
| `loading` | boolean | boolean | `false` |  | Loading state |
| `required` | boolean | boolean | `false` |  | Required state |
| `size` | string | text |  |  |  |
| `wide` | boolean | boolean | `true` |  | Full width |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the value of the toggle switch changes. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-toggle--default` | label="Toggle option", desc="This is a description for the toggle", size="md", layout="start", checked=false |
| Checked | `components-toggle--checked` | label="Toggle option", desc="", size="md", layout="start", checked=true |
| Layout End | `components-toggle--layout-end` | label="Toggle option", desc="This is a description for the toggle", size="md", layout="end", checked=false |
| Required | `components-toggle--required` | label="Toggle option", desc="", size="md", layout="start", checked=false |
| Has Description | `components-toggle--has-description` | label="Toggle option", desc="This is a description for the toggle", size="md", layout="start", checked=false |
| Loading | `components-toggle--loading` | label="Toggle option", desc="", size="md", layout="start", checked=false |
| Is Checked Property | `components-toggle--is-checked-property` | label="Toggle option", desc="", size="md", layout="start", checked=false |
| Disabled | `components-toggle--disabled` | label="Toggle option", desc="", size="md", layout="start", checked=false |
| Disabled Checked | `components-toggle--disabled-checked` | label="Toggle option", desc="", size="md", layout="start", checked=true |
| Has Error | `components-toggle--has-error` | label="Toggle option", desc="", size="md", layout="start", checked=false |
| Feature Gated | `components-toggle--feature-gated` | label="Toggle option", desc="This is a description for the toggle", size="md", layout="start", checked=false |

**Rendered markup — “Default”**

```html
<s-toggle label="Toggle option" desc="This is a description for the toggle" size="md" layout="start" wide="" class="s-toggle w-full start md ltr hydrated">
</s-toggle>
```

---

### 2.37 Tooltip

**Tag:** `<s-tooltip>`  ·  **Related elements:** `<s-button>`, `<s-tooltip-action>`, `<s-icon>`, `<s-avatar>`, `<s-tag>`  
**Storybook:** `components-tooltip` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-tooltip>

Tooltip component provides contextual information when users hover or click on an element. It displays helpful content in a small overlay positioned relative to the trigger element.

It exposes three slots:

- `toggle`: the trigger element, any element can be used (button, avatar, icon, inline text…).
- `title`: the tooltip heading, it is bolded by the component.
- default: the tooltip body, it accepts any markup, including `<s-tooltip-action>` actions.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `layout` | string | select | `normal` | tight, normal, relaxed | Tooltip layout |
| `placement` | string | select | `top center` | bottom, bottom-start, bottom-end, top, top-start, top-end, right, right-start, right-end,  | Tooltip placement |
| `theme` | string | select | `default` | default, secondary, white, feature, danger | Tooltip theme |
| `toggleAction` | string | select | `hover` | hover, click | Toggle action |
| `width` | string | text | `300px` |  | Tooltip width |

**Slots**

| Slot | Description |
|---|---|
| `content` | Default slot, raw HTML for the tooltip body. It accepts any markup: paragraphs, lists, media, `s-tooltip-action` or `s-button` actions. |
| `title` | `title` slot, the content is rendered inside `<h4 slot="title">` so inline markup such as icons is supported. Leave it empty to render a tooltip without a title. |
| `toggle` | `toggle` slot, raw HTML for the trigger element, it must carry `slot="toggle"`. Any element works: `s-button`, `s-avatar`, `s-tag`, an icon or plain inline text. |

**Events**

| Event | Description |
|---|---|
| `onclose` | Emitted when the tooltip is closed. |
| `onopen` | Emitted when the tooltip is opened. |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-tooltip--default` | theme="default", placement="top", toggleAction="hover", width="300px", layout="normal" |
| Secondary | `components-tooltip--secondary` | theme="secondary", placement="top", toggleAction="hover", width="300px", layout="normal" |
| White | `components-tooltip--white` | theme="white", placement="top", toggleAction="hover", width="300px", layout="normal" |
| Danger | `components-tooltip--danger` | theme="danger", placement="top", toggleAction="hover", width="300px", layout="normal" |
| Top Start | `components-tooltip--top-start` | theme="default", placement="top-start", toggleAction="hover", width="300px", layout="normal" |
| Top End | `components-tooltip--top-end` | theme="default", placement="top-end", toggleAction="hover", width="300px", layout="normal" |
| Bottom Center | `components-tooltip--bottom-center` | theme="default", placement="bottom", toggleAction="hover", width="300px", layout="normal" |
| Bottom Start | `components-tooltip--bottom-start` | theme="default", placement="bottom-start", toggleAction="hover", width="300px", layout="normal" |
| Bottom End | `components-tooltip--bottom-end` | theme="default", placement="bottom-end", toggleAction="hover", width="300px", layout="normal" |
| Center Start | `components-tooltip--center-start` | theme="default", placement="left", toggleAction="hover", width="300px", layout="normal" |
| Center End | `components-tooltip--center-end` | theme="default", placement="right", toggleAction="hover", width="300px", layout="normal" |
| Click Toggle | `components-tooltip--click-toggle` | theme="default", placement="top", toggleAction="click", width="300px", layout="normal" |
| Tight | `components-tooltip--tight` | theme="default", placement="top", toggleAction="hover", width="300px", layout="tight" |
| Relaxed | `components-tooltip--relaxed` | theme="default", placement="top", toggleAction="hover", width="300px", layout="relaxed" |
| Custom Width | `components-tooltip--custom-width` | theme="default", placement="top", toggleAction="hover", width="500px", layout="normal" |
| Icon Trigger | `components-tooltip--icon-trigger` | theme="default", placement="top", toggleAction="hover", width="260px", layout="normal" |
| Avatar Trigger | `components-tooltip--avatar-trigger` | theme="white", placement="bottom-start", toggleAction="hover", width="280px", layout="normal" |
| Inline Text Trigger | `components-tooltip--inline-text-trigger` | theme="secondary", placement="top", toggleAction="hover", width="280px", layout="tight" |
| Title With Icon | `components-tooltip--title-with-icon` | theme="white", placement="top", toggleAction="hover", width="300px", layout="normal" |
| Without Title | `components-tooltip--without-title` | theme="default", placement="top", toggleAction="hover", width="240px", layout="tight" |
| List Content | `components-tooltip--list-content` | theme="white", placement="top", toggleAction="hover", width="320px", layout="normal" |
| Key Value Content | `components-tooltip--key-value-content` | theme="white", placement="top", toggleAction="hover", width="300px", layout="normal" |
| Media Content | `components-tooltip--media-content` | theme="white", placement="top", toggleAction="hover", width="300px", layout="normal" |
| Multiple Actions | `components-tooltip--multiple-actions` | theme="white", placement="top", toggleAction="click", width="320px", layout="normal" |
| Feature Locked | `components-tooltip--feature-locked` | theme="feature", placement="top", toggleAction="hover", width="300px", layout="normal" |
| Media Card With Image | `components-tooltip--media-card-with-image` | theme="white", placement="bottom", toggleAction="hover", width="400px", layout="normal" |
| Media Card With Video | `components-tooltip--media-card-with-video` | theme="white", placement="bottom", toggleAction="click", width="400px", layout="normal" |

**Rendered markup — “Default”**

```html
<div style="min-height: 30vh;" class="flex items-center justify-center">
  <s-tooltip theme="default" width="300px" placement="top" toggle-action="hover" layout="normal" class="s-tooltip s-tooltip--default ltr hydrated" data-toggle="hover">
    <s-button slot="toggle" theme="default" class="s-btn s-btn--default default md ltr hydrated" target="_self">Show Tooltip</s-button>
    <h4 slot="title">Tooltip title</h4>
    <article>
      <p>This is the tooltip content that provides helpful information to users.</p>
      <s-tooltip-action class="hydrated" theme="default">Click here to learn more</s-tooltip-action>
    </article>
  </s-tooltip>
</div>
```

---

### 2.38 Uploader

**Tag:** `<s-uploader>`  ·  **Related elements:** `<s-button>`  
**Storybook:** `components-uploader` · <https://dashboard-ui-components.pages.dev/?path=/docs/components-uploader>

Uploader component allows users to upload files with various layouts and configurations. It supports drag & drop, multiple files, file type restrictions, and preview functionality.

**Props**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `allowAlt` | boolean | boolean | `true` |  | Show the ALT text button/editor under each file preview |
| `autoUpload` | boolean | boolean | `false` |  | Enable auto upload to server (deprecated, use server.instantUpload instead) |
| `buttonLabel` | string | text | `Submit` |  | Button text for file selection |
| `cropShapes` | object | text | `undefined` |  | Crop shapes for image cropping (e.g., '1:1' or ['1:1', '9:16', '1.91:1']). Restricts cropping to only these shapes. |
| `desc` | string | text | `""` |  | Description text for the uploader |
| `disabled` | boolean | boolean | `false` |  | Disabled state |
| `editable` | boolean | boolean | `true` |  | Allow users to edit files |
| `fileSize` | string | text | `"2MB"` |  | Maximum file size |
| `filesAllowed` | string | select | `"all"` | all, images, videos, fonts, file | Allowed file types |
| `has3D` | boolean | boolean | `false` |  | Enable 3D image support |
| `hasError` | boolean | boolean | `false` |  | Error state |
| `hasPreview` | boolean | boolean | `false` |  | Show only preview without uploader area |
| `headers` | object | text | `undefined` |  | Custom headers for upload (deprecated, use server.headers instead) |
| `hideBrowseButton` | boolean | boolean | `false` |  | Hide the built-in browse button and keep only the actions slotted by the consumer (thumbnail layout only) |
| `hideSize` | boolean | boolean | `false` |  | Hide file size display |
| `instantEdit` | boolean | boolean | `false` |  | Automatically open the image editor after upload completes (thumbnail layout only) |
| `items` | string | text | `"[]"` |  | Initial files to display |
| `label` | string | text | `Browse or drag and drop files here` |  | Label text for the uploader |
| `layout` | string | select | `"drag-drop"` | inline, drag-drop, thumbnail | Uploader layout type |
| `loading` | boolean | boolean | `false` |  | Loading state |
| `max` | number | number | `-1` |  | Maximum number of files (-1 for unlimited) |
| `maxVideos` |  | number | `undefined` |  | Opt-in cap on video files only (images stay governed by `max`). Unset = no video cap. |
| `method` | object | text | `null` |  | Upload method for inline layout |
| `multiple` | boolean | boolean | `false` |  | Allow multiple file upload |
| `name` | string | text | `"file"` |  | Name attribute for the input |
| `noBorder` | boolean | boolean | `false` |  | Remove border styling |
| `payloadParameters` | object | text | `null` |  | Additional payload parameters (deprecated, use server.upload.additionalRequestData instead) |
| `placeholder` | string | text | `Choose a file...` |  | Placeholder text for inline layout |
| `selectable` | boolean | boolean | `true` |  | Allow users to select files as primary |
| `server` | object | object | `undefined` |  | Server configuration object for upload, edit, and remove operations |
| `sortable` | boolean | boolean | `true` |  | Enable file sorting |
| `src` | object | text | `undefined` |  | Upload URL (deprecated, use server.url instead) |
| `verticalThumbnail` | boolean | boolean | `false` |  | Use vertical thumbnail layout |

**Events**

| Event | Description |
|---|---|
| `altTextChange` | Event emitted when a file's alt text is changed. Provides the file information. |
| `edit` | Event emitted when a file is edited. Provides the edited file information. |
| `fileUpload` | Event emitted when an item is uploaded (deprecated, use upload instead). |
| `remove` | Event emitted when a file is deleted. Provides the deleted file information. |
| `sort` | Event emitted when a file is reordered. Provides file, newIndex, and oldIndex. |
| `upload` | Event emitted when an item is uploaded. Provides files, file, and error information. |

**Editor options**

| Prop | Type | Control | Default | Options | Description |
|---|---|---|---|---|---|
| `cropShapes` | object | text | `undefined` |  | Crop shapes for image cropping (e.g., '1:1' or ['1:1', '9:16', '1.91:1']). Restricts cropping to only these shapes. |
| `instantEdit` | boolean | boolean | `false` |  | Automatically open the image editor after upload completes (thumbnail layout only) |

**Stories**

| Story | id | Key args |
|---|---|---|
| Default | `components-uploader--default` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Inline | `components-uploader--inline` | name="file", layout="inline", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Thumbnail | `components-uploader--thumbnail` | name="file", layout="thumbnail", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Thumbnail Multiple | `components-uploader--thumbnail-multiple` | name="file", layout="thumbnail", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Multiple | `components-uploader--multiple` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Images Only | `components-uploader--images-only` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Videos Only | `components-uploader--videos-only` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Thumbnail Video Player | `components-uploader--thumbnail-video-player` | name="file", layout="thumbnail", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| With Predefined Items | `components-uploader--with-predefined-items` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Preview Mode | `components-uploader--preview-mode` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Non Selectable | `components-uploader--non-selectable` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Non Editable | `components-uploader--non-editable` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Non Sortable | `components-uploader--non-sortable` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Hide File Size | `components-uploader--hide-file-size` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Alt Disabled | `components-uploader--alt-disabled` | name="file", layout="thumbnail", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| No Border | `components-uploader--no-border` | name="file", layout="inline", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Vertical Thumbnail | `components-uploader--vertical-thumbnail` | name="file", layout="thumbnail", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| Disabled | `components-uploader--disabled` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| With Server Config | `components-uploader--with-server-config` | name="file", layout="drag-drop", label="Browse or drag and drop files here", placeholder="Choose a file...", buttonLabel="Submit" |
| With Custom Actions | `components-uploader--with-custom-actions` |  |
| External Editor Trigger | `components-uploader--external-editor-trigger` |  |

**Rendered markup — “Default”**

```html
<s-uploader name="file" layout="drag-drop" label="Browse or drag and drop files here" placeholder="Choose a file..." button-label="Submit" files-allowed="all" max="-1" file-size="2MB" selectable="" editable="" sortable="" items="[]" class="s-uploader--selectable s-uploader--sortable drag-drop ltr hydrated">
  <p slot="feedback">The suitable image size is 350X263 pixels</p>
</s-uploader>
```

---

## 3. Appendix — story markup index

Every story can be opened standalone at:

```
https://dashboard-ui-components.pages.dev/iframe.html?id=<story-id>&viewMode=story
```

…and the full index of stories is machine-readable at `https://dashboard-ui-components.pages.dev/index.json`.
