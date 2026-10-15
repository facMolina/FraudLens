# 2026-10-15 — Correcciones tras la revisión de MDV (User Story Mapping, User Flow, herramienta del backlog)

| | |
|---|---|
| **Tipo** | Correcciones de documentos, con asistencia de Claude Code |
| **Duración** | ⬜ |
| **Participantes** | Facundo Molina (FM) |

## Qué se hizo

MDV revisó el 14/10 las tres tarjetas de FM y las devolvió a 🔨 En curso (ver [`2026-10-14-revision-tickets-en-revision.md`](2026-10-14-revision-tickets-en-revision.md)). FM pidió revisar el feedback. Se leyeron los 3 comentarios de Trello y la bitácora de MDV, y se corrigió **lo que se podía resolver sin decidir por el equipo**.

## Qué se definió

| Pregunta | Respuesta de FM (2026-10-15) | Alternativas que no eligió |
|---|---|---|
| El mapa deja HU-13 sin carril y el Flujo 5 la usa | **Meter HU-13 en el mapa**, paso 5, como tarea de R1 (el mapa pasa de 8 a 9 tareas) | Sacarla del Flujo 5 · dejarlo como pregunta para el equipo |
| El Flujo 4 no tiene camino alternativo | **Sin factores, solo el aviso "historial insuficiente"** (propuesta de FM, pendiente de ML) | Mostrar los factores con el aviso al lado · dejarlo como pregunta para ML |

## Qué se cambió

| Cambio | Archivo |
|---|---|
| HU-13 agregada al paso 5 del mapa; R1 = 9 tareas; HU-13 sale de "sin carril" (quedan HU-07 a HU-10 y HU-14) | [`user-story-map.md`](../docs/05-producto/user-story-map.md) · P-32 en [`preguntas-abiertas.md`](../docs/00-proyecto/preguntas-abiertas.md) |
| **Borrador nuevo** del 6 Sombreros del mapa: blanco con hechos del repo, negro/amarillo/verde marcados como borrador de Claude Code, **rojo vacío para las 4 voces** | [`6-sombreros-mvp-user-story-map.md`](../docs/05-producto/analisis/6-sombreros-mvp-user-story-map.md) |
| Camino alternativo en el Flujo 4; dibujo del Flujo 4 regenerado en FigJam (se borró el viejo y se generó el nuevo) | [`user-flows.md`](../docs/05-producto/user-flows.md) · [tablero](https://www.figma.com/board/tKo7wt7bStXRCGCLNzqlRA) |
| **Verificado:** el conector de Trello **no puede crear la etiqueta HU**; el tablero tiene 3 etiquetas sin nombre y sin uso. Se anotó en el análisis | [`6-sombreros-herramienta-backlog.md`](../docs/05-producto/analisis/6-sombreros-herramienta-backlog.md) |

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| **Mover el FigJam a un proyecto compartido o compartirlo** con MDV, FGR y ML: hoy nadie más lo abre | FM | ⬜ |
| Mirar las formas del docente en el deck original de la Clase 10 y ajustar el dibujo | FM | ⬜ |
| Verificar que el dibujo no tenga líneas cruzadas (hace falta acceso) | Quien abra el tablero | ⬜ |
| Confirmar el camino "historial insuficiente" del Flujo 4 (qué se muestra) | ML | ⬜ |
| **Sombrero rojo de las 4 voces** en los 6 Sombreros del mapa y en el de la herramienta | MDV · FGR · ML · FM | ⬜ |
| MoSCoW de las 9 tareas (da el orden vertical del mapa) | Equipo | ⬜ |
| Responder P-32 (HU-07 a HU-10 y HU-14 sin carril) | Equipo | ⬜ |
| Decisión 0007 y cerrar P-30 (herramienta del backlog) | Equipo | ⬜ |
| Crear la etiqueta HU a mano en Trello, si el equipo confirma Trello | Equipo | ⬜ |
| Una captura o link al tablero visual del mapa (lo pide la tarjeta) | FM | ⬜ |
| Que el equipo valide el mapa | Equipo | ⬜ |

## Dudas que surgieron

- El camino "historial insuficiente" del Flujo 4 es propuesta de FM: los requerimientos no dicen qué factores se muestran en ese caso.
- **HU-12** (choque con la decisión 0005) y **HU-06 / HU-11** (solape) siguen sin resolver.

## Aviso sobre commits

Desde esta sesión los commits salen con el usuario de Git de FM (ver el aviso del 14/10 sobre `a053847`).

## Archivos tocados

- Nuevos: `docs/05-producto/analisis/6-sombreros-mvp-user-story-map.md` · `bitacora/2026-10-15-correcciones-de-la-revision-de-mdv.md`
- Modificados: `docs/05-producto/user-story-map.md` · `docs/05-producto/user-flows.md` · `docs/05-producto/analisis/6-sombreros-herramienta-backlog.md` · `docs/05-producto/analisis/README.md` · `docs/00-proyecto/preguntas-abiertas.md` · `registro/historial-aportes.md` · `docs/00-proyecto/declaracion-uso-ia.md`
