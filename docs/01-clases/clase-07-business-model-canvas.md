# Clase 07 — Roadmap · Modelo de negocio · Business Model Canvas

| | |
|---|---|
| **Fecha** | Miércoles 9/9, según el cronograma oficial |
| **Docente** | Daniel Britez |
| **Material** | `007_-_Clase_08_SIPI_Business_Model_Canvas.md` |
| **Cargada por** | Facundo Molina (FM) |
| **Fecha de carga** | 2026-09-15 |

> ⚠️ **Numeración ([P-20](../00-proyecto/preguntas-abiertas.md#p-20)):** el archivo original trae
> **dos numeraciones distintas entre sí** — el prefijo del nombre es `007` pero el título interno
> dice "Clase_08". Ninguna de las dos coincide necesariamente con el cronograma. Se cargó como
> **Clase 07** de este repo (siguiente después de la 06), por prefijo y por orden — sin asumir cuál
> de los dos números internos es el "correcto" para el docente.

---

## 1. De qué se trató

La clase retoma el proceso de Design Thinking (Empatizar → Definir → Idear → Prototipar → Testear)
y la Estrategia del Océano Azul de la clase anterior, y avanza al bloque de **modelo de negocio**:
qué es un Business Model Canvas, cómo se arma bloque por bloque, y cómo se calcula el costo de un
proyecto con el concepto de Profit & Loss (P&L). Cierra con los modelos de monetización más usados.

---

## 2. Conceptos

### Business Model Canvas (BMC)

Herramienta para definir y crear modelos de negocio innovadores, que simplifica el negocio en
**4 grandes áreas**: **Clientes**, **Oferta**, **Infraestructura**, **Viabilidad Económica** — y
dentro de esas áreas, **9 bloques**:

| Bloque | Pregunta que responde |
|---|---|
| **Segmentos de clientes** | ¿Cuáles son nuestros segmentos más importantes? ¿Mercado masivo o nicho? ¿Hay varios segmentos interrelacionados? |
| **Propuesta de valor** | ¿Qué problema solucionamos y qué valor aportamos? (novedad, diseño, marca/status, rendimiento, precio, personalización, reducción de costos) |
| **Canales** | ¿Cómo entregamos la propuesta de valor a cada segmento? ¿Cuáles son los más rentables? |
| **Relación con clientes** | ¿Qué relación mantenemos? (asistencia personal, autoservicio, comunidades, co-creación) |
| **Fuentes de ingreso** | ¿Qué valor están dispuestos a pagar? ¿Cómo pagan hoy y cómo les gustaría pagar? |
| **Recursos clave** | Físicos, intelectuales, humanos, financieros |
| **Actividades clave** | Las que permiten entregar la propuesta de valor a través de los canales y la relación elegida |
| **Socios clave** | Alianzas que complementan capacidades y reducen incertidumbre (red de proveedores, partners) |
| **Estructura de costos** | Costos fijos y variables asociados a las actividades y recursos de arriba |

> 🎯 **Aplicado a FraudLens:** los 9 bloques son exactamente los que ya usamos en
> [`modelo-negocio.md`](../05-producto/modelo-negocio.md) (armado el 14/9, antes de tener esta
> clase cargada) — coincide bloque por bloque. Lo que la clase agrega y todavía no teníamos es el
> **Profit & Loss** (ver abajo).

### Profit & Loss (P&L) y Horas-Hombre (HH)

El P&L es el "excel" donde se cargan los costos y se planean las ganancias. Se arma en 5 pasos:

1. **Identificar recursos y tareas** — personas, actividades, herramientas, hosting, licencias.
2. **Calcular Horas-Hombre (HH)** — cantidad de tiempo que un trabajador dedica a una tarea.
   *Ejemplo del docente:* 2 personas × 3 horas = 6 HH.
3. **Separar costos fijos y variables.**
4. **Registrar egresos e ingresos** — por mes o cuatrimestre, en dólar oficial y sin inflación.
5. **Analizar viabilidad** — inversión inicial, cuándo llegan los ingresos, cuándo hay beneficio,
   cuándo se recupera la inversión.

> 🎯 **Aplicado a FraudLens:** esto es exactamente lo que **no tenemos todavía**. El
> [modelo de negocio](../05-producto/modelo-negocio.md) tiene los 9 bloques como hipótesis, pero
> cero estimación de costos en HH ni un P&L armado. Es tarea nueva, no cubierta hasta ahora.

### Modelos de monetización

**5 técnicas para monetizar** (mencionadas por el docente): Freemium · Pago por descarga ·
Compras In-App · Suscripciones · Anuncios In-App *(el docente marca explícitamente que NO
recomienda esta última)*.

**3 patrones de modelo de negocio** además de las técnicas de monetización:

| Modelo | Cómo funciona |
|---|---|
| **Long Tail** | Vender menos cantidad de más variedad — muchos productos de bajo volumen individual |
| **Cebo y Anzuelo** | Vender (o regalar) un producto barato para "enganchar" al cliente en la compra repetitiva de algo con mejor margen (repuestos, consumibles, servicios) |
| **Plataforma Multilateral** | Reúne 2+ grupos de clientes interdependientes; el valor lo crea la interacción entre grupos (negocios P2P) |

> 🎯 **Aplicado a FraudLens:** el [modelo de negocio](../05-producto/modelo-negocio.md) ya propuso
> **Suscripción/licencia** como fuente de ingreso — coincide con una de las 5 técnicas que dio el
> docente, y explícitamente **no** es el modelo de garantía financiera (que sería más parecido a
> "Cebo y Anzuelo" invertido) que ya se había descartado en el benchmarking.

---

## 3. Aplicación a FraudLens

| Qué | Por qué | Dónde se refleja |
|---|---|---|
| Los 9 bloques del BMC ya están cubiertos como hipótesis | Se armaron el 14/9, antes de tener esta clase — coinciden con la estructura real que enseñó el docente | [`modelo-negocio.md`](../05-producto/modelo-negocio.md) |
| Falta el **P&L** (costos en HH, egresos/ingresos, viabilidad) | Es lo único de esta clase que no está cubierto todavía en el proyecto | ⬜ Nuevo, sin empezar |
| El modelo de ingresos elegido (suscripción) coincide con una técnica válida del docente | Confirma que no se inventó una categoría rara — es una de las 5 técnicas dadas en clase | [`modelo-negocio.md`](../05-producto/modelo-negocio.md#5-fuentes-de-ingreso--⬜-hipótesis-sin-confirmar) |
| "Terminar de armar el MVP en su totalidad" (research → solución → benchmarking → roadmap → costos) es el pedido explícito para la próxima clase | Ya tenemos research (bloqueado), solución/narrativa, benchmarking y roadmap — **sólo falta costos** | Ver sección 4 |

---

## 4. Qué tenemos que hacer para la próxima

| Tarea | Responsable | Fecha límite | Trello |
|---|---|---|---|
| Armar el P&L: identificar recursos/tareas, calcular HH, separar costos fijos/variables | ⬜ Sin asignar | Antes de la próxima clase | ⬜ Crear tarjeta |
| Terminar de armar el MVP en su totalidad (research, solución, benchmarking, roadmap, costos) | Equipo | Antes de la próxima clase | Ya cubierto por tarjetas existentes + P&L nueva |
| Presentación de Avance | Equipo — rota según la regla de Sprint Reviews | Próxima clase | ⬜ Crear tarjeta |

---

## 5. Dudas que quedaron

- La numeración del archivo (`007` vs "Clase_08" interno) — sumado a [P-20](../00-proyecto/preguntas-abiertas.md#p-20), que ya venía con desfases de numeración en clases anteriores.
- El docente no aclaró en el material si el P&L usa una planilla modelo propia de la cátedra — el texto dice *"tomar planilla modelo"* pero no se adjuntó ninguna en este material.

---

## 6. Términos nuevos para el glosario

- [x] *Business Model Canvas (BMC)* → actualizado (ya estaba, se completa) en [`glosario.md`](../00-proyecto/glosario.md)
- [x] *Profit & Loss (P&L)* → actualizado (ya estaba, se completa) en [`glosario.md`](../00-proyecto/glosario.md)
- [x] *Horas-Hombre (HH)* → agregado a [`glosario.md`](../00-proyecto/glosario.md)
- [x] *Modelos de monetización (Freemium, Suscripción, etc.)* → agregado a [`glosario.md`](../00-proyecto/glosario.md)
- [x] *Long Tail / Cebo y Anzuelo / Plataforma Multilateral* → agregado a [`glosario.md`](../00-proyecto/glosario.md)
