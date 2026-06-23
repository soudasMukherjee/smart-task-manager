---
name: Intelligent Efficiency System
colors:
  surface: '#fcf8ff'
  surface-dim: '#dcd8e5'
  surface-bright: '#fcf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f2ff'
  surface-container: '#f0ecf9'
  surface-container-high: '#eae6f4'
  surface-container-highest: '#e4e1ee'
  on-surface: '#1b1b24'
  on-surface-variant: '#464555'
  inverse-surface: '#302f39'
  inverse-on-surface: '#f3effc'
  outline: '#777587'
  outline-variant: '#c7c4d8'
  surface-tint: '#4d44e3'
  primary: '#3525cd'
  on-primary: '#ffffff'
  primary-container: '#4f46e5'
  on-primary-container: '#dad7ff'
  inverse-primary: '#c3c0ff'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#7e3000'
  on-tertiary: '#ffffff'
  tertiary-container: '#a44100'
  on-tertiary-container: '#ffd2be'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2dfff'
  primary-fixed-dim: '#c3c0ff'
  on-primary-fixed: '#0f0069'
  on-primary-fixed-variant: '#3323cc'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffdbcc'
  tertiary-fixed-dim: '#ffb695'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7b2f00'
  background: '#fcf8ff'
  on-background: '#1b1b24'
  surface-variant: '#e4e1ee'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  container-max: 1280px
  gutter: 24px
---

## Brand & Style
The design system is engineered for high-performance productivity, targeting professionals who require clarity and speed. The brand personality is **reliable, focused, and forward-thinking**. 

The design style leans into **Modern Minimalism** with a focus on functional aesthetics. It utilizes an airy, expansive layout to reduce cognitive load while maintaining high information density through a strict grid. The emotional response should be one of "quiet confidence"—where the interface recedes to let the user's work take center stage. Key characteristics include purposeful whitespace, a refined color palette, and high-contrast elements to ensure maximum accessibility and focus.

## Colors
The palette is rooted in a "Work-Focused" spectrum. 
- **Primary (Indigo):** Used for primary actions, focus states, and active navigation. It denotes intent and intelligence.
- **Secondary (Emerald):** Reserved strictly for success states, completed tasks, and positive growth indicators.
- **Danger (Rose):** Specifically for overdue tasks, critical alerts, and destructive actions.
- **Neutrals:** A range of cool grays that define structure without adding visual noise. The background uses a soft off-white to reduce eye strain during long sessions.

All color combinations must pass WCAG 2.1 AA standards for contrast, particularly for text on colored backgrounds and interactive icons.

## Typography
The system uses a dual-font approach to balance character and utility. **Geist** is used for headlines and labels to provide a precise, technical edge. **Inter** is used for all body copy and task descriptions for its world-class legibility and neutral tone.

For mobile devices, `display-lg` scales down to 36px, and `headline-lg` scales to 28px to ensure comfortable viewing. All text utilizes high-contrast color tokens (Neutral 900 for headings, Neutral 600 for secondary text) to ensure readability across all lighting conditions.

## Layout & Spacing
The layout follows a **12-column fluid grid** for desktop and a **single-column fluid layout** for mobile. 

- **Desktop (1024px+):** 12 columns, 24px gutters, 40px side margins.
- **Tablet (768px - 1023px):** 8 columns, 20px gutters, 24px side margins.
- **Mobile (Up to 767px):** 4 columns, 16px gutters, 16px side margins.

The spacing rhythm is based on a **4px baseline grid**. Components should always use increments of 4px for padding and margins to maintain a strict visual cadence. Vertical rhythm is prioritized, with larger gaps between logical sections (Task Groups) and tighter spacing within nested items (Subtasks).

## Elevation & Depth
Depth is created through **Tonal Layering** supplemented by **Ambient Shadows**. 

1. **Level 0 (Base):** Background (#F9FAFB). No shadow.
2. **Level 1 (Cards/Surface):** White background with a subtle, highly diffused shadow (0px 1px 3px rgba(0,0,0,0.05)).
3. **Level 2 (Hover/Active):** Slightly lifted shadow (0px 10px 15px rgba(0,0,0,0.08)) to indicate interactivity.
4. **Level 3 (Modals/Overlays):** Deepest shadow (0px 20px 25px rgba(0,0,0,0.1)) to draw focus.

Borders are used sparingly, primary for defining input fields and dividers. A subtle 1px border (#E5E7EB) is applied to cards to maintain definition against the light background.

## Shapes
This design system utilizes a **Rounded** shape language to soften the professional tone and make the UI feel modern and approachable. 

The standard radius for most components (Cards, Buttons, Inputs) is **0.5rem (8px)**. For larger layout containers or distinct feature blocks, a **rounded-xl (1.5rem/24px)** radius is preferred to create a soft, "contained" aesthetic. Icons should follow a 2px stroke weight with slightly rounded caps to match the UI's geometry.

## Components
- **Buttons:** Large, clear hit areas. Primary buttons use the Indigo hex with white text. Secondary buttons use a subtle gray ghost style. All buttons use `rounded-lg`.
- **Task Cards:** The core component. Features a white background, 1px neutral-200 border, and `rounded-xl` corners. High contrast text for task titles. Status indicators (dots or thin left-hand strips) use the Primary/Secondary/Danger colors.
- **Chips/Badges:** Small, `pill-shaped` indicators for tags (e.g., "Urgent", "Design"). Used with low-opacity background tints of the status colors (e.g., 10% Rose background with 100% Rose text).
- **Inputs:** Clean, outlined boxes with a 1px Neutral-300 border that transforms to a 2px Indigo border on focus.
- **Checkboxes:** Large (20px x 20px) with `rounded` corners (4px). When checked, they fill with Emerald and show a white checkmark to signal clear completion.
- **Progress Bars:** Thin, linear tracks with Emerald fills. The background track should be a very light Neutral-100 to maintain the "airy" feel.