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

Docente: **Lic. Daniel Britez**.
Tablero: https://trello.com/b/iUaTi33p/fraudlens-analizador-probabilidad-de-fraude

**Quién hizo qué** (importa para no atribuir mal):
- **ML** propuso el tema y escribió los requerimientos funcionales del MVP.
- **FGR** creó el tablero de Trello y armó el prototipo (backend con Claude, frontend con Codex).
- **MDV** cargó la planilla de relevamiento inicial del docente.
- **FM** armó este repositorio.

## ⚠️ No corras `/init` en este repo

Este `CLAUDE.md` está escrito a mano con las reglas del proyecto. `/init` lo pisaría con un resumen
automático de peor calidad. Si el usuario lo pide, avisale antes de sobrescribir.

## Cómo arranca una sesión de trabajo

**Regla del equipo: toda sesión arranca desde un ticket de Trello.**

Cuando alguien abre una sesión, antes de escribir código o documentos:

1. **Verificá que el conector de Trello esté activo.** Si no lo está, **frená y pedíselo**: sin
   tablero no se puede trabajar en este proyecto. Instrucciones en
   `docs/04-metodologia/trello.md`. Es requisito, no una comodidad — el tablero es ítem de
   evaluación de la materia.
2. Preguntá **quién es** (alias: MDV / FGR / ML / FM), si no lo dijo.
3. **Listale los tickets** del tablero agrupados por lista, marcando cuáles están sin dueño y
   cuáles vencen primero.
4. Si todavía no tomó un ticket, ayudalo a elegir uno y **recordale que se lo asigne en Trello**
   (el conector no puede asignar miembros: lo tiene que hacer la persona con "Unirme").
5. Leé `docs/00-proyecto/cronograma.md` para saber qué se viene y con qué urgencia.
6. Revisá `docs/00-proyecto/preguntas-abiertas.md` — puede que lo que va a hacer dependa de algo
   sin definir.
7. Decile qué entendiste y qué te falta saber **antes** de empezar.

Al cerrar la sesión, recordale el checklist: `.md` actualizado · bitácora · historial de aportes ·
**comentario de resolución en la tarjeta de Trello** · tarjeta movida · commit con **su propio
usuario de Git**.

> 🔴 **Ningún ticket pasa a ✅ Hecho sin comentario de resolución en Trello** — qué se decidió, qué
> se descartó y por qué. No alcanza con documentarlo en el repo: va en **los dos lugares**.
> Plantilla del comentario en `docs/04-metodologia/convencion-de-tickets.md`.
>
> Cuando el usuario cierre un ticket, **escribile vos el comentario** con `trelloWriteCard`
> (`action: "add_comment"`) a partir de lo que se hizo en la sesión.

> ⚠️ **Limitación conocida:** el conector de Trello **no puede asignar miembros a tarjetas**.
> Cuando haya un responsable, escribilo en la descripción de la tarjeta y avisale a la persona que
> tiene que darle "Unirme" a mano.

## Dónde está cada cosa

| Necesito… | Voy a… |
|---|---|
| Saber qué es el proyecto | `docs/00-proyecto/ficha-proyecto.md` |
| **Fechas, parciales, entregas** | `docs/00-proyecto/cronograma.md` ← el deck de la Clase 1 NO sirve para esto |
| Una definición | `docs/00-proyecto/glosario.md` |
| Saber qué falta definir | `docs/00-proyecto/preguntas-abiertas.md` |
| Ver qué se dio en una clase | `docs/01-clases/` (nota trabajada) · `docs/01-clases/material/` (deck crudo) |
| Saber qué se entrega y cuándo | `docs/02-entregables/README.md` |
| Saber por qué se decidió algo | `docs/03-decisiones/` |
| Saber cómo trabajamos | `docs/04-metodologia/flujo-de-trabajo.md` |
| **Crear o cerrar un ticket** | `docs/04-metodologia/convencion-de-tickets.md` |
| **Analizar una decisión** | `docs/04-metodologia/seis-sombreros.md` (consigna del docente) |
| Ver qué hizo cada uno | `registro/historial-aportes.md` + `git log --author` |
| El prototipo que ya existe | `docs/05-producto/prototipo.md` |
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

9. **Toda decisión se analiza con los 6 Sombreros.** Es consigna del docente
   (`docs/04-metodologia/seis-sombreros.md`, decisión 0003). Aplica a decisiones y entregables de la
   materia, **no** a tareas operativas. Criterio: *"¿esto se puede hacer mal de más de una manera?"*.

   Al aplicarlo:
   - El sombrero **blanco** sólo usa hechos que aportó el equipo. **Nunca rellenes datos que no
     tenés** — listalos como faltantes. Es la regla 7 aplicada a este método.
   - El sombrero **rojo** lo escribe **el equipo**, no vos. Podés dejar un borrador marcado como tal.
   - El análisis va en `docs/05-producto/analisis/6-sombreros-<tema>.md` y se linkea desde la
     tarjeta de Trello.

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

- **Cursada:** miércoles 18:45 a 22:15. **1° Parcial 16/9 · 2° Parcial 11/11.**
  Hay una **clase remota sincrónica el sábado 5/9 de 9 a 13 hs**.
- El docente exige **datos reales** para el User Research. No se puede inventar evidencia.
  *(Las "400 respuestas" que pidió la Clase 4 son una guía, no una obligación — pero el número que
  elijamos hay que justificarlo.)*
- **Honestidad académica:** el cronograma advierte que se sanciona. El prototipo parte de un
  notebook público de Kaggle y de código generado con IA: eso está bien **siempre que esté citado**
  y que el equipo pueda explicar lo que muestra. Ver `docs/05-producto/prototipo.md`.
- Los **tableros de trabajo (Trello/Jira) son un ítem de evaluación**.
- El **MVP tiene que ser chico**. El error clásico es irse de alcance. Cuando el equipo agregue
  funcionalidades, contrastar contra la lista de "NO MVP" en `docs/05-producto/problema.md`.
- Las **Sprint Reviews rotan de presentador** semana a semana.
- El documento final es la **sumatoria de pequeñas tareas iteradas** — por eso este repo existe.

## Etiquetas de los tickets

Cada ticket lleva **una** etiqueta de categoría: 🟣 Negocio · 🟢 Research · 🔵 Diseño ·
🟡 Datos & Modelo · 🟠 Código · 🔴 Entrega · ⚫ Gestión.
La **prioridad no va en etiquetas**: se lee de la lista y de la fecha de vencimiento.

Detalle y formato completo en `docs/04-metodologia/convencion-de-tickets.md`.

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
