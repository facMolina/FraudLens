# Preguntas abiertas

Todo lo que falta definir. Cuando una pregunta se responde: se marca **✅ Resuelta**, se escribe la
respuesta, y si la respuesta cambia el rumbo del proyecto se registra además como
[decisión](../03-decisiones/).

**Prioridad:** 🔴 bloqueante · 🟡 importante · 🟢 puede esperar

| ID | Pregunta | Prioridad | Para quién | Estado |
|---|---|---|---|---|
| [P-01](#p-01) | ¿Cuál es el título oficial del proyecto? | 🟡 | Equipo | ✅ **Resuelta** |
| [P-02](#p-02) | ¿El problema ya está aprobado por los docentes? | 🔴 | Docente | ✅ **Resuelta** |
| [P-03](#p-03) | ¿El equipo queda con 4 integrantes? | 🔴 | Docente | ✅ **Resuelta** |
| [P-04](#p-04) | ¿Cuál es el calendario real de 2C 2026? | 🔴 | Docente | 🔲 Abierta |
| [P-05](#p-05) | ¿Dónde vive el código del MVP? | 🟡 | Equipo | 🔲 Abierta |
| [P-06](#p-06) | ¿Qué datos reales vamos a usar? | 🔴 | Equipo | 🟡 **Parcial** |
| [P-07](#p-07) | ¿Quién es el usuario objetivo? | 🔴 | Equipo | 🔲 Abierta |
| [P-08](#p-08) | ¿Qué roles toma cada integrante? | 🟡 | Equipo | 🔲 Abierta |
| [P-09](#p-09) | ¿Cómo se estructura el tablero de Trello? | 🟡 | Equipo | 🔲 Abierta |
| [P-10](#p-10) | ¿Qué stack tecnológico usamos? | 🟢 | Equipo | 🔲 Abierta |
| [P-11](#p-11) | ¿Cuál es el dataset de casos de prueba del MVP? | 🟡 | Equipo | 🔲 Abierta |
| [P-12](#p-12) | ¿En qué estado está el User Research? | 🔴 | Equipo | 🔲 Abierta |
| [P-13](#p-13) | ¿Qué entregables de las Clases 2, 3 y 4 ya están hechos? | 🔴 | Equipo | 🔲 Abierta |
| [P-14](#p-14) | ¿Cuándo es la Clase 5 y qué pide? | 🔴 | Equipo | 🔲 Abierta |
| [P-15](#p-15) | ¿Qué se hace con el documento de requerimientos de FGR? | 🟡 | Equipo | 🔲 Abierta |
| [P-16](#p-16) | ¿El ejercicio de los 4 ejes (Clase 3) se aplica al problema del proyecto? | 🟢 | Docente | 🔲 Abierta |
| [P-17](#p-17) | Las 400 respuestas, ¿son sólo de la encuesta o del total? | 🔴 | Docente | 🔲 Abierta |
| [P-18](#p-18) | Los 3 usuarios del Design Thinking, ¿son 3 personas o 3 perfiles? | 🔴 | Docente | 🔲 Abierta |

---

## P-01
### ¿Cuál es el título oficial del proyecto?

**✅ Resuelta** *(FM, 2026-09-02)*

> **FraudLens** es el **nombre "marketinero"** que el equipo le puso al sistema.

El título académico que figura en la planilla del docente es *"Sistema inteligente de detección de
fraude en transacciones en tiempo real"*. Los dos conviven: **FraudLens** es el nombre de producto
(marca, tablero, pitch) y la frase larga es la descripción formal del proyecto.

---

## P-02
### ¿El problema ya está aprobado por los docentes?

**✅ Resuelta** *(FM, 2026-09-02)*

> **Sí. El docente aprobó el problema.**

FraudLens es la problemática confirmada del equipo para todo el cuatrimestre. La instancia de
selección de problema (Clases 2 y 3) ya está superada.

---

## P-03
### ¿El equipo queda con 4 integrantes?

**✅ Resuelta** *(FM, 2026-09-02)*

> **Sí, el equipo queda con 4 integrantes**, porque este cuatrimestre hay menos gente cursando.

La indicación de "seis/ocho integrantes" de la Clase 1 no aplica a esta cursada.

**Consecuencia:** el trabajo de la materia está dimensionado para equipos de 6-8. Con 4 personas
cada uno carga más. Es un motivo más para llevar la documentación al día en vez de acumularla.

---

## P-04
### ¿Cuál es el calendario real de 2C 2026?

**🔲 Abierta** — FM confirmó que **el cronograma del deck de Clase 1 hay que ignorarlo** (es del 1C)
y que va a pasar el cronograma real.

Hace falta:
- Fecha de cada clase
- Fecha de la **Primera Entrega** y de la **Segunda Entrega**
- Fechas de inicio/fin de cada uno de los **4 Sprints**
- Fecha de **entrega de documentación final**, **Simulacro The Pitch** y **The Pitch**
- Fecha del **recuperatorio** (última clase del cuatrimestre)

**Impacto:** sin esto no se puede planificar nada. Es lo primero a completar en
[`docs/02-entregables/README.md`](../02-entregables/README.md).

---

## P-05
### ¿Dónde vive el código del MVP?

Este repo es el centro de cómputos, no el producto. El MVP (API + modelo + web) necesita su lugar.

Opciones:
1. **Repositorio aparte** — más prolijo, separa documentación de código. *(sugerido)*
2. **Carpeta dentro de este repo** — todo junto, más simple de encontrar.

Sea cual sea, hay que dejar el link acá y en el README.

---

## P-06
### ¿Qué datos reales vamos a usar?

**🟡 Parcialmente resuelta** *(FM, 2026-09-02)*

El docente exige **datos reales** para el User Research. Para FraudLens esto se abre en dos frentes:

**a) Datos para el modelo — ✅ resuelto en parte:** el equipo **tiene un dataset de casos de prueba
para el MVP**. Falta registrar cuál es, de dónde sale y qué contiene → ver [P-11](#p-11).

**b) Datos del problema (User Research) — 🔲 abierto:** ¿a quién entrevistamos? ¿Gente que sufrió
fraude? ¿Alguien que trabaje en prevención de fraude en un banco, fintech o procesador de pagos?
La Clase 4 pide **400 respuestas en total** entre encuestas, entrevistas y observaciones.

**Pendiente asociado:** definir con qué **métricas** se evalúa el modelo. Los datos de fraude están
muy desbalanceados, así que *accuracy* no sirve.

---

## P-07
### ¿Quién es el usuario objetivo?

FraudLens "asiste en la decisión de aprobar, rechazar o revisar". ¿Quién toma esa decisión?

- ¿Un **analista de fraude** que revisa una cola de casos? → el producto es un panel de revisión.
- ¿Un **sistema automático** del comercio? → el producto es una API y la web es secundaria.
- ¿El **dueño de un comercio chico** sin equipo antifraude? → el producto es otra cosa distinta.

**Impacto:** define la interfaz, el MVP y todo el User Research. Es la pregunta más importante de
la lista después del calendario. Se trabaja en la **Clase 2 (Segmentación de usuarios / Target)**.

---

## P-08
### ¿Qué roles toma cada integrante?

Ver la tabla de roles propuesta en [`equipo.md`](equipo.md#roles-a-repartir).
También hay que armar la rotación de presentadores de Sprint Reviews.

---

## P-09
### ¿Cómo se estructura el tablero de Trello?

El tablero **forma parte de la evaluación** ("Tableros de trabajo (Trello/Jira)"), así que no puede
estar desprolijo. Hay que definir listas, etiquetas y convención de tarjetas.

Propuesta inicial en [`docs/04-metodologia/trello.md`](../04-metodologia/trello.md) — falta validarla
contra el estado actual del tablero.

---

## P-10
### ¿Qué stack tecnológico usamos?

API, modelo e interfaz web. A definir cuando lleguemos al bloque de desarrollo, pero conviene
tenerlo pensado antes del Sprint 1 para no perder tiempo.

Criterio sugerido: **elegir lo que el equipo ya sabe usar**. El cuatrimestre es corto y la nota no
premia aprender un framework nuevo — premia tener un MVP funcionando.


---

## P-11
### ¿Cuál es el dataset de casos de prueba del MVP?

FM confirmó que el equipo **tiene un dataset de casos de prueba para el MVP**. Falta registrarlo:

- ¿Cuál es? ¿Nombre, origen, link?
- ¿Es un dataset público, uno provisto por el docente, o generado por el equipo?
- ¿Cuántos registros tiene y qué columnas?
- ¿Trae la etiqueta de fraude (`is_fraud`) o hay que construirla?
- ¿Alcanza para **entrenar** el modelo o sólo para **probar** el MVP? *(no es lo mismo)*

Cuando esté la respuesta, se documenta en `docs/05-producto/datos.md`.

> **Recordatorio:** los datasets **no se versionan** en este repo (`data/` y `*.csv` están en
> `.gitignore`). Se documenta de dónde bajarlo, no el archivo.

---

## P-12
### ¿En qué estado está el User Research?

**🔲 Abierta** — FM pidió avanzar esto **después** de tener el repo listo y Trello conectado.

La Clase 4 pide, para la **Clase 5 (que es la próxima)**:

- Armar y realizar la difusión de **encuestas, entrevistas y observaciones — 400 respuestas en total**
- **Design Thinking de al menos 3 posibles usuarios**: User Persona · Mapa de Empatía · Escenario Actual

Lo que sí sabemos *(FM, 2026-09-02)*: en la Clase 4 el equipo trabajó en el **documento de
requerimientos funcionales del MVP** y definió el nombre **FraudLens**. Es decir, **las herramientas
de Design Thinking todavía no se aplicaron a FraudLens**.

Falta confirmar:

- ¿Ya se armó la encuesta? ¿Está difundida? ¿Cuántas respuestas hay hoy?
- ¿Se hicieron entrevistas? ¿A quiénes?

🔴 **Es el pendiente más pesado del proyecto: 400 respuestas no se juntan en dos días.**

---

## P-13
### ¿Qué entregables de las Clases 2, 3 y 4 ya están hechos?

Del material de esas clases surgen entregables concretos. Falta saber cuáles ya están:

| Origen | Entregable | ¿Hecho? |
|---|---|---|
| Clase 2 | Redacción del problema **con su segmentación y target** (adelanta el primer entregable) | ⬜ |
| Clase 2 / 3 | Selección definitiva de la problemática | ✅ *(el docente aprobó — [P-02](#p-02))* |
| Clase 3 | Árbol de Problemas | ⬜ |
| Clase 3 | Análisis de causa raíz (**5 Por Qué**) | ⬜ |
| Clase 4 | User Persona (× 3 usuarios) | ❌ **No** |
| Clase 4 | Mapa de Empatía (× 3 usuarios) | ❌ **No** |
| Clase 4 | Escenario Actual / AS-IS | ❌ **No** |
| Clase 4 | User Journey Map | ❌ **No** |
| Clase 4 | Encuestas / entrevistas / observaciones (400 respuestas) | ❌ **No** → [P-12](#p-12) |
| *(fuera de consigna)* | Requerimientos funcionales del MVP | ✅ Hecho por FGR en la Clase 4 — [borrador](../05-producto/requerimientos-funcionales-mvp.md) |
| *(fuera de consigna)* | Definición del nombre **FraudLens** | ✅ Hecho en la Clase 4 |

---

## P-14
### ¿Cuándo es la Clase 5 y qué pide?

**🟡 Parcialmente resuelta** *(FM, 2026-09-02)*

> **La Clase 5 es la próxima** — todavía no se dio.

Por lo tanto, lo que hay que llevar preparado es **lo que pidió la Clase 4**:

1. Encuestas, entrevistas y observaciones difundidas — **400 respuestas en total**
2. **User Persona · Mapa de Empatía · Escenario Actual** de al menos 3 posibles usuarios

**Falta:** la **fecha** de la Clase 5 (depende del cronograma real → [P-04](#p-04)).

---

## P-15
### ¿Qué se hace con el documento de requerimientos de FGR?

Francisco escribió [`docs/05-producto/requerimientos-funcionales-mvp.md`](../05-producto/requerimientos-funcionales-mvp.md)
y lo pasó **para revisión, no como definición**.

El equipo tiene que decidir:

1. **Se aprueba como está** → pasa a ser definición y se registra como decisión.
2. **Se aprueba con ajustes** → se anotan los cambios y después se registra.
3. **Se posterga** hasta tener el User Research, porque define el usuario por adelantado.

Los puntos a discutir están listados al final del propio documento.


---

## P-16
### ¿El ejercicio de los 4 ejes (Clase 3) se aplica al problema del proyecto?

El deck de la Clase 3 trae un ejercicio de evaluación de problemas con cuatro ejes (áreas afectadas ·
gravedad · duración · número de problemas simultáneos), pero está **redactado en primera persona y
en clave personal/emocional** ("mi vida", "salud emocional").

No queda claro del material si el docente lo usa tal cual, o como analogía para evaluar la
**relevancia y persistencia** de un problema de producto.

**Impacto:** bajo. Es una herramienta de apoyo, no un entregable. Pero si hay que aplicarla a
FraudLens conviene saberlo antes del documento final.

---

## P-17
### Las 400 respuestas, ¿son sólo de la encuesta o del total?

La consigna dice: *"Armar y realizar la difusión de encuestas, entrevistas y observaciones
(400 respuestas en total)"*.

- **Lectura A:** 400 respuestas **de encuesta**, más entrevistas y observaciones aparte.
- **Lectura B:** 400 en total sumando las tres técnicas.

**Impacto: alto.** Cambia por completo el esfuerzo de difusión y a cuánta gente hay que llegar.
Con 4 integrantes son **100 respuestas por persona** en el peor caso.

---

## P-18
### Los 3 usuarios del Design Thinking, ¿son 3 personas o 3 perfiles?

La consigna dice: *"Design Thinking de al menos 3 posibles usuarios: User Persona, Mapa de empatía,
Escenario actual"*.

- **Lectura A:** 3 **perfiles/segmentos distintos** (por ejemplo: analista de fraude, administrador,
  dueño de comercio) — cada uno con su Persona, Mapa y Escenario.
- **Lectura B:** 3 **personas reales entrevistadas** del mismo perfil.

**Impacto: alto.** Si es la lectura A, hay que definir **cuáles son nuestros 3 perfiles candidatos**
antes de arrancar — y eso conecta directo con [P-07](#p-07).

> El documento de FGR ya nombra tres actores humanos posibles (**sistema cliente**,
> **analista de fraude**, **administrador**). Podrían ser el punto de partida, pero **eso hay que
> decidirlo en equipo**, no darlo por hecho.
