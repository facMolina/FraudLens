# Plan de research

| | |
|---|---|
| **Estado** | 🟡 Plan escrito — **falta ejecutarlo** |
| **Responsable** | Mateo Lewinzon (ML) |
| **Fecha** | 2026-09-10 |
| **Ticket** | [2. Plan de research](https://trello.com/c/EkjU3QyB) |
| **Entregable de** | Clase 5 (2/9) — vencido |

## Por qué este documento y no antes

El User Research partió de cero. A la fecha de esta actualización hay **2 entrevistas registradas
(Perfiles A y B) y 0 encuestas completadas**. Este plan no inventa datos — documenta cómo se
consiguen y analizan. La encuesta del Perfil C sigue pendiente.

Dos relojes corren sobre esto:

- **1° Parcial el 16/9.** El docente exige datos reales, no hipótesis.
- **La ventana de ML.** Permitió concretar la entrevista con Nicolás, analista de fraude, y ya no es
  un bloqueo para el Perfil A.

## A quién investigamos

Los 3 perfiles ya están decididos en [`usuarios.md`](usuarios.md), con la accesibilidad como
criterio explícito. No se vuelve a discutir acá:

| Perfil | Rol | Técnica | Por qué esa técnica |
|---|---|---|---|
| **A · Analista de fraude** | el que **decide** | Entrevista en profundidad | Necesitamos el *proceso* y las *excepciones* — no entra en un formulario |
| **B · Analista de producto** | el que **paga/decide integrar** | Entrevista | Necesitamos entender el riesgo, el costo y la decisión de integrar la solución |
| **C · Consumidor** | el que **sufre** | Encuesta | Es el único perfil donde el volumen es alcanzable, y lo que buscamos (frecuencia de un evento raro) necesita **n** grande |

## Contactos identificados

| Perfil | Contacto | Estado |
|---|---|---|
| **A · Analista de fraude** | **Nicolás** | Entrevista realizada |
| **B · Analista de producto** | **Agustín** | Entrevista realizada |
| **C · Usuario final** | **Encuesta abierta** | En difusión; falta recopilar y analizar respuestas |

## Qué tiene que responder cada instrumento

No alcanza con "investigar el fraude". Cada instrumento tiene que devolver algo concreto que hoy
no tenemos y que le falta a un enunciado como *"los sistemas tradicionales se apoyan en reglas
predefinidas que pueden resultar insuficientes"* — que no nombra a nadie ni cuantifica nada.

### Entrevista — Perfil A (analista de fraude)

**Objetivo:** entender el proceso real de revisión, no nuestra idea de cómo debería ser.

**Guía de temas** *(no un cuestionario cerrado — dejar hablar y repreguntar)*:

1. **El día a día.** ¿Cómo es tu cola de casos hoy? ¿Cuántos revisás por turno? ¿Cuánto tardás en
   promedio por caso, y cuánto en uno difícil?
2. **La herramienta actual.** ¿Qué mirás para decidir? ¿Qué información te falta en el momento de
   decidir y tenés que ir a buscar a otro lado?
3. **Las excepciones.** Contame el último caso que te hizo dudar. ¿Por qué dudaste? ¿Qué hiciste?
4. **El costo del error.** ¿Qué pasa cuando aprobás algo que era fraude? ¿Y cuando rechazás algo que
   era legítimo? ¿Cuál de los dos te preocupa más en tu rol?
5. **El número que falta.** ¿Cuánto tiempo o plata estimás que se ahorraría si tuvieras [x]? — dejar
   que lo complete la persona, no sugerirle la respuesta.

⚠️ **Es la entrevista más valiosa y la más escasa.** Preparar esta guía con el equipo antes de
usarla — no se puede improvisar y volver a llamar.

### Entrevista — Perfil B (responsable de riesgo/producto en fintech o banco)

> 🔄 **Actualizada el 2026-09-14** tras la redefinición del Perfil B —
> [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md). La guía original
> apuntaba a "dueño de comercio/e-commerce chico"; queda en el historial de esta misma sesión
> (2026-09-10).

**Objetivo:** entender cómo gestiona hoy el riesgo de fraude y cuantificar el costo real, en un
contexto donde el BCRA exige tener un programa de gestión de riesgo de fraude (Comunicaciones "A"
8471 y "A" 8473, 2026).

**Guía de temas:**

1. ¿Cómo gestionan hoy el riesgo de fraude? ¿Reglas propias, un proveedor externo, ambos?
2. ¿Cómo están encarando la Comunicación "A" 8471 del BCRA? ¿Ya tienen una función/persona
   responsable asignada, autoevaluaciones hechas?
3. ¿Cuánto estiman que pierden al año en fraude, o en el esfuerzo de cumplir con la normativa?
4. De los dos errores — rechazar una operación buena o dejar pasar un fraude — ¿cuál les preocupa
   más y por qué?
5. ¿Contratarían una herramienta que complemente lo que ya tienen? ¿Cuánto sería razonable pagar?

⚠️ **Contacto identificado: Agustín.** Falta confirmar disponibilidad y realizar la entrevista. Es
el punto crítico que señaló el [análisis de 6 sombreros](analisis/6-sombreros-enfoque-fintech.md).

## Resultados preliminares de entrevistas

> **Fecha de registro:** 2026-09-16 · **Entrevistados:** Nicolás (Perfil A) y Agustín (Perfil B).
> Estos hallazgos corresponden a las respuestas recibidas y todavía deben contrastarse con más
> entrevistas y con la encuesta del Perfil C.

### Nicolás — Analista de fraude

- El mayor dolor es reunir y relacionar información distribuida entre distintas herramientas.
  Esto demora la investigación, puede generar revisiones repetidas y dificulta entender el contexto
  completo de una alerta.
- El motor actual detecta bien patrones conocidos, pero genera falsos positivos y no siempre explica
  por qué activó una alerta. Los casos ambiguos, montos inusuales y dispositivos nuevos suelen pasar
  a revisión manual.
- La IA ayuda a detectar patrones complejos, priorizar alertas y analizar grandes volúmenes, pero
  requiere supervisión por riesgos de sesgo y falta de explicabilidad. No debería bloquear cuentas ni
  rechazar casos sensibles sin intervención humana.
- La mejora prioritaria para la interfaz sería una **vista unificada del caso**, con línea de tiempo,
  resumen de señales de riesgo, historial de operaciones, datos del dispositivo y antecedentes del
  cliente.

### Agustín — Analista de producto

- El desafío principal es reducir el fraude sin perjudicar a los usuarios legítimos. Se mide con
  pérdidas económicas, tasa de fraude, falsos positivos, operaciones rechazadas, tiempo de resolución,
  reclamos, confianza y abandono.
- La satisfacción con el motor actual es intermedia: responde bien ante patrones conocidos y permite
  aplicar controles rápidamente, pero necesita mayor precisión y adaptación. Faltan simulación de
  cambios, explicabilidad y seguimiento más completo.
- La IA puede mejorar la detección de anomalías, automatizar análisis y adaptar controles. Los
  principales obstáculos son la calidad de datos, integración, regulación y falta de especialistas.
  Se exigirían trazabilidad, explicaciones comprensibles, monitoreo y supervisión humana en decisiones
  de alto impacto.
- La interfaz actual fragmenta la información, dificulta comparar períodos y no siempre presenta
  indicadores claros. La funcionalidad prioritaria sería un **panel configurable por perfil**, con
  vistas adecuadas para analistas, líderes operativos, riesgo y producto.

### Síntesis inicial

Ambos entrevistados coinciden en tres necesidades: **reducir falsos positivos**, **explicar las
señales que motivan una alerta** y **centralizar la información para decidir con mayor rapidez**.
La propuesta de interfaz debe contemplar tanto la vista operativa detallada del analista como una
vista configurable de seguimiento para perfiles de producto y riesgo.

### Encuesta — Perfil C (usuario final de fintech/billetera/pasarela)

**Objetivo:** medir la frecuencia real de dos eventos — que le clonen una compra, y que le rechacen
una compra legítima — y cuál pesa más en la experiencia.

**Buenas prácticas** (de la Clase 4, ya en el ticket, no se repiten con criterio propio):

- Sin preguntas de "respuesta ideal" que inducen la respuesta.
- Demográficas al principio o al final, y sólo las necesarias.
- Abiertas limitadas y opcionales.
- Rangos de respuesta **impares** (3, 5 o 7) con punto medio neutro.
- Agregar siempre **"Otros"** y **"NS/NC"**.
- Anonimizar las respuestas.

**Borrador de preguntas:**

1. ¿Usás tarjeta de débito/crédito o billetera virtual para comprar online? *(filtro — sin esto no
   sigue)*
2. ¿Alguna vez te rechazaron una compra que sabías que era legítima? *(Sí / No / No estoy seguro)*
3. Si sí: ¿qué tan seguido te pasa? *(Nunca · Una vez · Alguna vez al año · Varias veces al año ·
   NS/NC)*
4. ¿Alguna vez notaste un cargo en tu cuenta que no reconocías? *(Sí / No / No estoy seguro)*
5. De estas dos situaciones, ¿cuál te generó más bronca? *(Que me rechacen una compra real / Que me
   aprueben un cargo que no hice / Las dos por igual / Ninguna me pasó / NS/NC)*
6. *(opcional, abierta)* Contanos brevemente qué pasó la última vez.
7. Edad *(rango)* · Con qué frecuencia comprás online *(rango)* — al final.

## Cuántas respuestas buscamos, y por qué alcanza

Por [P-17](../00-proyecto/preguntas-abiertas.md#p-17): las 400 respuestas de la Clase 4 son una
**guía**, no una obligación — el docente confirmó que el número lo elige y lo justifica el equipo.

**Propuesta: 80-100 respuestas para la encuesta del perfil C.**

Justificación: no buscamos un dato con significancia estadística para publicar — buscamos evidencia
de que el problema existe y una primera magnitud del tamaño (¿es "le pasó a 1 de cada 20" o "a 1 de
cada 3"?). Con 80-100 respuestas ya se puede distinguir si el rechazo indebido es un evento raro o
frecuente entre conocidos del equipo. Si el resultado es ambiguo, se amplía la difusión — no hace
falta fijar el número antes de ver los primeros datos.

**Para las entrevistas (perfiles A y B): 2-3 conversaciones por perfil**, no un número grande. Lo
que buscamos ahí es profundidad de proceso, no muestra representativa.

## Canales de difusión

- **Encuesta (perfil C):** grupos y contactos personales del equipo, redes sociales propias. Es
  auto-selección, no aleatoria — hay que decirlo así en el documento final, no como si fuera una
  muestra representativa de la población.
- **Entrevistas (perfil A):** Nicolás — ✅ entrevista realizada.
- **Entrevistas (perfil B):** Agustín — ✅ entrevista realizada.

## Cronograma de ejecución

| Cuándo | Qué |
|---|---|
| Ya | Armar y revisar en equipo la guía de entrevista del perfil A (no hay margen para improvisar) |
| Antes del 16/9 | Difundir la encuesta del perfil C — cuanto antes, porque las respuestas tardan días en juntarse |
| 16/9 | Entrevista con Nicolás, analista de fraude — ✅ realizada |
| 16/9 | Entrevista con Agustín, analista de producto — ✅ realizada |
| Con los resultados | Cargar hallazgos en `usuarios.md` (User Persona, Mapa de Empatía) y corregir `problema.md` si hace falta |

## Qué hacemos con lo que salga

Regla ya escrita en [`usuarios.md`](usuarios.md#-el-sesgo-que-hay-que-vigilar): si el research
contradice los [requerimientos funcionales](requerimientos-funcionales-mvp.md) o las 3
reformulaciones de [`problema.md`](problema.md), se corrigen esos documentos — no el research.

## Listo cuando

- [x] Guía de entrevista del perfil A revisada por el equipo
- [ ] Encuesta del perfil C armada y **difundida** (no alcanza con tenerla lista)
- [x] Al menos 1 entrevista de cada perfil A y B realizada
- [ ] Primeras respuestas de la encuesta cargadas y analizadas
- [ ] Hallazgos volcados en `usuarios.md` y contrastados contra `problema.md` y
      `requerimientos-funcionales-mvp.md`
