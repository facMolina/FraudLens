# 2026-10-14 — Revisión de los tickets en 👀 En revisión

| | |
|---|---|
| **Tipo** | Revisión de tablero, con asistencia de Claude Code |
| **Duración** | ⬜ |
| **Participantes** | Mateo Diaz Valdez (MDV) |

## Qué se hizo

MDV pidió revisar las 6 tarjetas de 👀 En revisión: puntos clave, preguntas y que el asistente se encargue del resto. Se leyó el tablero (48 tarjetas), se contrastó cada tarjeta con sus "Listo cuando" y con los archivos del repo, y se aplicó lo que MDV eligió: **informe + comentarios + mover tarjetas**.

## Veredicto por tarjeta

| Tarjeta | Resp. | Veredicto | Qué se hizo en Trello |
|---|---|---|---|
| [Stakeholders y expertos consultados](https://trello.com/c/NTsPXw2W) | — | ✅ Cumple | Comentario de resolución · movida a ✅ Hecho |
| [Encuestas y entrevistas](https://trello.com/c/KPXsyG4O) | — | ✅ Cumple, con límites | Comentario de resolución (análisis preliminar, sin validar, n=28 contra 80–100) · movida a ✅ Hecho |
| [Documentar el prototipo de FGR](https://trello.com/c/DC1vH1F6) | — | ✅ La documentación cumple; los pendientes son de FGR | Comentario de resolución · movida a ✅ Hecho · **tarjeta nueva** [Citar el notebook de Kaggle, declarar el uso de IA y probar el prototipo](https://trello.com/c/BmqJQ5uC) en 📥 Backlog |
| [Decidir la herramienta del Product Backlog](https://trello.com/c/kceMBbCj) | FM | ❌ No cumple | Comentario de revisión · devuelta a 🔨 En curso |
| [Armar la propuesta de MVP con User Story Mapping](https://trello.com/c/mxSfKQw6) | FM | ❌ No cumple | Comentario de revisión · devuelta a 🔨 En curso |
| [Plantear los User Flow](https://trello.com/c/ivQo0hEI) | FM | ❌ No cumple | Comentario de revisión · devuelta a 🔨 En curso |

## Qué se definió

MDV decidió (2026-10-14), eligiendo entre opciones que se le presentaron con sus costos:

| Decisión | Alternativas que descartó |
|---|---|
| Informe + comentarios + mover tarjetas | Solo informe sin tocar Trello · además completar huecos que no son del equipo (decisión 0007, esqueleto del 6 Sombreros) |
| Cerrar Encuestas ahora, aclarando los límites del análisis | Dejarla en revisión hasta que el equipo valide · cerrarla y abrir una tarjeta para ampliar la muestra |
| Cerrar la documentación del prototipo y abrir una tarjeta para FGR | Dejarla tal cual · devolverla a En curso con FGR de dueño |

## Hallazgos de la revisión

1. **El mapa y los flujos se contradicen.** El User Story Map deja HU-13 (aprobar por regla los montos bajos) "sin carril"; el Flujo 5 del User Flow la usa como paso de R1.
2. **HU-12 y HU-11 / HU-06** siguen sin resolver (choque con la decisión 0005 y solape). La 0005 recorta CU-02 y CU-07 a configuración fija, no los elimina: la regla de monto mínimo sigue aplicando.
3. **Todo el recorrido del analista entra en R1**, en tensión con "MVP chico" de la Clase 1. FM lo dejó a la vista.
4. **El FigJam de los User Flow no lo puede abrir nadie más.** Se probó con la cuenta de MDV (`get_figjam`) y devuelve "no tenés acceso": está en los borradores de FM.
5. **Falta `6-sombreros-mvp-user-story-map.md`**, que la tarjeta del User Story Mapping dice que hay que crear.
6. **El commit `a053847`** (dibujo en FigJam) está firmado como "Claude", no con un usuario del equipo.
7. **Ninguna tarjeta que estaba en revisión tenía revisor asignado ni etiqueta de categoría** (P-22 sin aprobar). Las 3 de FM tienen a FM como dueño.
8. **El relevamiento del prototipo es de segunda mano:** lo hizo otro chat de Claude con Claude in Chrome, sin ejecutar. Nadie del equipo corrió el prototipo ni sus 12 tests.

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| Sombrero rojo de las 4 voces en `6-sombreros-herramienta-backlog.md`, decisión 0007 y cerrar P-30 | Equipo (FM lleva la tarjeta) | ⬜ |
| Escribir `6-sombreros-mvp-user-story-map.md`, resolver P-32 y hacer el MoSCoW que da el orden vertical | Equipo (FM lleva la tarjeta) | ⬜ |
| Compartir el FigJam, confirmar las formas del docente y agregar un camino alternativo al Flujo 4 | FM | ⬜ |
| Alinear mapa y flujos sobre HU-13 | FM | ⬜ |
| Citar el notebook de Kaggle, declarar la IA y probar el prototipo | FGR (tiene que darle "Unirme" a la tarjeta nueva) | ⬜ |
| Justificar en el documento final el n=28 de la encuesta C y que el análisis lo valide el equipo | Equipo | ⬜ |
| Confirmar con ML si está de acuerdo en que Nicolás y Agustín se citen con su nombre de pila en el documento final | MDV · ML | ⬜ |
| Aprobar la taxonomía de etiquetas y asignar revisor en 👀 En revisión (P-22) | Equipo | ⬜ |

## Dudas que surgieron

- ¿Quién revisa las tarjetas en 👀 En revisión? La regla dice "se asigna al revisor" y ninguna lo tenía.
- ¿Se firman con el usuario del equipo los commits que genera el asistente? El `a053847` no cumple la regla.

## Archivos tocados

- Nuevos: `bitacora/2026-10-14-revision-tickets-en-revision.md`
- Modificados: `registro/historial-aportes.md` · `docs/00-proyecto/declaracion-uso-ia.md`
- Trello: 6 comentarios, 6 tarjetas movidas, 1 tarjeta creada.
