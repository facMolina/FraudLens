# Instrucciones para Claude — Proyecto FraudLens

## Qué es este repositorio

**Centro de cómputos** del Trabajo Integrador Final (TIF/SIP) de la materia *Seminario de Gestión
Tecnológica* — UADE, Licenciatura en Sistemas, 2C 2026.

**No es el producto final.** Es el registro de todo lo que el equipo define, hace y decide.
El código del MVP vive en otro lado (ver [P-05](docs/00-proyecto/preguntas-abiertas.md#p-05)).

## Idioma

**Toda la documentación se escribe en español**, en registro rioplatense (voseo en instrucciones
al equipo: *"cargá"*, *"revisá"*). Los términos técnicos y de la materia se mantienen como los usa
el docente (MVP, Sprint Review, User Research, BMC, P&L, OKR, KPI, The Pitch).

## El equipo

| Integrante | Legajo | Alias |
|---|---|---|
| Diaz Valdez, Mateo | 1192969 | MDV |
| Guerrero Rojas, Francisco Daniel | 1042529 | FGR |
| Lewinzon, Mateo | 1151641 | ML |
| Molina, Facundo Roman | 1115862 | FM |

Docente: **Daniel Britez**. Tablero: https://trello.com/b/iUaTi33p/fraudlens-analizador-probabilidad-de-fraude

## Dónde está cada cosa

| Necesito… | Voy a… |
|---|---|
| Saber qué es el proyecto | `docs/00-proyecto/ficha-proyecto.md` |
| Una definición | `docs/00-proyecto/glosario.md` |
| Saber qué falta definir | `docs/00-proyecto/preguntas-abiertas.md` |
| Ver qué se dio en una clase | `docs/01-clases/` (nota trabajada) · `docs/01-clases/material/` (deck crudo) |
| Saber qué se entrega y cuándo | `docs/02-entregables/README.md` |
| Saber por qué se decidió algo | `docs/03-decisiones/` |
| Saber cómo trabajamos | `docs/04-metodologia/flujo-de-trabajo.md` |
| Ver qué hizo cada uno | `registro/historial-aportes.md` + `git log --author` |
| Ver qué se hizo un día | `bitacora/` |

## Reglas al trabajar en este repo

1. **Todo lo definido queda en un `.md`.** Si el usuario define algo en la conversación, escribilo
   en el archivo que corresponde antes de terminar. No dejes definiciones sólo en el chat.

2. **Cada sesión de trabajo deja rastro.** Crear o actualizar el archivo del día en `bitacora/`
   y sumar la fila correspondiente en `registro/historial-aportes.md`.

3. **Las decisiones se numeran y no se editan.** Nueva decisión en `docs/03-decisiones/` con el
   número siguiente. Para cambiar una vieja, se escribe una que la supersede.

4. **Las dudas van a `preguntas-abiertas.md`** con ID, prioridad y destinatario. Cuando se responde,
   se marca resuelta con la respuesta escrita.

5. **No inventar información de la materia.** Si algo no está en el material de clase ni lo dijo el
   equipo, se marca `⬜ A definir` o se carga como pregunta abierta. Es preferible un hueco
   explícito a un dato inventado en un documento que después se entrega.

6. **Distinguir fuentes.** Marcar siempre si algo viene del docente, de la planilla, de una decisión
   del equipo o de una sugerencia tuya. En un trabajo académico esa distinción importa.

7. **No deducir.** Este es el punto más importante para este equipo. Si falta un dato, se pregunta;
   no se completa con lo que "tendría sentido". Un documento con huecos explícitos es útil; uno con
   datos inventados es un riesgo en una entrega evaluada.

8. **Borrador ≠ definición.** Un documento que un integrante pasó "para revisar" se guarda marcado
   como borrador y no se usa como fuente de verdad hasta que el equipo lo apruebe.

## Cuando llega una clase nueva

Es el flujo más frecuente de este repositorio.

### 🚨 REGLA DE FORMATO — hacer cumplir siempre

**El material de clase se carga en Markdown, NUNCA en PDF.**

Si el usuario intenta pasar material en PDF (o PPT), **no lo aceptes**: pedile que lo convierta
primero en 👉 **https://cloudconvert.com/pdf-to-md** y que suba el `.md` resultante.

Motivo: los PDFs son pesados, no tienen diff útil en Git, y su texto muchas veces no se puede
extraer. `*.pdf`, `*.pptx` y `*.xlsx` están en `.gitignore`.

### Pasos

1. Guardar el `.md` crudo en `docs/01-clases/material/` como `clase-NN-tema.md` y sumarlo al índice
   de `docs/01-clases/material/README.md`.
2. Copiar `docs/01-clases/_plantilla-clase.md` → `docs/01-clases/clase-NN-tema.md`.
3. Completar resumen y conceptos, **con las definiciones tal como las dio el docente**.
4. **Completar "Aplicación a FraudLens"** — sección obligatoria. Una clase sin bajada al proyecto
   no sirve. Acá es donde aportás valor real.
5. Sumar los términos nuevos al glosario, marcados ✅ con la clase de origen.
6. Cargar las tareas de "para la próxima" y avisar que hay que pasarlas a Trello.
7. Agregar la fila al índice en `docs/01-clases/README.md`.
8. Revisar `preguntas-abiertas.md`: ¿la clase respondió alguna? ¿abrió alguna nueva?
9. Actualizar bitácora e historial de aportes.

> ⚠️ La conversión de PDF a Markdown de estos decks es **imperfecta**: son muy visuales, y el
> texto llega desordenado y con palabras mezcladas. **No completes a ojo lo que no se entiende.**
> Marcá el hueco y preguntá al equipo o al docente.

## Contexto de la materia que conviene tener presente

- El docente exige **datos reales** para el User Research. No se puede inventar evidencia.
- Los **tableros de trabajo (Trello/Jira) son un ítem de evaluación**.
- El **MVP tiene que ser chico**. El error clásico es irse de alcance. Cuando el equipo agregue
  funcionalidades, contrastar contra la lista de "NO MVP" en `docs/05-producto/problema.md`.
- Las **Sprint Reviews rotan de presentador** semana a semana.
- El documento final es la **sumatoria de pequeñas tareas iteradas** — por eso este repo existe.

## Convención de commits

`<tipo>: <qué cambió>` — tipos: `clase`, `docs`, `decision`, `bitacora`, `chore`.

## Graphify

El repositorio usa [Graphify](https://github.com/Graphify-Labs/graphify) como capa de lectura
opcional (decisión 0002). Si `graphify-out/graph.json` existe, consultá el grafo antes de leer
archivos crudos. Si no existe, trabajá normalmente — **el repo se lee perfectamente sin Graphify**.

```bash
graphify . --update
graphify query "..."
```

Ver `docs/04-metodologia/graphify.md`.
