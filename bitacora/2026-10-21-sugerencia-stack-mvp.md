# 2026-10-21 — Sugerencia de stack para el MVP (P-10)

| | |
|---|---|
| **Tipo** | Trabajo individual, con asistencia de Claude Code |
| **Duración** | — |
| **Participantes** | Mateo Diaz Valdez (MDV) |

## Qué se hizo

- MDV le preguntó a Claude Code qué stack elegiría para FraudLens, partiendo de un selector de stack para MVPs (artifact de Claude con research del 20-oct-2026, externo al proyecto) y sabiendo que es un proyecto universitario.
- Claude Code cruzó ese selector con el prototipo de FGR y las decisiones 0005 y 0006, y propuso 4 alternativas con sus tradeoffs.
- A pedido de MDV, la propuesta quedó cargada en [P-10](../docs/00-proyecto/preguntas-abiertas.md#p-10), **marcada como sugerencia de Claude Code**.

## Qué se definió

- **Nada.** P-10 sigue abierta. La sugerencia es la alternativa A (FastAPI + modelo en Python + frontend React del prototipo), pero no la aprobó nadie del equipo.

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| Relevar qué sabe usar cada integrante (Python, NestJS, React) | ⬜ | Antes de decidir P-10 |
| 6 Sombreros del stack, con el sombrero rojo de las 4 voces | ⬜ | ⬜ |

## Dudas que surgieron

- Las columnas del dataset 1 (0006) están anonimizadas: un modelo entrenado solo con él no puede puntuar una transacción cargada desde el formulario. Quedó anotado como riesgo en P-10.

## Archivos tocados

- [`docs/00-proyecto/preguntas-abiertas.md`](../docs/00-proyecto/preguntas-abiertas.md) (P-10)
- [`registro/historial-aportes.md`](../registro/historial-aportes.md)
- [`docs/00-proyecto/declaracion-uso-ia.md`](../docs/00-proyecto/declaracion-uso-ia.md)
