# 6 Sombreros — ¿Confirmamos el stack implementado para el MVP?

| | |
|---|---|
| **Decisión** | ¿Confirmamos como stack del MVP el que ya está implementado en el repo de código (Next.js, MongoDB Atlas y Vercel), o cambiamos alguna pieza? |
| **Fecha** | 2026-11-04 |
| **Participantes** | MDV, con asistencia de Claude Code. ⬜ Faltan las voces de FGR, ML y FM |
| **Tarjeta de Trello** | [Definir el stack tecnológico del MVP (P-10)](https://trello.com/c/QLA7vu9Y) |
| **Estado** | 🟡 **BORRADOR.** ⬜ Falta el sombrero rojo de las 4 voces y la decisión del equipo |

> ⚠️ **Qué es de quién en este archivo** (regla 6 del repo):
> - ⚪ Blanco: hechos del repo del MVP (`main`, commit `da20858`), de este repositorio y de Trello, con su fuente.
> - ⚫🟡🟢 Negro, amarillo y verde: **💡 borrador de Claude Code.** El equipo los corrige, completa o descarta.
> - 🔴 Rojo: **lo escribe el equipo.** Acá sólo están las preguntas.
> - 🔵 Azul: **💡 propuesta de Claude Code para discutir.** La decisión la firma el equipo.

## El problema, en una frase

A una semana del 2° Parcial, ¿confirmamos el stack que ya está implementado en el repo del MVP o
cambiamos alguna pieza, sabiendo que el modelo de fraude todavía no está resuelto?

**Qué no se decide acá:** qué modelo de fraude usa el MVP. Eso va en la tarjeta
[Modelos de IA a utilizar](https://trello.com/c/HgigLF8C). Este análisis sólo mira cómo condiciona
al stack.

---

## ⚪ Sombrero Blanco — Analista racional

### Lo que sabemos

| Hecho | Fuente |
|---|---|
| El stack es Next.js App Router, React y TypeScript estricto, con Route Handlers en Node.js 24 | README y `package.json` del repo del MVP |
| La base es MongoDB Atlas en producción y MongoDB 8 en Docker para desarrollo, con Mongoose | README del repo del MVP |
| La IA declarada es Vercel AI SDK con el proveedor TypeSafe (Jev) | README del repo del MVP |
| Se aloja en Vercel, con frontend y API en un solo deploy | README del repo del MVP |
| `main` tiene 3 commits de ML y el merge del PR #1, el último del 30/10 | `git log` del repo del MVP |
| El `POST` de evaluaciones persiste en MongoDB y devuelve un resultado fijo; no ejecuta reglas ni inferencia | README del repo del MVP |
| El `GET` lista las evaluaciones con paginación | README del repo del MVP |
| Se verificaron lint, tipos, build, la página inicial, `/api/health` y MongoDB local | README del repo del MVP (declarado, no ejecutado por nosotros) |
| Atlas y la inferencia real de TypeSafe no se probaron | README del repo del MVP |
| El deploy público respondió HTTP 200 el 28/10, sin probar MongoDB, Jev ni funciones de negocio | [`mvp.md`](../mvp.md) |
| `main` no tiene archivos Python, notebooks ni modelos exportados | `git ls-tree` del commit `da20858` |
| La guía del repo pide una única app desplegable y no crear otro servicio | `AGENTS.md` del repo del MVP |
| La API de decisiones de AI SDK es experimental | `AGENTS.md` del repo del MVP |
| El código de `apps/web/src` no menciona autenticación ni tenants | `git grep` del commit `da20858` |
| El adapter de Groq está en los PR #2 y #3, abiertos por MDV, sin mergear y desconectado del flujo HTTP | GitHub · `docs/design/ai-integration.md` del PR #3 |
| El diseño aclara que Groq no es la elección definitiva del modelo de fraude | `docs/design/ai-integration.md` del PR #3 |
| La decisión 0006 prevé un modelo con 3 datasets: entrenamiento, explicabilidad y test | [Decisión 0006](../../03-decisiones/0006-tres-datasets-para-el-modelo.md) |
| Jev interpreta texto y no reemplaza a un modelo tabular | [`typesafe-jev.md`](../typesafe-jev.md) |
| El 30/9 la cuenta de TypeSafe respondió *"Your organization is out of funds"* | [P-25](../../00-proyecto/preguntas-abiertas.md#p-25) |
| Multi-tenant está fuera del MVP y figura como línea futura | [`problema.md`](../problema.md) |
| La decisión 0007 descartó MongoDB para el **prototipo**, porque su aislamiento entre organizaciones depende de RLS de PostgreSQL | [Decisión 0007](../../03-decisiones/0007-prototipo-postgresql-un-deploy-vercel.md) |
| El criterio sugerido en P-10 es elegir lo que el equipo ya sabe usar | [P-10](../../00-proyecto/preguntas-abiertas.md#p-10) |
| El 2° Parcial es el 11/11 y la documentación final se entrega el 18/11 | [`cronograma.md`](../../00-proyecto/cronograma.md) |

### Lo que NO sabemos

- ⬜ **Qué sabe usar cada integrante** (Next.js, TypeScript, MongoDB). Es el criterio de P-10 y no se relevó.
- ⬜ **Por qué se eligió este stack**, y en particular MongoDB. No está escrito en ningún documento.
- ⬜ Si FGR, referente técnico del equipo, está de acuerdo.
- ⬜ Si Atlas está configurado y funciona en el deploy público. **No se probó.**
- ⬜ Los límites vigentes de los planes de Vercel y Atlas que usa el proyecto. **No se verificaron.**
- ⬜ Cómo se resuelve el modelo de fraude: entrenado, LLM o reglas.
- ⬜ Si el MVP reutiliza algo del prototipo ([P-05](../../00-proyecto/preguntas-abiertas.md#p-05)).
- ⬜ Si los cuatro integrantes tienen acceso al repo del MVP.

---

## 🔴 Sombrero Rojo — Mente emocional

> Emociones, miedos e intuiciones. **Sin justificar.** Lo escribe el equipo, no la IA.

Preguntas para cada integrante:
- ¿Qué te genera este stack? ¿Te sentís cómodo/a trabajando con él?
- ¿Te animás a explicarlo y defenderlo frente al docente en el 2° Parcial?
- ¿Qué te preocupa de llegar al 11/11 con lo que hay hoy?
- ¿Qué te genera que el stack se haya definido en el código antes que en una decisión del equipo?

- **MDV:** ⬜
- **FGR:** ⬜
- **ML:** ⬜
- **FM:** ⬜

---

## ⚫ Sombrero Negro — Crítico estratégico

> 💡 Borrador de Claude Code.

| Riesgo | Cómo se ve el fracaso |
|---|---|
| **El modelo entrenado no entra en el stack** | La 0006 sigue vigente, pero para servir un modelo Python hay que sumar un servicio, contra la regla de una sola app, o exportarlo a Node. No llega a tiempo |
| **Reemplazar el modelo por un LLM sin decidirlo** | Se termina usando Jev o Groq para puntuar, y en la defensa no se puede explicar por qué se abandonó la 0006 ni qué significa el puntaje |
| **Llegar al parcial con resultado fijo** | La demo muestra siempre la misma respuesta y el docente ve que el producto todavía no evalúa nada |
| **Atlas falla en la demo** | Nunca se probó: el `POST` no puede persistir y la app no muestra nada en vivo |
| **Sin saldo o sin cuota en el proveedor de IA** | La inferencia depende de una cuenta sin fondos o de una cuota gratuita que se corta durante la presentación |
| **Sólo una persona entiende el código** | Si el resto no lo conoce, nadie más puede explicarlo o corregirlo en la semana del parcial |
| **Aprobar por hecho consumado** | El docente pregunta por qué se eligió el stack y el equipo no tiene razones propias ni alternativas analizadas |
| **Dos bases de código que se confunden** | El documento final mezcla el prototipo (PostgreSQL) con el MVP (MongoDB) y se contradice |
| **Multi-tenant a futuro** | La línea futura se vende como simple, pero con MongoDB el aislamiento hay que hacerlo en código, el problema que la 0007 quiso evitar |

---

## 🟡 Sombrero Amarillo — Optimista estratégico

> 💡 Borrador de Claude Code.

- El stack ya existe y está desplegado: el equipo no pierde la semana previa al parcial reescribiendo.
- Un solo lenguaje y un solo deploy: menos servicios que se apagan y menos piezas para explicar en The Pitch.
- Encaja con el recorte de la 0005: sin autenticación, sin roles y sin multi-tenant, no hacen falta las piezas que obligaron a mantener PostgreSQL en el prototipo.
- El `POST` y el `GET` ya persisten evaluaciones, así que el modelo se puede enchufar sin rehacer ese camino.
- Si entra el adapter del PR #2, cambiar de proveedor de IA queda concentrado en un solo punto.
- Las alternativas de P-10 quedan como comparación documentada para justificar el stack en el documento final.

---

## 🟢 Sombrero Verde — Pensamiento creativo

> 💡 Borrador de Claude Code. Sin filtrar. Las ideas técnicas son conocimiento general, sin verificar.

1. Portar a TypeScript el motor determinista del prototipo (`risk.service.ts`) como primer puntaje real.
2. Entrenar en un notebook y exportar coeficientes a JSON: una regresión logística se calcula en TypeScript sin librerías.
3. Entrenar en Python y exportar a ONNX para correrlo con `onnxruntime-node`, la alternativa C de P-10.
4. Sumar una función Python en el mismo proyecto de Vercel sólo para `/predict`.
5. Puntuar con reglas o modelo, y usar el LLM sólo para redactar la explicación al analista.
6. Precalcular puntajes del dataset 3 y cargarlos como seed para la demo.
7. Tener MongoDB local en Docker como plan B de la demo si Atlas falla.
8. Cambiar a PostgreSQL en Neon para compartir base y conocimiento con el prototipo.
9. Hacer una sesión de 30 minutos donde ML le muestre el código al resto antes del parcial.

---

## 🔵 Sombrero Azul — Director estratégico

> 💡 Propuesta de Claude Code para discutir. **No es decisión**: falta el rojo y la firma del equipo.

### Puntos clave de cada sombrero

| Sombrero | Lo que aportó |
|---|---|
| ⚪ Blanco | El stack existe y responde, pero Atlas y la IA no se probaron, y no hay registro de por qué se eligió ni de qué sabe usar el equipo |
| 🔴 Rojo | ⬜ Pendiente del equipo |
| ⚫ Negro | El riesgo mayor no está en Next.js ni en MongoDB: está en cómo entra el modelo de fraude y en poder defender el stack |
| 🟡 Amarillo | No reescribir a una semana del parcial; una sola app; encaja con el recorte de la 0005 |
| 🟢 Verde | Hay caminos para meter un puntaje real sin romper la regla de una sola app (ideas 1, 2, 3 y 5) |

### Contradicciones a resolver

- **P-10 pide elegir lo que el equipo ya sabe, y el stack se definió antes de relevarlo.** Falta preguntarlo.
- **La guía del repo pide una sola app, y la 0006 prevé un modelo entrenado.** Hoy no hay Python en el repo. Lo resuelve la tarjeta [Modelos de IA a utilizar](https://trello.com/c/HgigLF8C).
- **El README declara TypeSafe, el PR #2 agrega Groq y `typesafe-jev.md` dice que Jev no reemplaza al modelo tabular.** Hay que aclarar qué rol tiene cada uno.
- **La 0007 descartó MongoDB y el MVP lo usa.** No se contradicen: la 0007 es del prototipo y multi-tenant está fuera del MVP. Conviene dejarlo escrito.

### Propuesta

> **(💡 Claude Code, sin validar)** Confirmar Next.js, MongoDB Atlas y Vercel como stack del MVP, y
> resolver el modelo de fraude aparte, en [Modelos de IA a utilizar](https://trello.com/c/HgigLF8C).
> → Cuando el equipo decida, se registra como decisión numerada en `docs/03-decisiones/` y se cierra P-10.

### Qué la sostiene

- No hay tiempo para reescribir antes del 11/11, y el stack actual ya persiste evaluaciones.
- Multi-tenant está fuera del MVP, así que el motivo de la 0007 para evitar MongoDB no aplica acá.
- Separar el modelo evita frenar esta decisión por una discusión distinta.

### Qué la haría cambiar

- Que el relevamiento muestre que el equipo no puede trabajar ni defender este stack.
- Que el modelo elegido no se pueda servir dentro de una sola app.
- Que Atlas no funcione desde el deploy en Vercel.
- Que ML o FGR aporten una razón que este borrador no conoce.

---

## Verificación final

- [ ] El problema se analizó desde múltiples perspectivas reales — ⬜ falta el rojo del equipo
- [ ] El resultado **no** refleja un único sesgo emocional o racional — ⬜ falta el rojo del equipo
- [ ] La decisión del azul integra y equilibra todas las visiones anteriores — ⬜ falta el rojo y la decisión
- [x] El blanco **no inventó** ningún dato
