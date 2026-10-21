# 2026-10-21 — Stack del prototipo: un solo deploy en Vercel con PostgreSQL

| | |
|---|---|
| **Tipo** | Trabajo individual, con asistencia de Claude Code |
| **Duración** | — |
| **Participantes** | Francisco Guerrero Rojas (FGR) |

## Qué se hizo

- FGR tomó la tarjeta [Reconvertir stack de prototipo para modelo mejorado con un solo Deploy](https://trello.com/c/6LaBsgsa): pasó de 📥 Backlog a 🔨 En curso, con vencimiento el **25/10 09:00 (GMT-3)**.
- Claude Code relevó el código del prototipo y encontró que el aislamiento entre organizaciones depende de funciones propias de PostgreSQL (RLS, `set_config`, `pg_advisory_xact_lock`, SQL crudo del dashboard).
- FGR primero confirmó MongoDB Atlas como firme. Después de ver los riesgos, decidió **mantener PostgreSQL en esta fase**.
- Se actualizó la descripción de la tarjeta con la decisión, sus motivos y el plan corregido.
- Se escribieron la [decisión 0007](../docs/03-decisiones/0007-prototipo-postgresql-un-deploy-vercel.md) y el [borrador del 6 Sombreros](../docs/05-producto/analisis/6-sombreros-stack-prototipo-vercel.md).

## Qué se definió

- **(FGR)** El prototipo pasa a Next.js (frontend + API routes) en un solo deploy en Vercel y **mantiene PostgreSQL**. MongoDB Atlas queda descartado para esta fase → [0007](../docs/03-decisiones/0007-prototipo-postgresql-un-deploy-vercel.md), 🟡 Propuesta hasta que la validen MDV y ML.
- **(FGR)** La migración vence el **25/10**.

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| Validar la decisión 0007 (estaban asignados a la tarjeta) | MDV · ML | Antes del 25/10 |
| Sombrero rojo del 6 Sombreros | Los 4 | ⬜ |
| Ponerle etiqueta a la tarjeta: el tablero no tiene 🟠 Código ([P-22](../docs/00-proyecto/preguntas-abiertas.md#p-22)) | ⬜ | ⬜ |
| Implementar la migración en el repo del prototipo | FGR | 25/10 |

## Dudas que surgieron

- ⬜ Por qué la tarjeta original planteaba MongoDB Atlas. Quedó como faltante en el sombrero blanco.
- ⬜ Si la conexión con pooler funciona con el esquema de RLS desde funciones de Vercel. No se probó.
- El índice de [`docs/03-decisiones/README.md`](../docs/03-decisiones/README.md) no lista las decisiones 0004 a 0006. Se sumó sólo la 0007.

## Archivos tocados

- [`docs/03-decisiones/0007-prototipo-postgresql-un-deploy-vercel.md`](../docs/03-decisiones/0007-prototipo-postgresql-un-deploy-vercel.md) (nuevo)
- [`docs/03-decisiones/README.md`](../docs/03-decisiones/README.md)
- [`docs/05-producto/analisis/6-sombreros-stack-prototipo-vercel.md`](../docs/05-producto/analisis/6-sombreros-stack-prototipo-vercel.md) (nuevo)
- [`docs/05-producto/analisis/README.md`](../docs/05-producto/analisis/README.md)
- [`docs/00-proyecto/preguntas-abiertas.md`](../docs/00-proyecto/preguntas-abiertas.md) (P-10)
- [`registro/historial-aportes.md`](../registro/historial-aportes.md)
- [`docs/00-proyecto/declaracion-uso-ia.md`](../docs/00-proyecto/declaracion-uso-ia.md)
