# Identidad visual — decisión final

| | |
|---|---|
| **Estado** | ✅ **Decidido** — el equipo aprobó |
| **Responsable** | Facundo Molina (FM) |
| **Fecha de decisión** | 2026-09-09 *(propuesta original: 2026-09-02)* |
| **Ticket** | [Identidad visual](https://trello.com/c/ncNYKzbF) — ✅ Hecho |
| **Entregable** | [Presentación en Canva](https://www.canva.com/design/DAHUDsuQPB8) — 17 páginas, español |

## Decisión final

El equipo eligió la **Opción B · Anomalía en grilla**: una grilla de puntos violeta con una
anomalía resaltada — la irregularidad dentro de un patrón regular, metáfora directa de lo que
detecta el fraude.

- **Isotipo:** Anomalía en grilla (path y colores en la tabla de abajo).
- **Color de marca:** violeta — `#9333EA` (modo claro) / `#A855F7` (modo oscuro), fuera de la
  escala de riesgo LOW→CRITICAL.
- **Descartados:** Opción A (Embudo) y Opción C (Prisma), documentados abajo como alternativas
  exploradas.

El board de Canva cierra con tres páginas agregadas para presentarlo formalmente:

| Pág. | Contenido |
|---|---|
| **15** | **Logo Final** — isotipo + wordmark, y su aplicación como favicon/ícono de app |
| **16** | **La marca en el mercado** — un cartel/billboard mostrando la marca ya posicionada |
| **17** | **Gracias** — cierre con crédito del equipo |

## Qué es el resto del board

Las primeras 14 páginas son el material con el que se llegó a la decisión: **símbolo, color y
tipografía** comparados y medidos. Queda como historial de cómo se decidió, no sólo el resultado.

## Estructura de la presentación

| Pág. | Contenido |
|---|---|
| 1 | Portada |
| 2 | Contexto del producto — qué es, quién lo usa, qué le exige a la identidad |
| 3 | Dirección de diseño — estética y función |
| 4 | Exploración: 27 símbolos → 6 → 3 |
| 5 | Las tres direcciones (lente · datos · abstracto) |
| 6 | Los tres finalistas, con el símbolo dibujado al lado |
| 7 | Color de marca: swatches y contrastes medidos |
| 8 | Escala de riesgo medida, nivel por nivel |
| 9 | Accesibilidad |
| 10 | Tipografía: caracteres inconfundibles y cifras tabulares |
| 11 | El dashboard en modo oscuro y claro |
| 12 | Cierre: qué elegimos |
| **13** | **El logo completo** — símbolo + palabra, que es como se usa de verdad |
| **14** | **Las tres propuestas finales** |

## Los tres finalistas

Los símbolos están dibujados como **vectores nativos** en la presentación (no imágenes generadas),
así que son editables y escalan sin pérdida. Los paths quedan acá para poder reconstruirlos:

| Opción | Concepto | Path SVG |
|---|---|---|
| **A · Embudo** | Filtrar lo relevante de un flujo grande | `M6,10 L94,10 L57,54 L57,90 L43,90 L43,54 Z` *(viewBox 100×100)* |
| **B · Anomalía en grilla** | Una irregularidad dentro de un patrón regular | 8 círculos r=8 en grilla 3×3 + 1 círculo r=12 en (78,22) *(viewBox 100×100)* |
| **C · Prisma** | Separar una señal en niveles de riesgo | `M42,12 L76,80 L8,80 Z M82,34 H116 V40 H82 Z M82,54 H116 V60 H82 Z M82,74 H116 V80 H82 Z` *(viewBox 120×100)* |

## Qué se descartó y por qué

| Descartado | Motivo |
|---|---|
| **Cyan** como color de marca | 2.33:1 sobre fondo claro — muy por debajo del mínimo AA de 4.5 |
| **Ámbar** en modo claro | 1.60:1 — inusable |
| Rojo, verde y naranja como color de marca | Ya están tomados por la escala de riesgo. La marca mentiría sobre el estado de la transacción |
| **Círculos concéntricos** | Se leen como una **diana** |
| **Círculo con barra** | Se lee como **prohibido** |

## 🔴 Lo que queda pendiente (fuera de este ticket)

- ⬜ **Corregir el rojo CRITICAL en modo oscuro:** `#DC2626` mide **4.02:1** y no llega al mínimo
  AA de 4.5. Ver [`paleta.md`](paleta.md).
- ⬜ **Elegir entre Inter e IBM Plex Sans** para la tipografía de UI del producto — es una decisión
  distinta del wordmark del logo, que ya está resuelto en el board.

## ⚠️ Deuda técnica del material

Las 8 imágenes generadas con IA que se subieron a Canva son **anteriores a la decisión del
violeta**: están en azul y sobre fondo claro. Por eso **no se usaron** en la versión final — los
símbolos y los swatches se dibujaron nativos, en el violeta aprobado.

Si en algún momento se quieren usar esas láminas, hay que regenerarlas con los **prompts 5, 6 y 7**
de [`../prompts-nano-banana.md`](../prompts-nano-banana.md), que ya están escritos para el violeta.

Las dos únicas imágenes generadas que sobrevivieron son los **mockups del dashboard** (pág. 11).
El de modo oscuro tiene las filas de datos mal renderizadas — es un defecto conocido del modelo de
imagen, y el prompt 6 lo corrige.

## Dependencia declarada

La identidad se apoya en una **hipótesis de FM**, no en una decisión del equipo: que FraudLens es
B2B para fintechs que integran el sistema como complemento de su antifraude, más un dashboard de
revisión.

El usuario objetivo real se define en [P-07](../../00-proyecto/preguntas-abiertas.md#p-07) y en el
[análisis de 6 sombreros](../analisis/6-sombreros-usuario-objetivo.md). **Si el research lo
contradice, la identidad se revisa.**
