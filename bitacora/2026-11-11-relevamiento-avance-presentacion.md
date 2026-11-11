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

- **Limpieza del tablero** (acordada con MDV). Cada movimiento lleva su comentario con el motivo.
  - Archivadas: Preparar la Sprint Review 1 (la fecha pasó y no hay registro), Armar el Sprint 1 (quedó superada), 6 Sombreros del recorte de alcance (ya decidido en la 0005), Wireframes (2 de 9 pantallas; la interfaz real las reemplaza), Citar Kaggle / declarar IA / probar el prototipo.
  - Pasadas a ✅ Hecho como borrador aceptado: User Persona ×3 y Mapa de Empatía ×3 (con huecos explícitos) y Plantilla de Retrospectiva.
  - Movida a 🎯 Esta semana: **Problem Statement validado**. Es entregable de la Clase 5 y **no está redactado** en el repo.

- **Actualización de la tarde:** MDV integró los PRs #7, #8 y #9 (14:46, sin revisión de otro integrante). Se verificó que la migración está en `main`. El CI de `main` quedó en rojo porque GitHub bloqueó la cuenta por facturación, no por el código. El deploy público responde. Se actualizaron `mvp.md` y el índice de entregables, y la tarjeta [Migrar frontend](https://trello.com/c/qW9sArxq) pasó a ✅ Hecho con su comentario de resolución.

## Qué se definió

- MDV decidió dejar las metodologías largas por falta de tiempo y priorizar lo que se evalúa: tablero, documentación final y demo.
- User Persona y Mapa de Empatía se entregan con huecos explícitos, sin más trabajo de campo.

## Error corregido en la sesión

- La tarjeta "Citar Kaggle…" se archivó con un motivo incompleto: pedía la cita y la declaración de IA **en el README del repo del prototipo**, y eso no se verificó. El conector no permite desarchivar, así que se dejó un comentario de corrección. Queda vigente declarar en el repo del MVP que su interfaz viene del prototipo, que generó Codex (FGR). Hace falta una tarjeta nueva para eso.

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| ~~Revisar e integrar los PRs #7 ← #8 ← #9~~ ✅ integrados por MDV el 11/11 | MDV | 11/11 |
| Resolver el bloqueo de facturación de GitHub que frena el CI | ⬜ (sugerido: ML, dueño del repo) | ⬜ |
| Decidir el modelo de IA: LLM (Groq), modelo entrenado (decisión 0006) o los dos | Equipo | ⬜ |
| Resolver la diferencia MongoDB (implementado) vs. PostgreSQL (decisión 0007, tarjeta "Reconvertir stack") y cerrar P-10 | Equipo | ⬜ |
| Confirmar acceso de escritura de FGR y FM al repo del MVP | ⬜ | ⬜ |
| Redactar el Problem Statement | ⬜ | 18/11 (documentación final) |
| Declarar en el repo del MVP el origen de la interfaz migrada (prototipo de FGR, Codex) | ⬜ (sugerido: FGR) | 18/11 |
| Archivar las tarjetas de Jev y TypeSafe, si el equipo confirma Groq | Equipo | ⬜ |

## Dudas que surgieron

- Las tarjetas de FM en 🔨 En curso (MoSCoW, herramienta del backlog, User Flow, Story Mapping) vencían el 7/10 y no tienen comentario de cierre. No se tocaron.

## Archivos tocados

- `docs/05-producto/mvp.md`
- `docs/02-entregables/README.md`
- `docs/00-proyecto/declaracion-uso-ia.md`
- `registro/historial-aportes.md`
- `bitacora/2026-11-11-relevamiento-avance-presentacion.md`
