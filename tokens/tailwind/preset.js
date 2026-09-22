/**
 * Salla Design System - Tailwind preset
 *
 * Exposes the system-tier tokens as Tailwind theme values so product code writes
 * `bg-primary-container text-brand rounded-small px-default` instead of raw
 * values. Every value resolves to the CSS custom properties in
 * tokens/css/tokens.css, so theming stays in CSS.
 *
 *   // tailwind.config.js
 *   module.exports = { presets: [require('./tokens/tailwind/preset')], content: [...] }
 */
module.exports = {
  theme: {
    fontFamily: {
      sans: ['"Ping AR + LT"', '"PingAR+LT"', '"PingARLT"', '"PT Sans"', 'system-ui', 'sans-serif'],
    },
    extend: {
      colors: {
        primary: {
          DEFAULT: 'var(--sys-color-primary)',
          disabled: 'var(--sys-color-primary-disabled)',
          container: 'var(--sys-color-primary-container)',
          'container-hover': 'var(--sys-color-primary-container-hover)',
          'container-subtle': 'var(--sys-color-primary-container-subtle)',
        },
        'on-primary': 'var(--sys-color-on-primary)',
        'on-primary-container': 'var(--sys-color-on-primary-container)',
        surface: {
          DEFAULT: 'var(--sys-color-surface)',
          input: 'var(--sys-color-surface-input)',
          neutral: 'var(--sys-color-surface-neutral)',
          disabled: 'var(--sys-color-surface-disabled)',
        },
        outline: {
          light: 'var(--sys-color-outline-light)',
          DEFAULT: 'var(--sys-color-outline)',
          hover: 'var(--sys-color-outline-hover)',
          strong: 'var(--sys-color-outline-strong)',
          primary: 'var(--sys-color-outline-primary)',
          'primary-strong': 'var(--sys-color-outline-primary-strong)',
        },
        text: {
          primary: 'var(--sys-color-text-primary)',
          secondary: 'var(--sys-color-text-secondary)',
          tertiary: 'var(--sys-color-text-tertiary)',
          disabled: 'var(--sys-color-text-disabled)',
          brand: 'var(--sys-color-text-brand)',
          inverse: 'var(--sys-color-text-inverse)',
        },
        success: { lighter: 'var(--sys-color-success-lighter)', light: 'var(--sys-color-success-light)', DEFAULT: 'var(--sys-color-success-primary)', dark: 'var(--sys-color-success-dark)', darker: 'var(--sys-color-success-darker)' },
        danger:  { lighter: 'var(--sys-color-danger-lighter)',  light: 'var(--sys-color-danger-light)',  DEFAULT: 'var(--sys-color-danger-primary)',  dark: 'var(--sys-color-danger-dark)',  darker: 'var(--sys-color-danger-darker)' },
        warning: { lighter: 'var(--sys-color-warning-lighter)', light: 'var(--sys-color-warning-light)', DEFAULT: 'var(--sys-color-warning-primary)', dark: 'var(--sys-color-warning-dark)', darker: 'var(--sys-color-warning-darker)' },
        info:    { lighter: 'var(--sys-color-info-lighter)',    light: 'var(--sys-color-info-light)',    DEFAULT: 'var(--sys-color-info-primary)',    dark: 'var(--sys-color-info-dark)',    darker: 'var(--sys-color-info-darker)' },
        neutral: { lighter: 'var(--sys-color-neutral-lighter)', light: 'var(--sys-color-neutral-light)', DEFAULT: 'var(--sys-color-neutral-primary)', dark: 'var(--sys-color-neutral-dark)', darker: 'var(--sys-color-neutral-darker)' },
        feature: { start: 'var(--sys-color-feature-gradient-start)', end: 'var(--sys-color-feature-gradient-end)', on: 'var(--sys-color-on-feature)' },
        upgrade: { lighter: 'var(--sys-color-upgrade-lighter)', DEFAULT: 'var(--sys-color-upgrade-primary)', dark: 'var(--sys-color-upgrade-dark)', darker: 'var(--sys-color-upgrade-darker)' },
      },
      spacing: {
        '3xs': 'var(--ref-space-3xs)',
        '2xs': 'var(--ref-space-2xs)',
        xs: 'var(--ref-space-xs)',
        sm: 'var(--ref-space-sm)',
        md: 'var(--ref-space-md)',
        lg: 'var(--ref-space-lg)',
        xl: 'var(--ref-space-xl)',
        '2xl': 'var(--ref-space-2xl)',
        '3xl': 'var(--ref-space-3xl)',
        '4xl': 'var(--ref-space-4xl)',
        '5xl': 'var(--ref-space-5xl)',
        '6xl': 'var(--ref-space-6xl)',
        '7xl': 'var(--ref-space-7xl)',
        '8xl': 'var(--ref-space-8xl)',
        '9xl': 'var(--ref-space-9xl)',
        hairline: 'var(--sys-space-hairline)',
        tight: 'var(--sys-space-tight)',
        compact: 'var(--sys-space-compact)',
        default: 'var(--sys-space-default)',
        comfortable: 'var(--sys-space-comfortable)',
        loose: 'var(--sys-space-loose)',
        section: 'var(--sys-space-section)',
        gutter: 'var(--sys-space-gutter)',
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
        'elevation-4': 'var(--sys-elevation-4)',
        focus: 'var(--sys-focus-ring)',
      },
      height: {
        'control-sm': 'var(--ref-size-control-sm)',
        'control-md': 'var(--ref-size-control-md)',
        'control-lg': 'var(--ref-size-control-lg)',
        row: 'var(--ref-size-control-row)',
        bar: 'var(--ref-size-control-bar)',
      },
      transitionDuration: { short: 'var(--ref-duration-short)', medium: 'var(--ref-duration-medium)', long: 'var(--ref-duration-long)' },
      transitionTimingFunction: { standard: 'var(--ref-easing-standard)', emphasized: 'var(--ref-easing-emphasized)' },
    },
  },
  plugins: [
    function typeRoles({ addUtilities }) {
      const roles = ['display-lg', 'headline-lg', 'headline-md', 'title-lg', 'title-md', 'title-sm', 'body-lg', 'body-md', 'body-sm', 'label-lg', 'label-md', 'label-sm'];
      addUtilities(Object.fromEntries(roles.map((r) => [`.type-${r}`, { font: `var(--sys-type-${r})` }])));
    },
  ],
};
