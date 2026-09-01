# 2026-09-01 — Armado de la base del repositorio

| | |
|---|---|
| **Tipo** | Trabajo individual (con asistencia de Claude Code) |
| **Duración** | — |
| **Participantes** | Facundo Molina (FM) |

## Qué se hizo

- Se creó el repositorio **FraudLens** como centro de cómputos del TIF.
- Se procesó la planilla `TIF_2C2026_Clase1597_Britez.xlsx` (cargada por Mateo Diaz Valdez) y se
  volcó su contenido a [`docs/00-proyecto/ficha-proyecto.md`](../docs/00-proyecto/ficha-proyecto.md)
  y [`docs/00-proyecto/equipo.md`](../docs/00-proyecto/equipo.md).
- Se procesó el material de la **Clase 1** (`001__SIP_Clase__01Vp_MVP_v1.2_1.pdf`, 51 diapositivas)
  y se escribió la nota completa en
  [`docs/01-clases/clase-01-mvp-y-problema.md`](../docs/01-clases/clase-01-mvp-y-problema.md),
  con la bajada de cada concepto a FraudLens.
- Se armó la estructura documental completa: proyecto, clases, entregables, decisiones, metodología,
  producto, bitácora y registro de aportes.
- Se escribieron las plantillas de **clase**, **decisión** y **sesión de bitácora**.
- Se cargaron **10 preguntas abiertas** en
  [`docs/00-proyecto/preguntas-abiertas.md`](../docs/00-proyecto/preguntas-abiertas.md).
- Se configuró **Graphify** (`.graphifyignore` + documentación de uso).

## Qué se definió

- **[Decisión 0001]** El repositorio es el centro de cómputos del TIF. El código del MVP vive aparte.
- **[Decisión 0002]** Graphify se adopta como capa de lectura, **opcional**: el repo se lee bien sin él.
- Convención de commits, de ramas y de nombres de archivo → [`flujo-de-trabajo.md`](../docs/04-metodologia/flujo-de-trabajo.md).
- Estructura propuesta para el tablero de Trello → [`trello.md`](../docs/04-metodologia/trello.md) *(falta validar contra el tablero real)*.

## Hallazgos a revisar con el equipo y con el docente

1. **El deck de Clase 1 trae el cronograma del 1C** (09/03 → 20/07) y nuestro período es 2C 2026.
   No tenemos fechas reales. → [P-04](../docs/00-proyecto/preguntas-abiertas.md#p-04)
2. **La Clase 1 pide equipos de 6-8 integrantes** y somos 4. → [P-03](../docs/00-proyecto/preguntas-abiertas.md#p-03)
3. **La Clase 1 pide llevar propuestas de problema** aunque la planilla ya tenga uno cargado.
   No está claro si FraudLens ya está aprobado. → [P-02](../docs/00-proyecto/preguntas-abiertas.md#p-02)
4. **El título no coincide** entre la planilla y el tablero de Trello. → [P-01](../docs/00-proyecto/preguntas-abiertas.md#p-01)
5. **"Datos reales" es exigencia del docente**, y en fraude conseguir datos es difícil. Es el riesgo
   más grande del proyecto. → [P-06](../docs/00-proyecto/preguntas-abiertas.md#p-06)
6. **Falta definir el usuario objetivo.** Sin eso no se puede definir el MVP.
   → [P-07](../docs/00-proyecto/preguntas-abiertas.md#p-07)

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| Dar acceso al repositorio a los 4 integrantes | FM | ⬜ |
| Validar la estructura del repo con el equipo | Equipo | ⬜ |
| Cargar las Clases 2, 3 y 4 | FM | ⬜ |
| Habilitar el conector de Trello en claude.ai | FM | ⬜ |
| Llevar al docente las preguntas P-02, P-03 y P-04 | Equipo | Próxima clase |
| Completar roles y alias de cada integrante | Equipo | ⬜ |

## Dudas que surgieron

Todas cargadas en [`preguntas-abiertas.md`](../docs/00-proyecto/preguntas-abiertas.md) (P-01 a P-10).

## Archivos tocados

Creación inicial del repositorio completo.
