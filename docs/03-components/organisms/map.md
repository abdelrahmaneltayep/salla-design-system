# Map

> Embedded map for addresses and branches.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| organism | Data display | 2 - Standalone | existing | figma, storybook | `<s-maps>` |

## Props

| Prop | Values / type |
|---|---|
| `center` | latlng |
| `markers` | array |
| `language` | `ar`, `en` |

## How to build it

Build as **separate, explicitly named components**. Share styling through tokens and small internal layout helpers, not through a shared prop bag.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Maps` | Maps | 2 | Language: Default, English |

## Source in the Twilight Storybook today

### `<s-maps>`

[components-maps](https://dashboard-ui-components.pages.dev/?path=/docs/components-maps) · 4 stories · Maps component provides an interactive map interface with search functionality and location services.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `apiKey` | string |  |  | Google Maps API Key. |
| `hasCurrentLocationButton` | boolean | `false` |  | Show or hide the 'Go to current location' button. |
| `height` | string | `300px` |  | Map wrapper height. Accepts CSS height property values. |
| `latitude` | number | `21.4255186` |  | The latitude coordinate of the map's center |
| `longitude` | number | `39.7858435` |  | The longitude coordinate of the map's center |
| `searchPlaceholder` | string | `Search...` |  | Search input placeholder. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-maps--default), [With Current Location Button](https://dashboard-ui-components.pages.dev/?path=/story/components-maps--with-current-location-button), [Custom Coordinates](https://dashboard-ui-components.pages.dev/?path=/story/components-maps--custom-coordinates), [Custom Height](https://dashboard-ui-components.pages.dev/?path=/story/components-maps--custom-height)

**Rendered markup (default story)**

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
_Generated from `catalog/components.json` (id `map`). Edit the catalog, not this file._
