# Salla Design System

The merchant dashboard design system for Salla, restructured on **Atomic Design** (Brad Frost) with **Material Design 3** as the structural reference.

It takes what Salla has today, the `Merchant - Storybook DS` Figma library (17 sections, 117 component frames, ~10,000 variants) and the public Twilight Storybook at `dashboard-ui-components.pages.dev`, and reorganises it into a layered system: tokens, foundations, styles, and components sorted by atomic level and Material category.

> Status: **v0.2 - structure, tokens and documentation**. Token values are read from the Figma library (`catalog/figma-tokens-harvest.json`). Component code is not in this repo yet; every component page carries a build plan (structure type, props, tokens) so implementation can start from it.

**Browse the docs:** run `python3 scripts/build-site.py` and open `site/index.html`, a single-file site with foundations, styles, every component page and live token-rendered examples.

## How the system is layered

```
┌───────────────────────────────────────────────────────────────┐
│  PAGES        real merchant screens (Orders, Products ...)     │  Atomic: pages
├───────────────────────────────────────────────────────────────┤
│  TEMPLATES    list page, list-detail, form page, wizard        │  Atomic: templates
├───────────────────────────────────────────────────────────────┤
│  ORGANISMS    Header, Table, DropDownList, Alertbox, Steps ... │  Atomic: organisms
├───────────────────────────────────────────────────────────────┤
│  MOLECULES    TextField, CheckboxField, Status, Breadcrumb ... │  Atomic: molecules
├───────────────────────────────────────────────────────────────┤
│  ATOMS        Button, Icon, Checkbox, Toggle, Avatar, Loader   │  Atomic: atoms
├───────────────────────────────────────────────────────────────┤
│  STYLES       color · typography · spacing · shape · elevation │  Material: Styles
│               icons · illustrations · motion                   │
├───────────────────────────────────────────────────────────────┤
│  FOUNDATIONS  tokens · layout · interaction states · a11y      │  Material: Foundations
│               content & localisation (AR/EN, RTL)              │
└───────────────────────────────────────────────────────────────┘
```

Every component is classified on three axes:

| Axis | Values | Why |
|---|---|---|
| **Atomic level** | atom · molecule · organism · template · page | Where it sits in the composition hierarchy |
| **Material category** | Actions · Communication · Containment · Navigation · Selection · Text inputs · Data display | How designers find it (Material's component taxonomy, plus Data display for tables) |
| **Structure type** | 1 Configurable · 2 Standalone · 3 Base + Global · 4 Slot / Composition · 5 Headless | How engineers build it, from the internal *Component Structure Types* document |

## Repository map

```
salla-design-system/
├── README.md
├── docs/
│   ├── 00-overview/
│   │   ├── methodology.md              Atomic × Material: how the two fit together
│   │   ├── component-structure-types.md The 5 build patterns and which component uses which
│   │   ├── current-state-audit.md      What Salla has today and what is inconsistent
│   │   ├── migration-map.md            Old Figma section / Storybook story → new home
│   │   └── naming-conventions.md       Component, prop, token and file naming rules
│   ├── 01-foundations/                 Material "Foundations"
│   │   ├── design-tokens.md · layout.md · interaction-states.md
│   │   ├── accessibility.md · content-and-localization.md
│   ├── 02-styles/                      Material "Styles"
│   │   ├── color.md · typography.md · spacing.md · shape.md · elevation.md
│   │   ├── icons.md · illustrations.md · motion.md
│   └── 03-components/                  Atomic levels (generated from catalog/components.json)
│       ├── README.md                   Index by atomic level and by Material category
│       ├── atoms/ · molecules/ · organisms/ · templates/ · pages/
├── tokens/
│   ├── tokens.json                     W3C DTCG format, three tiers: ref → sys → comp
│   ├── css/tokens.css                  CSS custom properties (--ref-*, --sys-*, --comp-*)
│   └── tailwind/preset.js              Tailwind preset mapped onto the CSS variables
├── catalog/
│   ├── components.json                 The source of truth: every component, its level, category,
│   │                                   structure type, props, states, Figma frame and Storybook story
│   ├── figma-inventory.json            Raw extract of the Figma library (sections → frames → variant props)
│   └── figma-tokens-harvest.json       Variable name → value pairs read from 20 Figma frames (token evidence)
├── assets/icons/icon-inventory.json    4,049 icon names + styles from Icons DS_V.1.fig
├── scripts/
│   ├── build-catalog.py                Regenerates docs/03-components from the catalog
│   └── build-site.py                   Bundles docs + catalog + examples into site/index.html
├── site/index.html                     The documentation site (generated, single file)
└── preview/index.html                  Live examples of 20 components built only from tokens.css
```

## Quick start

```bash
# Regenerate the component docs after editing catalog/components.json
python3 scripts/build-catalog.py

# Preview tokens and atoms
open preview/index.html
```

Use the tokens in product code:

```css
@import "salla-design-system/tokens/css/tokens.css";
.my-card { background: var(--sys-color-surface); border-radius: var(--sys-shape-small); padding: var(--sys-space-md); }
```

```js
// tailwind.config.js
module.exports = { presets: [require('./tokens/tailwind/preset')], content: ['./src/**/*.{html,js,ts,vue}'] };
```

## Sources of truth

| Source | What it gives us | Where it is captured |
|---|---|---|
| Figma `Merchant - Storybook DS` (file `zuGhoKg2BaBIYUreKuSBGY`, branch `dnmyqzYKK9dUJjVHuIWMDS`, page *Main Components (Full)*) | Component anatomy, variants, states, token names and values | `catalog/figma-inventory.json`, `tokens/tokens.json` |
| Figma `Icons DS_V.1` | Icon set: 4,049 names, Stroke/Solid/Bulk/Twotone/Duotone × Rounded/Sharp | `assets/icons/icon-inventory.json`, `docs/02-styles/icons.md` |
| Storybook `dashboard-ui-components.pages.dev` (Twilight web components) | Shipped component names and stories | `catalog/components.json` → `storybook` field |
| *Component Structure Types* (internal PDF, 2025-07-06) | The five build patterns | `docs/00-overview/component-structure-types.md` |
| Material Design 3 (m3.material.io) | Foundations / Styles / Components structure, token tiers, category taxonomy | `docs/00-overview/methodology.md` |

## Next steps

1. Confirm the values marked `assumed` in `tokens/tokens.json` against Figma and add elevation styles to the library.
2. Rename Figma frames and variables per `docs/00-overview/migration-map.md` (typos, `--` prefixes, the two spacing scales).
3. Implement atoms first (Button, Icon, Checkbox, Radio, Toggle, Loader, Avatar) as Base + Global or Configurable components, then molecules, following each component page's build plan.
4. Wire Storybook to the same catalog so story titles follow `Level / Category / Component`.
