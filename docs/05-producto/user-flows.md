# User Flow del MVP — guion para dibujar en Figma

| | |
|---|---|
| **Estado** | 🟡 **Borrador — propuesta de FM, pendiente del equipo.** El contenido está escrito acá y **hay un primer dibujo generado por Claude Code** (ver abajo), **sin revisar**. Volvió a En curso tras la [revisión de MDV](../../bitacora/2026-10-14-revision-tickets-en-revision.md) |
| **Fecha** | 2026-10-14 |
| **Responsable** | Facundo Molina (FM) |
| **Ticket** | [Plantear los User Flow de las funcionalidades del MVP](https://trello.com/c/ivQo0hEI) |
| **Herramienta** | **Figma** *(FM)* — se usó **FigJam** vía el conector de Figma · [Tablero con los 5 flujos](https://www.figma.com/board/tKo7wt7bStXRCGCLNzqlRA) |
| **Cantidad** | **5 flujos, uno por paso del [recorrido](user-story-map.md#paso-2--el-user-journey)** *(FM)* |
| **Alcance** | Solo **R1**, que es lo que se entrega *(FM)*. Usuario: Analista de fraude |

Fuentes: **(FM)** respuesta de FM del 2026-10-14 · **(R)** documento del repo · **(S)** sugerencia de Claude Code, sin aprobar · **⬜** no está definido.

## Cómo usar este archivo

Cada flujo trae sus **pasos en orden**, quién actúa en cada uno, las **decisiones** y los **caminos alternativos**. Se dibujan en Figma respetando las reglas del docente ([Clase 10](../01-clases/clase-10-user-story-mapping-y-backlog.md)):

- De **izquierda a derecha y de arriba a abajo**, **sin cruzar líneas**.
- Las **decisiones del usuario** y las **decisiones del sistema** van con **formas distintas**.
- Se refinan con comentarios del equipo.

> ⬜ **Las formas concretas que usa el docente no llegaron en la conversión del deck.** No se inventan. **FM va a mirarlas en el deck original de la Clase 10.** Mientras tanto, este guion marca cada decisión con **(U)** si la toma el usuario o **(S)** si la toma el sistema, para que el dibujo no dependa de la forma.

## El dibujo (generado por Claude Code, sin revisar)

**Tablero:** https://www.figma.com/board/tKo7wt7bStXRCGCLNzqlRA — los 5 flujos, uno al lado del otro, de izquierda a derecha. Los generó **Claude Code** (conector de Figma → FigJam, a partir de este guion) el 2026-10-14, a pedido de FM. Es un **primer borrador**, no el entregable final.

**Formas y colores usados** *(S — elegidas por Claude Code porque las del docente no se conocen; se cambian cuando FM las confirme)*:

| Elemento | Forma | Color |
|---|---|---|
| Inicio / fin del flujo | Rectángulo redondeado | Azul |
| Paso del analista | Rectángulo | Azul |
| Paso del sistema | Rectángulo | Sin color |
| **Decisión del sistema (S)** | **Rombo** | Amarillo |
| **Decisión del usuario (U)** | **Hexágono** | Violeta |

**Qué se completó en el dibujo que el guion no dice** *(todo (S), para que el equipo lo revise)*:
- **Flujo 1:** el estado vacío termina ahí; el guion no dice a dónde sigue.
- **Flujo 2:** la decisión "¿acotar o reordenar?" tiene dos salidas (filtrar / ordenar). El guion no dice qué pasa si **no** quiere ninguna.
- **Flujo 3:** si el historial es suficiente, el flujo sigue directo a "flujo 4 o volver a la lista"; si no, pasa antes por "historial insuficiente". Si el análisis no está disponible, el flujo termina en ese estado.
- **Flujo 4:** el camino "historial insuficiente" se agregó el 2026-10-15 (propuesta de FM, ver el flujo). El dibujo del Flujo 4 se regeneró.
- **Flujo 5:** las tres decisiones de umbral se dibujaron **encadenadas** (monto → revisión → bloqueo), que equivale a lo que dice el guion. El camino "monto bajo" también llega al paso "muestra la decisión recomendada": el guion no lo dice explícitamente.
- Los textos van **sin tildes** (limitación de la herramienta de generación).

⚠️ El tablero quedó creado en la cuenta de FM (borradores del plan "El equipo de Facundo Molina"). **El equipo todavía no tiene acceso**: FM tiene que moverlo a un proyecto compartido o compartirlo con MDV, FGR y ML.

**Actor de todos los flujos:** Analista de fraude. **Pasos del sistema** son los que ocurren sin que el analista haga nada.

---

## Flujo 1 — Ver la cola

**Entra por:** el analista abre el dashboard. · **Historias:** HU-01, HU-05 · **Casos de uso:** CU-05

| # | Quién | Paso | Fuente |
|---|---|---|---|
| 1 | Sistema | Muestra la lista de transacciones analizadas con: fecha y hora, identificador, usuario, monto y moneda, puntaje de riesgo, nivel de riesgo, decisión y estado del análisis | (R) CU-05, HU-01 |
| 2 | **Decisión (S)** | **¿Hay transacciones para mostrar?** | (R) HU-01 |
| 2a | Sistema | **No** → muestra un **estado vacío claro**, no una tabla en blanco | (R) CU-05, HU-01 |
| 2b | Sistema | **Sí** → muestra la lista. Los datos sensibles no se muestran completos | (R) HU-01 |
| 3 | Sistema | Cuando llega una transacción nueva, **aparece sin que el analista recargue**, o por actualización periódica | (R) CU-05, HU-05 |
| 4 | Analista | Mira la lista y sigue al **flujo 2** (encontrar casos) o al **flujo 3** (abrir uno) | (S) |

**Sale por:** el analista pasa al flujo 2 o 3.

⬜ **Qué datos son "sensibles"** no está definido (pregunta de MDV a ML). ⬜ **Cada cuánto se actualiza la lista** (decisión técnica de FGR).

---

## Flujo 2 — Encontrar los casos que importan

**Entra por:** el analista tiene la lista a la vista (flujo 1). · **Historias:** HU-02, HU-03, HU-04 · **Casos de uso:** CU-05

| # | Quién | Paso | Fuente |
|---|---|---|---|
| 1 | **Decisión (U)** | **¿Quiere acotar o reordenar la lista?** | (S) |
| 2a | Analista | **Filtra** por rango de fechas, nivel de riesgo, decisión, identificador de usuario o identificador de transacción | (R) CU-05, HU-02 |
| 3a | Sistema | Muestra **solo las transacciones que cumplen** el filtro | (R) HU-02 |
| 4a | **Decisión (S)** | **¿Alguna cumple?** → **No:** muestra el estado vacío claro | (R) HU-02 |
| 2b | Analista | **Ordena** por fecha o por riesgo | (R) CU-05, HU-03 |
| 3b | Sistema | **Reordena la tabla** según ese campo | (R) HU-03 |
| 5 | Sistema | En todo momento, los **riesgos altos y los bloqueos se distinguen visualmente** del resto, con la clasificación Bajo / Medio / Alto / Crítico | (R) CU-05, HU-04 |
| 6 | Analista | Elige un caso y sigue al **flujo 3** | (S) |

**Sale por:** el analista elige una transacción.

⬜ **Si se pueden combinar varios filtros a la vez** y **cuál es el orden por defecto**: no está definido. ⬜ **Cómo se distingue lo alto** (color, ícono o etiqueta): es decisión de diseño. Hay una regla escrita: el color **nunca va solo**, siempre con una forma o un texto ([`paleta.md`](identidad/paleta.md)).

---

## Flujo 3 — Abrir un caso

**Entra por:** el analista eligió una transacción. · **Historias:** HU-06 · **Casos de uso:** CU-06

| # | Quién | Paso | Fuente |
|---|---|---|---|
| 1 | Analista | **Abre el detalle** de la transacción | (R) CU-06 |
| 2 | **Decisión (S)** | **¿Se pudo analizar la transacción?** | (R) HU-06 |
| 2a | Sistema | **No** → muestra el estado explícito **"análisis no disponible"**, **nunca una aprobación** | (R) HU-06, requerimientos §7 |
| 2b | Sistema | **Sí** → muestra el detalle completo (ver abajo) | (R) CU-06 |
| 3 | **Decisión (S)** | **¿El usuario tiene historial suficiente?** → **No:** el resultado indica **"historial insuficiente"** | (R) CU-03 |
| 4 | Analista | Lee el detalle y sigue al **flujo 4** o **vuelve a la lista** (flujo 1) | (S) |

**Lo que muestra el detalle** *(R: CU-06)*: datos recibidos · puntaje y nivel de riesgo · decisión recomendada · reglas aplicadas · factores que elevaron el riesgo · resumen del historial utilizado · fecha y hora del análisis · configuración de umbrales vigente al analizarla.

**Sale por:** el analista sigue leyendo (flujo 4) o vuelve a la lista.

**El analista no tiene ninguna acción sobre el caso dentro de FraudLens** *(FM)*: solo ve la recomendación y actúa por fuera.

---

## Flujo 4 — Entender por qué se marcó

**Entra por:** el detalle de un caso está abierto (flujo 3). · **Historias:** HU-11 · **Casos de uso:** CU-03

| # | Quién | Paso | Fuente |
|---|---|---|---|
| 1 | **Decisión (S)** | **¿El usuario tiene historial suficiente?** | (R) CU-03 |
| 1a | Sistema | **Sí** → muestra **hasta tres factores relevantes** que elevaron el riesgo, **sin explicaciones avanzadas del modelo** | (R) CU-03, HU-11 |
| 1b | Sistema | **No** → **no muestra factores** y muestra el aviso **"historial insuficiente"** | **(FM)**, 2026-10-15 — pendiente de ML |
| 2 | Analista | Lee los factores (o el aviso), junto con el **resumen del historial utilizado** y las **reglas aplicadas** del detalle | (R) CU-06 |
| 3 | Analista | Sigue al **flujo 5** | (S) |

**Sale por:** el analista pasa a leer la recomendación.

⬜ **Qué factores se muestran cuando el historial es insuficiente** no está definido en los requerimientos (solo dicen que el resultado indica "historial insuficiente"). El camino 1b es **propuesta de FM**: sin factores, solo el aviso. **ML tiene que confirmarlo.** ⚠️ **Este flujo se solapa con el 3**: el detalle ya incluye los factores. MDV dejó abierta la duda de si HU-06 y HU-11 se fusionan; **FM los dejó en pasos distintos**, así que acá van separados.

---

## Flujo 5 — Leer la recomendación

**Entra por:** el analista mira la decisión del caso. · **Historias:** HU-12, HU-13 *(HU-13 ya está en el [mapa](user-story-map.md), paso 5, desde el 2026-10-15)* · **Casos de uso:** CU-04, CU-02

| # | Quién | Paso | Fuente |
|---|---|---|---|
| 1 | **Decisión (S)** | **¿El monto es menor al mínimo de análisis?** | (R) requerimientos §4, CU-02 |
| 1a | Sistema | **Sí** → **aprueba por regla, sin ejecutar el modelo**, y la marca **"no evaluada por el modelo"** (no le asigna un riesgo de 0 %) | (R) requerimientos §4 |
| 2 | **Decisión (S)** | **Si no:** ¿el riesgo es menor al umbral de revisión? → **Sí:** decisión **aprobar** | (R) CU-04 |
| 3 | **Decisión (S)** | ¿El riesgo es igual o mayor al de revisión y menor al de bloqueo? → **Sí:** **revisar** | (R) CU-04 |
| 4 | **Decisión (S)** | ¿El riesgo es igual o mayor al umbral de bloqueo? → **Sí:** **bloquear** | (R) CU-04 |
| 5 | Sistema | Muestra la **decisión recomendada** y **qué regla o umbral la produjo** | (R) CU-04, HU-12 |
| 6 | Analista | **Lee la recomendación y actúa por fuera de FraudLens** | **(FM)** |

**Sale por:** fin del flujo dentro de FraudLens.

⬜ **Los valores 60 % y 85 % son un ejemplo de los requerimientos, no una decisión.** Los **umbrales son fijos**, cargados al levantar el sistema ([decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md)): por eso el flujo **no incluye** cambiarlos. ⚠️ **HU-12 choca con la 0005** (MDV lo marcó) y no se resolvió acá.

---

## Qué falta

- [ ] **FM mira las formas del docente** en el deck original de la Clase 10 y las anota acá; después se ajustan las formas del tablero
- [x] ~~Dibujar los 5 flujos~~ → primer borrador generado por Claude Code ([tablero](https://www.figma.com/board/tKo7wt7bStXRCGCLNzqlRA))
- [ ] **FM mueve el tablero a un proyecto compartido o lo comparte con MDV, FGR y ML.** Hoy está en sus borradores y **nadie más lo puede abrir** (MDV lo comprobó el 14/10)
- [ ] **Revisar que no haya líneas cruzadas** en el dibujo: lo tiene que mirar alguien con acceso
- [x] ~~Camino alternativo del Flujo 4~~ → agregado (propuesta de FM, pendiente de ML)
- [ ] Revisar que cada flujo muestre **camino principal y al menos un camino alternativo** (los hay: filtro sin resultados, análisis no disponible, historial insuficiente, monto bajo)
- [ ] **Revisión del equipo**, en particular de FGR por lo técnico (frecuencia de actualización, qué es sensible)
- [ ] Si el equipo decide **otro actor o más historias**, se agregan flujos ([P-32](../00-proyecto/preguntas-abiertas.md#p-32))

## Fuentes

[`user-story-map.md`](user-story-map.md) · [`product-backlog-borrador.md`](product-backlog-borrador.md) · [`requerimientos-funcionales-mvp.md`](requerimientos-funcionales-mvp.md) · [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md) · [Clase 10](../01-clases/clase-10-user-story-mapping-y-backlog.md) · [`identidad/paleta.md`](identidad/paleta.md)
