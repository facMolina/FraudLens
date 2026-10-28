# Retrospectivas

Plantilla para documentar cada retrospectiva y registro de quién la facilitó.
Responde a la tarjeta [Armar la plantilla de Retrospectiva y el registro de facilitadores](https://trello.com/c/5VB8UDLb).

## Qué dice la cátedra y qué no

**Fuente:** [Clase 09](../01-clases/clase-09-agile-scrum-kanban.md) (sección "NOSOTROS") y [glosario](../00-proyecto/glosario.md#retrospectiva--sprint-retrospective--clase-1-y-clase-09).

| Regla | Fuente |
|---|---|
| Se hace **al final de cada sprint** | Docente (Clase 09) |
| El **facilitador no es siempre el mismo**: uno distinto cada vez | Docente (Clase 09) |
| **Se documenta en el Trello** | Docente (Clase 09) |
| En Scrum la facilita uno del equipo y cubre aspectos a mejorar, reconocimientos, etc. | Docente (definición, según la tarjeta) |

> ⬜ **El Taller de Retrospectivas se está dando el 14/10 (hoy), no el 7/10** *(MDV, 2026-10-14; el
> cronograma decía 7/10 y no está confirmado por escrito)*. No hay deck de esa clase en
> [`docs/01-clases/material/`](../01-clases/material/README.md), así que **esta plantilla no incorpora
> nada del taller**. **Lo que explique el docente reemplaza lo que dice acá.** Después de la clase,
> cargar el deck y revisar el formato y los bloques de abajo.

> 📌 **Origen del contenido.** Solo las 3 reglas de la tabla de arriba vienen de la cátedra. **El resto
> (bloques de la plantilla, tiempos, escritura en silencio, máximo 3 acciones, la rotación sin
> repetir) es conocimiento general de retrospectivas ágiles y sugerencias de Claude Code: no lo dijo
> el docente ni lo decidió el equipo.** Hasta que el equipo lo apruebe, es borrador. Los "hechos para
> recordar" sí salen del repo y de Trello.

## Plantilla

Copiar el bloque, completarlo y pegarlo en Trello (ver [dónde se documenta](#dónde-se-documenta)).
Los bloques "qué salió bien / qué mejorar / acciones" son la **propuesta** de formato; el único
contenido que pide la cátedra son los aspectos a mejorar y los reconocimientos.

```markdown
# Retrospectiva N — [fecha AAAA-MM-DD]

**Sprint / período que cubre:** ⬜
**Facilitador/a:** ⬜ (alias)
**Participaron:** ⬜ MDV · FGR · ML · FM (marcar quiénes estuvieron)

## Reconocimientos
- ⬜ (a quién y por qué)

## Qué salió bien
- ⬜

## Aspectos a mejorar
- ⬜

## Acciones para el próximo sprint
| Acción | Responsable | Para cuándo |
|---|---|---|
| ⬜ | ⬜ | ⬜ |

## Seguimiento de la retro anterior
- ⬜ ¿Se cumplieron las acciones de la retro anterior? (sí / no / parcial, y por qué)
```

**Reglas de uso**

- Habla **de cómo trabajó el equipo**, no de qué construyó (eso es la Sprint Review).
- Las acciones llevan **responsable y fecha**; sin eso, no se cuentan.
- Se escribe lo que el equipo dijo. **No se completa con lo que "tendría sentido"** (regla 7 del proyecto).

## Guion de la Retro 1 (14/10) — facilita MDV

> 📌 **Propuesta de Claude Code, sin aprobar.** Los tiempos son una estimación: ⬜ no sé cuánto
> tiempo da la cátedra para la retro en clase. Ajustar al tiempo real.

**Período que cubre:** ⬜ confirmar. FM dijo el 7/10 que el Sprint 1 arrancó *"la semana pasada"* y que
*"no es muy estricto"* ([P-31](../00-proyecto/preguntas-abiertas.md#p-31)), así que no hay fecha exacta.
Sugerencia: hablar de **todo lo trabajado desde el 1° Parcial (16/9)**.

| Min | Bloque | Qué hace el facilitador |
|---|---|---|
| 2 | **Apertura** | Dice el objetivo: hablar de **cómo trabajamos**, no de qué construimos. Regla: se habla de hechos y del trabajo, no de personas |
| 3 | **Escritura en silencio** | Cada uno anota solo, sin hablar, 1–2 ideas por bloque (reconocimientos · salió bien · mejorar). Así las 4 voces quedan registradas y nadie copia al primero que habla |
| 5 | **Reconocimientos** | Una ronda: cada uno reconoce a alguien por algo concreto |
| 5 | **Qué salió bien** | Una ronda. El facilitador anota |
| 8 | **Aspectos a mejorar** | Una ronda. Se agrupan los parecidos. Se pide **un hecho** por cada punto, no una opinión |
| 5 | **Acciones** | Se eligen **máximo 3**, cada una con responsable y fecha. Si no tiene los dos, no entra |
| 2 | **Cierre** | El facilitador lee las acciones en voz alta y avisa dónde queda documentado |

**Después de la retro:** MDV copia la plantilla en una tarjeta nueva de Trello ("Retrospectiva 1"),
la completa con lo que se dijo y la mueve a ✅ Hecho. También va una línea en la bitácora del día.

### Hechos para recordar *(sacados del repo, no son conclusiones)*

Sirven para que la charla parta de cosas concretas. **Qué salió bien o mal lo dice el equipo.**

- 1° Parcial (16/9): **nota 9 para los 4** *(informado por FM)*.
- Research: entrevistas a Perfil A y B hechas; encuesta del Perfil C con **28 respuestas**.
- Datos: se decidieron **3 datasets** ([0006](../03-decisiones/0006-tres-datasets-para-el-modelo.md)).
- Clases 9 y 10 cargadas; se recortó el alcance del MVP ([0005](../03-decisiones/0005-recorte-alcance-mvp.md)).
- Jev: investigado, pero la prueba **no se pudo hacer** por falta de saldo.
- Tablero hoy: **3 tarjetas vencen hoy sin dueño** (Product Backlog, Sprint Review 1, plantilla de
  Retro) y **3 tarjetas con vencimiento 7/10 siguen "En curso"** (User Story Mapping, User Flow,
  herramienta del backlog).
- Puntos de partida para preguntar, no para acusar: *¿por qué las tarjetas llegan al día de la
  entrega sin dueño?* · *¿cómo nos enteramos de lo que hace cada uno?* · *¿el 1° Parcial salió bien
  por cómo nos organizamos o a pesar de eso?*

## Dónde se documenta

La cátedra exige "en el Trello" pero no dice en qué parte. **Propuesta (sin aprobar):**

| Opción | Se gana | Se paga |
|---|---|---|
| **Una tarjeta por retro** en la lista ✅ Hecho (título "Retrospectiva N"), con la plantilla en la descripción | Fácil de encontrar y mostrar al docente; queda con fecha | Suma tarjetas al tablero; hay que moverlas a mano |
| **Un comentario por retro** en una única tarjeta "Retrospectivas" | Tablero limpio, todo junto en un lugar | Los comentarios largos se leen peor; más difícil de ordenar y citar |

**Recomendación:** una tarjeta por retro. Una retro es una instancia evaluable ("el docente evalúa
retros", Clase 09) y conviene que cada una sea visible por sí misma.

⬜ **El equipo decide.** Además, cada retro se registra también en la
[bitácora](../../bitacora/README.md) del día.

## Registro de facilitadores

**Regla:** uno distinto cada vez. Con 4 integrantes, la rotación completa es de 4 retros.

| Retro | Fecha | Facilitador/a | Tarjeta de Trello |
|---|---|---|---|
| 1 | 14/10 | **MDV** *(se ofreció él, 2026-10-14)* | ⬜ |
| 2 | ⬜ | ⬜ | ⬜ |
| 3 | 4/11 | ⬜ | ⬜ |
| Big Retro | ⬜ | ⬜ | ⬜ |

**Qué falta confirmar:**

- ✅ **La Retro 1 (14/10) la facilita MDV**, porque se ofreció *(MDV, 2026-10-14)*. No hace falta una
  votación: la regla de la cátedra pide rotar, y alguien tiene que empezar. **Como MDV es quien armó
  la plantilla, no repite en la Retro 3**: facilitan los otros tres antes de que vuelva a tocarle.
  Quién facilita la Retro 3 y la Big Retro queda ⬜ para el equipo.
- ⬜ **La Retro 2 no figura en el cronograma** oficial (solo la 1 el 14/10 y la 3 el 4/11).
  Es una duda abierta que el equipo decidió **no perseguir**: ver [P-19](../00-proyecto/preguntas-abiertas.md#p-19).
  Hasta que se aclare, este registro deja la fila vacía.
- ⬜ La **Big Retro** del cierre del cuatrimestre la menciona el glosario; no tiene fecha en el cronograma.

> 🔑 Para mantener la rotación honesta, cada vez que se facilita se anota acá **antes** de la retro
> siguiente, y el que facilitó no repite hasta que pasen los otros tres.
