# Graphify

[Graphify](https://github.com/Graphify-Labs/graphify) convierte el repositorio en un **grafo de
conocimiento consultable**: en vez de buscar texto archivo por archivo, se consultan **relaciones**
entre conceptos.

Decisión asociada: [0002](../03-decisiones/0002-graphify-como-capa-de-lectura.md).

> **Es opcional.** El repositorio se lee perfectamente sin Graphify. Esto es una capa de comodidad,
> no un requisito para trabajar.

## Instalación

```bash
uv tool install graphifyy      # recomendado (aislado)
# alternativas:
# pipx install graphifyy
# pip install graphifyy
```

Registrarlo con el asistente:

```bash
graphify install                # detecta el asistente
graphify claude install         # específico para Claude Code
```

`graphify claude install` escribe instrucciones persistentes (en `CLAUDE.md`) e instala hooks para
que el asistente consulte el grafo antes de leer archivos crudos.

## Construir el grafo

> ⚠️ **Importante para este repositorio.** Graphify parsea **código** en forma local (tree-sitter,
> sin LLM), pero la **documentación Markdown necesita un modelo** para la extracción semántica.
> Como este repo es 100% documentación, correr `graphify .` desde la terminal falla con
> `error: no LLM API key found`.
>
> **La forma de usarlo acá es desde el asistente**, con el comando `/graphify .` dentro de
> Claude Code: en ese caso usa el modelo del propio asistente y no hace falta ninguna API key.

**Desde el asistente (recomendado):**

```
/graphify .                     # construir desde cero
/graphify . --update            # re-extraer sólo lo que cambió
/graphify . --mode deep         # extracción de relaciones más agresiva
```

**Desde la terminal** (requiere `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY` u otra):

```bash
cd FraudLens
export ANTHROPIC_API_KEY=...
graphify .                      # construir desde cero
graphify . --update             # re-extraer sólo lo que cambió
graphify . --no-viz             # sin HTML, sólo JSON + reporte
```

Genera `graphify-out/`:

| Archivo | Qué es |
|---|---|
| `graph.html` | Visualización interactiva — abrir en el navegador, clickear nodos, filtrar, buscar |
| `GRAPH_REPORT.md` | Conceptos clave, conexiones inesperadas, consultas sugeridas |
| `graph.json` | Grafo completo, para consultar sin releer archivos |

## Consultar

```bash
graphify query "¿qué relaciona el MVP con las entregas?"
graphify path "User Research" "Primera Entrega"
graphify explain "MVP"
```

## Mantener el grafo al día

```bash
graphify hook install           # reconstruye solo en commit y cambio de rama
graphify update .               # después de un git pull
```

Atajo útil:

```bash
git config --global alias.gpull '!git pull && graphify update .'
```

## Qué se ignora

[`.graphifyignore`](../../.graphifyignore), con la misma sintaxis de `.gitignore`. Graphify respeta
`.gitignore` automáticamente; los patrones de `.graphifyignore` se evalúan al final y ganan.

## Qué NO versionamos

`graphify-out/` está en `.gitignore`. El repositorio es chico y el grafo se reconstruye en segundos,
así que versionarlo sólo agregaría ruido a los diffs. Si el proyecto crece y reconstruirlo se vuelve
costoso, se revisa la decisión 0002.

## Privacidad

El parseo de código es **local** (tree-sitter, sin LLM, nada sale de la máquina). La documentación,
los PDFs y las imágenes sí usan el modelo del asistente. No hay telemetría.

> ⚠️ Tenerlo en cuenta si en algún momento incorporamos datos de transacciones reales al
> repositorio. **Los datos sensibles no van al repo** — ni al grafo.
