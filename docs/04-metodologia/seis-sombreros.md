# Método de los 6 Sombreros para Pensar

> **Fuente:** consigna del docente. Es de aplicación **obligatoria** en el proyecto.
> Método original de **Edward de Bono** (*Six Thinking Hats*).

## Para qué sirve

Analizar problemas complejos **desde múltiples perspectivas**, eliminando los sesgos personales,
emocionales y cognitivos propios de una sola cabeza.

> **No pienses como una persona. Pensá como un equipo.**

La idea central: en vez de discutir todos a la vez mezclando datos, miedos, críticas y entusiasmo,
**todos piensan con el mismo sombrero al mismo tiempo**, y después se cambia. Eso separa el análisis
de la discusión y evita que el más convencido gane por insistencia.

## Los seis sombreros

| Sombrero | Rol | Qué hace | Qué tiene **prohibido** |
|---|---|---|---|
| ⚪ **Blanco** | Analista racional | Sólo **hechos objetivos**: datos verificables, información disponible, contexto real, y **qué datos faltan** | Opiniones, juicios, emociones |
| 🔴 **Rojo** | Mente emocional | Emociones, miedos, intuiciones y sensaciones asociadas al problema | **Justificar o racionalizar.** Sólo se exponen |
| ⚫ **Negro** | Crítico estratégico | Riesgos reales, fallos posibles, consecuencias negativas. Escenarios donde la decisión **fracasa** y por qué | Suavizar o compensar con lo bueno |
| 🟡 **Amarillo** | Optimista estratégico | Oportunidades, beneficios, escenarios positivos. Qué valor se obtiene **si funciona** | Ignorar que hay riesgos (eso ya lo dijo el negro) |
| 🟢 **Verde** | Pensamiento creativo | Ideas nuevas, alternativas no evidentes, enfoques distintos | **Evaluar o filtrar.** Prioriza originalidad y cantidad |
| 🔵 **Azul** | Director estratégico | Organiza todo lo anterior, extrae los puntos clave, **elimina contradicciones** y propone la decisión final | Aportar contenido nuevo que no salió de los otros sombreros |

## Reglas de aplicación

1. **Secuencial y sin mezclar roles.** Cada sombrero mantiene su lógica sin contaminarse con los otros.
2. **Concreto y accionable.** Nada de generalidades, clichés ni respuestas obvias.
3. **El azul va último** y tiene que **integrar y equilibrar** todas las visiones, no elegir su favorita.
4. **El objetivo es mejorar la calidad del pensamiento, no delegar la decisión.** El análisis no
   decide por nosotros: nos da con qué decidir.

### Verificación antes de dar por cerrado un análisis

- [ ] ¿El problema se analizó desde múltiples perspectivas reales?
- [ ] ¿El resultado refleja un único sesgo emocional o racional? *(si sí, rehacer)*
- [ ] ¿La decisión del sombrero azul integra y equilibra todo lo anterior?

## 📌 Cuándo lo aplicamos

**A toda decisión del proyecto**, según pidió el docente.

Ahora bien: aplicarlo a *"invitar a los integrantes al tablero de Trello"* no aporta nada y llena el
repositorio de ruido. El criterio práctico del equipo:

| Tipo de tarjeta | ¿6 Sombreros? |
|---|---|
| **Decisión** — elegir entre opciones, definir alcance, elegir usuario, elegir dataset, elegir stack | ✅ **Sí, obligatorio.** El análisis va en `docs/05-producto/analisis/` |
| **Entregable de la materia** — Problem Statement, solución elegida, MVP Canvas | ✅ **Sí.** Es exactamente lo que el docente quiere ver |
| **Tarea operativa** — invitar gente, crear un repo, cargar un documento | ❌ No. Es ejecución, no decisión |

> Si dudás de si una tarjeta lleva análisis: preguntate **"¿esto se puede hacer mal de más de una
> manera?"**. Si la respuesta es sí, lleva análisis.

## Dónde vive cada análisis

```
docs/05-producto/analisis/6-sombreros-<tema>.md
```

Y la tarjeta de Trello correspondiente **linkea al archivo**.

## Plantilla

Copiá [`_plantilla-6-sombreros.md`](../05-producto/analisis/_plantilla-6-sombreros.md).

## El prompt del docente, textual

> Guardado sin modificar para poder reproducirlo.

```
Contexto y Rol

Actúa como un sistema de pensamiento estratégico avanzado que simula el análisis de un problema
como si fuera realizado por un equipo completo de expertos, cada uno con una forma de pensar
distinta.

El objetivo no es dar una respuesta rápida, sino expandir mi visión del problema, eliminando sesgos
personales, emocionales y cognitivos propios de una sola mente.

No pienses como una persona.
Piensa como un equipo.

Consulta / Tarea

Analiza el siguiente problema importante utilizando el método de los seis sombreros para pensar,
aplicándolo de forma rigurosa, secuencial y sin mezclar roles.

Problema a analizar:
[AQUÍ ESCRIBE EL PROBLEMA, DECISIÓN O SITUACIÓN]

Especificaciones de Análisis

Analiza el problema desde cada sombrero como si fuera una persona distinta dentro del equipo, con su
propia lógica interna y su propio objetivo.

Sombrero blanco, analista racional
Evalúa únicamente hechos objetivos.
Datos verificables, información disponible, contexto real y datos que faltan para una mejor decisión.
Prohibido emitir opiniones, juicios o emociones.

Sombrero rojo, mente emocional
Expresa emociones, miedos, intuiciones y sensaciones internas asociadas al problema.
No justifiques ni racionalices estas emociones. Limítate a exponerlas con claridad.

Sombrero negro, crítico estratégico
Identifica riesgos reales, fallos posibles y consecuencias negativas.
Evalúa escenarios donde la decisión fracasa y explica por qué podría salir mal.

Sombrero amarillo, optimista estratégico
Analiza oportunidades, beneficios y escenarios positivos.
Explica qué puede salir muy bien y qué valor se puede obtener si la decisión funciona.

Sombrero verde, pensamiento creativo
Genera ideas nuevas, alternativas no evidentes y enfoques diferentes.
No evalúes ni filtres las ideas. Prioriza la originalidad y la expansión de opciones.

Sombrero azul, director estratégico
Organiza todo el análisis anterior.
Extrae los puntos clave de cada sombrero, elimina contradicciones y propone una decisión final
consciente, basada en una visión completa del problema.

Criterios de Excelencia
Cada sombrero debe mantener su rol sin contaminarse con otros.
El análisis debe ser profundo, concreto y accionable.
Evitar generalidades, clichés y respuestas obvias.
El objetivo es mejorar la calidad del pensamiento, no delegar la decisión.

Cómo debe ser la respuesta
Claramente estructurada por sombreros.
Lenguaje preciso, claro y directo.
Enfoque psicológico y estratégico.
Pensar como un equipo de alto nivel enfrentándose a una decisión real.

Verificación Final
Antes de finalizar, comprueba que:
El problema ha sido analizado desde múltiples perspectivas reales.
El resultado no refleja un único sesgo emocional o racional.
La decisión final del sombrero azul integra y equilibra todas las visiones anteriores.
```

## ⚠️ Advertencia de uso

El prompt está pensado para que **un modelo de IA haga el análisis**. Eso está bien y es lo que
pidió el docente. Pero:

- El sombrero **blanco** sólo puede usar **hechos que nosotros aportemos**. Si le pedimos datos que
  no tenemos, los va a completar — y eso es un dato inventado en un documento evaluado.
  **Regla del repo: el blanco lista lo que sabemos y lo que falta. No rellena.**
- El sombrero **rojo** son **nuestras** emociones, no las de un modelo. Ese lo escribe el equipo.
- El **azul decide**, pero la decisión la firma el equipo. En la defensa nos van a preguntar
  *por qué* decidimos algo, y "lo dijo la IA" no es una respuesta.
