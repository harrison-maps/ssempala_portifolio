# Design System Strategy: The Precise Monolith

## 1. Overview & Creative North Star: "The Digital Obsidian"
This design system is anchored in the concept of **The Digital Obsidian**. It moves away from the "web-standard" card-based layout in favor of a monolithic, high-contrast aesthetic that feels carved rather than assembled. 

By utilizing a "Precise Monolith" approach, we prioritize extreme geometric clarity, zero-radius corners, and a sharp, editorial use of emerald green (#10B981) against a deep, light-absorbing background (#0E0E0E). We break the traditional grid through **Intentional Asymmetry**: large Display type is often offset or pushed to the margins, creating a sense of "engineered" tension that feels premium and custom-built.

## 2. Colors: High-Chroma Precision
The color palette is a study in extreme contrast. The background is a "True Dark" (`surface`: #0E0E0E), providing a void for the vibrant Emerald Primary and Secondary tokens to live within.

### The "No-Line" Rule
Traditional borders are strictly prohibited for sectioning. Structural definition must be achieved through **Value Shifting**. To separate a sidebar from a main view, move from `surface` (#0E0E0E) to `surface_container_low` (#131313). 

### Surface Hierarchy & Nesting
Instead of shadows, we use "Tonal Sculpting." Layers are defined by their elevation in the surface stack:
*   **Base:** `surface` (#0E0E0E)
*   **Embedded Elements:** `surface_container_low` (#131313)
*   **Primary Interaction Zones:** `surface_container_high` (#20201F)
*   **Active Overlays:** `surface_container_highest` (#262626)

### The "Glass & Gradient" Rule
To add "soul" to the monolith, use high-blur glassmorphism. Floating panels should use `surface_container` at 70% opacity with a `40px` backdrop blur. For CTAs, apply a subtle linear gradient from `primary` (#69F6B8) to `primary_container` (#06B77F) at a 135-degree angle to give the emerald green a liquid, metallic depth.

## 3. Typography: The Editorial Scale
We pair the technical, wide-set geometry of **Space Grotesk** for headlines with the utilitarian clarity of **Inter** for data and body.

*   **Display & Headlines (Space Grotesk):** These are your architectural anchors. Use `display-lg` (3.5rem) with tight tracking (-0.02em) to create a sense of massive scale.
*   **Body (Inter):** Keep body copy clean and breathable. `body-md` (0.875rem) is the workhorse.
*   **Labels (Inter):** Use `label-sm` (0.6875rem) in all-caps with increased letter spacing (+0.05em) for technical metadata to reinforce the "precise" aesthetic.

The hierarchy conveys authority: large headers command attention, while small, sharp labels provide the technical "readout" feel.

## 4. Elevation & Depth: Tonal Layering
In this design system, "Up" does not mean "Shadow." It means "Lighter."

*   **The Layering Principle:** A card does not sit *on top* of a page; it is a higher-density area *within* the page. Place a `surface_container_highest` (#262626) component inside a `surface_container_low` (#131313) area to create immediate visual hierarchy.
*   **Ambient Shadows:** If a floating element (like a context menu) requires a shadow, it must be `on_surface` (#FFFFFF) at 4% opacity with a `64px` blur. It should look like a faint glow, not a dark stain.
*   **The "Ghost Border" Fallback:** If accessibility requires a stroke, use `outline_variant` (#484847) at 20% opacity. Never use 100% opaque lines.

## 5. Components: The Monolith Set

### Buttons
*   **Primary:** Solid Emerald (`primary` #69F6B8) with `on_primary` (#005A3C) text. 0px border radius.
*   **Secondary:** Ghost style. `outline` (#767575) stroke at 20% opacity. Text is `primary`.
*   **Tertiary:** Text-only in `primary`, using `1.75rem` (Space 8) horizontal padding to maintain a wide, monolithic footprint.

### Input Fields
*   **Styling:** Fields are `surface_container_low`. No bottom border. Use a 2px left-accent bar in `primary` only when the field is focused.
*   **Error State:** Change the left-accent bar to `error` (#FF716C).

### Cards & Lists
*   **Constraint:** Zero dividers. Use `2.25rem` (Space 10) of vertical whitespace to separate list items.
*   **Interaction:** On hover, a list item should shift from `surface` to `surface_container_low`.

### The "Data Monolith" (Custom Component)
For displaying key metrics, use a `display-sm` value paired with a `label-sm` title, nested inside a `surface_container_highest` block. Ensure the block is perfectly square to reinforce the geometric theme.

## 6. Do's and Don'ts

### Do:
*   **Do** use 0px border radius for everything. Sharp corners signify precision.
*   **Do** use asymmetrical margins (e.g., 20% left margin, 5% right margin) for editorial layouts.
*   **Do** lean heavily on `primary` (#69F6B8) for moments of success or critical action.

### Don't:
*   **Don't** use standard "Grey" for backgrounds. Stick to the deep Obsidian tones provided in the Surface palette.
*   **Don't** use 1px solid dividers. If you feel the need for a line, increase your whitespace instead.
*   **Don't** use rounded icons. Use sharp, linear icon sets that match the `outline` token weight.