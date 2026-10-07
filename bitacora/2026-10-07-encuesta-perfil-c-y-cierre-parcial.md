# 2026-10-07 — Respuestas de la encuesta del Perfil C y cierre del 1° Parcial

| | |
|---|---|
| **Tipo** | Research + gestión del tablero, con asistencia de Claude Code |
| **Duración** | — |
| **Participantes** | Facundo Molina (FM) |

## Qué se hizo

- **Se cargaron las 28 respuestas de la encuesta del Perfil C** (export que aportó FM) en
  [`encuesta-perfil-c-respuestas.md`](../docs/05-producto/encuesta-perfil-c-respuestas.md), **anonimizadas**: sin marca temporal por fila y con
  un nombre de club omitido en una respuesta. Es lo único que se tocó.
- **Primer análisis** en [`encuesta-perfil-c-analisis.md`](../docs/05-producto/encuesta-perfil-c-analisis.md): conteos por pregunta, cruces, temas de las
  respuestas abiertas (con la lista de respuestas de cada tema, para poder auditarlos) y los límites de los datos. **Sin validar por el equipo.**
- Se actualizaron [`user-research.md`](../docs/05-producto/user-research.md), [`usuarios.md`](../docs/05-producto/usuarios.md) (una nota, sin tocar la hipótesis)
  y [`docs/02-entregables/README.md`](../docs/02-entregables/README.md).
- **1° Parcial: nota 9 para los cuatro integrantes** (informado por FM). Se registró en entregables y en la guía del parcial, y se cerró la tarjeta en Trello.
- **FM tomó las 3 tarjetas urgentes** — [User Story Mapping](https://trello.com/c/mxSfKQw6), [User Flow](https://trello.com/c/ivQo0hEI) y
  [herramienta del backlog](https://trello.com/c/kceMBbCj) — y se escribió su nombre en la línea *Responsable* de cada una. FM ya les dio "Unirme"
  y **las tres pasaron a 🔨 En curso**.
- Se intentó leer el repo del prototipo de FGR (`fguerrero2/FraudLens-prototipo`): **la sesión no tiene acceso**. FM sí puede abrirlo con su cuenta.
  FM propuso usar Claude in Chrome, pero **en esta sesión no hay herramientas de Chrome disponibles**: no se pudo. Sigue pendiente (ver abajo).
- La tarjeta [Encuestas y entrevistas](https://trello.com/c/KPXsyG4O) pasó a **👀 En revisión**, con un comentario que dice qué tiene que revisar el equipo.
- Declaración de uso de IA actualizada (análisis de datos de la encuesta).

## Qué se definió

Nada se decidió. Lo que dicen los datos, **con n = 28, auto-selección y 22 de 28 con 18-34 años**:

- A la pregunta de qué situación genera más inconveniente: **19** *"que se apruebe una operación que no hice"*, **8** *"ambas por igual"*, **1** *"que rechacen una compra legítima"*.
- **11 de 28** sufrieron un rechazo legítimo y **10 de 28** un consumo no reconocido (**3** ambos).
- **21 de 28** dicen que la explicación al rechazo es poco clara o inexistente. ⬜ Falta ver las opciones reales del Form para leerlo bien.

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| Revisar el análisis de la encuesta, en especial el punto 5.1 (*"costo invisible" del falso positivo*) | Equipo | ⬜ |
| Decidir si se amplía la difusión (hay 28 de las 80-100 que propuso el plan, P-17) | Equipo | ⬜ |
| Cerrar la tarjeta [Encuestas y entrevistas](https://trello.com/c/KPXsyG4O) *(está en En revisión)* cuando el equipo revise el análisis | Equipo | ⬜ |

## Dudas que surgieron

- ¿Qué opciones tenía realmente la pregunta 8 del Form? (¿existía una opción de explicación clara?)
- ¿FraudLens llega al mensaje que recibe el usuario final, o solo al analista? *(Planteada en el análisis, punto 5.2; no se deduce.)*
- ~~¿El docente dio una devolución cualitativa del parcial, además de la nota?~~ → **No dio devolución** (FM, 2026-10-07).

## Archivos tocados

- Nuevos: `docs/05-producto/encuesta-perfil-c-respuestas.md` · `docs/05-producto/encuesta-perfil-c-analisis.md`
- Modificados: `user-research.md` · `usuarios.md` · `docs/02-entregables/README.md` · `guia-1er-parcial.md` · `declaracion-uso-ia.md` · `registro/historial-aportes.md`
- **Trello:** responsable escrito en 3 tarjetas; tarjeta del 1° Parcial cerrada con comentario de resolución. **No se movió ninguna otra tarjeta.**

---

## Tercera parte — relevamiento del Form y del repo del prototipo

Esta sesión no tiene Claude in Chrome ni acceso al repo de FGR. FM corrió un **prompt en otro chat de Claude que sí los tiene** y trajo el informe
(solo lectura, sin responder el Form, sin ejecutar nada). Quedó cargado en [`prototipo.md`](../docs/05-producto/prototipo.md) y en los documentos de la encuesta.

**Resolvió:**
- ✅ **Pregunta 8 del Form:** la opción *"Una explicación clara"* **sí existía** y **ningún** encuestado la marcó. Se quitó el hueco del análisis.
- ✅ Estructura completa del Form con todas las opciones y cuáles eran obligatorias (solo la 1 y la 2). El Form **no filtra** y **no tiene texto de consentimiento**.
- ✅ Título publicado del Form: *Encuesta sobre experiencias de fraude en bancos y fintech*. El que figuraba en el repo era el del diseño previo.

**Corrigió un error mío:** en `prototipo.md` había dejado escrito que el prototipo *"no tiene un modelo ni reglas funcionando detrás"*. **Es falso:** hay un backend con un
motor de reglas ponderadas y determinista, base de datos y 12 tests. **Lo que no hay es un modelo de ML.** También se corrigió la guía del parcial. ⚠️ **La
diapositiva 11 de la presentación en PDF del parcial** dice que es *"un prototipo de interfaz: todavía no tiene la lógica del modelo detrás"*: queda desactualizada
(ese PDF no está en el repo).

**Lo que el informe dejó a la vista, para hablar con FGR** (ninguno se dedujo):
- El prototipo **no usa los 3 datasets** de la decisión 0006 y el **notebook de Kaggle no está citado** con título ni link en su repo.
- **Ningún archivo menciona Claude ni Codex**; quién generó qué no se puede confirmar desde el repo.
- Implementa **CU-02 y CU-07 como funciones vivas** y **3 roles**, lo que la decisión 0005 recortó para el MVP.
- `node_modules` commiteado, claves de desarrollo en texto plano (también en `Frontend/src/api.js`) y contradicciones entre su README y el código (SQLite / PostgreSQL).

**Quedó abierto:**

| Tarea | Responsable | Para cuándo |
|---|---|---|
| Ejecutar el prototipo y sus 12 tests para confirmar lo que dice el código | MDV y FGR *(según FM; ver abajo)* | ⬜ |
| Citar bien el notebook de Kaggle y declarar el uso de IA en el repo de FGR; confirmar qué generó cada herramienta | FGR | ⬜ |
| Decidir si el MVP parte del código del prototipo o arranca de cero (P-05) | Equipo | ⬜ |
| Contrastar el total de respuestas del Form con las 28 del export (solo lo ve un editor) | FM | ⬜ |

---

## Cuarta parte — decisiones de FM

- **Presentación en PDF del parcial:** no se actualiza por cada cambio. **Se actualiza todo junto cuando se acerque el 2° Parcial (11/11).** Hasta entonces la diapositiva 11 queda desactualizada.
- **Quién ejecuta el prototipo y los tests:** *"están MDV y FGR. MDV está con lo de Jev para aplicar y FGR tiene la iniciativa del prototipo"* (FM). Se registra tal cual; **no es una asignación formal** de la tarea de ejecutar.
- **Tarjeta [Preguntar al profe: huecos del cronograma](https://trello.com/c/16leWNGS): desestimada** por FM y **archivada**. Las preguntas **siguen abiertas** en `preguntas-abiertas.md` (P-19, P-29, P-31). Ojo: [Armar el Sprint 1](https://trello.com/c/MPrYaqYT) quedó bloqueada por P-31 y
  [Preparar la Sprint Review 1](https://trello.com/c/65jEv8rn) depende de la misma pregunta, y **ya no hay un recordatorio con fecha para preguntarla**.
- **Preguntas para FGR** dejadas como comentario en la tarjeta [Documentar el prototipo de FGR](https://trello.com/c/DC1vH1F6), con mención a su usuario de Trello: 13 preguntas sobre autoría de IA, citas, modelo, datasets, alcance, estado del repo y ejecución.
