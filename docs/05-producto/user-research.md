# Plan de research

| | |
|---|---|
| **Estado** | 🟡 Plan escrito — **falta ejecutarlo** |
| **Responsable** | ⬜ *(sin asignar en Trello)* |
| **Fecha** | 2026-09-10 |
| **Ticket** | [2. Plan de research](https://trello.com/c/EkjU3QyB) |
| **Entregable de** | Clase 5 (2/9) — vencido |

## Por qué este documento y no antes

El User Research está en **cero** desde que arrancó el proyecto: 0 entrevistas, 0 encuestas. Este
plan no inventa datos — define **cómo** se van a conseguir. Nada de lo que sigue reemplaza al
research real; es el instrumento para hacerlo.

Dos relojes corren sobre esto:

- **1° Parcial el 16/9.** El docente exige datos reales, no hipótesis.
- **La ventana de ML.** Confirmó acceso a analistas de fraude *"en las próximas 2 semanas"* desde el
  2/9 — se cierra alrededor del 16/9. Es el activo más escaso de todo el research: pocas entrevistas,
  no se repiten.

## A quién investigamos

Los 3 perfiles ya están decididos en [`usuarios.md`](usuarios.md), con la accesibilidad como
criterio explícito. No se vuelve a discutir acá:

| Perfil | Rol | Técnica | Por qué esa técnica |
|---|---|---|---|
| **A · Analista de fraude** | el que **decide** | Entrevista en profundidad | Necesitamos el *proceso* y las *excepciones* — no entra en un formulario |
| **B · Dueño de comercio chico** | el que **paga** | Entrevista | Accesible sin contactos especiales; conversación corta alcanza |
| **C · Consumidor** | el que **sufre** | Encuesta | Es el único perfil donde el volumen es alcanzable, y lo que buscamos (frecuencia de un evento raro) necesita **n** grande |

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

### Entrevista — Perfil B (dueño de comercio / e-commerce chico)

**Objetivo:** cuantificar el dolor en plata real, y sin equipo antifraude de por medio.

**Guía de temas:**

1. ¿Tenés hoy algún sistema o proceso para prevenir fraude? ¿Cuál, o por qué no?
2. ¿Cuánto estimás que perdiste el último año en contracargos o ventas fraudulentas?
3. De los dos errores — rechazar una venta buena o dejar pasar un fraude — ¿cuál te duele más y
   por qué?
4. ¿Pagarías por una herramienta que te ayude con esto? ¿Cuánto te parecería razonable?

### Encuesta — Perfil C (consumidor)

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
- **Entrevistas (perfil A):** contactos de ML en el rubro.
- **Entrevistas (perfil B):** contactos personales del equipo con comercios chicos o e-commerce
  propio; si no hay, grupos de Facebook/WhatsApp de vendedores de plataformas como Tiendanube o
  Mercado Shops.

## Cronograma de ejecución

| Cuándo | Qué |
|---|---|
| Ya | Armar y revisar en equipo la guía de entrevista del perfil A (no hay margen para improvisar) |
| Antes del 16/9 | Difundir la encuesta del perfil C — cuanto antes, porque las respuestas tardan días en juntarse |
| Antes del 16/9 | Al menos 1 entrevista con analista de fraude (vía ML), antes de que se cierre la ventana |
| Antes del 16/9 | Al menos 1 entrevista con dueño de comercio chico |
| Con los resultados | Cargar hallazgos en `usuarios.md` (User Persona, Mapa de Empatía) y corregir `problema.md` si hace falta |

## Qué hacemos con lo que salga

Regla ya escrita en [`usuarios.md`](usuarios.md#-el-sesgo-que-hay-que-vigilar): si el research
contradice los [requerimientos funcionales](requerimientos-funcionales-mvp.md) o las 3
reformulaciones de [`problema.md`](problema.md), se corrigen esos documentos — no el research.

## Listo cuando

- [ ] Guía de entrevista del perfil A revisada por el equipo
- [ ] Encuesta del perfil C armada y **difundida** (no alcanza con tenerla lista)
- [ ] Al menos 1 entrevista de cada perfil A y B realizada
- [ ] Primeras respuestas de la encuesta cargadas y analizadas
- [ ] Hallazgos volcados en `usuarios.md` y contrastados contra `problema.md` y
      `requerimientos-funcionales-mvp.md`
