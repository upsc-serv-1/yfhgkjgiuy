# Dr. CSE Current Affairs Magazine — Article Pages Design System (DESIGN.md)
**Universal Specification for Daily Current Affairs Capsule Magazine Article & Content Pages**

---

## 1. Editorial Architecture & Page Surfaces

| Surface Role | Canvas Tint | Purpose & Behavior |
| :--- | :--- | :--- |
| **Cover Page (Page 1)** | `#EEF2EE` (Warm Sage-Ivory) | Full bleed, 100% shelf-aligned logo, dynamic Vol/Issue/Date stamp, frosted colophon pill. |
| **Executive Index (Page 2)** | `#EEF2EE` (Warm Sage-Ivory) | Interactive Bento grid with single-line gold strip (`#A97D2B`), 100% clickable jumping links. |
| **Article & Content Pages (Pages 3+)** | `#FFFFFF` (Pure Crisp White) | High-contrast, dense academic reading canvas optimized for print & tablets. |
| **Box / Container Interiors** | `#F8FAFC` (Soft Slate) | Neutral, calm tinted background for callout boxes, drills, and tables. |

---

## 2. Color Palette & Semantic Design Tokens

```css
:root {
  /* Brand Inks & Heavy Titles */
  --primary-dark: #102A43;   /* Article titles, major GS headings, table headers */
  --accent-teal:  #167C80;   /* Table top rules, hyperlinked sources, takeaway borders */
  --color-mains:  #A97D2B;   /* Part A Mains badge, gold accent bars, masthead kickers */
  --color-prelims:#4F8F86;   /* Part B Prelims badge, factsheet header bars */
  --color-mcq:    #6E9468;   /* Part C MCQs badge, correct answer highlights */
  
  /* Reading Typography & Neutrals */
  --text-body:    #263238;   /* Dark Charcoal primary body reading text */
  --text-muted:   #64748B;   /* Subtitles, date slugs, source attributions */
  --border-light: #CBD5E1;   /* Card borders (0.5pt), subtle dividers (0.5pt) */
  --border-rule:  #D9E0E5;   /* Table inner row dividing rules (0.5pt) */
  --bg-secondary: #F8FAFC;   /* Box backgrounds, table header fills, summary pills */
  --bg-page:      #FFFFFF;   /* Pure white page background */
}
```

---

## 3. Page Geometry & Layout Dimensions (A4)

* **Page Format:** Standard A4 (`595.27 pt` × `841.89 pt`).
* **Margins:**
  * Left / Right Margin: `14.4 pt` (`0.20 in`).
  * Top Margin: `18.0 pt` (`0.25 in`).
  * Bottom Margin: `20.0 pt` (`0.28 in`).
  * Printable Height: `803.89 pt`.
* **Column Standards:**
  * **1-Column Dossier Layout:** `col_width = 566.47 pt` (Used for Part A deep analysis & wide tables).
  * **2-Column Magazine Layout:** `col_width = 277.23 pt` with `gap = 12.0 pt` (Used for continuous reading articles).

---

## 4. Typography Hierarchy & Leading Rules

| Element | Font Face | Size / Leading | Color | Margins / Spacing |
| :--- | :--- | :--- | :--- | :--- |
| **GS Category Banner** | `Helvetica-Bold` / `IBM Plex Sans` | `11.5 pt / 14.5 pt` | `#102A43` | Top rule `1.25 pt` (`#102A43`), space before `10 pt` |
| **Article Title** | `Helvetica-Bold` / `Fraunces` | `17.0–20.0 pt / 22.0–24.0 pt` | `#102A43` | `spaceBefore=14pt`, `spaceAfter=4pt` |
| **Sources & Attribution Line** | `Helvetica-Oblique` | `8.0 pt / 10.5 pt` | `#64748B` | Hyperlinked sources in `#167C80` |
| **Section Subheadings** | `Helvetica-Bold` | `10.5 pt / 13.0 pt` | `#102A43` | `spaceBefore=10pt`, `spaceAfter=3pt` |
| **Body Reading Text** | `Helvetica` / `IBM Plex Sans` | `9.0–9.5 pt / 13.0–13.5 pt` | `#263238` | `spaceAfter=4.5pt` (~65–75 chars/line) |
| **Table Content** | `Helvetica` | `8.0–8.5 pt / 11.0–11.5 pt` | `#263238` | Padding: V `5.5pt`, H `6.0pt` |
| **Running Header / Footer** | `IBM Plex Mono` | `7.5 pt / 9.5 pt` | `#64748B` | Hairline divider rule `0.5 pt` (`#CBD5E1`) |

---

## 5. Container & Box Anatomy (`RoundedContainer`)

### 1. Context / Lead Introduction Box
* **Background:** `#F8FAFC` (Soft Slate).
* **Border:** `0.5 pt solid #CBD5E1`.
* **Left Accent Bar:** `3.0 pt solid #167C80` (Editorial Teal).
* **Corner Radius:** `4.0 pt`.
* **Purpose:** Sets the backdrop, context, and UPSC relevance before the main deep-dive text.

### 2. Mains Drill & PYQ Practice Box (`drill_box`)
* **Background:** `#F8FAFC`.
* **Border:** `0.75 pt solid #CBD5E1`.
* **Left Accent Bar:** `3.5 pt solid #A97D2B` (Warm Gold).
* **Corner Radius:** `4.0 pt`.
* **Internal Structure:**
  * **Top Header:** PYQ Reference (`10M / 15M`, Year) in bold `#A97D2B`.
  * **Question Text:** Crisp `Helvetica-Bold 9.5pt` in `#102A43`.
  * **Model Approach / Dimensions:** 3–4 bulleted pointers highlighting structural anchors.

### 3. Factsheet & Prelims Booster Box
* **Background:** `#F8FAFC`.
* **Border:** `0.5 pt solid #CBD5E1`.
* **Left Accent Bar:** `3.0 pt solid #4F8F86` (Sage Green).
* **Purpose:** Quick-recall points, map markers, species statuses, constitutional articles.

---

## 6. Editorial Table Styling (*Booktabs Standard*)

* **Vertical Gridlines:** **0 vertical gridlines** (Strictly borderless vertical axes).
* **Header Row:**
  * Background: `#F4F7F8`.
  * Text: `Helvetica-Bold 8.5pt` in `#102A43`.
  * Top Rule: `1.25 pt solid #167C80` (Accent Teal).
  * Bottom Rule: `1.0 pt solid #102A43` (Primary Dark).
* **Body Rows:**
  * Background: `#FFFFFF`.
  * Text: `Helvetica 8.0–8.5pt` in `#263238`.
  * Row Dividers: `0.5 pt solid #D9E0E5`.
* **Table Integrity:** `repeatRows=1` hardcoded across multi-page table splits.

---

## 7. Running Headers & Jump Anchors

* **Running Header:**
  * Left: `DR. CSE · DAILY CURRENT AFFAIRS CAPSULE`
  * Right: Date & Issue Reference (`DD MONTH YYYY · VOL. 1`)
  * Divider: `0.5 pt` hairline rule (`#CBD5E1`).
* **Running Footer:**
  * Left: Colophon line `EDITOR — RUBIKA | DESIGN — DAISY | PUBLISHED BY DR. CSE`
  * Right: Dynamic page number `Page X of Y`.
  * Divider: `0.5 pt` hairline rule.
* **Anchor Links:** 100% active internal jump links linking table of contents and bento cards directly to corresponding article headings.
