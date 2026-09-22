# ColorPickerField

> Colour swatch + hex entry with a picker popover.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | figma, storybook | `<s-color-picker>` |

## Props

| Prop | Values / type |
|---|---|
| `value` | hex |
| `presets` | array |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

- Figma component set: `colorPicker 1d931b4a`

_No matching frame in the current Figma library._

## Source in the Twilight Storybook today

### `<s-color-picker>`

[components-colorpicker](https://dashboard-ui-components.pages.dev/?path=/docs/components-colorpicker) · 6 stories · A color picker field component that allows users to select colors using a color input. It supports various states and configurations for different use cases.

Related elements: `<s-icon>`

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `disabled` | boolean | `false` |  | Disabled state |
| `hasError` | boolean | `false` |  | Error state |
| `noBorder` | boolean | `false` |  | Border-less field ( required in certain cases) |
| `noLabel` | boolean | `false` |  | Label-less field ( required in certain cases) |
| `required` | boolean | `false` |  | Required state |
| `value` | string | `#000000` |  | Field value |

**Events**

| Event | Description |
|---|---|
| `colorChanged` | Emitted when the color changes. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-colorpicker--default), [Initial Value](https://dashboard-ui-components.pages.dev/?path=/story/components-colorpicker--initial-value), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-colorpicker--has-error), [Label Less](https://dashboard-ui-components.pages.dev/?path=/story/components-colorpicker--label-less), [Border Less](https://dashboard-ui-components.pages.dev/?path=/story/components-colorpicker--border-less), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-colorpicker--disabled)

**Rendered markup (default story)**

```html
<s-color-picker value="#000000" @colorchanged="ev=&gt;console.log(" color="" changed:",ev.detail)"="" class="ltr hydrated">
  <s-icon icon="hgi-stroke hgi-color-picker" slot="start" class="hydrated">
  </s-icon>
</s-color-picker>
```


---
_Generated from `catalog/components.json` (id `color-picker-field`). Edit the catalog, not this file._
