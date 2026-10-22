# Declaración de Uso de Inteligencia Artificial — FraudLens

| | |
|---|---|
| **Proyecto** | FraudLens — Sistema inteligente de detección de fraude en transacciones en tiempo real |
| **Materia** | Seminario de Gestión Tecnológica — TIF, 2C 2026 |
| **Equipo** | Diaz Valdez, Mateo (1192969) · Guerrero Rojas, Francisco Daniel (1042529) · Lewinzon, Mateo (1151641) · Molina, Facundo Roman (1115862) |
| **Fecha** | 2026-09-30 *(documento vivo — se actualiza cada vez que cambia el uso de IA)* |
| **Marco normativo** | [Lineamientos de Uso de Inteligencia Artificial — UADE](https://dre.uade.edu.ar/PDFs/lineamientosiaalumnos1.pdf), sección *"Uso de IA en Trabajos Integradores Finales, Trabajos Finales de Investigación, Proyectos Finales de Ingeniería"* |

> Esta declaración se presenta porque el lineamiento de la UADE la exige de forma **obligatoria**
> para TIF: *"Los alumnos deberán presentar una declaración informando si se utilizaron
> herramientas de IA."* La omisión, o presentar información falsa o engañosa, se considera falta a
> la integridad académica — la declaración en sí **no penaliza**.

## Herramientas utilizadas

| Herramienta | Quién la usó | Para qué |
|---|---|---|
| **Claude** (chat web) | Los 4 integrantes del equipo | Consultas de estudio, redacción y comprensión de conceptos de la materia — uso instrumental |
| **Claude Code** | Facundo Molina (FM), con validación del equipo en cada sesión | Construcción y mantenimiento de este repositorio: documentación de clases, decisiones, diseño del research, identidad visual, benchmarking, ideación, revisión de requerimientos |
| **Claude Code** | Mateo Diaz Valdez (MDV), desde 2026-09-30 | Gestión del tablero de Trello (lectura del estado, comentario de resolución, movimiento de tarjetas) y del rastro en el repo (bitácora, historial de aportes, estado de tickets). Desde 2026-10-21, también wireframes en Figma con el conector de Figma |
| **Claude** | Francisco Guerrero Rojas (FGR) | Generación del **backend** del prototipo de FraudLens |
| **Codex** | Francisco Guerrero Rojas (FGR) | Generación del **frontend** del prototipo, ajustado al backend ya generado |
| **Gemini / Nano Banana** (Google AI Studio) | Facundo Molina (FM) | Generación de imágenes exploratorias para la identidad visual: isotipos, paletas de color, mockups de dashboard y lámina de tipografía — ver [`prompts-nano-banana.md`](../05-producto/prompts-nano-banana.md) |

## Alcance del uso, por etapa

| Etapa / entregable | Herramienta | Qué se generó con IA | Qué hizo el equipo |
|---|---|---|---|
| Documentación de clases (`docs/01-clases/`) | Claude Code | Redacción de notas trabajadas a partir del material crudo cargado por el equipo | El equipo aportó el material fuente y la bajada a FraudLens se basa en decisiones y hechos que el equipo confirmó en sesión |
| Identidad visual (logo, paleta, tipografía) | Gemini/Nano Banana (generación de imágenes) + Claude Code (prompts, análisis, contraste WCAG, Canva, assets finales) | Dos rondas de generación (2/9 en azul, 2/9 en violeta ya decidido): 3 láminas de isotipos, 2 de paleta, 2 de mockup de dashboard, 1 de tipografía — analizadas en [`analisis-generacion-01.md`](../05-producto/identidad/analisis-generacion-01.md) | El equipo votó entre las 3 propuestas finales de isotipo y aprobó la decisión final (violeta, "Anomalía en grilla") |
| Plan de research, benchmarking, ideación, Árbol de Problemas/5 Por Qué | Claude Code | Redacción de los documentos, búsqueda web para benchmarking y normativa citada | FM corrigió cada punto en vivo (ver `bitacora/2026-09-14-*.md`); ninguna afirmación fáctica quedó sin fuente marcada |
| Revisión de requerimientos funcionales del MVP | Claude Code | Análisis de los puntos a discutir, propuesta de recorte de alcance | El equipo definió las respuestas de fondo (roles, alcance, qué es MVP); Claude Code documentó y estructuró |
| Documentación del dataset del MVP (`datos.md`) | Claude Code | Investigación web para identificar qué dataset usa cada notebook candidato y sus características (registros, columnas, licencia), marcando qué quedó confirmado con fuente y qué no | **FGR decidió** usar 3 datasets y el rol de cada uno (entrenamiento / validación y explicabilidad / test final) — no fue una sugerencia del asistente |
| Análisis de las respuestas de la encuesta del Perfil C (2026-10-07) | Claude Code | Tabulación de las 28 respuestas con un script y lectura manual de las respuestas abiertas, agrupadas en temas con la lista de respuestas de cada uno | **FM** aportó el export de datos. El análisis queda marcado como **primer análisis sin validar**: el equipo lo tiene que revisar. Se anonimizó una respuesta y se aclaró en el documento |
| Relevamiento del formulario de la encuesta y del repo del prototipo de FGR (2026-10-07) | Claude (otro chat, con Claude in Chrome) | Lectura en **solo lectura** del Form público y del repo privado (commit `5f6528c`), con la evidencia de cada dato; informe de hechos y de lo que no pudo verificar | **FM** abrió el chat con su navegador y su sesión de GitHub y aportó el informe. Los estados "implementado" **no se ejecutaron**: son lectura de código. El informe es de segunda mano para el resto del repo |
| Gestión del tablero de Trello y rastro en el repo (2026-09-30) | Claude Code | Redacción del comentario de resolución de la tarjeta "Decidir los 3 perfiles" a partir de lo ya documentado en el repo y en Trello, y de la bitácora/historial de esa sesión | **MDV decidió** cerrar la tarjeta sin la voz de ML en el sombrero rojo y **dejar sin tocar** la tarjeta del 1° Parcial hasta tener la devolución del docente; el asistente propuso, no decidió |
| Investigación de TypeSafe AI / Jev (2026-09-30) | Claude Code | Búsqueda web y lectura de la documentación oficial y de una fuente secundaria; redacción de `typesafe-jev.md` con arquitectura propuesta y diagramas Mermaid, marcando fuente oficial / secundaria / hipótesis; borrador de `6-sombreros-jev.md` (blanco con hechos; negro, amarillo y verde como propuesta); redacción de las tarjetas de Trello y de las preguntas P-25 a P-27 | **MDV** definió el objetivo y el alcance y aprobó el plan de documentos y tarjetas. **El sombrero rojo lo escribe el equipo** y el azul no se decidió: nada se adopta hasta el 6 Sombreros y la aprobación del equipo |
| Prueba de Jev en el playground (2026-09-30) | Claude Code (con control del navegador) | Redacción del caso de prueba **sintético** y carga en el playground de TypeSafe; lectura de la documentación oficial; corrección del propio documento. **No se generó código ni se obtuvieron resultados de Jev** (la cuenta no tenía fondos) | **MDV** pidió la prueba y decide si se cargan fondos: el asistente no hizo ningún pago. No se usaron datos reales |
| Plantilla de Retrospectiva (2026-10-14) | Claude Code | Lectura del estado del tablero de Trello, del cronograma y de las preguntas abiertas; redacción de `retrospectivas.md` a partir de las reglas de la Clase 09, con el formato y el lugar de documentación como **propuesta** | **MDV** eligió la tarea. No se cargó el material del Taller de Retrospectivas (7/10), así que la plantilla no lo incorpora; el facilitador de la Retro 1 y el formato quedan para que el equipo los decida |
| Borrador del Product Backlog (2026-10-14) | Claude Code | Reescritura de CU-05 y CU-06 de los requerimientos de ML al formato de historia de usuario (Como/Quiero/Para y Dado/Cuando/Entonces), marcando la fuente de cada criterio y lo que falta; publicación de un comentario en Trello redactado a pedido de MDV | **MDV** pidió el borrador y aprobó publicar el comentario. Ningún criterio se inventó: lo que los requerimientos no dicen quedó como pendiente. **El equipo todavía no revisó** el borrador ni decidió el MoSCoW |
| User Flow del MVP (2026-10-14) | Claude Code (con el conector de Figma) | Redacción del guion de los 5 flujos a partir de los requerimientos y las historias del repo, y generación de un primer dibujo en FigJam a partir de ese guion. Las formas y colores son elección del asistente porque las del docente no se conocen; lo que el dibujo completa y el guion no dice quedó listado en `user-flows.md` | **FM** definió el usuario, la cantidad de flujos (5) y la herramienta, y pidió que lo dibuje el asistente. **El equipo todavía no revisó** el dibujo ni las formas |
| Correcciones tras la revisión de MDV (2026-10-15) | Claude Code (con el conector de Figma) | Lectura de la revisión de MDV en Trello y en el repo; incorporación de HU-13 al mapa y de un camino alternativo al Flujo 4 (regenerando ese dibujo en FigJam); borrador del 6 Sombreros del mapa con el blanco armado solo con hechos del repo; verificación de las herramientas del conector de Trello sobre etiquetas | **FM** decidió las dos correcciones de contenido entre opciones que se le presentaron. **El sombrero rojo del nuevo análisis queda vacío**: lo escribe el equipo. Nada de esto está validado por el equipo |
| Revisión de las tarjetas en 👀 En revisión (2026-10-14) | Claude Code (con el conector de Trello y el de Figma) | Lectura del tablero y del repo, contraste de cada tarjeta con sus "Listo cuando", redacción de 3 comentarios de resolución y 3 de revisión, creación de una tarjeta para FGR, movimiento de 6 tarjetas, e intento de abrir el FigJam de los User Flow (sin acceso) | **MDV** eligió el alcance (informe, comentarios y mover tarjetas) y decidió cerrar Encuestas con el análisis marcado como preliminar y cerrar la documentación del prototipo; el asistente propuso, no decidió. Los comentarios sobre las tarjetas de FM se publicaron con la cuenta de MDV |
| Sugerencia de stack del MVP (2026-10-21) | Claude Code + un selector de stack hecho con Claude (artifact externo al proyecto) | Propuesta de 4 alternativas de stack con sus tradeoffs, a partir del prototipo, las decisiones 0005 y 0006 y el selector; cargada en P-10, marcando qué viene del repo, qué del selector y qué del conocimiento general del asistente | **MDV** hizo la pregunta y pidió cargarla. **No es decisión**: falta relevar qué sabe usar el equipo y hacer el 6 Sombreros |
| Wireframes low-fi (2026-10-21) | Claude Code (con el conector de Figma) | Lectura del frontend web del prototipo, lista de 9 pantallas y dibujo en Figma de la primera (Panel de control). El estilo low-fi (cajas, rayas grises, X) y el orden de las pantallas son elección del asistente | **MDV** definió los criterios (low-fi de concepto, desktop 1440, sin responsive, una pantalla a la vez) y pidió bajar la fidelidad de la primera versión. **El equipo todavía no revisó** los wireframes |
| Prototipo — backend | Claude | Código del backend a partir del documento de requerimientos y un notebook de Kaggle citado | FGR es responsable de entender, ejecutar y poder defender el código |
| Prototipo — frontend | Codex | Código del frontend, ajustado al backend | FGR es responsable de entender, ejecutar y poder defender el código |
| Prototipo — ajuste de identidad visual y usabilidad del frontend web y móvil (2026-10-18) | Claude Code | Reescritura de la hoja de estilos con los tokens de la paleta, sistema único de botones, reorganización de Administración, corrección de la grilla de permisos, rediseño visual de la app móvil y revisión con las heurísticas de Nielsen; capturas con Chrome headless contra una API simulada | **FGR** definió el pedido (identidad, botones del mismo tamaño, Nielsen, grilla de roles). La lógica de la app no se cambió. FGR es responsable de revisar y poder defender el código. La app móvil no se probó en dispositivo |
| Prototipo — esquema de privilegios de usuario (PR #3, 2026-10-21) | Claude Code | Código del commit `435ce61`: roles Administrador y Organización Admin, selector de organizaciones según el usuario, rol en la barra de sesión, reporte de organizaciones en Excel y txt, historial de auditoría y 4 tests. En otra sesión, Claude Code relevó el diff, corrió los tests y documentó los cambios en `prototipo.md` y en la tarjeta de Trello | **FGR** escribió los requerimientos (a a g) en la tarjeta y mergeó el PR. FGR es responsable de revisar y poder defender el código |
| Decisión del stack del prototipo en un solo deploy (2026-10-21) | Claude Code (con el conector de Trello) | Relevamiento del código del prototipo (dependencias de PostgreSQL), comparación MongoDB vs. PostgreSQL, redacción de la descripción de la tarjeta, de la decisión 0007 y del borrador del 6 Sombreros (negro, amarillo y verde como propuesta) | **FGR** decidió mantener PostgreSQL y fijó el vencimiento; el asistente propuso, no decidió. El sombrero rojo lo escribe el equipo y **MDV y ML todavía no validaron** la decisión |
| Documento de requerimientos funcionales del MVP | — | Escrito por Mateo Lewinzon (ML) | Sin asistencia de IA declarada por el autor a la fecha de este documento |

## Procesos de validación

Este repositorio tiene reglas propias, escritas desde el inicio del proyecto (`CLAUDE.md`), que
funcionan como control de validación sobre el uso de IA:

- **"No deducir nada."** Ninguna afirmación fáctica se completa sin fuente. Lo que no se sabe se
  marca explícitamente como falta (⬜), nunca se rellena "porque tendría sentido".
- **El sombrero rojo (emociones) del método de 6 Sombreros lo escribe siempre el equipo**, nunca
  la IA — está documentado así en cada análisis (`docs/05-producto/analisis/`).
- **Cada documento generado se revisó y corrigió en vivo** antes de darlo por cerrado. Ejemplos con
  fecha: la cadena de 5 Por Qué del 14/9 fue corregida punto por punto por FM; el benchmarking del
  10/9 corrigió la propia hipótesis del equipo cuando la evidencia no la sostenía; la identidad
  visual se sometió a votación del equipo antes de cerrarse.
- **Las decisiones quedan registradas, numeradas y no se editan retroactivamente**
  (`docs/03-decisiones/`) — para cambiar una, se escribe una nueva que la supersede.
- **Todos los commits de git quedan firmados** con la autoría real de quien los hizo y, cuando hubo
  asistencia de Claude Code, con un trailer `Co-Authored-By` — el historial de git es evidencia
  auditable de cuándo y en qué se usó.

### ⬜ Pendiente de completar

- Documentar con más detalle **qué partes del código del prototipo entiende y puede defender cada
  integrante** — señalado como falta en [`prototipo.md`](../05-producto/prototipo.md) desde el
  2/9 y todavía sin resolver.
- Confirmar con ML si usó alguna herramienta de IA para el documento de requerimientos, para
  completar la fila correspondiente de esta tabla.

## Responsabilidad sobre el contenido

El equipo de FraudLens declara que:

- Asume la **responsabilidad académica plena** sobre todo el contenido presentado, generado con o
  sin asistencia de IA.
- El uso de IA fue de **apoyo instrumental y de producción asistida con supervisión humana** en
  todos los casos — no reemplazó las decisiones de fondo, que fueron tomadas y validadas por el
  equipo.
- Cada integrante puede explicar y defender lo que su parte del proyecto muestra.
