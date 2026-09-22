/**
 * Salla Design System - Tailwind preset
 *
 * Exposes the system-tier tokens as Tailwind theme values so product code
 * writes `bg-primary text-on-primary rounded-small p-md` instead of raw
 * values. Every value resolves to the CSS custom properties in
 * tokens/css/tokens.css, so theming stays in CSS.
 *
 * Usage:
 *   // tailwind.config.js
 *   module.exports = { presets: [require('@salla/design-system/tokens/tailwind/preset')], content: [...] }
 */
module.exports = {
  theme: {
    fontFamily: {
      sans: ['"PingAR+LT"', '"PingARLT"', '"PT Sans"', 'system-ui', 'sans-serif'],
    },
    extend: {
      colors: {
        primary: {
          DEFAULT: 'var(--sys-color-primary)',
          container: 'var(--sys-color-primary-container)',
        },
        'on-primary': 'var(--sys-color-on-primary)',
        'on-primary-container': 'var(--sys-color-on-primary-container)',
        surface: {
          DEFAULT: 'var(--sys-color-surface)',
          input: 'var(--sys-color-surface-input)',
        },
        outline: {
          DEFAULT: 'var(--sys-color-outline)',
          primary: 'var(--sys-color-outline-primary)',
        },
        text: {
          primary: 'var(--sys-color-text-primary)',
          secondary: 'var(--sys-color-text-secondary)',
          brand: 'var(--sys-color-text-brand)',
          inverse: 'var(--sys-color-text-inverse)',
        },
        success: {
          DEFAULT: 'var(--sys-color-success-primary)',
          dark: 'var(--sys-color-success-dark)',
          darker: 'var(--sys-color-success-darker)',
        },
        danger: {
          lighter: 'var(--sys-color-danger-lighter)',
          DEFAULT: 'var(--sys-color-danger-primary)',
          dark: 'var(--sys-color-danger-dark)',
          darker: 'var(--sys-color-danger-darker)',
        },
        warning: {
          DEFAULT: 'var(--sys-color-warning-primary)',
        },
        info: {
          lighter: 'var(--sys-color-info-lighter)',
          light: 'var(--sys-color-info-light)',
          DEFAULT: 'var(--sys-color-info-primary)',
          darker: 'var(--sys-color-info-darker)',
        },
        feature: {
          start: 'var(--sys-color-feature-gradient-start)',
          end: 'var(--sys-color-feature-gradient-end)',
          on: 'var(--sys-color-on-feature)',
        },
      },
      spacing: {
        '3xs': 'var(--sys-space-3xs)',
        '2xs': 'var(--sys-space-2xs)',
        xs: 'var(--sys-space-xs)',
        sm: 'var(--sys-space-sm)',
        md: 'var(--sys-space-md)',
        lg: 'var(--sys-space-lg)',
        xl: 'var(--sys-space-xl)',
        '2xl': 'var(--sys-space-2xl)',
        '3xl': 'var(--sys-space-3xl)',
        '4xl': 'var(--sys-space-4xl)',
      },
      borderRadius: {
        none: 'var(--sys-shape-none)',
        'extra-small': 'var(--sys-shape-extra-small)',
        small: 'var(--sys-shape-small)',
        medium: 'var(--sys-shape-medium)',
        large: 'var(--sys-shape-large)',
        full: 'var(--sys-shape-full)',
      },
      boxShadow: {
        'elevation-1': 'var(--sys-elevation-1)',
        'elevation-2': 'var(--sys-elevation-2)',
        'elevation-3': 'var(--sys-elevation-3)',
        focus: 'var(--sys-focus-ring)',
      },
      height: {
        'control-sm': 'var(--ref-size-control-sm)',
        'control-md': 'var(--ref-size-control-md)',
        'control-lg': 'var(--ref-size-control-lg)',
      },
      transitionDuration: {
        short: 'var(--ref-duration-short)',
        medium: 'var(--ref-duration-medium)',
        long: 'var(--ref-duration-long)',
      },
      transitionTimingFunction: {
        standard: 'var(--ref-easing-standard)',
        emphasized: 'var(--ref-easing-emphasized)',
      },
    },
  },
};
