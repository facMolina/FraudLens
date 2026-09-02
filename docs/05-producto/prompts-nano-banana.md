# Prompts para Nano Banana — Identidad visual de FraudLens

> **Nano Banana** es el modelo de imágenes de Google (Gemini). Se usa en
> [Google AI Studio](https://aistudio.google.com) o en la app de Gemini.
>
> Brief completo: [`identidad-visual.md`](identidad-visual.md)
>
> **Decisiones que ya están tomadas y se reflejan en estos prompts:** el nombre se escribe
> **FraudLens** · la **UI va en inglés** · tipografías de **Google Fonts** · **sin colores vetados**.

## Cómo usar esto

1. Copiá el prompt completo, **sin recortar**. Estos modelos responden mejor a descripciones largas
   y específicas que a listas de palabras sueltas.
2. Los prompts están **en inglés** a propósito: los modelos de imagen rinden bastante mejor así.
   Donde hace falta texto en español dentro de la imagen, está indicado explícitamente.
3. Generá **varias corridas del mismo prompt** — salen distintas cada vez.
4. Guardá lo que sirva en `docs/05-producto/identidad/` *(crear la carpeta; las imágenes sí se
   versionan, son livianas)*.

> ⚠️ **Los modelos de imagen deforman las letras.** Por eso el prompt 1 genera **sólo el símbolo,
> sin texto**. El nombre "FraudLens" se monta después con tipografía real.

---

## Prompt 1 — Isotipo (símbolo sin texto)

> Genera 3 láminas, una por dirección conceptual. Corré cada una por separado.

### 1A · Dirección "lente"

```
A clean vector logo mark presentation sheet on a neutral light gray background (#F5F5F7).
Show a 3x3 grid of nine distinct abstract logo symbols — icons only, absolutely NO text,
NO letters, NO words anywhere in the image.

The symbols explore the concept of a LENS: camera apertures, optical lenses, focus rings,
viewfinders, concentric rings narrowing to a point, light refracting through glass.

Style: minimal geometric vector marks in the spirit of Stripe, Linear and Vercel.
Flat, single-color, no gradients, no drop shadows, no 3D, no skeuomorphism.
Each mark is built from simple geometric primitives — circles, arcs, straight lines,
consistent stroke weight. Each mark reads clearly at 24 pixels.
Generous white space around each mark. Marks are deep electric blue (#2563EB) on light gray.

The aesthetic is a premium B2B fintech infrastructure product, not a consumer app.
Sober, precise, engineered. Square 1:1 image.
```

### 1B · Dirección "lente + dato"

```
A clean vector logo mark presentation sheet on a neutral light gray background (#F5F5F7).
Show a 3x3 grid of nine distinct abstract logo symbols — icons only, absolutely NO text,
NO letters, NO words anywhere in the image.

The symbols fuse two ideas: OPTICAL FOCUS and DATA ANOMALY. Think of one outlier dot
standing out inside a regular grid of dots; a scanning line crossing a dataset; a lens
that isolates a single irregular node among identical ones; a signal spike inside a
uniform waveform; a magnifying frame highlighting one deviant element in a pattern.

Style: minimal geometric vector marks in the spirit of Stripe, Linear and Vercel.
Flat, two-tone maximum, no gradients, no drop shadows, no 3D.
Built from simple primitives — dots, grids, arcs, lines — with consistent stroke weight.
Each mark reads clearly at 24 pixels. Generous white space around each mark.
Primary shapes in deep electric blue (#2563EB); the anomaly element in a single
contrasting accent.

The aesthetic is a premium B2B fintech infrastructure product. Sober, precise, engineered.
Square 1:1 image.
```

### 1C · Dirección abstracta

```
A clean vector logo mark presentation sheet on a neutral light gray background (#F5F5F7).
Show a 3x3 grid of nine distinct abstract logo symbols — icons only, absolutely NO text,
NO letters, NO words anywhere in the image.

The symbols are purely abstract geometric marks suggesting FILTERING, LAYERS and
SEPARATION: overlapping translucent planes, a funnel of parallel lines, a mesh that
catches one element, layered shapes that filter a flow, forms that split a stream in two.
No magnifying glasses, no eyes, no shields, no locks, no checkmarks.

Style: minimal geometric vector marks in the spirit of Linear, Vercel and Stripe.
Flat, single-color, no gradients, no shadows, no 3D. Simple primitives, consistent stroke
weight, strong negative space. Each mark reads clearly at 24 pixels.
Deep electric blue (#2563EB) on light gray.

The aesthetic is a premium B2B fintech infrastructure product. Sober, precise, engineered.
Square 1:1 image.
```

---

## Prompt 2 — Paletas de color

> Corré este prompt varias veces: da opciones en distintas familias cromáticas.

```
A professional brand color palette specification sheet, presented as a clean design system
document on a white background. Editorial layout, generous margins, no decoration.

The sheet shows FOUR alternative brand palettes stacked as horizontal rows, one per
brand color family: deep electric blue, violet/purple, cyan/teal, and indigo.

For each palette row, show a horizontal strip of color swatches as flat rectangles:
- 1 primary brand color
- 1 darker and 1 lighter variant of it
- 4 neutral grays from near-white to near-black
- then, separated by a small gap, a RISK SCALE of exactly four swatches
  labeled LOW, MEDIUM, HIGH, CRITICAL going from calm green through amber and
  orange to deep red

Critical requirement: the brand color must be clearly distinguishable from every color
in the risk scale, so it never reads as a status.

Include the hex code under each swatch in a small monospaced font.
Keep all text minimal and precise — only hex codes and the four risk labels.

Style reference: Stripe's design system documentation, Linear's brand guidelines.
Clean, technical, premium. Landscape 16:9 image.
```

### 2B · Versión modo oscuro

Mismo prompt, cambiando el primer párrafo por:

```
A professional brand color palette specification sheet for a DARK MODE interface,
presented as a clean design system document on a very dark charcoal background (#0D0D10).
Editorial layout, generous margins, no decoration. All swatches and labels must remain
clearly legible against the dark background.
```

---

## Prompt 3 — Mockup del dashboard

```
A realistic UI mockup of a professional B2B fintech fraud-detection dashboard, shown as
a flat screenshot with no browser chrome, no device frame, no perspective, no shadow.

The interface is in ENGLISH. Dark mode: very dark charcoal background (#0D0D10), panels
in slightly lighter charcoal, deep electric blue as the single accent color.

Layout:
- A slim left sidebar with small icon-only navigation items
- A top bar with the page title "Transactions" and a set of filter chips
- A row of four compact metric cards showing large numbers with small labels underneath
- Below, a dense data table filling most of the screen. Table columns titled:
  DATE, TRANSACTION ID, USER, AMOUNT, RISK, DECISION.
  About twelve rows of transaction data.
  The RISK column shows a small horizontal score bar plus a numeric value out of 100.
  The DECISION column shows compact status pills reading APPROVE, REVIEW or BLOCK.

Critical: each risk state is communicated by BOTH color AND a distinct small icon shape,
so the table stays readable in grayscale. Risk colors run from calm green through amber
and orange to deep red, and are clearly distinct from the blue brand accent.

Typography: a clean geometric sans-serif. All numeric columns are tabular and perfectly
aligned. Small text sizes, high information density, generous row padding.

Style reference: the visual precision of Linear and Stripe combined with the data density
of Datadog and Grafana. Premium, sober, engineered. Landscape 16:9 image.
```

### 3B · Versión modo claro

Mismo prompt, cambiando el párrafo de color por:

```
The interface is in ENGLISH. Light mode: near-white background (#FAFAFA), panels in pure
white with very subtle 1px borders, deep electric blue as the single accent color.
```

---

## Prompt 4 — Lámina de tipografía

```
A typography specification sheet for a design system, on a clean white background.
Editorial layout with generous margins, in the style of Stripe's or Linear's brand
documentation.

The sheet demonstrates a single geometric sans-serif typeface across a type scale:
- One large display heading
- One medium subheading
- A short paragraph of body text at small size
- A caption at very small size

Below that, a dedicated section demonstrating NUMERALS for a financial data table:
show a right-aligned column of monetary amounts with thousands separators, perfectly
aligned using tabular figures. Beside it, show the characters 0 O 1 l I 5 S 8 B enlarged
side by side to demonstrate that they are clearly distinguishable from one another.

All sample text is in English. Label each section with a small monospaced caption.
No decoration, no color other than black, gray and one blue accent.
Portrait 4:5 image.
```

---

## Después de generar

1. **Elegí** los 2-3 isotipos más fuertes de cada dirección.
2. **Chequeá que funcionen chicos.** Reducilos a 24px: si no se entienden, no sirven.
3. **Chequeá en escala de grises.** Si el dashboard deja de entenderse, la paleta falla.
4. Montá el **wordmark** "FraudLens" con tipografía real junto al isotipo elegido.
5. Armá el **board de presentación** para el equipo.
6. Cargá la decisión final —y **qué descartaste y por qué**— en
   [`identidad-visual.md`](identidad-visual.md) y en el comentario de resolución de la tarjeta.

> ⚠️ **Honestidad académica:** si se usan imágenes generadas por IA en el documento final o el
> pitch, **se cita la herramienta**. Ver [`prototipo.md`](prototipo.md).

---

# Segunda ronda — con violeta decidido

> Decisiones de FM (2026-09-02): **color de marca violeta** · **3 isotipos finalistas** ·
> **regenerar los dos mockups** · el board presenta **variaciones**.
>
> Valores verificados en [`identidad/paleta.md`](identidad/paleta.md).

## Prompt 5 — Variaciones de los 3 isotipos finalistas

```
A logo mark exploration sheet on a neutral light gray background (#F5F5F7).
Icons only — absolutely NO text, NO letters, NO words anywhere in the image.

Show a 3x4 grid: three ROWS, one per concept, each row containing four variations
of the SAME concept.

ROW 1 — FUNNEL: a set of parallel lines converging downward into a single point or
narrow channel, representing filtering a stream down to what matters.
ROW 2 — GRID ANOMALY: a regular grid of cells or dots where exactly one cell stands
out, representing one irregular transaction inside a normal flow.
ROW 3 — PRISM: a triangular prism splitting one incoming beam into several separate
outgoing rays, representing one stream separated into distinct risk levels.

Within each row, vary only the execution: thin outline, thicker outline, partially
filled, and a version built from separated segments. Keep the concept identical
across the four variations in a row.

Style: minimal geometric vector marks in the spirit of Stripe, Linear and Vercel.
Flat, no gradients, no shadows, no 3D. Simple geometric primitives, strong negative
space. Every mark must read clearly at 24 pixels.

Color: violet #9333EA on the light gray background. Single color only.

The aesthetic is a premium B2B fintech infrastructure product. Sober, precise,
engineered. Square 1:1 image.
```

## Prompt 6 — Dashboard modo oscuro, corregido

> ⚠️ La versión anterior salió con métricas sin sentido y con los scores contradiciendo las
> decisiones. Este prompt **fija los datos exactos** para que eso no pase.

```
A realistic UI mockup of a professional B2B fintech fraud-detection dashboard, shown as
a flat screenshot with no browser chrome, no device frame, no perspective, no shadow.

Interface in ENGLISH. Dark mode: page background #0D0D10, panels #16161A,
violet #A855F7 as the single brand accent color.

Layout:
- A slim left sidebar with small icon-only navigation items, the active one in violet
- A top bar with the page title "Transactions" and four filter controls labeled exactly:
  "Date Range", "Risk Level", "Status", "Search transactions"
- A row of exactly four metric cards, each with a large number and a small label below.
  Use exactly these, in this order:
    "14,250" / Total Transactions
    "312"    / Flagged for Review
    "85"     / Blocked
    "42"     / Avg. Risk Score
- Below, a dense data table. Column headers exactly:
  DATE, TRANSACTION ID, USER, AMOUNT, RISK, DECISION
  Use exactly these eight rows, and keep every value consistent:
    Oct 27, 2023 | TXN-901234 | j.smith@company.com  | $1,250.00  | 15 | APPROVE
    Oct 27, 2023 | TXN-901235 | m.jones@provider.net | $5,800.00  | 48 | REVIEW
    Oct 27, 2023 | TXN-901236 | l.lee@innovate.io    | $750.00    | 72 | REVIEW
    Oct 27, 2023 | TXN-901237 | r.brown@corp.org     | $12,900.00 | 94 | BLOCK
    Oct 26, 2023 | TXN-901238 | a.diaz@fintech.co    | $320.00    | 8  | APPROVE
    Oct 26, 2023 | TXN-901239 | k.patel@shop.com     | $2,400.00  | 55 | REVIEW
    Oct 26, 2023 | TXN-901240 | s.moore@store.net    | $8,100.00  | 88 | BLOCK
    Oct 26, 2023 | TXN-901241 | t.nguyen@pay.io      | $610.00    | 21 | APPROVE

Critical rules, follow exactly:
- The RISK column shows a small horizontal bar whose fill length matches the number,
  plus the numeric value.
- Risk color follows the score: 0-39 green #16A34A, 40-59 amber #FBBF24,
  60-84 orange #F97316, 85-100 red #DC2626.
- Each risk level ALSO carries a distinct small icon shape so it is readable in
  grayscale: check circle for green, triangle for amber, diamond for orange,
  filled circle for red.
- The DECISION column shows compact pills reading APPROVE, REVIEW or BLOCK, matching
  the score bands above.
- The violet brand accent is used ONLY for navigation and interactive elements,
  never for a risk state.

Typography: a clean geometric sans-serif. All numeric columns tabular and right-aligned.
Small text sizes, high information density.

Style: the visual precision of Linear and Stripe with the data density of Datadog.
Premium, sober, engineered. Landscape 16:9 image.
```

## Prompt 7 — Dashboard modo claro, en violeta

Mismo prompt 6, cambiando **sólo** estos dos bloques:

```
Interface in ENGLISH. Light mode: page background #FAFAFA, panels pure white with
very subtle 1px light gray borders, violet #9333EA as the single brand accent color.
```

y la regla de colores de riesgo:

```
- Risk color follows the score, using these DARKER values chosen for contrast on a
  light background: 0-39 green #15803D, 40-59 amber #B45309, 60-84 orange #C2410C,
  85-100 red #B91C1C.
```

> ⚠️ **No uses los colores vivos en modo claro.** `#FBBF24` sobre blanco da un contraste de
> **1.60** — es prácticamente invisible. Ver [`identidad/paleta.md`](identidad/paleta.md).
