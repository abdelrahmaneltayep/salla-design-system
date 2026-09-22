# Switch

> On/off control (Material: Switch). Has a loading state, which is unusual and worth keeping because Salla toggles often trigger a server call.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| atom | Selection | 3 - Base + Global | existing | figma, storybook | `<s-toggle>` |

## Anatomy

- track
- thumb
- loading spinner (in thumb)

## Props

| Prop | Values / type |
|---|---|
| `checked` | boolean |
| `size` | `sm (16px)`, `default (24px, track 39px)` |
| `loading` | boolean |
| `disabled` | boolean |

## States

- off
- on
- loading
- disabled
- focus-visible

## Tokens

- comp.toggle.*
- sys.color.primary
- sys.shape.full

## RTL and localisation

Thumb travels inline-start -> inline-end; on/off direction mirrors in RTL.

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

## Notes and migration

Figma exports the whole toggle as one SVG per variant; rebuild it from primitives so the track and thumb take tokens. Keep the name Toggle in Storybook for continuity, alias Switch in docs.

## Source in Figma today

- Figma node: `12411:21835`

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `Toggle` | Toggle | 20 | Language: Arabic, English; selected: false, true; disabled: false, true; loading: false, true; size: default-24px, sm-16px |

## Source in the Twilight Storybook today

### `<s-toggle>`

[components-toggle](https://dashboard-ui-components.pages.dev/?path=/docs/components-toggle) · 11 stories · Toggle component is used to switch between two states, typically on/off or enabled/disabled. It provides a clear visual indication of the current state and allows users to toggle between states with a single interaction.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `checked` | boolean | `false` |  | Checked state |
| `desc` | string |  |  | Toggle description |
| `disabled` | boolean | `false` |  | Disabled state |
| `feature` | text | `true (omitted in HTML when unset)` |  | Feature guard: `true` (default), `false` to show gated UI + tag, a flag key string, or JSON for structured state (same as the `feature` attribute on the component). |
| `hasError` | boolean | `false` |  | Error state |
| `ischecked` | boolean | `false` |  | Checked state (deprecated, and will be removed soon) |
| `label` | string | `Toggle option` |  | Toggle label |
| `layout` | string | `start` |  | Layout position, start or end |
| `loading` | boolean | `false` |  | Loading state |
| `required` | boolean | `false` |  | Required state |
| `size` | string |  |  |  |
| `wide` | boolean | `true` |  | Full width |

**Events**

| Event | Description |
|---|---|
| `valueChanged` | Emitted when the value of the toggle switch changes. |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-toggle--default), [Checked](https://dashboard-ui-components.pages.dev/?path=/story/components-toggle--checked), [Layout End](https://dashboard-ui-components.pages.dev/?path=/story/components-toggle--layout-end), [Required](https://dashboard-ui-components.pages.dev/?path=/story/components-toggle--required), [Has Description](https://dashboard-ui-components.pages.dev/?path=/story/components-toggle--has-description), [Loading](https://dashboard-ui-components.pages.dev/?path=/story/components-toggle--loading), [Is Checked Property](https://dashboard-ui-components.pages.dev/?path=/story/components-toggle--is-checked-property), [Disabled](https://dashboard-ui-components.pages.dev/?path=/story/components-toggle--disabled), [Disabled Checked](https://dashboard-ui-components.pages.dev/?path=/story/components-toggle--disabled-checked), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-toggle--has-error), [Feature Gated](https://dashboard-ui-components.pages.dev/?path=/story/components-toggle--feature-gated)

**Rendered markup (default story)**

```html
<s-toggle label="Toggle option" desc="This is a description for the toggle" size="md" layout="start" wide="" class="s-toggle w-full start md ltr hydrated">
</s-toggle>
```


---
_Generated from `catalog/components.json` (id `toggle`). Edit the catalog, not this file._
