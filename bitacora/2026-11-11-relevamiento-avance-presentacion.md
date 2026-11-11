# 2026-11-11 — Relevamiento del avance para la presentación

| | |
|---|---|
| **Tipo** | Trabajo individual |
| **Duración** | ⬜ |
| **Participantes** | MDV, con asistencia de Claude Code |

## Qué se hizo

- Se leyó el tablero completo (56 tarjetas): 30 en ✅ Hecho, 3 en 👀 En revisión, 6 en 🔨 En curso, 3 en 🎯 Esta semana y 14 en 📥 Backlog.
- Se relevaron los PRs del [repo del MVP](https://github.com/mateolewinzon/fraudlens): #1, #4, #5 y #6 integrados en `main`; #7, #8 y #9 abiertos, con checks en verde y sin revisiones.
- Se actualizó [`mvp.md`](../docs/05-producto/mvp.md) con la sección "Avance al 2026-11-11". El estado anterior decía que no había flujos implementados y ya no era cierto.
- Se sumaron a la [declaración de uso de IA](../docs/00-proyecto/declaracion-uso-ia.md) los PRs de código de MDV (#4, #5, #7, #8 y #9) y este relevamiento.
- Se dejaron comentarios de avance en 3 tarjetas: [Arrancar el repositorio](https://trello.com/c/ec7Xd3xy), [Migrar frontend](https://trello.com/c/qW9sArxq) y [Modelos de IA a utilizar](https://trello.com/c/HgigLF8C).

- Se buscó trabajo a medio hacer. En el repo del MVP no hay nada a medias: la migración de la interfaz tiene sus 4 tareas cerradas y la copia local está limpia. Quedan ramas viejas sin uso.
- Se corrigió con un comentario la tarjeta de [Retrospectiva](https://trello.com/c/5VB8UDLb): su nota decía que las aclaraciones del 14/10 no estaban publicadas, y ya están en `main` (commit `797dde5`).

## Qué se definió

- Ninguna tarjeta pasó a ✅ Hecho: las 3 tienen ítems que dependen del equipo.

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| Revisar e integrar los PRs #7 ← #8 ← #9 | ⬜ (sugerido: ML, dueño del repo) | ⬜ |
| Decidir el modelo de IA: LLM (Groq), modelo entrenado (decisión 0006) o los dos | Equipo | ⬜ |
| Resolver la diferencia MongoDB (implementado) vs. PostgreSQL (decisión 0007, tarjeta "Reconvertir stack") y cerrar P-10 | Equipo | ⬜ |
| Confirmar acceso de escritura de FGR y FM al repo del MVP | ⬜ | ⬜ |

## Dudas que surgieron

- Las tarjetas de FM en 🔨 En curso (MoSCoW, herramienta del backlog, User Flow, Story Mapping) vencían el 7/10 y no tienen comentario de cierre. No se tocaron.

## Archivos tocados

- `docs/05-producto/mvp.md`
- `docs/00-proyecto/declaracion-uso-ia.md`
- `registro/historial-aportes.md`
- `bitacora/2026-11-11-relevamiento-avance-presentacion.md`
