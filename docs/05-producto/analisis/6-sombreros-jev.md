# 6 Sombreros — ¿Incorporamos Jev (TypeSafe AI) como modelo de IA de FraudLens?

| | |
|---|---|
| **Decisión** | ¿Usamos Jev como capa de señales dentro de FraudLens, lo descartamos, o lo dejamos como línea futura? |
| **Fecha** | 2026-09-30 (inicio) |
| **Participantes** | ⬜ Faltan las voces del equipo. Borrador armado por MDV con asistencia de Claude Code |
| **Tarjeta de Trello** | [Escribir el 6 Sombreros de usar Jev como modelo de IA](https://trello.com/c/dNrC2EWY) · [Evaluar modelo de IA "Jev"](https://trello.com/c/yOSmUHOx) |
| **Estado** | 🟡 **BORRADOR — en análisis.** ⬜ El sombrero rojo y el azul no están escritos |
| **Insumo** | [`typesafe-jev.md`](../typesafe-jev.md) |

> ⚠️ **Qué es de quién en este archivo** (regla 6 del repo):
> - ⚪ Blanco: hechos tomados de [`typesafe-jev.md`](../typesafe-jev.md), con su fuente.
> - ⚫🟡🟢 Negro, amarillo y verde: **💡 borrador de Claude Code** derivado de esos hechos. El
>   equipo los corrige, completa o descarta.
> - 🔴 Rojo: **lo escribe el equipo.** Acá sólo están las preguntas.
> - 🔵 Azul: **sin decidir.** Se escribe al final, con las voces del equipo.

## El problema, en una frase

¿Incorporamos a Jev —un modelo de TypeSafe AI que devuelve respuestas tipadas con confianza a partir
de texto— como capa de señales del MVP de FraudLens, sabiendo que no tenemos acceso confirmado a su
API, que no pudimos verificar su política de datos y que su calibración no fue testeada por terceros?

---

## ⚪ Sombrero Blanco — Analista racional

> Sólo hechos verificables. Sin opiniones ni juicios.

### Lo que sabemos

| Hecho | Fuente |
|---|---|
| Jev es el primer modelo de la clase "System One" de TypeSafe: recibe texto más preguntas con esquema y devuelve valores tipados con probabilidad y confianza | 📗 [typesafe.ai](https://typesafe.ai/) |
| System One **no es un agente**: no genera código ni elige su próxima acción; el código controla el flujo | 📗 [docs.typesafe.ai](https://docs.typesafe.ai/concepts/how-to-build-with-system-one) |
| Tiene 3 tipos de pregunta: **Noul** (sí/no), **Choice** (opción de una lista fija) y **Score** (escala ordenada) | 📗 idem |
| La documentación oficial menciona "Financial Crime": evaluar narrativas de transacciones, documentos KYC e historiales de alertas, y derivar casos ambiguos a un investigador | 📗 [Casos de uso](https://docs.typesafe.ai/concepts/use-case-map) |
| TypeSafe **no se presenta como plataforma antifraude**; la documentación da marcos generales, sin esquemas concretos para fraude | 📗 idem |
| Endpoint `POST https://api.typesafe.ai/v1/systemone`, autenticación `Bearer`, clave en console.typesafe.ai | 📗 [Quick start](https://docs.typesafe.ai/introduction/quickstart) |
| SDK oficial de Python (licencia MIT); también hay uno de .NET | 📗 [repo](https://github.com/typesafe-ai/typesafe-sdk-python) |
| Precio publicado: **$42 por billón de tokens de entrada** | 📗 [typesafe.ai](https://typesafe.ai/) |
| Estado: **early access**; según un tercero, con **lista de espera** y un único API hosteado, sin on-premise | 📗 typesafe.ai · 📙 [TrueFoundry](https://www.truefoundry.com/blog/typesafe-ai-jev) |
| Latencia declarada 70–500 ms, **auto-reportada**; calibración **no testeada por terceros**; benchmarks "self-graded" | 📙 TrueFoundry |
| Máximo de 255 opciones por campo | 📙 TrueFoundry |
| El MVP devuelve riesgo 0–100, nivel, decisión (aprobar/revisar/bloquear) y hasta 3 motivos; los errores del modelo **no deben producir aprobaciones silenciosas** | [`requerimientos-funcionales-mvp.md`](../requerimientos-funcionales-mvp.md) (borrador de ML) |
| El dataset 1 (entrenamiento) son columnas PCA anonimizadas sin texto; el dataset 3 trae comercio, categoría y monto | [`datos.md`](../datos.md) |
| Nuestro cliente objetivo son fintech y bancos tradicionales | [decisión 0004](../../03-decisiones/0004-enfoque-cliente-fintech-bancos.md) |

### Lo que NO sabemos

> No se completa a ojo. Si falta, se marca como falta.

- ⬜ **Si tenemos acceso a la API** (clave) y quién del equipo se anotaría.
- ⬜ **Qué retiene TypeSafe** de los datos que recibe ni si los usa para entrenar (el Trust Center no se pudo leer).
- ⬜ **Límites de uso (rate limits)** y si el precio publicado aplica a early access.
- ⬜ **Si la confianza de Jev está bien calibrada** para nuestro tipo de datos — nadie lo midió.
- ⬜ **Qué texto/contexto real tendríamos para pasarle**, dado el mapeo pendiente de datasets.
- ⬜ **Qué stack usa el MVP** (P-10): si no es Python, se usa REST directo.
- ⬜ **Si agrega señal** sobre el modelo tabular solo.

---

## 🔴 Sombrero Rojo — Mente emocional

> Emociones, miedos e intuiciones. **Sin justificar.** Lo escribe el equipo, no la IA.

**⬜ Pendiente. Cada integrante responde con lo que siente de verdad, sin justificar:**

1. ¿Qué sentís al pensar en depender de una API de terceros en early access para algo del MVP?
2. ¿Te da miedo la pregunta del docente "¿por qué usaron esto y no algo más simple?"
3. ¿Qué te genera mandar datos de transacciones a un servicio del que no sabemos qué retiene?
4. ¿Cuánto te entusiasma que sea un diferencial tecnológico frente a la competencia?
5. ¿Sentís que estamos eligiendo esto porque sirve o porque suena novedoso?
6. ¿Te sentís capaz de explicar y defender cómo funciona Jev en The Pitch?

| Integrante | Estado |
|---|---|
| MDV | ⬜ |
| FGR | ⬜ |
| ML | ⬜ |
| FM | ⬜ |

---

## ⚫ Sombrero Negro — Crítico estratégico

> 💡 **Borrador de Claude Code**, derivado de los hechos del sombrero blanco. Riesgos reales y
> escenarios donde esto **fracasa**.

| Riesgo | Cómo se ve el fracaso |
|---|---|
| **No conseguimos acceso** (lista de espera) | Diseñamos la arquitectura alrededor de una API a la que no podemos llamar antes de la entrega del prototipo (28/10) |
| **Dependencia cerrada y externa** | Si la API cae o cambia de versión, el MVP pierde una pieza; sin on-premise no hay plan B propio |
| **Privacidad incumplible para el cliente** | Un banco o fintech pregunta qué retiene TypeSafe y no tenemos respuesta; el pitch pierde credibilidad |
| **Calibración sin verificar** | Jev "elige con seguridad" la opción equivocada entre las que le damos; el sistema manda a aprobar un fraude con falsa confianza |
| **No agrega señal** | Medimos y Jev no mejora al modelo tabular: construimos complejidad para nada |
| **No hay texto que leer** | El dataset de entrenamiento es PCA anonimizado; el contexto textual que le pasemos lo inventamos nosotros y sesga el resultado |
| **Nadie puede explicarlo** | En The Pitch no podemos defender qué hace Jev por dentro (es un modelo propietario) — choca con "cada integrante puede defender lo que muestra" |
| **Distracción del alcance** | Dedicar horas a Jev en vez de al MVP mínimo y al User Research, que sigue pendiente; el MVP tiene que ser chico |

---

## 🟡 Sombrero Amarillo — Optimista estratégico

> 💡 **Borrador de Claude Code.** Qué puede salir muy bien y qué valor se obtiene.

- **Encaja con "revisar":** la confianza como segundo eje de decisión (patrón oficial
  *Confidence-Gated Routing*) mapea directo al flujo aprobar / revisar / bloquear.
- **Motivos legibles** para el Perfil A sin que el modelo invente texto: Jev elige de un catálogo
  cerrado, lo que cubre "devolver los motivos" del CU-01.
- **Diferencial frente a la competencia**: incorporar un modelo de decisión tipada es innovación
  tecnológica demostrable (criterio que evalúa el docente), aunque sea un componente chico.
- **Costo bajo declarado** ($42 por billón de tokens de entrada): si se confirma, no es un problema
  de presupuesto para un MVP.
- **El diseño se puede mantener chico:** un spike con el dataset 3 cuesta poco y produce evidencia
  propia, aunque el resultado sea "no sirve" — eso también es un hallazgo defendible.
- **Hay SDK oficial y REST documentado:** la integración técnica no es el riesgo.

---

## 🟢 Sombrero Verde — Pensamiento creativo

> 💡 **Borrador de Claude Code.** Ideas nuevas y alternativas no evidentes. **Sin filtrar ni evaluar.**

1. Usar Jev **sólo para priorizar la cola** del analista (Score), sin tocar la decisión aprobar/bloquear.
2. Usarlo **sólo para generar los motivos** (Choice) y dejar el puntaje al modelo tabular.
3. Dejarlo como **línea futura** documentada, sin integrarlo al MVP, y mostrar el diagrama en The Pitch.
4. Hacer el spike como **ejercicio del documento final**: "evaluamos X, medimos Y, descartamos Z".
5. Sustituir Jev por **otro modelo de clasificación de texto** o un LLM con salida estructurada.
6. Armar la arquitectura con una **interfaz de "proveedor de señales"** para poder enchufar Jev u otro
   proveedor sin reescribir.
7. Probar Jev con **las narrativas reales de las entrevistas** (Nicolás, Agustín) en vez de filas de dataset.
8. Pedirle a TypeSafe **acceso de early access mencionando que es un proyecto académico**.

---

## 🔵 Sombrero Azul — Director estratégico

> ⬜ **No se escribe todavía.** El azul integra las cinco visiones y **el equipo firma la decisión**;
> no se completa hasta que el sombrero rojo tenga las cuatro voces. La decisión, cuando exista,
> se registra como [decisión numerada](../../03-decisiones/).

### Puntos clave de cada sombrero

| Sombrero | Lo que aportó |
|---|---|
| ⚪ Blanco | ⬜ |
| 🔴 Rojo | ⬜ |
| ⚫ Negro | ⬜ |
| 🟡 Amarillo | ⬜ |
| 🟢 Verde | ⬜ |

### Contradicciones a resolver

- ⬜

### Decisión

> ⬜

### Qué la sostiene

- ⬜

### Qué la haría cambiar

- ⬜

---

## Verificación final

- [ ] El problema se analizó desde múltiples perspectivas reales
- [ ] El resultado **no** refleja un único sesgo emocional o racional
- [ ] La decisión del azul integra y equilibra todas las visiones anteriores
- [ ] El blanco **no inventó** ningún dato
