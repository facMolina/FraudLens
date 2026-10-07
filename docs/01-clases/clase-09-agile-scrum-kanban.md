# Clase 09 — Agile · Scrum · Kanban

| | |
|---|---|
| **Fecha** | **Miércoles 23/9** *(confirmada por FM, 2026-10-07; no figura en el material)* |
| **Docente** | Daniel Britez *(el deck está firmado por Ing. Juan C. Montero · Ing. Julieta Viarengo · Ing. Silvina Gentile)* |
| **Material** | `Clase_09_SIPI_AgileScrumKanban.md` → [`material/clase-09-agile-scrum-kanban.md`](material/clase-09-agile-scrum-kanban.md) |
| **Cargada por** | Facundo Molina (FM) |
| **Fecha de carga** | 2026-10-07 |

> ✅ **Fecha ([P-28](../00-proyecto/preguntas-abiertas.md#p-28), resuelta):** FM confirmó que esta clase fue el **23/9**. Con esa
> fecha la regla de [P-20](../00-proyecto/preguntas-abiertas.md#p-20) (*deck NN = clase NN-1 del cronograma*) cierra: deck 09 =
> clase 8 del cronograma. ⚠️ Pero el cronograma anuncia para el 23/9 **Taller de Oratoria**, no Agile/Scrum/Kanban: el tema de
> esta clase **no figura** en el cronograma de ese día.
>
> ⚠️ **La tarea del cierre se repite.** El "Para la próxima clase…" de este deck es **textual** el de
> la Clase 07 (BMC, "terminar de armar el MVP en su totalidad", Presentación de Avance). Parece un
> cierre reutilizado: **no se toma como tarea nueva ni como evidencia de fecha.**

---

## 1. De qué se trató

La clase abre con un **repaso** — el Business Model Canvas (con un ejemplo de Starbucks y una tabla de
costos) y Design Thinking en las etapas de *Prototipar y Testear* — y entra al tema central:
**cómo vamos a trabajar el resto del cuatrimestre**. Primero la agilidad como mentalidad, después
dos marcos concretos (**Scrum** y **Kanban**), después **cómo se estiman las tareas** (Story Points,
Planning Poker) y por último la sección **"NOSOTROS"**: las reglas de juego de la cátedra para los
sprints, las Sprint Reviews y las retrospectivas.

Importa porque a partir de acá el proyecto deja de ser research y pasa a ser **ejecución en
sprints**, y el docente evalúa Sprint Reviews y retros.

> ⚠️ **Calidad de la conversión.** Este deck es muy visual. Varias diapositivas llegaron como texto
> mezclado (ver `<!-- Start of picture text -->` en el crudo). **No se completó a ojo lo que no se
> entiende** — cada hueco está marcado ⬜ en la sección que corresponde.

---

## 2. Conceptos

### Repaso: Prototipar y Testear *(Design Thinking para ingenieros)*
El proceso **no es una línea recta** (Empatizar → Definir → Idear → Prototipar → Testear). Frases
del deck para las etapas 4 y 5:

- **"Falla antes de programar."** El prototipo son *mockups en Figma*, **no es software terminado**.
- Buscar **feedback "brutalmente honesto"**.
- **"Un prototipo te cuesta días. Un MVP programado te cuesta meses. Descubre si tu idea es mala en días."**

> 🎯 **Aplicado a FraudLens:** el prototipo de FGR es una interfaz **sin lógica** (ver
> [`prototipo.md`](../05-producto/prototipo.md)), que es justamente lo que esta frase describe. El
> cronograma pide un **Prototipo clickeable (Figma | Código)** el 21/10.

> ⬜ *El repaso del BMC (ejemplo Starbucks y tabla de costos) llegó ilegible: cifras mezcladas. No se
> transcribe. Ver el crudo si hace falta.*

### Agilidad
> *"La capacidad de crear y responder al cambio para tener éxito en un entorno incierto y turbulento."*

### Agilidad en informática
Una **mentalidad (mindset) y un conjunto de metodologías de desarrollo de software** basadas en la
**entrega iterativa, incremental y colaborativa**. Permite adaptarse rápido a los cambios del mercado
mediante **feedback continuo**, dividiendo proyectos grandes en **pequeños ciclos (sprints)** para
mejorar la eficiencia.

### Mindset ágil
Forma de pensar y abordar el trabajo centrada en **colaboración, adaptabilidad, aprendizaje continuo
y entrega constante de valor**. Se basa en **"ser ágil"** (valores y principios) **antes** que
**"hacer ágil"** (prácticas): abrazar el cambio y priorizar a las personas por sobre procesos rígidos.

### El corazón de la agilidad y el Manifiesto Ágil
> ⬜ **Hueco del material.** Las diapositivas "¿Qué es el corazón de la agilidad?" y "12 principios
> del Manifiesto" son casi todo imagen. Se rescata solo esto, **sin armar el resto**:
> - Se lee, desordenado: *propósito · espacio común · innovación · equipos multidisciplinarios ·
>   entender · vulnerabilidad · ofrecer confianza · pedir ayuda*.
> - Del manifiesto se lee con claridad **una** frase: *"Respuesta ante el cambio por encima de
>   seguir un plan"*, y dos principios: **equipo auto-organizado** y **reflexión sobre la mejora
>   continua**.
> - Los cuatro valores completos y los 12 principios **no están en el material**. Si el docente los
>   pide, se cita el Manifiesto original, **no se reconstruye de memoria**. *(Se intentó traerlo de
>   internet el 2026-10-07: el entorno bloquea `agilemanifesto.org`.)*

### Scrum
**Marco ágil** que optimiza la gestión de proyectos con un enfoque **iterativo e incremental**. Está
diseñado para fomentar colaboración, adaptabilidad y comunicación continua; organiza el trabajo en
ciclos cortos llamados **sprints**. El deck cita a Takeuchi y Nonaka (1986): *"…as in rugby, the ball
gets passed within the team as it moves as a unit up the field"*.

**Roles:**

| Rol | Definición del deck |
|---|---|
| **Product Owner (PO)** | Voz del cliente y los usuarios. **Define el product backlog.** Vela por el valor y las funcionalidades del producto/negocio. **Valida los entregables de cada Sprint.** |
| **Scrum Master** | Facilitador. Líder servil. Colabora con el equipo, ayuda a remover impedimentos, vela por el cumplimiento del proceso. |
| **Scrum Team** | Equipo de trabajo de **5 a 9 personas**. Interdisciplinario y autoorganizado. Define con el PO el alcance de cada Sprint. Construye el producto a nivel técnico. |
| **Stakeholders** | Personas interesadas en el proyecto, a las que les diseñamos la solución. |

**Reuniones:**

| Reunión | Definición del deck |
|---|---|
| **Daily Scrum** | Cada integrante cuenta qué hizo el día anterior y en qué va a trabajar hoy. Avisa si hay un impedimento o necesita ayuda. |
| **Sprint Planning** | Facilitada por el *team leader*: se cierra el Sprint anterior y se **planean y estiman** las tareas del próximo. |
| **Sprint Review** | Facilitada por el **Product Owner**: se presentan a los stakeholders las features y tasks que pasaron a **"done"** y se **valida** con ellos el avance. |
| **Sprint Retrospective** | Facilitada por **uno de los miembros del equipo**: se revisa el Sprint — aspectos a mejorar, reconocimientos, etc. |

> ⬜ *El diagrama "SCRUM Methodology" no se extrajo (es imagen).*

> 🎯 **Aplicado a FraudLens:** ver sección 3 — somos **4**, el deck habla de equipos de 5 a 9, y
> nuestros roles hoy (proceso / técnico / producto / documentación) **no son** PO / Scrum Master.
> No se asigna nada por deducción: queda en [P-29](../00-proyecto/preguntas-abiertas.md#p-29).

### Kanban
Método basado en la **visualización del flujo de trabajo y la búsqueda de su mejora continua**. **No
es una técnica específica del desarrollo de software**: su objetivo es gestionar cómo se van
completando tareas en general.

**Para qué sirve:**
- **Visualizar** el trabajo y las fases del flujo. El trabajo se divide en partes, se escribe en
  **tarjetas** y se pone en un **tablero** con **tantas columnas como estados** pueda tener una tarea.
- Fijar un límite de **trabajo en curso (WIP — Work in Progress)**: foco solo en las tareas actuales,
  para terminar más rápido los elementos individuales.
- **Medir** Lead Time y Cycle Time.

| Métrica | Definición del deck |
|---|---|
| **Lead Time** | Tiempo total desde que se **solicita** un elemento (o se crea en el backlog) hasta que se **entrega funcional** al usuario final. |
| **Cycle Time** | Tiempo (generalmente en días) desde que el equipo **empieza a trabajar activamente** en la tarea (pasa a *"En Progreso"*) hasta que se completa (*"Done"*). |

Ambas se miden sobre un **PBI** (*Product Backlog Item*, elemento del Product Backlog).

> 🎯 **Aplicado a FraudLens:** nuestro tablero de Trello ya es un Kanban (Backlog · Esta semana · En
> curso · En revisión · Bloqueado · Hecho), pero **no tiene límite de WIP definido**. El historial de
> movimientos de las tarjetas (el conector de Trello lista los eventos `MOVE_CARD`) permitiría medir
> Cycle Time; el Lead Time necesita la fecha de creación. Si el docente las pide como métricas, hay
> con qué calcularlas — pero **nadie las midió todavía**.

### Estimación: Story Points
Unidades de medida que se asignan a cada tarea; permiten ver el **esfuerzo** que el equipo necesita
para terminar la implementación de forma íntegra. Se usa una **escala discreta de valores** (limitarse
a valores discretos simplifica el proceso):

| Escala | Valores | Se usa para |
|---|---|---|
| **Fibonacci** | 1, 2, 3, 5, 8, 13, 21 … 40, 100 | Features / tareas |
| **T-Shirt Sizing** | S · M · L · XL | Épicas |

**Qué se tiene en cuenta** al asignar puntos: cuánto más grande o más chica es una Historia de Usuario
respecto de otra (**triangulación entre historias**, que genera conversaciones de entendimiento común),
la **cantidad de trabajo**, la **incertidumbre** y la **complejidad**. Los puntos son un *nivel de
indirección que protege al equipo de presiones externas* (ej.: que le pongan fechas u horas).

**Planning Poker** — pasos:
1. Se describe la HU y su feature, **definiendo cuándo está completa**.
2. Se debate brevemente: ¿qué implica?, ¿qué riesgos hay? Cada persona piensa y elige su carta.
3. **A la cuenta de 3**, todos muestran la carta. La distribución suele parecer una campana de Gauss:
   se **escucha a los de los extremos (outliers)**, que pueden tener información que el resto omite.
4. Si no hay consenso, se repite.

**Tips del deck:** que participe todo el equipo · que todos sepan qué es un "1" (la medida más
trivial) · **no centrarse en el puntaje sino en la conversación**, no pretender precisión · definir de
antemano el **DoD (Definition of Done)** · que la HU signifique lo mismo para todos · si no hay
consenso, triangular contra historias ya trabajadas · **acotar el tiempo** (5 minutos por User Story
suele alcanzar).

**Herramientas virtuales** que menciona: apps de mazos virtuales (App Store / Play Store),
scrumpoker.online, planningpoker.com, planningpokeronline.com.

### NOSOTROS — cómo vamos a trabajar *(reglas de la cátedra)*
Esta es la sección más importante para el proyecto: **son pautas del docente, no teoría**.

| Elemento | Qué dice el deck |
|---|---|
| **Sprints** | Duración: **2 semanas**. Cada sprint tiene un **objetivo definido** (ej.: *"Armar mockup"*, *"Armar módulo de IA"*). |
| **Planning Meeting** | **Al inicio de cada sprint.** Se planifican las tareas que entran y **se estiman**. |
| **Trello** | Herramienta para **plasmar lo que van desarrollando a lo largo del Sprint**. |
| **Sprint Review** | **Al final de cada sprint.** **5 minutos.** **Dos personas por equipo** hablan del objetivo del sprint y su desarrollo. Incluir: **¿qué hicieron y cómo? ¿qué problemas tuvieron/tienen y cómo podemos ayudarlos? ¿qué van a hacer en el próximo Sprint?** |
| **Retrospectiva** | **Al final de cada sprint.** El **facilitador no debe ser siempre el mismo** — uno distinto cada vez. **Debe documentarse en el Trello.** |
| **Design & Coding** | Herramientas recomendadas: **Git, Miro, Trello, Figma / Adobe XD / Marvel.** |

---

## 3. Aplicación a FraudLens

*Sección obligatoria.* Fuente de cada fila: **(D)** dice el docente · **(R)** hecho del repo ·
**(S)** sugerencia de Claude Code, sin aprobar por el equipo.

| Qué | Por qué | Dónde se refleja |
|---|---|---|
| **Sprints de 2 semanas con objetivo** (D) — ⬜ **no sabemos cuándo arranca el Sprint 1 ni cuántos hay**. El cronograma lista Sprint Review el 14/10, 21/10 (dos veces "Sprint Review 1"), 28/10 y 4/11 | Si no sabemos qué sprint estamos corriendo, no podemos redactar su objetivo. No se deduce un calendario de sprints a partir de esas fechas | [P-31](../00-proyecto/preguntas-abiertas.md#p-31) · [P-19](../00-proyecto/preguntas-abiertas.md#p-19) · tarjeta *Preguntar al profe: huecos del cronograma* |
| **Sprint Review: 5 min, 2 personas, 3 preguntas** (D) | Es un formato cerrado que se puede ensayar. Hay que decidir **quiénes presentan** (la Clase 1 exige rotación) | [`historial-aportes.md`](../../registro/historial-aportes.md) — la tabla "Presentaciones en clase" está vacía (R) |
| **Retro con facilitador rotativo, documentada en Trello** (D) | No tenemos plantilla ni lugar para las retros | (S) una plantilla en `docs/04-metodologia/` y un registro de quién facilitó. **Sin hacer** — es una sugerencia |
| **Roles Scrum: PO · Scrum Master · Team de 5–9** (D) | Somos 4 y nuestros roles son *proceso / técnico / producto / documentación* (R). **No se asigna PO ni Scrum Master por deducción** | [P-29](../00-proyecto/preguntas-abiertas.md#p-29) |
| **Trello como herramienta del sprint** (D) | Ya lo usamos y ya tiene forma de Kanban (R). Falta: WIP, y decidir si los sprints se reflejan en el tablero | [`flujo-de-trabajo.md`](../04-metodologia/flujo-de-trabajo.md) no menciona sprints (R) |
| **Estimación con Story Points / Planning Poker** (D) | Hoy ninguna tarjeta tiene estimación (R). Ojo: el **P&L** (Clase 07) pide **Horas-Hombre**, que es **otra unidad**: no son intercambiables | [P-31](../00-proyecto/preguntas-abiertas.md#p-31) — ¿el docente exige estimar el backlog? |
| **Herramientas recomendadas: Git, Miro, Trello, Figma** (D) | Git ✅ y Trello ✅ ya están. **Figma** va a hacer falta para el prototipo clickeable del 21/10. **Miro** se menciona de nuevo en la Clase 10 para el User Story Mapping | [Clase 10](clase-10-user-story-mapping-y-backlog.md) |

---

## 4. Qué tenemos que hacer para la próxima

El cierre de este deck **repite** el de la Clase 07 (ver aviso arriba). Las tareas de esa clase siguen
siendo las mismas y **ya tienen tarjeta**:

| Tarea | Responsable | Fecha límite | Trello |
|---|---|---|---|
| Armar el P&L | ⬜ Sin asignar | ⬜ | [Armar el P&L](https://trello.com/c/mMTyvp1F) *(Backlog)* |
| "Terminar de armar el MVP en su totalidad" | Equipo | ⬜ | Cubierto por las tarjetas existentes — ver la lista de pendientes en la [bitácora](../../bitacora/2026-10-07-clases-9-y-10.md) |
| Presentación de Avance | ⬜ rota según la regla de Sprint Reviews | ⬜ | ⬜ sin tarjeta propia — ver [Preparar la Sprint Review 1](https://trello.com/c/65jEv8rn) |

---

## 5. Dudas que quedaron

- ~~¿Qué fecha tiene esta clase?~~ → ✅ 23/9, [P-28](../00-proyecto/preguntas-abiertas.md#p-28) resuelta
- ¿Quién ocupa PO / Scrum Master, o alcanza con los roles actuales? → [P-29](../00-proyecto/preguntas-abiertas.md#p-29)
- ¿Cuándo arranca el Sprint 1, cuántos sprints hay y se estima el backlog? → [P-31](../00-proyecto/preguntas-abiertas.md#p-31)
- El texto del Manifiesto Ágil (4 valores, 12 principios) no llegó en la conversión. **Se intentó traerlo de internet (2026-10-07) y no se pudo:** `agilemanifesto.org` y `es.wikipedia.org` están bloqueados por el proxy de salida del entorno. Si alguien lo pega acá, se carga **marcado como fuente externa, no del docente**.

---

## 6. Términos nuevos para el glosario

- [x] *Agilidad · Mindset ágil · Scrum · Product Owner · Scrum Master · Scrum Team · Daily Scrum ·
  Sprint Planning · Kanban · WIP · Lead Time · Cycle Time · PBI · Story Points · Fibonacci ·
  T-Shirt Sizing · Planning Poker · DoD* → agregados a [`glosario.md`](../00-proyecto/glosario.md)
- [x] *Sprint · Sprint Review · Retrospectiva* → completados (estaban 🔜 anunciados)
