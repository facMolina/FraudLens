# 2026-11-04 — Corrección de la tarjeta de stack del MVP

| | |
|---|---|
| **Tipo** | Mantenimiento documental y de Trello con asistencia de Claude Code |
| **Participantes** | Mateo Diaz Valdez (MDV) |
| **Alcance** | Alinear la tarjeta de P-10 con el stack implementado en el repo de código del MVP, sin declarar una validación del equipo |

## Qué se hizo

- MDV indicó que el stack del MVP ya está definido en el repo de código y pidió corregir la tarjeta [Definir el stack tecnológico del MVP (P-10)](https://trello.com/c/QLA7vu9Y).
- Se relevó el stack en `main` de [mateolewinzon/fraudlens](https://github.com/mateolewinzon/fraudlens) (commit `da20858`, 30/10): Next.js App Router, React, TypeScript, Route Handlers en Node.js 24, MongoDB Atlas con Mongoose, Vercel AI SDK con TypeSafe (Jev) y un solo deploy en Vercel.
- Se reescribió la descripción de la tarjeta: el objetivo pasa de elegir entre las alternativas A-D a registrar y validar el stack implementado.
- En "Listo cuando", el relevamiento de qué sabe usar cada integrante se reemplazó por la confirmación del equipo, y se sumó definir cómo se resuelve el modelo de fraude.
- Se agregó el dato nuevo en [P-10](../docs/00-proyecto/preguntas-abiertas.md#p-10) y se actualizó su fila en el índice. La pregunta sigue abierta.

## Qué se encontró

- El `POST` de evaluaciones devuelve un resultado fijo: no hay reglas ni inferencia.
- El README indica que Atlas y la inferencia real de TypeSafe no se probaron.
- El adapter de Groq está en los PR abiertos #2 y #3, y no llegó a `main`.
- La decisión 0006 prevé un modelo entrenado con 3 datasets, y el stack no tiene hoy ninguna pieza de entrenamiento.
- [`mvp.md`](../docs/05-producto/mvp.md) sigue citando el commit `4cba610` y dice que no hay flujos implementados. No se modificó en esta sesión.

## Qué sigue pendiente

- Confirmación del equipo sobre el stack.
- Definir el modelo de fraude: entrenado, LLM o reglas, y con qué proveedor.
- 6 Sombreros del stack, con el sombrero rojo de las 4 voces.
- Decisión numerada en `docs/03-decisiones/` y cierre de P-10.
- La tarjeta sigue en 👀 En revisión.
