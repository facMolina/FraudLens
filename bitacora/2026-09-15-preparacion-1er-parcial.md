# 2026-09-15 — Preparación del 1° Parcial (16/9)

| | |
|---|---|
| **Tipo** | Trabajo individual, con validación en el momento (con asistencia de Claude Code) |
| **Duración** | — |
| **Participantes** | Facundo Molina (FM) |

## Por qué esta sesión

El docente confirmó el formato del 1° Parcial: presentación **oral** por grupo de los avances del
MVP, con una lista de ítems esperados. Faltaba un día. Se auditó el repo contra esa lista punto por
punto, y se cerraron los huecos que se podían cerrar en el tiempo disponible.

## Auditoría contra la consigna del docente

| Ítem | Estado antes de hoy | Qué se hizo |
|---|---|---|
| Documento de equipo (legajo + tareas) | 🔴 Roles todos ⬜ en `equipo.md` | ✅ Roles asignados y justificados |
| **Declaración de uso de IA** | 🔴 No existía | ✅ Documento nuevo, basado en los Lineamientos de la UADE |
| Modelo de negocio | 🔴 No existía | 🟡 BMC armado como hipótesis explícita, sin validar |
| Líneas futuras / próximas versiones | 🟡 Existía como lista "No es MVP" sin reformular | ✅ Reformulada como roadmap en `problema.md` |
| Encuestas / entrevistas | 🔴 Diseñadas, 0 ejecutadas | Sin cambios — no se inventa lo que no se hizo |
| Código del MVP | 🔴 No existe, sólo el prototipo de FGR sin ubicación | Sin cambios — sigue como pendiente real (P-05) |

## Declaración de uso de IA

El docente pidió leer y aplicar los **Lineamientos de Uso de Inteligencia Artificial de la UADE**
(6 PDFs que subió FM, ya que el link directo estaba bloqueado por la política de red de este
entorno). La sección aplicable es la de **Trabajos Integradores Finales**, que exige declarar:
herramientas usadas, alcance por etapa, proceso de validación y responsabilidad sobre el contenido.

Se armó [`docs/00-proyecto/declaracion-uso-ia.md`](../docs/00-proyecto/declaracion-uso-ia.md) con:

- **Herramientas:** Claude (los 4 integrantes, uso instrumental) · Claude Code (FM, construcción del
  repo) · Claude y Codex (FGR, backend y frontend del prototipo).
- **Validación:** se citan mecanismos ya existentes en el proyecto (regla de no deducir, sombrero
  rojo escrito siempre por el equipo, decisiones numeradas y no editables, commits firmados con
  `Co-Authored-By`).
- **Pendiente marcado explícito:** falta documentar qué partes del prototipo puede defender cada
  integrante (deuda ya señalada en `prototipo.md` desde el 2/9), y confirmar si ML usó IA para el
  documento de requerimientos.

## Roles del equipo

`equipo.md` tenía la tabla de roles vacía desde el 2/9. Se propuso una asignación basada en lo que
cada uno ya venía haciendo (evidencia, no preferencia adivinada) y el equipo la confirmó:

- **ML** — Referente de producto (propuso el tema, escribió los requerimientos).
- **FGR** — Referente técnico (armó el prototipo).
- **FM** — Referente de documentación (ya lo viene haciendo).
- **MDV** — Referente de proceso (rol elegido para sumarlo de lleno al tablero y las ceremonias,
  donde tenía menos evidencia de participación registrada).

Se resolvió [P-08](../docs/00-proyecto/preguntas-abiertas.md#p-08). Queda pendiente la rotación de
Sprint Reviews (arranca el 14/10) — **para el parcial de mañana presenta FM**, aclarado como algo
distinto de esa rotación.

## Modelo de negocio (BMC)

[`docs/05-producto/modelo-negocio.md`](../docs/05-producto/modelo-negocio.md) — Business Model
Canvas completo, marcado en cada bloque si viene de algo **ya confirmado** en el proyecto
(segmentos de clientes, propuesta de valor) o si es **hipótesis sin validar** (canales, ingresos,
socios). El modelo de ingresos propuesto es explícitamente **suscripción/licencia, no garantía
financiera** — para no confundirse con el modelo de ClearSale/Signifyd/Riskified que el
benchmarking ya había descartado.

## Registro en Trello

- Tarjeta del **1° Parcial** actualizada con el formato real confirmado por el docente y el estado
  honesto contra cada ítem de la consigna — no se movió (el parcial es mañana).
- Tarjeta nueva **"Declaración de uso de IA"**, creada directo en ✅ Hecho a pedido de FM, con la
  resolución anotada. FM se encarga de cerrar los dos puntos que quedaron abiertos en el propio
  documento (confirmar con ML, documentar qué defiende cada uno del prototipo).

## Reorganización del tablero contra la consigna del docente

A pedido de FM, se reordenó el tablero completo para que refleje exactamente los ítems que pidió
el docente para la oral, priorizados:

- **"Definir roles del equipo y rotación de Sprint Reviews"** → roles marcados hechos, rotación
  queda como pendiente separado (no bloquea mañana). Movida a 👀 En revisión.
- **"Clase 6: Roadmap + Modelo de negocio + BMC"** → resolución con el BMC-hipótesis y el roadmap
  de hoy. Movida a 👀 En revisión.
- **"Documentar el prototipo de FGR"**, **"Documentar el dataset de casos de prueba"**,
  **"Arrancar el repositorio de código del MVP"** → subidas de 📥 Backlog a 🎯 Esta semana,
  priorizadas porque el docente pidió explícitamente código/plataformas si existen.
- **"🔴 12. Encuesta difundida..."** → renombrada a **"Encuestas y entrevistas"** para cubrir los
  dos ítems de la consigna que comparten el mismo bloqueo real (0 ejecutado). Sigue en 🚧 Bloqueado.
- **"Stakeholders y expertos consultados"** *(nueva)* → 🎯 Esta semana. Estado real: Perfil A con
  acceso confirmado (ML), Perfil B todavía sin contacto.
- **"Modelos de IA a utilizar"** *(nueva)* → 🚧 Bloqueado, depende de P-11 (dataset). Se dejó
  igual el argumento de la estrategia (modelo asistivo, no autónomo) para poder hablarlo mañana.
- **"🔴 1° PARCIAL"** → movida al tope de 🎯 Esta semana, como referencia central de la semana.

## Revisión de las tarjetas en "En revisión"

FM pidió repasar juntas las 8 tarjetas que estaban en 👀 En revisión. Se separaron en dos grupos:
las que tenían una tarea concreta sin terminar que sólo puede resolver el equipo (sombreros rojos,
revisión de otro integrante, un conflicto real sin resolver), y las que ya cumplían su propio
checklist y sólo les faltaba una validación futura normal (research, The Pitch). FM confirmó pasar
estas 5 a **✅ Hecho**, con cierre anotado en cada una:

- **Árbol de Problemas y 5 Por Qué** — sin blocker real.
- **9. Benchmarking con curva de valor** — el entregable está completo; "es continuo" es su
  naturaleza, no una tarea pendiente.
- **11. Narrativa de la propuesta de solución** — cumple su checklist; converger en una sola queda
  para The Pitch.
- **Definir roles del equipo** — roles confirmados; la rotación de Sprint Reviews (14/10) no
  bloquea nada hoy.
- **Clase 6 — BMC/Roadmap** — el BMC-hipótesis es justo lo que pedía la tarjeta; validarlo es
  trabajo futuro atado al research del Perfil B.

Quedan en 👀 En revisión, con tarea concreta pendiente del equipo (no mía): **1. Decidir los 3
perfiles** (dos sombreros rojos sin escribir), **2. Plan de research** (falta revisión de otro
integrante + ejecución) y **10. Ideación y Grilla de Priorización** (conflicto CU-07 sin resolver).

## División final de tareas para el parcial

Con el equipo repasando por WhatsApp, FM ajustó la asignación dos veces: primero corrigió que el
código del MVP no aplica a esta entrega (siguen definiendo objetivos clase a clase), y después
movió la revisión del Plan de research de ML a MDV, para balancear el aporte individual de este
último. Quedó registrado en cada tarjeta de Trello:

| Quién | Tareas |
|---|---|
| **Lewinzon, Mateo (ML)** | Conseguir la encuesta/entrevista (prioridad máxima) · confirmar si usó IA para los requerimientos · buscar contacto para el Perfil B |
| **Guerrero Rojas, Francisco Daniel (FGR)** | Elegir y documentar el dataset · resolver junto con ML la tensión CU-07 vs. ideación |
| **Diaz Valdez, Mateo (MDV)** | Coordinar la escritura de los dos sombreros rojos · revisar el Plan de research |
| **Molina, Facundo Roman (FM)** | Documentación y coordinación general |

Código del MVP: confirmado que **no aplica a esta entrega**.

## Cuarta parte — Carga de la Clase 07 (Business Model Canvas) y protocolo de IA

FM preguntó hasta qué clase estaba cargado el repo (Clase 06) y pasó el material de la Clase 07
(Business Model Canvas), con una discrepancia de numeración nueva: el archivo trae el prefijo
`007` pero el título interno dice "Clase_08" — se cargó como Clase 07 por prefijo y orden, sin
resolver cuál es la numeración real del docente (sumado a [P-20](../docs/00-proyecto/preguntas-abiertas.md#p-20)).

### Hallazgo clave: el BMC ya armado el 14/9 coincide con la clase real

Los 9 bloques del [`modelo-negocio.md`](../docs/05-producto/modelo-negocio.md) armado ayer
coinciden exactamente con la estructura que enseñó esta clase — se escribió antes de tener el
material, y aun así calzó. Lo que sí falta y es nuevo: el **Profit & Loss** (costos en Horas-Hombre,
egresos/ingresos, viabilidad) — no estaba cubierto hasta ahora. Se creó una tarjeta nueva en
Trello para armarlo.

### Protocolo de Declaración de uso de IA

FM preguntó si había quedado anotado un protocolo para que la Declaración de uso de IA se
actualice cada vez que el proyecto avance con algo — **no lo había, sólo estaba la nota dentro del
propio documento.** Se agregó como **regla 10** en `CLAUDE.md` y como ítem del checklist de cierre
de sesión: cada vez que se use IA para algo nuevo (herramienta, etapa, integrante), se actualiza
`declaracion-uso-ia.md` en el momento, no al final.

## Qué queda pendiente para mañana

| Tarea | Urgencia |
|---|---|
| Repasar todo lo visto de la Clase 1 a la 6 | 🔴 |
| Hablar en equipo todo lo cerrado hoy antes de presentar (roles, IA, modelo de negocio) | 🔴 |
| Confirmar con ML si usó IA para el documento de requerimientos (falta en la declaración) | 🟡 |
| Documentar qué parte del prototipo puede defender cada integrante | 🟡 |
| Decidir si armar una guía corta de 1 página por bloque para la oral | 🟢 — ofrecido, sin definir |

## Archivos

- `docs/00-proyecto/declaracion-uso-ia.md` *(nuevo)*
- `docs/05-producto/modelo-negocio.md` *(nuevo)*
- `docs/00-proyecto/equipo.md` — roles asignados
- `docs/00-proyecto/preguntas-abiertas.md` — P-08 resuelta
- `docs/05-producto/problema.md` — sección de líneas futuras
- `docs/02-entregables/README.md` — tabla de contenido actualizada
- `registro/historial-aportes.md`
