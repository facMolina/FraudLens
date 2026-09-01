# 0002 — Usar Graphify como capa de lectura del repositorio

| | |
|---|---|
| **Fecha** | 2026-09-01 |
| **Estado** | ✅ Aceptada |
| **Decidido por** | Facundo Molina (a validar con el equipo) |
| **Pregunta relacionada** | — |

## Contexto

El repositorio va a crecer: 4 clases o más de notas, decisiones numeradas, documentos de producto,
bitácoras semanales y el historial de aportes. Buscar información saltando entre archivos se vuelve
lento, y para un asistente de IA implica leer muchos archivos completos antes de responder.

[Graphify](https://github.com/Graphify-Labs/graphify) construye un **grafo de conocimiento** del
repositorio —código, documentación Markdown, PDFs, schemas— y permite consultarlo por relaciones en
vez de grepear archivo por archivo.

## Alternativas consideradas

| Opción | A favor | En contra |
|---|---|---|
| **Graphify** | Grafo consultable, visualización HTML, integración directa con Claude Code, parseo local vía tree-sitter | Herramienta joven, hay que reconstruir el grafo cuando el repo cambia |
| Sólo estructura de carpetas + índices | Cero dependencias | No escala bien cuando el repo crece |
| Buscador de GitHub | Ya está | Búsqueda por texto, no por relaciones |

## Decisión

Adoptamos **Graphify** como capa de lectura del repositorio, sin que sea obligatorio para trabajar.
El repositorio tiene que seguir siendo **perfectamente legible sin Graphify**.

## Por qué

- Optimiza la lectura del proyecto por parte del equipo y del asistente de IA.
- El parseo de código es **local** (tree-sitter, sin LLM, nada sale de la máquina); sólo la
  documentación y los PDFs usan el modelo del asistente.
- Se integra con Claude Code mediante `graphify claude install`, lo que hace que el asistente
  consulte el grafo antes de leer archivos crudos.

## Consecuencias

- Se agrega un [`.graphifyignore`](../../.graphifyignore) al repositorio.
- `graphify-out/` **no se versiona** por ahora: el repo es chico y el grafo se reconstruye en
  segundos. Si el proyecto crece y la reconstrucción se vuelve costosa, se revisa esta decisión.
- **Graphify es opcional para los integrantes.** Nadie queda bloqueado por no tenerlo instalado.
- Instrucciones en [`docs/04-metodologia/graphify.md`](../04-metodologia/graphify.md).
