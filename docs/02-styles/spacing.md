# Spacing

A single 4px scale. Today Figma carries two spacing variable sets that contradict each other; both migrate here.

## The scale

| Ref | Value | System alias | Typical use (verified in Figma) |
|---|---|---|---|
| `ref.space.0` | 0 | – | |
| `ref.space.1` | 2px | `sys.space.3xs` | Checkbox inner padding ✓, TranslationToggle gap ✓ |
| `ref.space.2` | 4px | `sys.space.2xs` | Button icon–label gap ✓, Status dot–label gap ✓, Alert title–body gap ✓ |
| `ref.space.3` | 8px | `sys.space.xs` | Button / field vertical padding ✓, field icon gap ✓, Status horizontal padding ✓ |
| `ref.space.4` | 12px | `sys.space.sm` | Button / field horizontal padding ✓, label–field gap ✓ |
| `ref.space.5` | 16px | `sys.space.md` | Alert vertical padding ✓, card padding on compact |
| `ref.space.6` | 20px | `sys.space.lg` | |
| `ref.space.7` | 24px | `sys.space.xl` | Alert horizontal padding ✓, Panel padding, page gutter |
| `ref.space.8` | 32px | `sys.space.2xl` | section gaps |
| `ref.space.9` | 40px | `sys.space.3xl` | |
| `ref.space.10` | 48px | `sys.space.4xl` | |
| `ref.space.11` | 64px | – | page-level rhythm |
| `ref.space.12` | 80px | – | |

## Migration from the two Figma scales

| Figma variable | Value | → New token |
|---|---|---|
| `spacing/6xs` | 2 | `sys.space.3xs` |
| `spacing/5xs` | 4 | `sys.space.2xs` |
| `spacing/3xs` | 8 | `sys.space.xs` |
| `spacing/xs` | 12 | `sys.space.sm` |
| `spacing/base` | 16 | `sys.space.md` |
| `spacing/2xl` | 24 | `sys.space.xl` |
| `Spacing/Sizes/3xs` | 2 | `sys.space.3xs` |
| `Spacing/Sizes/sm` | 8 | `sys.space.xs` |
| `Spacing/Sizes/lg` | 12 | `sys.space.sm` |
| `Spacing/Sizes/{2xs,xs,md,xl,2xl,3xl,4xl,5xl,6xl,8xl,9xl}` | not read | map by value once exported |

The clash: `spacing/3xs` is 8px while `Spacing/Sizes/3xs` is 2px, and `spacing/xs` (12) equals `Spacing/Sizes/lg` (12). After migration, one name means one value.

## Rules

- Padding inside atoms and molecules comes from `comp.*` tokens that alias `sys.space.*`.
- Gaps between siblings use `sys.space.*` directly.
- Odd values (6, 10, 14) are not allowed; 2px exists only for hairlines.
- Page gutters: `md` on compact, `xl` on expanded and up (see [layout.md](../01-foundations/layout.md)).
