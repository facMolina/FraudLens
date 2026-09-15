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
