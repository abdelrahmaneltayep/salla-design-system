# Icons

Source: the `Icons DS_V.1` Figma library (exported 2026-07-07). Inventory: `assets/icons/icon-inventory.json`.

## What the library contains

| Property | Values | Count |
|---|---|---|
| Names | kebab-case, numbered where a family has several forms (`search-01`, `search-02`, `mail-open-01`) | **4,049** unique |
| Style | Stroke (3,889), Solid (3,889), Bulk (5), Twotone (3), Duotone (3) | |
| Type | Rounded (default), Sharp (3) | |
| Categories | Add Remove Delete · Alert Notification · Arrows · Artificial Intelligence · Award Reward · Bookmark Favourite · Brand logo · Building Landmark Places · Business and finance · Chat Bubbles · Check Validation · Cloth Accessories · Date and Time · Download Upload · Edit Formatting · Files Folders · Filter Sorting · Food Drink · Game Sports · Geometric Shapes · Global Map · Gym Fitness · Hand Gestures · Image Camera Video · Layout Borders · Link Unlink · Login Logout · More Menu · Mouse Cursors · Science Technology · Smiley Emojis · Wifi Signal · … | 60 category frames |

The Merchant DS consumes the set through two frames, `Icons/Outline` and `Icons/Filled`, and names instances `{name}-outline` / `{name}-filled` (`add-01-outline`, `arrow-down-01-outline`, `cancel-01-outline`, `information-circle-outline`, `file-01-outline`, `star-outline` were seen in component code). The Storybook still exposes the older `sicon-*` icon font.

## Shipped subset

Ship **Stroke** (as `outline`) and **Solid** (as `filled`), **Rounded** only. Bulk, Twotone, Duotone and Sharp stay in the source library; they are not part of the system.

## The Icon atom

```
<Icon name="add-01" style="outline" size="sm" />
```

| Prop | Values | Default |
|---|---|---|
| `name` | any inventory name | required |
| `style` | `outline` (Stroke), `filled` (Solid) | `outline` |
| `size` | `sm` 16 ✓, `md` 18 ✓, `lg` 20, `xl` 24 | `sm` in buttons and fields, `md` in alerts |
| `mirrorInRtl` | boolean | true for directional glyphs |
| `label` | string; omit for decorative icons (`aria-hidden`) | – |

Colour is `currentColor`; icons never carry their own colour tokens.

## Sizes in context (verified)

| Context | Size |
|---|---|
| Button, IconButton, field leading / trailing icons | 16px |
| Alert, Status leading icon | 18px |
| NavigationItem, Tab | 20px |
| EmptyState, MobileRow leading | 24px |

## Naming and migration

| Today | New |
|---|---|
| `add-01-outline` (Figma instance) | `name="add-01" style="outline"` |
| `sicon-add` (Storybook font class) | alias table → `add-01`; retire the font after migration |
| `Style=Stroke, Type=Rounded` (library variant) | `style="outline"` |
| `Style=Solid, Type=Rounded` | `style="filled"` |

## Delivery

- SVG sprite per style, generated from the Figma export; tree-shakeable named exports for frameworks.
- The 265 `Flag` glyphs and the brand `SocialIcon` set are separate atoms and separate sprites.
- Directional icons (arrows, chevrons, undo/redo, login/logout, indent) are tagged `mirror: true` in the inventory build so `mirrorInRtl` defaults correctly.
