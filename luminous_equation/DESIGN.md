---
name: Luminous Equation
colors:
  surface: '#f8f9ff'
  surface-dim: '#d0dbed'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e6eeff'
  surface-container-high: '#dee9fc'
  surface-container-highest: '#d9e3f6'
  on-surface: '#121c2a'
  on-surface-variant: '#414754'
  inverse-surface: '#27313f'
  inverse-on-surface: '#eaf1ff'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005bc0'
  primary: '#0059bb'
  on-primary: '#ffffff'
  primary-container: '#0070ea'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc7ff'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#712edd'
  on-tertiary: '#ffffff'
  tertiary-container: '#8b4ef7'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc7ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ebddff'
  tertiary-fixed-dim: '#d3bbff'
  on-tertiary-fixed: '#250059'
  on-tertiary-fixed-variant: '#5b00c5'
  background: '#f8f9ff'
  on-background: '#121c2a'
  surface-variant: '#d9e3f6'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  base: 16px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
---

## Brand & Style

The design system bridges the gap between playful engagement and technical rigor. It targets a broad demographic of learners, from primary school students to university-level mathematicians. The brand personality is **Dynamic, Intellectual, and Rewarding**.

The visual style is **Modern / Tactile**, utilizing a "Clean Gamification" approach. This avoids the cluttered aesthetics of traditional mobile games in favor of a sophisticated, high-performance interface. It uses vibrant color accents against a highly organized, professional structure to ensure that while the journey feels like a quest, the focus remains on the clarity of the mathematical logic. The UI should evoke a sense of progress, clarity, and "aha!" moments through crisp interactions and a luminous visual language.

## Colors

This design system utilizes a high-vibrancy palette to categorize the user experience:

*   **Electric Blue (Primary):** Used for primary actions, navigation, and core interactive elements. It represents the energy of learning.
*   **Emerald Green (Success):** Reserved for progress bars, correct answers, and achievement states. It reinforces positive feedback loops.
*   **Deep Purple (Advanced):** Introduced as users move into higher-level calculus, linear algebra, and complex proofs. It signals a "mastery" tier.
*   **Neutrals:** A range of cool grays provides the professional scaffolding necessary for technical focus, ensuring the vibrant colors do not cause cognitive fatigue during long study sessions.

## Typography

The typography system prioritizes legibility and technical precision. **Hanken Grotesk** serves as the primary typeface, offering a clean, contemporary feel that works equally well for playful headings and dense instructional text. 

For mathematical formulas, variables, and technical data, **JetBrains Mono** is utilized. Its monospaced nature ensures that vertical alignment in equations is maintained, providing the "technical" feel required for high-level math. 

*   **Headlines:** Heavy weights (700-800) for a confident, gamified look.
*   **Body:** Standard weights (400) with generous line-height to maintain readability during complex explanations.
*   **Formulae:** Always use the monospaced label font for clarity in variable distinction (e.g., distinguishing 'l' from '1').

## Layout & Spacing

The design system employs a **Fluid-Fixed Hybrid Grid**. Content is housed in a centered container with a maximum width of 1280px for desktop to prevent line lengths from becoming unreadable.

*   **Rhythm:** A strict 4px/8px baseline grid ensures vertical harmony.
*   **Mobile:** Uses a 4-column layout with 16px side margins. Interactive elements (buttons, inputs) must maintain a minimum height of 48px for touch accessibility.
*   **Desktop:** Uses a 12-column layout. Technical workspaces (the "Problem Area") should utilize a 2/3 width column, while the "Reference/Tools" sidebar occupies the remaining 1/3.
*   **Density:** Use "Relaxed" spacing for introductory levels to feel welcoming, and "Compact" spacing for advanced technical levels to allow more data on screen.

## Elevation & Depth

Depth is used to signify interactivity and layer hierarchy through **Ambient Shadows** and **Tonal Layers**.

1.  **Level 0 (Surface):** The main background, using the subtle neutral tint.
2.  **Level 1 (Cards):** White surfaces with a soft, 10% opacity shadow (Blur: 8px, Y: 4px). This is the primary container for questions and content.
3.  **Level 2 (Interactive):** Primary buttons use a slightly deeper shadow and a subtle inner-glow on the top edge to create a tactile, "pressable" feel.
4.  **Floating Elements:** Modals and tooltips use a high-diffused shadow (Blur: 24px, Opacity: 15%) to appear significantly closer to the user.

Avoid harsh black shadows; instead, use shadows tinted with the primary or neutral color to maintain a vibrant, clean aesthetic.

## Shapes

The shape language is **Friendly yet Structured**. 

*   **Standard Radius:** 8px (0.5rem) for cards and input fields. This provides a modern, softened look that is more approachable than sharp corners but more professional than full rounds.
*   **Large Radius:** 16px (1rem) for featured promo cards or level-selection tiles to emphasize the gamified "quest" elements.
*   **Buttons:** Should use the standard radius (8px) rather than pills to maintain a more technical, software-oriented feel for the advanced levels.

## Components

*   **Action Buttons:** Primary buttons use 'Electric Blue' with white text. Success actions (Submit Answer) use 'Emerald Green'. Advanced level gates use 'Deep Purple'.
*   **Progress Indicators:** Use a thick, 8px height bar with 'Emerald Green' for the fill. Background of the bar should be a 10% opacity version of the green.
*   **Input Fields:** Ghost-style borders (1px solid neutral-200) that transition to a 2px 'Electric Blue' border on focus.
*   **Math Cards:** Content is presented in white cards with an 8px radius. For "Advanced" modules, the card border can feature a subtle 2px top-accent of 'Deep Purple'.
*   **Feedback Toasts:** Use large icons and bold background colors (Green for correct, Red for incorrect) to provide instant, high-visibility gamified feedback.
*   **Step-by-Step Lists:** Use "Connectors" (vertical lines between numbers) to visualize the flow of a mathematical proof or operation.