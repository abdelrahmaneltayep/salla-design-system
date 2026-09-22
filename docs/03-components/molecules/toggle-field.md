# SwitchField

> Switch + label with the switch at inline-start or inline-end.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Selection | 3 - Base + Global | existing | figma, storybook | `<s-toggle> (label + desc, layout start\|end)` |

## Props

| Prop | Values / type |
|---|---|
| `label` | string |
| `description` | string |
| `position` | `start`, `end` |
| `checked` | boolean |
| `loading` | boolean |
| `disabled` | boolean |

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **Switch**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `toggleField` | Toggle | 20 | Language: Arabic, English; togglePosition: ending, starting; disabled: false, true; selected: false, true; loading: false, true |

## Source in the Twilight Storybook today

### `<s-toggle>` — label + desc, layout start|end

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
_Generated from `catalog/components.json` (id `toggle-field`). Edit the catalog, not this file._
