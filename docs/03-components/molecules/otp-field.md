# OtpField

> Single-digit boxes for verification codes.

| Atomic level | Material category | Structure type | Status | Sources | Twilight |
|---|---|---|---|---|---|
| molecule | Text inputs | 3 - Base + Global | existing | figma, storybook | `<s-otp>` |

## Props

| Prop | Values / type |
|---|---|
| `length` | number (default 4-6) |
| `autoSubmit` | boolean |

## RTL and localisation

Code boxes always read left-to-right, even on RTL pages.

## How to build it

Build a **private base component** that owns logic, states and accessibility, then export **pre-configured global components** that set the base's props. Consumers never import the base.

Base component: **BaseField**.

## Source in Figma today

| Figma frame | Section today | Variants | Variant properties (cleaned) |
|---|---|---|---|
| `_SingleDigit` | Inputs | 14 | State: Active, Active-Filled, default, disabled, filled, hover, preActive, read-only; error: Fals, False, True; Language: Arabic |

## Source in the Twilight Storybook today

### `<s-otp>`

[components-otp](https://dashboard-ui-components.pages.dev/?path=/docs/components-otp) · 8 stories · OTP (One-Time Password) component provides a user-friendly interface for entering and validating OTP codes. It supports configurable number of fields, timer functionality, and various sizes.

**Props**

| Prop | Type | Default | Options | Description |
|---|---|---|---|---|
| `fields` | number | `4` |  | OTP fields number |
| `hasError` | boolean | `false` |  | Error state |
| `hasTimer` | boolean | `true` |  | Enable countdown state |
| `resendLabel` | string | `Resend Code` |  | Resend button label |
| `size` | string | `md` | `md`, `lg` | Fields siz |
| `timer` | number | `60000` |  | Timer duration (in milliseconds) |

**Events**

| Event | Description |
|---|---|
| `canSend` | Emitted when the timer expires and user can resend OTP |
| `fieldUpdated` | Emitted when any OTP field value is updated |
| `otpComplete` | Emitted when all OTP fields are filled with complete values |
| `resendRequest` | Emitted when the resend button is clicked |

**Stories**

[Default](https://dashboard-ui-components.pages.dev/?path=/story/components-otp--default), [Size Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-otp--size-variants), [Field Variants](https://dashboard-ui-components.pages.dev/?path=/story/components-otp--field-variants), [Six Fields](https://dashboard-ui-components.pages.dev/?path=/story/components-otp--six-fields), [No Timer](https://dashboard-ui-components.pages.dev/?path=/story/components-otp--no-timer), [Short Timer](https://dashboard-ui-components.pages.dev/?path=/story/components-otp--short-timer), [Custom Resend Label](https://dashboard-ui-components.pages.dev/?path=/story/components-otp--custom-resend-label), [Has Error](https://dashboard-ui-components.pages.dev/?path=/story/components-otp--has-error)

**Rendered markup (default story)**

```html
<s-otp size="md" fields="4" has-timer="true" timer="60000" resend-label="Resend Code" class="flex flex-col items-center justify-center gap-6 hydrated">
</s-otp>
```


---
_Generated from `catalog/components.json` (id `otp-field`). Edit the catalog, not this file._
