# 2026-09-30 — Investigación de TypeSafe AI (Jev) y arquitectura propuesta

| | |
|---|---|
| **Tipo** | Investigación (con asistencia de Claude Code) |
| **Duración** | — |
| **Participantes** | Mateo Diaz Valdez (MDV) |

## Por qué esta sesión

MDV quiso usar TypeSafe AI en el proyecto y pidió un `.md` con la investigación desde fuentes
oficiales y la arquitectura diagramada con Mermaid. Es el modelo **Jev** de la tarjeta
["Evaluar modelo de IA Jev"](https://trello.com/c/yOSmUHOx).

## Qué se hizo

- Investigación en la documentación oficial (docs.typesafe.ai, typesafe.ai, SDK de Python) y una
  fuente secundaria (TrueFoundry), **separando en el documento lo oficial de lo secundario**.
- Documento [`typesafe-jev.md`](../docs/05-producto/typesafe-jev.md), **marcado BORRADOR**: qué es
  Jev, patrones, límites, arquitectura propuesta (2 diagramas Mermaid), contrato de la API y plan
  de validación.

- **6 Sombreros (borrador)** en [`analisis/6-sombreros-jev.md`](../docs/05-producto/analisis/6-sombreros-jev.md):
  blanco con hechos y faltantes; negro, amarillo y verde como borrador de Claude Code; **rojo vacío
  para el equipo**; azul sin decidir.
- **Preguntas P-25, P-26 y P-27** en `preguntas-abiertas.md` (acceso, privacidad, contexto textual)
  y nota en P-10 sobre los SDK oficiales.
- **Trello:** tarjeta existente "Evaluar modelo de IA Jev" actualizada (se conservó el texto original
  y se sumó el research); 3 tarjetas nuevas — [Conseguir acceso a la API](https://trello.com/c/mT2FcXyY)
  (Esta semana, MDV), [Completar el 6 Sombreros](https://trello.com/c/dNrC2EWY) y
  [Validar Jev con el dataset 3](https://trello.com/c/EYxcS7tu) (Backlog, esta última sin dueño);
  comentario de enlace en "Modelos de IA a utilizar".
- Decisiones de MDV: sin etiquetas de categoría (P-22 sin aprobar; la categoría quedó escrita en la
  descripción), y publicar todo junto en un solo commit.

## Hallazgos principales

- Jev **no es un clasificador tabular**: recibe texto + un esquema y devuelve respuestas tipadas con
  confianza. No reemplaza al modelo entrenado con los datasets de la decisión 0006; podría aportar
  señales y una "puerta de confianza" hacia *revisar*.
- **Acceso por lista de espera** (fuente secundaria) — no sabemos si tenemos clave.
- **Calibración sin verificar por terceros** y **privacidad/retención sin verificar** (el Trust
  Center no se pudo leer). Para un cliente banco/fintech es una objeción a preparar.

## Qué quedó abierto

- Confirmar acceso a la API y quién se anota.
- 6 Sombreros de la decisión de usar Jev (el sombrero rojo lo escribe el equipo).
- Stack (P-10) y repo del MVP (P-05) siguen sin definir; **no se escribió código**.
- Revisión del equipo: nada del documento es decisión.

## Archivos

- [`docs/05-producto/typesafe-jev.md`](../docs/05-producto/typesafe-jev.md) — nuevo
- [`docs/05-producto/README.md`](../docs/05-producto/README.md) — índice actualizado
- [`docs/05-producto/analisis/6-sombreros-jev.md`](../docs/05-producto/analisis/6-sombreros-jev.md) — nuevo
- [`docs/05-producto/analisis/README.md`](../docs/05-producto/analisis/README.md) — índice actualizado
- [`docs/00-proyecto/preguntas-abiertas.md`](../docs/00-proyecto/preguntas-abiertas.md) — P-25 a P-27 y nota en P-10
