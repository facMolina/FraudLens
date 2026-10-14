# 2026-10-14 — Borrador del User Story Mapping y de la herramienta del backlog

| | |
|---|---|
| **Tipo** | Documentación de producto, con asistencia de Claude Code |
| **Duración** | — |
| **Participantes** | Facundo Molina (FM) |

## Qué se hizo

FM pidió avanzar con sus 3 tarjetas en curso **a través de preguntas, de a una por vez**. Se hicieron 9 y salieron tres borradores:

- [`user-story-map.md`](../docs/05-producto/user-story-map.md) — tarjeta [User Story Mapping](https://trello.com/c/mxSfKQw6).
- [`6-sombreros-herramienta-backlog.md`](../docs/05-producto/analisis/6-sombreros-herramienta-backlog.md) — tarjeta [herramienta del backlog](https://trello.com/c/kceMBbCj). **El sombrero rojo quedó vacío**: lo escribe el equipo.
- [`user-flows.md`](../docs/05-producto/user-flows.md) — tarjeta [User Flow](https://trello.com/c/ivQo0hEI): el **guion** de los 5 flujos (pasos, decisiones del usuario y del sistema, caminos alternativos, con la fuente de cada uno). **El dibujo:** FM preguntó si Claude Code podía hacerlo con el conector de Figma; lo conectó y se generó un **primer borrador en FigJam** ([tablero](https://www.figma.com/board/tKo7wt7bStXRCGCLNzqlRA)), sin revisar. Las formas son provisorias (las del docente no se conocen).

## Qué se definió

Nada es decisión del equipo. Son **propuestas de FM**:

| Pregunta | Respuesta de FM |
|---|---|
| Herramienta del backlog | **Trello** |
| Dónde viven las historias | **La misma lista Backlog, con una etiqueta HU** *(se le advirtió que comparten el orden de prioridad con los tickets de trabajo)* |
| Usuario del mapa | **Solo el Analista de fraude** |
| Objetivo del usuario | **Decidir qué hacer con cada caso** |
| Qué hace con el caso en FraudLens | **Solo ve la recomendación** y actúa por fuera |
| Cantidad de User Flow | **5, uno por paso del recorrido** |
| Formato y herramienta de los flujos | **Figma** (FM). Al final los dibujó Claude Code en FigJam con el conector, a pedido de FM; FM revisa |
| Recorrido (5 pasos) | Ver la cola · encontrar los casos · abrir un caso · entender por qué · leer la recomendación — **confirmado** |
| Qué entra al MVP | **Los 5 pasos completos** (8 tareas) |
| R2 | Alertas y notificaciones · explicabilidad avanzada · configurar umbrales en vivo · reentrenamiento automático |
| Alcance de la entrega | **Solo R1.** *"El MVP llega a la R1 no más"* |

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| El equipo valida el mapa y la herramienta; sombrero rojo de las 4 voces | Equipo | ⬜ |
| MoSCoW de cada tarea | Equipo | ⬜ |
| Decidir cómo se llevan al backlog las historias que no son del analista (HU-07 a HU-10, HU-13, HU-14): sigue abierta [P-32](../docs/00-proyecto/preguntas-abiertas.md#p-32) | Equipo | ⬜ |
| Verificar si el conector de Trello puede crear la etiqueta HU (si no, hacerla a mano) | FM | ⬜ |
| Ajustar el borrador del backlog de MDV al mapa | ⬜ | ⬜ |
| **FM mira las formas del docente** en el deck original de la Clase 10 (decisión del usuario vs. del sistema) | FM | ⬜ |
| **FM revisa el tablero generado**, ajusta las formas con las del docente y lo comparte con el equipo (está en sus borradores) | FM | ⬜ |

## Dudas que surgieron

- Todo el recorrido entra a R1: la Clase 1 pide un MVP chico. Queda a la vista, sin cuestionarlo.
- El objetivo dice "decidir" y FraudLens solo recomienda: la acción ocurre afuera.

## Archivos tocados

- Nuevos: `docs/05-producto/user-story-map.md` · `docs/05-producto/analisis/6-sombreros-herramienta-backlog.md` · `docs/05-producto/user-flows.md`
- Modificados: `docs/00-proyecto/preguntas-abiertas.md` (P-30 y P-32, con la propuesta de FM) · `docs/05-producto/README.md` · `docs/05-producto/analisis/README.md` · `registro/historial-aportes.md`
