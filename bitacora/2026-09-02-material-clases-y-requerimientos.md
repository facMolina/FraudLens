# 2026-09-02 — Material de clases 2-4, requerimientos de FGR y estructura de carpetas

| | |
|---|---|
| **Tipo** | Trabajo individual (con asistencia de Claude Code) |
| **Duración** | — |
| **Participantes** | Facundo Molina (FM) |

## Qué se hizo

- Se creó **[`docs/01-clases/material/`](../docs/01-clases/material/)** para guardar el material
  crudo de cada clase, y se cargaron las **Clases 1, 2, 3 y 4** en Markdown.
- Se estableció la **regla de formato**: el material de clase se sube en Markdown, **nunca en PDF**.
  Conversión en https://cloudconvert.com/pdf-to-md. La regla quedó en `CLAUDE.md`,
  `docs/01-clases/README.md` y `docs/01-clases/material/README.md`, y `*.pdf`/`*.pptx`/`*.xlsx`
  quedaron en `.gitignore`.
- Se incorporó el documento de **Francisco (FGR)** como
  [`docs/05-producto/requerimientos-funcionales-mvp.md`](../docs/05-producto/requerimientos-funcionales-mvp.md),
  **marcado como borrador sin aprobar**, con una sección final de puntos a discutir.
- Se agregaron dos reglas a `CLAUDE.md`: **no deducir** (si falta un dato, se pregunta) y
  **borrador ≠ definición**.

## Qué se definió

Respuestas de FM que cierran preguntas abiertas:

| Pregunta | Respuesta |
|---|---|
| [P-01](../docs/00-proyecto/preguntas-abiertas.md#p-01) — Título del proyecto | **FraudLens** es el nombre "marketinero"; convive con el título académico de la planilla |
| [P-02](../docs/00-proyecto/preguntas-abiertas.md#p-02) — ¿Problema aprobado? | **Sí, el docente lo aprobó** |
| [P-03](../docs/00-proyecto/preguntas-abiertas.md#p-03) — ¿Equipo de 4? | **Sí**, porque este cuatrimestre hay menos gente cursando |
| [P-04](../docs/00-proyecto/preguntas-abiertas.md#p-04) — Cronograma | El del deck de Clase 1 **se ignora** (es del 1C). FM va a pasar el real |
| [P-06](../docs/00-proyecto/preguntas-abiertas.md#p-06) — Datos | El equipo **tiene dataset de casos de prueba** para el MVP. Falta documentarlo |

## Segunda parte de la sesión

- Se escribieron las **notas trabajadas de las Clases 2, 3 y 4**, con la bajada a FraudLens.
  En las Clases 2 y 3 se marcaron explícitamente los huecos que la conversión no permitió
  reconstruir, en vez de completarlos a ojo.
- Se sumaron al **glosario** dos secciones nuevas: *Segmentación y problema* (Clases 2 y 3) y
  *Design Thinking y User Research* (Clase 4) — 15 términos.
- Se redactaron los **17 tickets pendientes para la Clase 5** en
  [`docs/02-entregables/pendientes-clase-05.md`](../docs/02-entregables/pendientes-clase-05.md),
  listos para cargar en Trello.

### Historia del proyecto que quedó registrada *(FM)*

| Clase | Qué pasó |
|---|---|
| **Clase 2** | El equipo expuso las ideas de problema que tenía. Se evaluaban varios proyectos |
| **Clase 3** | Se decidió por este sistema. El docente lo aprobó |
| **Clase 4** | Se escribieron los requerimientos funcionales del MVP y se definió el nombre **FraudLens** |
| **Clase 5** | **Es la próxima** — todavía no se dio |

### 🔴 Hallazgo importante

En la Clase 4 el docente pidió **User Research** (400 respuestas + User Persona + Mapa de Empatía +
Escenario Actual de 3 usuarios). El equipo, en cambio, trabajó en los **requerimientos funcionales
del MVP**.

Es decir: **se definió la solución antes de hacer el research que define el problema**, que es
justamente lo que la Clase 4 advierte que hace fallar al 90% de las startups.

Esto **no invalida** el trabajo de Francisco, que es sólido y sirve como base. Pero significa que
el User Research está **entero pendiente** y que, si contradice lo asumido, hay que corregir el
documento — no al revés. Quedó registrado en la
[nota de la Clase 4](../docs/01-clases/clase-04-design-thinking.md#3-aplicación-a-fraudlens).

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| Pasar el cronograma real del 2C 2026 | FM | ⬜ |
| Documentar el dataset de casos de prueba ([P-11](../docs/00-proyecto/preguntas-abiertas.md#p-11)) | Equipo | ⬜ |
| Revisar en equipo el documento de requerimientos de FGR ([P-15](../docs/00-proyecto/preguntas-abiertas.md#p-15)) | Equipo | ⬜ |
| **Conectar Trello** a la cuenta de claude.ai (FM es admin del tablero) | FM | 🔴 Bloqueante |
| Cargar los 17 tickets al tablero una vez conectado | FM + asistente | ⬜ |
| Consultar al docente P-17 y P-18 (ambigüedades de la consigna de la Clase 4) | Equipo | Clase 5 |
| Cargar los aportes previos de ML y del resto del equipo | Equipo | ⬜ |

## Dudas que surgieron

Se cargaron 8 preguntas nuevas: **P-11 a P-18** en
[`preguntas-abiertas.md`](../docs/00-proyecto/preguntas-abiertas.md).

Las más urgentes son **P-17** (¿400 respuestas de encuesta o en total?) y **P-18** (¿3 perfiles o
3 personas?), porque cambian el tamaño del trabajo para la Clase 5.

> ⚠️ **Nota sobre el material crudo:** los decks son muy visuales y la conversión a Markdown llega
> desordenada, sobre todo en las **Clases 2 y 3**. En las notas de esas clases los huecos quedaron
> marcados como tales, sin completar.

## Archivos tocados

- `docs/01-clases/material/` *(nuevo)* — 4 clases + README con la regla de formato
- `docs/05-producto/requerimientos-funcionales-mvp.md` *(nuevo)*
- `docs/00-proyecto/preguntas-abiertas.md` — P-01/02/03 resueltas, P-06 parcial, P-11 a P-15 nuevas
- `docs/00-proyecto/ficha-proyecto.md`, `equipo.md` — propagación de las respuestas
- `docs/01-clases/README.md`, `docs/05-producto/README.md` — índices
- `CLAUDE.md`, `.gitignore`, `.graphifyignore`
- `docs/01-clases/clase-02-*.md`, `clase-03-*.md`, `clase-04-*.md` *(nuevos)*
- `docs/02-entregables/pendientes-clase-05.md` *(nuevo)* — 17 tickets
- `docs/00-proyecto/glosario.md` — 15 términos nuevos de las Clases 2, 3 y 4
- `docs/05-producto/problema.md` — historia del proyecto y fórmula "¿Cómo podríamos…?"
- `registro/historial-aportes.md` — aporte de FGR registrado

---

## Tercera parte de la sesión — cronograma real y Trello

### 🔴 Hallazgo crítico: el cronograma del deck no servía

FM adjuntó el **cronograma oficial de la cátedra**. Cambia cosas importantes:

| El deck decía | La realidad |
|---|---|
| 2 "instancias de evaluación previa" | **2 PARCIALES**: 16/9 y 11/11 |
| 4 sprints con 4 Sprint Reviews | 2 Sprint Reviews, en fechas concretas |
| Marzo a julio | **Agosto a diciembre**, miércoles 18:45-22:15 |
| Sólo clases presenciales | Hay **clase remota sincrónica el sábado 5/9 de 9 a 13 hs** |

Y sobre todo: **la Clase 5 es el miércoles 2/9**, con entregables concretos —
*Plan de research · Insight + Definición · User Persona · Mapa de Empatía · Problem Statement validado*.

Cargado en [`docs/00-proyecto/cronograma.md`](../docs/00-proyecto/cronograma.md) y propagado a
entregables, materia y README.

### Corrección de autoría

En la primera carga se atribuyó el documento de requerimientos funcionales a **FGR**. **Lo escribió
Mateo Lewinzon (ML)**, que además es quien propuso el tema y es el referente del rubro del equipo.

**FGR** aportó: la creación del tablero de Trello y el **prototipo** (backend con Claude, frontend
con Codex, sobre la base de un notebook de Kaggle y del documento de ML).

Corregido en el historial de aportes y en el documento de requerimientos.

### Prototipo documentado

Nuevo: [`docs/05-producto/prototipo.md`](../docs/05-producto/prototipo.md), con lo que hay, lo que
falta, y una sección sobre **honestidad académica** — el cronograma advierte explícitamente que se
sanciona, y hay que dejar citado el notebook de Kaggle y el uso de IA.

### Tablero de Trello limpiado y rearmado

Estaba la plantilla Kanban sin tocar. Se hizo:

- **14 tarjetas de plantilla archivadas** (*"Feature ABC"*, *"Task 123"*, las `💬 Move a card…`)
- **6 listas renombradas** al español: 📥 Backlog · 🎯 Esta semana · 🔨 En curso · 👀 En revisión · 🚧 Bloqueado · ✅ Hecho
- **6 tarjetas cargadas en "🎯 Esta semana"** con vencimiento el 2/9 18:45, una por entregable de la Clase 5
- **9 tarjetas en Backlog**: clase remota del sábado, sumar integrantes al tablero, dataset, revisión de requerimientos, prototipo, roles, Árbol de Problemas + 5 Por Qué, Clase 6, 1° Parcial
- Las 2 tarjetas reales que ya existían: la de requerimientos pasó a ✅ Hecho, la del repo a 🔨 En curso

⚠️ **El tablero tiene un solo miembro (Francisco).** Quedó una tarjeta para sumar a los otros tres:
sin eso no se puede demostrar participación individual, que es ítem de evaluación.

### README reescrito para onboarding

Ahora arranca con una sección **"¿Sos del equipo y es tu primera vez acá?"**: qué es el repo, los
5 pasos para arrancar una sesión con Claude Code o Codex desde un ticket de Trello, el prompt de
arranque listo para copiar, el checklist de cierre, y el aviso de **no correr `/init`** (pisaría el
`CLAUDE.md` escrito a mano).

### Preguntas

- ✅ Resueltas: **P-04** (cronograma), **P-17** (las 400 respuestas son una guía)
- 🟡 Parcial: **P-05** (hay prototipo, pero no se sabe dónde vive el código)
- 🔲 Nuevas: **P-19** (huecos del cronograma), **P-20** (numeración decks vs. cronograma)

---

## Cuarta parte — datasets, identidad visual y agenda de preguntas

### Correcciones de FM

| Antes se entendía | La realidad |
|---|---|
| El prototipo de FGR era "el código del MVP" y faltaba saber dónde vivía | **El código del MVP no está empezado.** El prototipo de FGR es una prueba aparte. Arrancar el repo del MVP queda **asignado a ML** |
| Había "un dataset de casos de prueba" | Hay **3 candidatos pre-seleccionados**, todavía sin elegir |

### Datasets candidatos

Cargados en [`docs/05-producto/datos.md`](../docs/05-producto/datos.md) con criterios de elección.

⚠️ **Detalle que hay que mirar:** los tres links son **notebooks** de Kaggle (`/code/`), no
**datasets** (`/datasets/`). Lo que necesitamos es el dataset que cada notebook usa por debajo.
Quedó anotado en la tarjeta y en el documento.

### Nueva regla del equipo: cuándo se le pregunta al docente

> Las preguntas no se acumulan ni se adelantan. Se preguntan en la clase donde se trata el tema, o
> en la anterior. Preguntar en septiembre algo de noviembre no sirve.

Documentada en [`flujo-de-trabajo.md`](../docs/04-metodologia/flujo-de-trabajo.md) y en el
encabezado de [`preguntas-abiertas.md`](../docs/00-proyecto/preguntas-abiertas.md). Cada pregunta al
docente lleva ahora un campo **📅 Cuándo preguntar** y su tarjeta de Trello con esa fecha.

Agenda resultante:

| Pregunta | Cuándo |
|---|---|
| P-18 (3 perfiles o 3 personas), P-20 (numeración), P-21 (qué es "validado") | **2/9** |
| P-19 — retros y Sprint Reviews | **7/10** |
| P-19 — cómo es The Pitch | **25/11** |

### Identidad visual

FM toma a cargo colorimetría, logo, tipografía e imagen de FraudLens. Tarjeta creada en
**🔨 En curso**.

Se sumaron dos consideraciones que salen del propio producto: la **paleta de riesgo**
(bajo/medio/alto/crítico) no puede depender sólo del color —hay que poder distinguir "alto" de
"crítico" sin ver color— y la tipografía necesita **números tabulares**, porque el dashboard muestra
montos, IDs y puntajes en columna.

### Nota sobre asignaciones en Trello

El conector de Trello **no permite asignar miembros a tarjetas** desde el asistente. Los
responsables quedan escritos en la descripción de cada tarjeta; hay que asignarlos a mano cuando los
integrantes entren al tablero.

---

## Quinta parte — Método de los 6 Sombreros

El docente pidió aplicar el **método de los 6 Sombreros para Pensar** (Edward de Bono) a los temas
del proyecto, y entregó un prompt específico para hacerlo con asistencia de IA.

### Qué se hizo

- [`docs/04-metodologia/seis-sombreros.md`](../docs/04-metodologia/seis-sombreros.md) — el método,
  las reglas de aplicación y **el prompt del docente guardado textual**.
- [Decisión 0003](../docs/03-decisiones/0003-metodo-seis-sombreros.md) — adopción del método.
- [`docs/05-producto/analisis/`](../docs/05-producto/analisis/) — carpeta nueva, con plantilla e índice.
- Término sumado al glosario. Regla 9 sumada a `CLAUDE.md`.
- Tarjeta de referencia en Trello con el método.

### Criterio de alcance

FM dijo *"para todos los tickets"*. Se aplicó con un criterio explícito, porque un análisis de 6
sombreros sobre *"invitar gente al tablero"* es ruido y el ruido tapa lo que sí importa:

| Tipo de tarjeta | ¿Análisis? |
|---|---|
| Decisión entre opciones | ✅ Sí |
| Entregable de la materia | ✅ Sí |
| Tarea operativa | ❌ No |

Criterio: **"¿esto se puede hacer mal de más de una manera?"**

### Primer análisis: ¿quién es el usuario de FraudLens?

[`6-sombreros-usuario-objetivo.md`](../docs/05-producto/analisis/6-sombreros-usuario-objetivo.md)

Es la decisión que bloquea los entregables del 2/9. Lo que salió:

- **El sombrero negro** encontró el problema central: el analista de fraude es el usuario más obvio
  y **el menos accesible del mundo** — trabaja en bancos y no habla de sus controles antifraude.
  Apostar todo a él es apostar a un punto único de falla.
- **El sombrero rojo** nombró el sesgo activo: **elegir el usuario que le queda cómodo al prototipo
  que ya existe**, en vez del que conviene al proyecto.
- **El verde** aportó la idea que resuelve: **los tres niveles del dolor** — quien lo *sufre*
  (consumidor), quien lo *decide* (analista), quien lo *paga* (comercio). Tres perfiles
  estructuralmente distintos, con mapas de empatía que no se van a parecer.
- **El azul** propuso esos tres perfiles con la **accesibilidad como filtro duro**, descartó
  "administrador" (es un rol de configuración, no una persona con dolor propio) y dejó un plan B.

**La contradicción que quedó abierta:** el negro dice que el analista es inaccesible, el amarillo
dice que ML tiene contactos en el rubro. No es diferencia de opinión: **es una pregunta con
respuesta, y la tiene ML**. Es la bisagra de la decisión y hay que preguntárselo antes de la clase.

### Pendientes del análisis

- ⬜ **El equipo tiene que reescribir el sombrero rojo.** El que está es un borrador visto desde
  afuera; las emociones son del equipo, no de un modelo.
- ⬜ **ML tiene que confirmar o descartar el acceso a expertos.**

---

## Sexta parte — Trello obligatorio al arrancar y ticket de debate

### Trello pasa a ser requisito de sesión

El README y `CLAUDE.md` ahora exigen **tener el conector de Trello activo antes de empezar a
trabajar**. Los pasos de conexión quedaron en el propio README, y el asistente tiene instrucción de
**frenar y pedirlo** si no está.

El flujo de arranque pasó de 5 a 6 pasos: ahora entre "abrir el asistente" y "trabajar" hay un paso
explícito de **leer el tablero y asignarse un ticket**, con las reglas del tablero (una persona por
tarjeta, máximo 1-2 en curso, mover a Bloqueado con el motivo escrito).

> ⚠️ **Limitación registrada:** el conector **no puede asignar miembros a tarjetas**. El responsable
> queda escrito en la descripción y la persona tiene que darle "Unirme" a mano.

### Tarjeta 8 — Temas a debatir en equipo

Nueva tarjeta con **12 puntos**, separando lo que decide el equipo de lo que se le pregunta al
docente (que ya estaba en la tarjeta 7): 3 decisiones que bloquean los entregables de hoy, 4 de
esta semana, 3 de deuda a blanquear y 2 operativas.

### Limpieza de preguntas abiertas

- **P-09** (estructura del tablero) → ✅ resuelta: el tablero está rearmado
- **P-14** (cuándo es la Clase 5) → ✅ resuelta: miércoles 2/9, 18:45
- **P-15** → corregida la autoría: los requerimientos los escribió **ML**, no FGR

---

## Séptima parte — identidad visual: presentación para el equipo

Se trabajó el ticket [Identidad visual](https://trello.com/c/ncNYKzbF) (FM) hasta dejarlo listo
para que el equipo decida. Quedó en **👀 En revisión**, no en Hecho: la elección es del equipo.

**Entregable:** [presentación en Canva](https://www.canva.com/design/DAHUDsuQPB8), 14 páginas, en
español. Documentada en
[`docs/05-producto/identidad/propuesta-canva.md`](../docs/05-producto/identidad/propuesta-canva.md).

### Lo que se decidió con datos, no con gusto

- **Color de marca violeta** — `#9333EA` claro (5.16:1) / `#A855F7` oscuro (4.90:1). El criterio no
  fue estético: el color de marca **no puede vivir dentro de la escala de riesgo**. Verde, ámbar,
  naranja y rojo ya están tomados por LOW→CRITICAL.
- **Escala de riesgo medida** con la fórmula WCAG de luminancia relativa, nivel por nivel, en los
  dos modos. Ver [`paleta.md`](../docs/05-producto/identidad/paleta.md).
- **Cyan descartado**: 2.33:1 sobre fondo claro. **Ámbar en claro descartado**: 1.60:1.
- **Tres finalistas** de 27 símbolos generados: Embudo · Anomalía en grilla · Prisma. Se
  descartaron los círculos concéntricos (se leen como **diana**) y el círculo con barra (se lee
  como **prohibido**).

### 🔴 Hallazgo: el rojo CRITICAL no pasa AA

`#DC2626` sobre fondo oscuro mide **4.02:1**, por debajo del mínimo de 4.5. Es el único valor de la
paleta que falla y hay que corregirlo antes de que entre al código.

### Decisión de método: vectores en vez de imágenes generadas

Las 8 láminas generadas con IA que se subieron a Canva son **anteriores a la decisión del violeta**:
están en azul, sobre fondo claro, y chocaban con el deck oscuro. En vez de usarlas, los tres
símbolos y todos los swatches se **dibujaron como vectores nativos** en Canva, en el violeta
aprobado.

Ventaja lateral: son editables, escalan sin pérdida, y los paths quedaron documentados en el repo.

### Lo que se le agregó al board

El deck original mostraba grillas de exploración pero **nunca un logo armado**. Se sumaron dos
páginas:

- **Pág. 13 — El logo completo:** cada símbolo al lado de la palabra *FraudLens*, que es como se
  va a usar de verdad.
- **Pág. 14 — Las tres propuestas:** las versiones finales, al cierre.

Y se llenaron tres páginas que estaban casi vacías (contexto de producto, color de marca,
tipografía) con los datos medidos.

### Incidencia de herramientas

El conector de Canva **se desconectó tres veces** durante la sesión, y cada corte destruye la
transacción de edición abierta. Se perdió trabajo dos veces. Se pasó a **commitear página por
página**, que es más lento pero no pierde nada. Queda anotado por si a alguien del equipo le pasa
lo mismo.

### Qué falta

| Tarea | Quién | Cuándo |
|---|---|---|
| **Elegir uno de los tres símbolos** | Equipo | Próxima reunión |
| Corregir el rojo CRITICAL en modo oscuro | FM | Antes de que entre al código |
| Elegir entre Inter e IBM Plex Sans | Equipo | Próxima reunión |
| Regenerar las láminas en violeta (prompts 5-7) si se quieren usar | FM | Opcional |
