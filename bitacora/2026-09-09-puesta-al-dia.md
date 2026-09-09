# 2026-09-09 — Puesta al día: una semana después

| | |
|---|---|
| **Tipo** | Revisión de estado (con asistencia de Claude Code) |
| **Duración** | — |
| **Participantes** | Facundo Molina (FM) |

## Por qué esta sesión

Pasó una semana desde la última (2/9). En el medio se dio la **Clase 5 (2/9)**, la **clase remota
del sábado 5/9**, y hoy es la **Clase 6 (9/9)**. El repo y el tablero habían quedado escritos
"desde el 2/9" y decían cosas que ya no eran ciertas.

## Lo que hicieron los compañeros

**FGR cerró la tarjeta 3 (Insight + Definición)** y la commiteó con su propio usuario de Git
(`fguerrero2`) — primer commit de otro integrante en el repo, y evidencia real de participación
individual.

Escribió **3 reformulaciones "¿Cómo podríamos nosotros...?"**, una por perfil, en vez de una sola.
El criterio es correcto y vale registrarlo: elegir una sola habría adelantado la respuesta de
[P-07](../docs/00-proyecto/preguntas-abiertas.md#p-07) sin evidencia, que es justo el sesgo que el
sombrero rojo del análisis había nombrado. Las tres quedaron marcadas como **hipótesis
pre-research**. Ver [su bitácora](2026-09-02-reformulacion-problema.md).

FGR además **se asignó** la tarjeta de documentar el dataset, que sigue en Backlog.

## 🔴 El estado real de los entregables de la Clase 5

De los 6 entregables que vencían el 2/9:

| Entregable | Estado |
|---|---|
| 1. Los 3 perfiles de usuario | ✅ Hecho (FM) |
| 3. Insight + Definición | ✅ Hecho (FGR) |
| **2. Plan de research** | 🔴 **Sin arrancar, sin dueño** |
| **4. User Persona ×3** | 🔴 **Sin arrancar, sin dueño** |
| **5. Mapa de Empatía ×3** | 🔴 **Sin arrancar, sin dueño** |
| **6. Problem Statement** | 🔴 **Sin arrancar, sin dueño** |

**El User Research sigue en cero.** `docs/05-producto/user-research.md` no existe. 0 encuestas,
0 entrevistas.

### Los dos relojes que corren

1. **1° Parcial el 16/9** — la semana que viene. El docente exige datos reales.
2. **La ventana de ML vence.** El 2/9 confirmó acceso a analistas de fraude *"en las próximas dos
   semanas"*. Esa ventana se cierra alrededor del **16/9**. Si no se usa, el perfil A cae al plan B
   (proxy) y se pierde el activo más valioso del research.

### Una consecuencia de orden que conviene mirar

La clase del 5/9 fue de **Ideación**, que normalmente parte de un Problem Statement cerrado. Como
el Problem Statement no se hizo, **se ideó sobre un problema todavía abierto**. No es fatal, pero
si el research corrige el problema, lo ideado el 5/9 puede quedar desalineado.

## Qué se actualizó

### Tablero de Trello

- Tarjetas **7 y 8** (preguntas y temas de la clase del 2/9) → **✅ Hecho**, con el balance de qué
  se resolvió y qué no.
- Tarjeta de la **clase remota del 5/9** → cambió de propósito: ya no es "preparar la clase" sino
  **cargarla al repo**. Movida a 🎯 Esta semana.
- **Clase 6 (hoy)** y **1° Parcial (16/9)** → movidas de Backlog a 🎯 Esta semana.
- Las **4 tarjetas vencidas** (2, 4, 5, 6) → comentario de estado en cada una, con qué las bloquea
  y por qué urgen.

### Repo

- [`docs/01-clases/README.md`](../docs/01-clases/README.md) — decía *"Clase 5: es la próxima"*.
  Ahora lista 2/9, 5/9 y 9/9 con la deuda de carga marcada.
- [`docs/02-entregables/pendientes-clase-05.md`](../docs/02-entregables/pendientes-clase-05.md) —
  decía que los tickets estaban sin cargar y la clase sin dar. Ahora dice qué se entregó y qué no.
- [`preguntas-abiertas.md` P-12](../docs/00-proyecto/preguntas-abiertas.md#p-12) — pasó de
  *"🔲 Abierta"* a **🔴 Abierta y ATRASADA**, con los dos relojes escritos.

## Qué quedó pendiente

| Tarea | Responsable | Urgencia |
|---|---|---|
| **Escribir el Plan de research** — es la raíz que bloquea 4, 5 y 6 | ⬜ **sin dueño** | 🔴 Ya |
| **Usar la ventana de entrevistas de ML** antes de que se cierre | ML | 🔴 Antes del 16/9 |
| Cargar al repo la clase del 5/9 (FM tiene el material) | FM | 🟡 Esta semana |
| Cargar la Clase 6 después de que se dé hoy | FM | 🟡 Hoy |
| Cargar las respuestas de P-20 y P-21, si se preguntaron el 2/9 | Equipo | 🟡 |
| Reescribir el sombrero rojo del análisis (6 puntos a debatir ya escritos) | Equipo | 🟡 |
| Elegir uno de los 3 logos + corregir el rojo CRITICAL | Equipo | 🟢 |

## Nota de método

Las 4 tarjetas vencidas **no se movieron ni se maquillaron**: quedaron donde estaban, con la deuda
escrita en cada una. El tablero es ítem de evaluación y sirve más mostrando el atraso real que
ordenado a último momento.

---

## Segunda parte — carga de las clases del 2/9 y del 5/9

FM pasó el material de las dos clases pendientes. Se cargaron las dos, con nota trabajada y bajada
a FraudLens.

### 🔴 Hallazgo 1: el deck del 5/9 pide 4 entregables **para hoy**

La lámina *"Para la próxima clase…"* del deck de Océano Azul pide, textual:

1. **Ideación y Grilla de Priorización**
2. **Narrativa de la propuesta de solución**
3. **Benchmarking con curva de valor**
4. **Encuesta difundida con respuestas y su análisis**

Ninguno estaba en el tablero — nadie los había visto porque el material no estaba cargado. Se
crearon las 4 tarjetas. La 12 (encuesta) fue directo a **🚧 Bloqueado**: pide la encuesta
*difundida, con respuestas y con análisis*, y el Plan de research ni siquiera está escrito.

**Es la tercera clase seguida que pide evidencia de usuarios** (26/8, 2/9 y 5/9) y la tercera vez
que la respuesta es cero.

### 🔎 Hallazgo 2: el cronograma no sirve para anticipar el tema de la clase

El deck del 2/9 es **Taller de Oratoria**, no *"Design Thinking. Redefinir el problema"* como decía
el cronograma. El del 5/9 sí coincide (Océano Azul).

Se resolvió parcialmente [P-20](../docs/00-proyecto/preguntas-abiertas.md#p-20): el desfase es de un
número (deck `NN` = clase `NN-1` del cronograma), pero lo importante es otra cosa — **el cronograma
sirve para fechas y entregables, no para saber qué se va a dictar.**

Dato que encaja: el punto 02 de la agenda del 2/9 era *"presentaciones: Design Thinking de al menos
3 posibles usuarios"*. Los entregables se presentaban esa clase aunque el tema dictado fuera otro.

### 🎯 Hallazgo 3: Storytelling con Datos es el pliego del dashboard

El cruce más útil de las dos clases con el producto. Los 10 principios de storytelling con datos se
leen como requisitos de UI, y **coinciden uno a uno con lo que ya se había decidido** en la
propuesta de identidad visual: eliminar el desorden, jerarquía y contraste, uso estratégico del
color, accesibilidad del texto.

O sea: el trabajo de identidad no era decorativo — respondía a esta clase antes de que se diera.
Conviene decirlo así en la defensa.

Y abre algo que **no** está resuelto: el principio *"contar una historia"* aplicado a **una sola
transacción**. Hoy el dashboard muestra un puntaje; la pregunta es si además debería contar **por
qué**. Eso es explicabilidad, y es material para el Problem Statement y para el alcance del MVP.

### 🔴 Hallazgo 4: dos trampas que apuntan a FraudLens

**La trampa 3 del océano rojo** es *"confundir innovación de valor con tecnología"*. Hoy FraudLens
se define como *"un filtro más eficaz gracias a la IA"* — que es exactamente eso. Del propio
material: *"la tecnología abre mercados cuando el comprador percibe el valor"*, y *"NetJets y Curves
crearon océanos sin tecnología disruptiva"*.

**La Clave 2 de Robbins** dice lo mismo desde la oratoria: *no digas "plataforma de automatización",
decí "ahorramos 12 horas por semana"*. Nuestro enunciado actual es la versión "plataforma de
automatización": **le falta el número, y ese número sale del research.**

### Lo bueno: el benchmarking no está bloqueado

De los 4 entregables nuevos, el **benchmarking con curva de valor** es el único que no depende de
conseguir entrevistas: se hace mirando la oferta pública de los competidores. Es lo más barato de
entregar hoy y quedó primero en la lista.

### Archivos

- `docs/01-clases/clase-05-oratoria-y-storytelling.md` *(nuevo)*
- `docs/01-clases/clase-06-oceano-azul.md` *(nuevo)*
- `docs/01-clases/material/` — 4 decks crudos nuevos
- `docs/00-proyecto/glosario.md` — 11 términos nuevos
- `docs/00-proyecto/preguntas-abiertas.md` — P-20 con lo aprendido
- `docs/01-clases/README.md` y `material/README.md` — índices

---

## Tercera parte — decisión final de identidad visual

FM cerró el [ticket de identidad visual](https://trello.com/c/ncNYKzbF): el equipo revisó el
board de Canva y aprobó avanzar.

### La decisión

**Opción B · Anomalía en grilla** — una grilla de puntos violeta con una anomalía resaltada.
Se descartaron la Opción A (Embudo) y la Opción C (Prisma), que quedan documentadas como
alternativas exploradas.

### Cierre del board para presentarlo

Se agregaron tres páginas finales al [board de Canva](https://www.canva.com/design/DAHUDsuQPB8)
(pasó de 14 a 17 páginas):

- **Logo Final** — el isotipo elegido junto al wordmark, más su aplicación como favicon/ícono de app.
- **La marca en el mercado** — un cartel/billboard mostrando la marca ya posicionada, para dar el
  cierre visual de "la marca lista para el mercado fintech".
- **Gracias** — cierre con el crédito del equipo (Diaz Valdez · Guerrero Rojas · Lewinzon · Molina).

### Registro en los dos lugares

Siguiendo la regla del proyecto (ningún ticket pasa a Hecho sin comentario de resolución en Trello
**y** documentación en el repo):

- Comentario de resolución cargado en la tarjeta de Trello, con la decisión, lo descartado y lo
  pendiente.
- Tarjeta movida a **✅ Hecho**.
- [`docs/05-producto/identidad/propuesta-canva.md`](../docs/05-producto/identidad/propuesta-canva.md)
  actualizado: pasa de "propuesta para decidir" a "decisión final", con la estructura de las 3
  páginas nuevas.

### Lo que queda pendiente, fuera de este ticket

- Corregir el rojo CRITICAL en modo oscuro (`#DC2626`, 4.02:1 — no llega al mínimo AA de 4.5).
- Elegir entre Inter e IBM Plex Sans para la tipografía de UI del producto — distinto del wordmark
  del logo, que ya quedó resuelto.
