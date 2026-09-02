# Análisis de la primera generación — Nano Banana

| | |
|---|---|
| **Fecha** | 2026-09-02 |
| **Generado por** | FM en Nano Banana (Gemini) |
| **Analizado por** | FM con asistencia de Claude Code |
| **Estado** | 🟡 Shortlist propuesta — **decide el equipo + el docente** |

8 imágenes: 3 láminas de isotipos, 2 de paleta, 2 de dashboard, 1 de tipografía.

---

## 1. Isotipos — shortlist

De los 27 símbolos generados, **6 sobreviven** al filtro de: concepto claro, legible a 24px, y que
no signifique otra cosa.

| # | Lámina | Cuál | Concepto | Por qué entra |
|---|---|---|---|---|
| **A** | 1C abstracta | Embudo de líneas convergentes *(fila 1, col 2)* | **Filtrado** | Es literalmente lo que FM dijo que hace el producto: *"un filtro más específico"*. El concepto y el producto coinciden sin explicación |
| **B** | 1C abstracta | Grilla con un punto en una celda *(fila 1, col 3)* | **Anomalía** | El más simple de todos. Funciona a 16px. Dice "algo distinto en un conjunto" sin decorar |
| **C** | 1A lente | Prisma refractando *(fila 1, col 3)* | **Separación en bandas** | Un prisma separa un haz en componentes; nosotros separamos un flujo en niveles de riesgo. Conceptualmente el más rico |
| **D** | 1A lente | Marco de foco con punto *(fila 2, col 2)* | **Foco / viewfinder** | Muy limpio y legible. Contra: es un patrón visto mil veces |
| **E** | 1B lente+dato | Waveform con pico *(fila 2, col 1)* | **Detección de anomalía** | Clarísimo de leer. Contra: el pico salió verde (ver problema abajo) |
| **F** | 1A lente | Apertura de cámara *(fila 1, col 1)* | **Lente** | Bien ejecutado. Contra: es el logo de toda app de cámara |

### Descartados que conviene nombrar

- **Círculos concéntricos con punto** (1A) → lee **diana / target**, no lente. Aparece dos veces.
- **Dos círculos con barra diagonal** (1A, fila 3 col 1) → lee **"prohibido"**. Significado equivocado.
- **Ráfaga radial** (1A, fila 3 col 3) → lee **sol o destello**.
- **Cubos isométricos, red de nodos, gráfico de barras** (1B) → conceptos correctos pero **demasiado
  detalle**: a 24px se convierten en una mancha.

### 🔴 Problema en la lámina 1B

**El acento salió verde** (#4ADE80 aprox), que es exactamente el color de **LOW** en la escala de
riesgo. Un logo verde en un producto donde verde significa "aprobado" es el choque que quisimos
evitar desde el principio. Si se elige **E**, hay que recolorear el pico.

---

## 2. Paletas — verificación de contraste

Medí el contraste WCAG real de las dos láminas. **Los números son verificables, no opinión.**

### Escala de riesgo

| Nivel | Hex (lámina oscura) | Sobre fondo oscuro | Sobre fondo claro |
|---|---|---|---|
| LOW | `#16A34A` | ✅ 5.89 | ⚠️ 3.16 |
| MEDIUM | `#FBBF24` | ✅ 11.62 | ❌ **1.60** |
| HIGH | `#F97316` | ✅ 6.92 | ❌ **2.69** |
| CRITICAL | `#DC2626` | ⚠️ 4.02 | ✅ 4.63 |

> ✅ ≥4.5 (texto normal) · ⚠️ ≥3 (texto grande o iconos) · ❌ insuficiente

**Conclusión dura:** en **modo claro**, amarillo y naranja **no se pueden usar como texto ni como
relleno con texto encima**. Fallan por lejos. En modo claro esos niveles tienen que ir como
**chip relleno con texto oscuro**, o con un tono bastante más profundo.

Esto no es un detalle estético: es la diferencia entre un dashboard que se lee y uno que no.

### Color de marca

| Familia | Hex | Sobre oscuro | Sobre claro | ¿Sirve para los dos modos? |
|---|---|---|---|---|
| Azul | `#2563EB` | ⚠️ 3.75 | ✅ 4.95 | ✅ Sí |
| Violeta | `#9333EA` | ⚠️ 3.61 | ✅ 5.16 | ✅ Sí |
| Indigo | `#4F46E5` | ⚠️ 3.09 | ✅ 6.02 | ✅ Sí, justo |
| Cyan | `#06B6D4` | ✅ 7.99 | ❌ **2.33** | ❌ **No** |

> 🔴 **El cyan queda descartado.** Como decidimos soportar modo claro **y** oscuro, un color que
> falla en uno de los dos no sirve. Quedan **azul, violeta e indigo**.

### Diferencia entre las dos láminas

Las dos láminas usan **valores distintos para los mismos nombres**:

- **Lámina clara:** `#007BFF`, `#6F42C1`, `#17A2B8`, `#6610F2` → son los colores por defecto de **Bootstrap**
- **Lámina oscura:** `#2563EB`, `#9333EA`, `#06B6D4`, `#4F46E5` → son los de **Tailwind**

**Los de la lámina oscura son mejores**: están calibrados perceptualmente y son el estándar actual.
Recomendación: usar esos valores para los dos modos.

---

## 3. Mockups de dashboard

### ✅ El de modo claro salió notablemente mejor

- Las métricas tienen sentido real: *Total Transactions 14,250 · Flagged for Review 312 ·
  Blocked Attempts 85 · Avg. Risk Score 42*
- **La accesibilidad funciona**: cada nivel de riesgo tiene **color + un ícono de forma distinta**
  (check, triángulo, rombo, círculo). Se entiende en escala de grises. Era el requisito y se cumplió
- Los scores son coherentes con las decisiones: 15→APPROVE, 48→REVIEW, 72→REVIEW, 94→BLOCK
- ⚠️ Una fila inconsistente: score 15 (verde) con decisión REVIEW

### ⚠️ El de modo oscuro tiene problemas de contenido

- Las métricas son **texto sin sentido**: *"Brandid scores"*, *"Metric scored"*, *"Amount score"*,
  *"Total metrics"*. Los filtros dicen *"All liits"*, *"All filtew"*
- **Los scores contradicen las decisiones**: 70/100 en verde con APPROVE, mientras 60/100 en rojo da
  BLOCK. La escala está invertida o inventada
- Todos los usuarios son el mismo *"aaam @smith"*

> Es ruido típico de generación de imágenes. **No invalida la dirección visual** —el layout y la
> paleta se leen bien— pero **este mockup no se puede mostrar tal cual** al docente: si alguien lee
> los números, la demo pierde credibilidad.

---

## 4. Tipografía

La lámina se ve bien y el estilo `[BRACKETS_MAYÚSCULA]` es coherente con la referencia Linear/Vercel.

**Pero tiene una limitación de fondo: no dice qué fuente es.** Nano Banana dibuja *una* geométrica
genérica; no elige una tipografía real que podamos usar.

Además, en la comparación de caracteres:
- La **S** y el **8** salieron en itálica mientras el resto es redonda — artefacto de generación
- El **0** y la **O** se parecen demasiado
- El **1** no tiene base ni remate, así que **1 / l / I** siguen siendo confundibles

Justo lo que la lámina tenía que demostrar que **no** pasaba.

### Hay que elegir una fuente real de Google Fonts

Dos candidatas que cumplen los requisitos del brief:

| Fuente | A favor |
|---|---|
| **Inter** | Diseñada para UI. Tiene **cifras tabulares** y un **cero barrado** opcional como set estilístico. Es la que usan Linear y buena parte del ecosistema moderno |
| **IBM Plex Sans** | Muy buena diferenciación de caracteres, cifras tabulares, y un aire técnico que encaja con la referencia Datadog/Grafana. Tiene familia **Mono** hermana para los IDs |

**Propuesta:** una de esas dos para la UI, más una **monoespaciada** (IBM Plex Mono o JetBrains Mono)
sólo para los `TRANSACTION ID`. Los IDs en mono se escanean mucho mejor.

⬜ **A verificar antes de cerrar:** descargar la fuente elegida y comprobar en el archivo real que
`0/O` y `1/l/I` se distinguen. No confiar en la lámina generada.

---

## 5. Qué falta para cerrar el ticket

- [ ] El equipo elige **1 isotipo** de la shortlist
- [ ] El equipo elige **1 color de marca** entre azul, violeta e indigo
- [ ] Elegir la **tipografía real** y verificarla
- [ ] Corregir los valores de la escala de riesgo para **modo claro**
- [ ] Rehacer el **mockup oscuro** con datos coherentes
- [ ] Montar el **wordmark** "FraudLens" con la tipografía elegida
- [ ] Board de presentación para el equipo y el docente
- [ ] Comentario de resolución en la tarjeta de Trello
