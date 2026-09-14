# Assets oficiales del logo — FraudLens

| | |
|---|---|
| **Estado** | ✅ Generados a partir del pptx exportado de Canva |
| **Fecha** | 2026-09-14 |
| **Fuente** | `Propuesta_de_Identidad_Visual_-_FraudLens.pptx` (Canva exportado), slide 14 "Logo Final" |
| **Referencia** | [`../propuesta-canva.md`](../propuesta-canva.md) |

## Cómo se generaron

**No se recortaron capturas de pantalla del pptx.** Se extrajo la geometría exacta de los shapes
vectoriales (`custGeom`) del slide 14 del pptx y se reconstruyó el isotipo en un script Python
([`make_logo_assets.py`](#script)), así los PNG son nítidos a cualquier tamaño y no arrastran
artefactos de compresión ni el fondo de la diapositiva.

La grilla confirma exactamente lo ya documentado en
[`propuesta-canva.md`](../propuesta-canva.md#los-tres-finalistas): 8 círculos r=8 en grilla 3×3
(columnas/filas en 22, 50, 78 sobre un viewBox 100×100) + 1 círculo r=12 (la anomalía) en la
posición (78, 22).

## Paleta usada (extraída del pptx, no inventada)

El pptx usa **dos tratamientos de color según el fondo** — esto ya estaba en el deck, no es una
decisión nueva:

| | Dots regulares | Anomalía | Texto "FraudLens" |
|---|---|---|---|
| **Modo claro** (fondo `#FAFAFA`) | `#6B21A8` | `#9333EA` | `#0D0D10` |
| **Modo oscuro** (fondo `#0D0D10`) | `#7E22CE` | `#C084FC` | `#FFFFFF` |

La versión **monocromática blanca** (`isotipo-monocromo-blanco.png`) **no está en el pptx** — es
una extrapolación práctica para usar el ícono sobre fondos de color o fotografías, siguiendo el
mismo criterio que ya usa el wordmark en blanco sobre fondo oscuro. Se marca acá para que quede
claro qué viene del deck y qué es agregado.

## ⚠️ Tipografía: sustitución declarada

El pptx usa **Arimo Bold** para el wordmark. Arimo no está instalada en este entorno, así que los
PNG usan **Liberation Sans Bold** — es la fuente métricamente compatible con Arial que también usa
Arimo como base, por lo que el ancho y la proporción de "FraudLens" son equivalentes. Si alguien
regenera estos assets con Arimo instalada, el resultado visual es el mismo.

## Archivos

| Archivo | Uso |
|---|---|
| `isotipo-modo-claro.png` | Ícono solo, para fondos claros |
| `isotipo-modo-oscuro.png` | Ícono solo, para fondos oscuros |
| `isotipo-monocromo-blanco.png` | Ícono solo, en blanco — para fondos de color o fotos |
| `logo-completo-modo-claro.png` | Isotipo + wordmark, horizontal, para fondos claros |
| `logo-completo-modo-oscuro.png` | Isotipo + wordmark, horizontal, para fondos oscuros |
| `favicon.png` | Ícono cuadrado con fondo (`#17171B`, borde `#7E22CE`), replica el mockup de "Favicon / ícono de app" del slide 14 |

Todos en PNG con fondo transparente (excepto `favicon.png`, que ya lleva su fondo), en alta
resolución (isotipos e ícono de app a 1024×1024 y 512×512; el logo completo a 1471×370).

## Script

[`make_logo_assets.py`](make_logo_assets.py) — Python + Pillow, reconstruye la grilla desde las
coordenadas exactas extraídas del pptx. Se puede volver a correr para regenerar los assets o
ajustar tamaños/paddings.

## Qué falta

- ⬜ Si el equipo quiere una versión **SVG** (vectorial, no rasterizada) de cada variante, se puede
  generar con el mismo script adaptado — hoy sólo produce PNG.
- ⬜ Validar que `favicon.png` se vea bien recortado a los tamaños reales que exige cada plataforma
  (16×16, 32×32, 180×180 para iOS, etc.) — hoy es un único tamaño base (512×512).
