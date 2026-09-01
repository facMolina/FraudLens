# 0001 — Usar este repositorio como centro de cómputos del TIF

| | |
|---|---|
| **Fecha** | 2026-09-01 |
| **Estado** | ✅ Aceptada |
| **Decidido por** | Facundo Molina (a validar con el equipo) |
| **Pregunta relacionada** | [P-05](../00-proyecto/preguntas-abiertas.md#p-05) |

## Contexto

El TIF se extiende todo el cuatrimestre, con 4 sprints, 2 entregas evaluables, un documento final y
un pitch. El docente advirtió que *"si la materia se lleva al día, el documento entregable resulta
una sumatoria de pequeñas tareas iteradas"* — y que el trabajo no se hace sólo en horario de clase.

Somos 4 personas trabajando en paralelo, con clases que van agregando conceptos que hay que aplicar
al proyecto. Sin un lugar único, la información se dispersa entre chats, audios, Drive y la memoria
de quien estuvo en cada charla.

## Alternativas consideradas

| Opción | A favor | En contra |
|---|---|---|
| **Repositorio Git con documentación en Markdown** | Historial de quién hizo qué, versionado, diffs, funciona offline, se lee en GitHub, es gratis | Requiere que los 4 usen Git con cierta fluidez |
| Google Drive / Docs compartido | Cero fricción, edición simultánea | Sin trazabilidad real de aportes, se desordena rápido, difícil de referenciar desde el código |
| Notion / Confluence | Lindo, buscador | Otra herramienta más, y el historial por persona es débil |
| Todo en Trello | Ya lo tenemos, es evaluado | Trello es para tareas, no para documentación de conceptos |

## Decisión

Este repositorio es el **centro de cómputos** del TIF: el registro único de definiciones, conceptos
de clase, decisiones, bitácora de trabajo e historial de aportes. **No es el producto final** — el
código del MVP vive aparte.

## Por qué

- **Trazabilidad de aportes por integrante**: el docente evalúa participación individual. Git da eso
  de forma automática (`git log --author`), y lo complementamos con un historial en Markdown legible.
- **Markdown es diffeable**: se puede ver exactamente qué cambió entre una entrega y la anterior.
- **Un solo lugar**: si no está acá, no existe. Es una regla simple de sostener.
- **Se convierte solo en el entregable**: el documento final se arma juntando lo que ya está escrito.

## Consecuencias

- Todo lo que se define en clase, en reunión o en un audio **tiene que terminar en un `.md`**.
- Cada sesión de trabajo deja un archivo en [`bitacora/`](../../bitacora/) y una línea en
  [`registro/historial-aportes.md`](../../registro/historial-aportes.md).
- Los 4 integrantes necesitan acceso de escritura al repositorio.
- Trello queda para **tareas** (y es evaluado); el repositorio queda para **conocimiento**.
  Las tarjetas de Trello linkean a los documentos y viceversa.
