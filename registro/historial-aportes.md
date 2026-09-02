# Historial de aportes

Quién hizo qué a lo largo del cuatrimestre.

## Por qué existe este archivo

El docente evalúa **participación individual** ("aportes en clase, conocimiento y dedicación
demostrada en el proyecto") y **participación grupal**. Este registro es la evidencia.

Existe además del historial de Git porque **buena parte del trabajo del TIF no pasa por el
repositorio**: presentar en clase, hacer entrevistas, contactar gente del rubro, armar el pitch,
coordinar al equipo. Nada de eso aparece en un `git log`, y todo eso es trabajo del proyecto.

| Registro | Qué captura | Cómo se consulta |
|---|---|---|
| **Git** | Cambios en archivos. Automático, no se puede falsear | `git log --author="Nombre" --oneline` |
| **Este archivo** | Todo lo demás | Se lee directo |

## Cómo se carga

Una fila por aporte, en la sesión en que se hizo. **No dejarlo para el final del cuatrimestre**:
nadie se acuerda después, y se nota.

Tipos de aporte: `Documentación` · `Clase` · `Research` · `Producto` · `Desarrollo` · `Gestión` · `Presentación`

---

## Registro

| Fecha | Quién | Tipo | Aporte | Evidencia |
|---|---|---|---|---|
| *(previo)* | MDV | Gestión | Carga de la planilla de relevamiento inicial de propuestas TIF 2C 2026 | `TIF_2C2026_Clase1597_Britez.xlsx` |
| 2026-09-01 | FM | Gestión | Armado de la estructura base del repositorio como centro de cómputos | [Bitácora](../bitacora/2026-09-01-armado-de-la-base.md) |
| 2026-09-01 | FM | Documentación | Procesamiento y carga de la Clase 1 (51 diapositivas) con bajada de conceptos a FraudLens | [Clase 01](../docs/01-clases/clase-01-mvp-y-problema.md) |
| 2026-09-01 | FM | Documentación | Glosario, ficha de proyecto, materia, entregables y 10 preguntas abiertas | [`docs/00-proyecto/`](../docs/00-proyecto/) |
| *(previo)* | ML | Producto | **Propuso el tema del proyecto.** Es el referente del rubro del equipo y tiene acceso a información de otros expertos | — |
| Clase 4 | ML | Producto | Redacción de los requerimientos funcionales del MVP: 7 casos de uso, flujo, criterios de aceptación, no funcionales y definición de "MVP terminado" | [Requerimientos (borrador)](../docs/05-producto/requerimientos-funcionales-mvp.md) |
| *(previo)* | FGR | Desarrollo | **Prototipo de FraudLens**: backend generado con Claude, frontend con Codex y ajustado al backend, sobre la base de un notebook de Kaggle y del documento de requerimientos | [Prototipo](../docs/05-producto/prototipo.md) |
| *(previo)* | FGR | Gestión | Creación del tablero de Trello | [Tablero](https://trello.com/b/iUaTi33p/fraudlens-analizador-probabilidad-de-fraude) |
| 2026-09-02 | FM | Gestión | Carga del material crudo de las Clases 2, 3 y 4; regla de formato Markdown para material de clase | [`docs/01-clases/material/`](../docs/01-clases/material/) |
| 2026-09-02 | FM | Documentación | Incorporación del documento de FGR al repo y resolución de las preguntas P-01, P-02 y P-03 | [Bitácora](../bitacora/2026-09-02-material-clases-y-requerimientos.md) |
| 2026-09-02 | FM | Documentación | Notas trabajadas de las Clases 2, 3 y 4 con bajada a FraudLens, y 15 términos nuevos al glosario | [`docs/01-clases/`](../docs/01-clases/) |
| 2026-09-02 | FM | Gestión | Redacción de los 17 tickets pendientes para la Clase 5 | [Pendientes Clase 5](../docs/02-entregables/pendientes-clase-05.md) |
| 2026-09-02 | FM | Gestión | Carga del cronograma oficial 2C 2026 y corrección de todas las fechas del proyecto | [Cronograma](../docs/00-proyecto/cronograma.md) |
| 2026-09-02 | FM | Gestión | Limpieza y rearmado del tablero de Trello: archivado de 14 tarjetas de plantilla, listas en español y 15 tarjetas reales | [Tablero](https://trello.com/b/iUaTi33p/fraudlens-analizador-probabilidad-de-fraude) |
| 2026-09-02 | FM | Producto | Toma a cargo la **identidad visual** de FraudLens: colorimetría, logo, tipografía e imagen de marca | [Tarjeta](https://trello.com/c/ncNYKzbF) |
| 2026-09-02 | Equipo | Producto | Pre-selección de 3 datasets/notebooks de Kaggle candidatos para el modelo | [`datos.md`](../docs/05-producto/datos.md) |
| 2026-09-02 | FM | Documentación | Incorporación del método de los **6 Sombreros** (consigna del docente): método, plantilla, decisión 0003 y regla de alcance | [`seis-sombreros.md`](../docs/04-metodologia/seis-sombreros.md) |
| 2026-09-02 | FM | Producto | Análisis de 6 Sombreros sobre **quién es el usuario de FraudLens** — la decisión que bloquea los entregables del 2/9 | [Análisis](../docs/05-producto/analisis/6-sombreros-usuario-objetivo.md) |
| 2026-09-02 | FM | Gestión | Rutina de inicio de sesión con Trello obligatorio y auto-asignación de tickets, en README y CLAUDE.md | [README](../README.md) |
| 2026-09-02 | FM | Gestión | Convención de tickets: taxonomía de 7 etiquetas, formato de tarjeta y comentario de resolución obligatorio | [Convención](../docs/04-metodologia/convencion-de-tickets.md) |
| 2026-09-02 | FM | Diseño | Brief de identidad visual de FraudLens y prompts para generación de isotipos, paletas, mockup y tipografía | [Brief](../docs/05-producto/identidad-visual.md) |

---

## Resumen por integrante

> Se actualiza antes de cada entrega. Sirve para detectar desbalances a tiempo, no para competir.

| Integrante | Aportes registrados | Última participación |
|---|---|---|
| Diaz Valdez, Mateo (MDV) | 1 | *(previo)* |
| Guerrero Rojas, Francisco Daniel (FGR) | 2 | *(previo)* |
| Lewinzon, Mateo (ML) | 2 | Clase 4 |
| Molina, Facundo Roman (FM) | 15 | 2026-09-02 |

> ⚠️ Faltan cargar los aportes previos de **MDV**, y las fechas exactas de los aportes marcados
> como *(previo)*.

> 📝 **Corrección (2026-09-02):** en una primera carga se atribuyó el documento de requerimientos
> funcionales a FGR. **Lo escribió ML.** FGR aportó el prototipo y el tablero de Trello.

## Presentaciones en clase

> La Clase 1 exige que **los presentadores de las Sprint Reviews roten semana a semana**.
> Acá queda el registro de quién presentó qué.

| Fecha | Instancia | Presentó |
|---|---|---|
| ⬜ | ⬜ | ⬜ |
