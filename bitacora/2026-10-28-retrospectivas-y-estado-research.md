# 2026-10-28 — Retrospectiva y estado del User Research

| | |
|---|---|
| **Tipo** | Mantenimiento documental y revisión de Trello con asistencia de Pi / el Gentleman |
| **Participantes** | Mateo Diaz Valdez (MDV) |
| **Alcance** | Actualizar la trazabilidad de la tarjeta de retrospectiva, revisar evidencia ya registrada y poner al día P-12 sin declarar validaciones del equipo |

## Qué se hizo

- Se revisó la tarjeta [Armar la plantilla de Retrospectiva y el registro de facilitadores](https://trello.com/c/5VB8UDLb). En la lectura posterior a los cambios, la descripción refleja a **MDV como responsable**, la plantilla existente y la facilitación planificada. Se comprobó que sigue en **Backlog**, abierta y sin completar, y que conserva el vencimiento **2026-10-14 12:00 UTC**.
- Se verificó el comentario de seguimiento publicado en la tarjeta: [comentario](https://trello.com/c/5VB8UDLb#comment-6ae2310791eff7adea563dba). No se cerró ni se marcó completa la tarjeta, y no se aprobaron propuestas.
- Se cotejaron `user-research.md` y `encuesta-perfil-c-analisis.md`. Las fuentes registran dos entrevistas (Nicolás y Agustín) del 16/9, y 28 respuestas de encuesta recopiladas del 16/9 al 22/9, cargadas el 7/10. El primer análisis continúa sin validar por el equipo.
- Se actualizó [P-12](../docs/00-proyecto/preguntas-abiertas.md#p-12) a **Parcial**, detallando la evidencia, las tareas pendientes de revisión/contraste y la diferencia entre la guía de 400 respuestas y el volumen que el equipo debe justificar (ver P-17).
- Se actualizó la declaración de uso de IA y se registró el aporte de MDV en el historial.

## Verificación

- Lectura posterior de Trello: responsable y comentario confirmados; lista, vencimiento y estado abierto preservados.
- `git diff --check`: sin errores de espacios; Git advierte que normalizará LF a CRLF en el historial de aportes.
- Chequeo estructural final: cambios de preguntas limitados a P-12, evidencia y validación pendiente presentes, filas de la declaración de IA separadas, 10 aportes de MDV y destinos de enlaces locales existentes en los cuatro archivos de esta tarea.
- En la lectura del diff se corrigió un salto de línea literal entre dos filas de la declaración de IA. Los primeros chequeos propios fallaron por escapes y codificación en el comando; el chequeo corregido pasó.
- La evaluación automática nativa no pudo evaluar el conjunto porque la bitácora nueva está sin seguimiento y requiere una declaración explícita de alcance. No se inició una revisión nativa ni se afirma su aprobación.
- No aplica RED/GREEN de comportamiento: son cambios documentales, sin código ejecutable modificado.

## Qué sigue pendiente

- El equipo debe revisar el primer análisis de la encuesta, decidir si amplía la difusión y contrastar los hallazgos en `usuarios.md`, `problema.md` y `requerimientos-funcionales-mvp.md`.
- Las aclaraciones existentes en [`retrospectivas.md`](../docs/04-metodologia/retrospectivas.md) y [`2026-10-14-plantilla-retrospectiva.md`](2026-10-14-plantilla-retrospectiva.md) se preservan; no se modificaron en esta tarea.
- Al terminar el mantenimiento no se había realizado commit ni push. Después, MDV autorizó el commit documental con el mensaje `docs: actualizar seguimiento de retrospectivas y estado del research`. El push queda pendiente de autorización separada.
