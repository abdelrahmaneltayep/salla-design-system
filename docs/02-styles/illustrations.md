# Illustrations

Spot illustrations for empty states, onboarding and success moments. Source frames: `Illustration` (variant web / mobile) and `Illustrations Collection` (20 named pieces) in the Merchant DS.

## Inventory (from Figma)

`search field not found` · `product custom fields` · `product options` · `add brands` · `export template` · `no values` · `add template` · `add category` · `classifications` · `no codes` · `add products` · `product measurements` · `add to cart` · `info settings` · `order filters empty` · (5 more in the collection frame)

## Usage

- Illustrations appear only inside `EmptyState` (organism) and onboarding `WizardPage` steps. Never as decoration in forms or tables.
- One illustration per screen state.
- Two sizes: `web` (~200px) and `mobile` (~140px), chosen by window size class.
- Illustrations use the brand palette (`ref.palette.teal.*`, `gray.*`) plus at most one status accent; they must read in both LTR and RTL without mirroring (avoid text and directional arrows inside artwork).

## Component

```
<Illustration name="add-products" device="web" />
```

Names migrate to kebab-case ids (`order-filters-empty`). The collection frame becomes `assets/illustrations/` with one SVG per id; `Illustration` is a thin atom that loads by id.

## Adding a new illustration

1. Draw at 200×200 on the web artboard, export mobile at 140.
2. Add to `Illustrations Collection` with the kebab-case id as the layer name.
3. Add the id to `assets/illustrations/index.json` and reference it from the `EmptyState` story.
