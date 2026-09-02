# 2026-09-02 — Material de clases 2-4, requerimientos de FGR y estructura de carpetas

| | |
|---|---|
| **Tipo** | Trabajo individual (con asistencia de Claude Code) |
| **Duración** | — |
| **Participantes** | Facundo Molina (FM) |

## Qué se hizo

- Se creó **[`docs/01-clases/material/`](../docs/01-clases/material/)** para guardar el material
  crudo de cada clase, y se cargaron las **Clases 1, 2, 3 y 4** en Markdown.
- Se estableció la **regla de formato**: el material de clase se sube en Markdown, **nunca en PDF**.
  Conversión en https://cloudconvert.com/pdf-to-md. La regla quedó en `CLAUDE.md`,
  `docs/01-clases/README.md` y `docs/01-clases/material/README.md`, y `*.pdf`/`*.pptx`/`*.xlsx`
  quedaron en `.gitignore`.
- Se incorporó el documento de **Francisco (FGR)** como
  [`docs/05-producto/requerimientos-funcionales-mvp.md`](../docs/05-producto/requerimientos-funcionales-mvp.md),
  **marcado como borrador sin aprobar**, con una sección final de puntos a discutir.
- Se agregaron dos reglas a `CLAUDE.md`: **no deducir** (si falta un dato, se pregunta) y
  **borrador ≠ definición**.

## Qué se definió

Respuestas de FM que cierran preguntas abiertas:

| Pregunta | Respuesta |
|---|---|
| [P-01](../docs/00-proyecto/preguntas-abiertas.md#p-01) — Título del proyecto | **FraudLens** es el nombre "marketinero"; convive con el título académico de la planilla |
| [P-02](../docs/00-proyecto/preguntas-abiertas.md#p-02) — ¿Problema aprobado? | **Sí, el docente lo aprobó** |
| [P-03](../docs/00-proyecto/preguntas-abiertas.md#p-03) — ¿Equipo de 4? | **Sí**, porque este cuatrimestre hay menos gente cursando |
| [P-04](../docs/00-proyecto/preguntas-abiertas.md#p-04) — Cronograma | El del deck de Clase 1 **se ignora** (es del 1C). FM va a pasar el real |
| [P-06](../docs/00-proyecto/preguntas-abiertas.md#p-06) — Datos | El equipo **tiene dataset de casos de prueba** para el MVP. Falta documentarlo |

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| Escribir las notas trabajadas de las Clases 2, 3 y 4 | FM | ⬜ |
| Pasar el cronograma real del 2C 2026 | FM | ⬜ |
| Documentar el dataset de casos de prueba ([P-11](../docs/00-proyecto/preguntas-abiertas.md#p-11)) | Equipo | ⬜ |
| Revisar en equipo el documento de requerimientos de FGR ([P-15](../docs/00-proyecto/preguntas-abiertas.md#p-15)) | Equipo | ⬜ |
| Conectar Trello a la cuenta de claude.ai | FM | ⬜ |
| Cargar los aportes previos de ML y del resto del equipo | Equipo | ⬜ |

## Dudas que surgieron

Se cargaron 5 preguntas nuevas: **P-11 a P-15** en
[`preguntas-abiertas.md`](../docs/00-proyecto/preguntas-abiertas.md).

> ⚠️ **Nota sobre el material crudo:** los decks del docente son muy visuales y la conversión a
> Markdown llega desordenada, sobre todo en las **Clases 2 y 3** (mucho texto de imagen mezclado).
> Por eso las notas trabajadas de esas clases **no se escribieron todavía**: hacerlo requeriría
> deducir contenido, y la instrucción del equipo es explícita en que no se deduce.

## Archivos tocados

- `docs/01-clases/material/` *(nuevo)* — 4 clases + README con la regla de formato
- `docs/05-producto/requerimientos-funcionales-mvp.md` *(nuevo)*
- `docs/00-proyecto/preguntas-abiertas.md` — P-01/02/03 resueltas, P-06 parcial, P-11 a P-15 nuevas
- `docs/00-proyecto/ficha-proyecto.md`, `equipo.md` — propagación de las respuestas
- `docs/01-clases/README.md`, `docs/05-producto/README.md` — índices
- `CLAUDE.md`, `.gitignore`, `.graphifyignore`
- `registro/historial-aportes.md` — aporte de FGR registrado
