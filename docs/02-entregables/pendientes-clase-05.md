# Pendientes para la Clase 5 — tickets listos para cargar en Trello

> **Estado:** 🟡 redactados, **sin cargar** — falta conectar el conector de Trello.
> Ver [`docs/04-metodologia/trello.md`](../04-metodologia/trello.md#cómo-conectar-trello-a-claude).
>
> **Fuente:** lámina *"Para la próxima clase…"* de la [Clase 4](../01-clases/clase-04-design-thinking.md#4-qué-pidió-para-la-próxima-clase).
> La Clase 5 **es la próxima** — todavía no se dio.

## Lo que pidió el docente, textual

| Tarea | Detalle |
|---|---|
| Armar y realizar la difusión de **encuestas, entrevistas y observaciones** | **400 respuestas en total** |
| **Design Thinking** de al menos **3 posibles usuarios** | User Persona · Mapa de Empatía · Escenario Actual |

⚠️ **Ninguna de las dos está empezada.**

---

## ⛔ Antes de crear los tickets: dos cosas a resolver

Estos tickets **no se pueden dimensionar bien** hasta cerrar dos ambigüedades de la consigna:

| Duda | Por qué bloquea |
|---|---|
| [P-17](../00-proyecto/preguntas-abiertas.md#p-17) — ¿400 respuestas **de encuesta**, o 400 sumando las tres técnicas? | Cambia el esfuerzo de difusión por completo |
| [P-18](../00-proyecto/preguntas-abiertas.md#p-18) — ¿3 **perfiles distintos** o 3 **personas entrevistadas**? | Si son 3 perfiles, primero hay que decidir cuáles ([P-07](../00-proyecto/preguntas-abiertas.md#p-07)) |

Y una decisión de equipo previa: **¿quiénes son nuestros 3 usuarios candidatos?**
El [documento de FGR](../05-producto/requerimientos-funcionales-mvp.md) propone *analista de fraude*,
*administrador* y *sistema cliente*, pero **eso no está decidido** — está en revisión.

---

## Tickets propuestos

> Formato listo para pegar en Trello. Los responsables van vacíos: los reparte el equipo.

### 🎯 Bloque A — Definición previa *(hay que hacerlo primero)*

> 🎩 **Todas las tarjetas de decisión llevan análisis de [6 Sombreros](../04-metodologia/seis-sombreros.md)** —
> consigna del docente. El de A1 ya está hecho:
> [`analisis/6-sombreros-usuario-objetivo.md`](../05-producto/analisis/6-sombreros-usuario-objetivo.md)

#### A1 · Decidir los 3 perfiles de usuario a investigar
- **Etiqueta:** 🟢 Producto · ⚫ Gestión
- **Qué hay que hacer:** reunión corta de equipo para elegir los 3 posibles usuarios sobre los que se harán User Persona, Mapa de Empatía y Escenario Actual.
- **Listo cuando:**
  - [ ] Los 3 perfiles están escritos en `docs/05-producto/usuarios.md`
  - [ ] Queda registrado por qué se eligieron esos y no otros
- **Bloquea a:** B1, B2, B3, C1

#### A2 · Consultar al docente las dos dudas de la consigna
- **Etiqueta:** 🟣 Clase
- **Qué hay que hacer:** preguntar (Teams o al inicio de clase) si las 400 respuestas son sólo de encuesta o del total, y si los 3 usuarios son perfiles o personas.
- **Listo cuando:**
  - [ ] Las respuestas están cargadas en `preguntas-abiertas.md` (P-17 y P-18)
- **Bloquea a:** C1

---

### 🎯 Bloque B — Design Thinking *(uno por cada perfil)*

#### B1 · User Persona × 3 perfiles
- **Etiqueta:** 🟡 User Research · 🔴 Entrega
- **Qué hay que hacer:** una User Persona por perfil, con el formato del docente: **Características** (edad, familia y relaciones, ocupación, intereses/hobbies, localización) · **Momento/Escenario** · **Motivaciones**.
- **Referencia:** ejemplo "Chiara" en la [nota de Clase 4](../01-clases/clase-04-design-thinking.md#user-persona)
- **Listo cuando:**
  - [ ] 3 User Persona completas, con los 3 bloques cada una
  - [ ] Cargadas en `docs/05-producto/usuarios.md`

#### B2 · Mapa de Empatía × 3 perfiles
- **Etiqueta:** 🟡 User Research · 🔴 Entrega
- **Qué hay que hacer:** completar los 6 cuadrantes por perfil: ¿Qué piensa y siente? · ¿Qué oye? · ¿Qué ve? · ¿Qué dice y hace? · Esfuerzos (miedos, frustraciones, obstáculos) · Resultados (deseos, medida del éxito).
- **Listo cuando:**
  - [ ] 3 mapas completos, sin cuadrantes vacíos

#### B3 · Escenario Actual / AS-IS × 3 perfiles
- **Etiqueta:** 🟡 User Research · 🔴 Entrega
- **Qué hay que hacer:** mapear por etapas cómo el usuario enfrenta **hoy** el problema del fraude, marcando los **puntos de dolor**.
- **Ojo:** *"la solución que seleccionemos debe pasar por estos puntos de dolor"*. Este es el puente entre el research y el producto.
- **Listo cuando:**
  - [ ] 3 escenarios por etapas, con puntos de dolor identificados

---

### 🎯 Bloque C — User Research *(lo más pesado — arrancar ya)*

#### C1 · Diseñar la encuesta
- **Etiqueta:** 🟡 User Research
- **Qué hay que hacer:** redactar la encuesta aplicando las buenas prácticas de la Clase 4.
- **Checklist de calidad** (de la clase):
  - [ ] Sin preguntas de "respuesta ideal" (que inducen la respuesta)
  - [ ] Preguntas demográficas al principio o al final, y sólo las necesarias
  - [ ] Preguntas abiertas limitadas y opcionales
  - [ ] Rangos de respuesta **impares** (3, 5 o 7) con punto medio neutro
  - [ ] Respuestas ordenadas y con orden mantenido
  - [ ] Opciones "Otros" y "NS/NC" donde corresponda
  - [ ] Se aclara que las respuestas son anónimas
- **Listo cuando:**
  - [ ] Encuesta publicada en un formulario, con link
  - [ ] Revisada por al menos otro integrante

#### C2 · Difundir la encuesta — meta 400 respuestas
- **Etiqueta:** 🟡 User Research · 🔴 Entrega
- **Qué hay que hacer:** difundir por todos los canales disponibles. **Con 4 integrantes son ~100 respuestas por persona.**
- **Listo cuando:**
  - [ ] Se alcanzó la meta de respuestas
  - [ ] Hay un registro de por qué canales se difundió
- ⚠️ **Este ticket es el de mayor riesgo del sprint.** No se resuelve en 48 horas.

#### C3 · Entrevistas — mínimo 5 personas
- **Etiqueta:** 🟡 User Research
- **Qué hay que hacer:** consigna literal de la Clase 4: *"Entrevistá a 5 personas reales que sufran el problema. Escuchá el 80% del tiempo."*
- **Listo cuando:**
  - [ ] 5 entrevistas hechas
  - [ ] Notas o transcripción de cada una guardadas en el repo
  - [ ] A quién se entrevistó y por qué, registrado

#### C4 · Observaciones
- **Etiqueta:** 🟡 User Research
- **Qué hay que hacer:** definir qué se puede observar del proceso real de revisión de transacciones y registrarlo.
- ⚠️ **A pensar:** en fraude, observar el trabajo real es difícil (es información sensible). Puede que haya que resolverlo distinto — conviene consultarlo con el docente.

#### C5 · Sintetizar los hallazgos
- **Etiqueta:** 🟡 User Research · 🔴 Entrega
- **Qué hay que hacer:** cruzar encuestas + entrevistas + observaciones y encontrar **patrones en las frustraciones** (etapa "Definir" de Design Thinking).
- **Listo cuando:**
  - [ ] Hallazgos escritos en `docs/05-producto/user-research.md`
  - [ ] El problema reformulado como **"¿Cómo podríamos nosotros…?"**
  - [ ] Se contrastó lo que dice el research contra lo que asume el [documento de FGR](../05-producto/requerimientos-funcionales-mvp.md)

---

### 🎯 Bloque D — Deuda de clases anteriores

#### D1 · Redacción del problema con segmentación y target
- **Etiqueta:** 🟠 Documentación · 🔴 Entrega
- **Origen:** consigna de la [Clase 2](../01-clases/clase-02-segmentacion-y-problema.md#4-qué-pidió-para-la-próxima-clase) — *"adelantan primer entregable"*
- **Estado:** ❓ a confirmar si ya se entregó → [P-13](../00-proyecto/preguntas-abiertas.md#p-13)

#### D2 · Árbol de Problemas de FraudLens
- **Etiqueta:** 🟠 Documentación
- **Origen:** Clases 2 y 3. El docente lo enseñó **dos veces** — es esperable que aparezca en el documento final.
- **Listo cuando:** causas → problema central → efectos, escrito en `docs/05-producto/problema.md`

#### D3 · Análisis 5 Por Qué
- **Etiqueta:** 🟠 Documentación
- **Origen:** Clases 2 y 3
- **Listo cuando:** la cadena de "por qué" está escrita hasta la causa raíz

---

### 🎯 Bloque E — Gestión del proyecto

#### E1 · Cargar el cronograma real del 2C 2026
- **Etiqueta:** ⚫ Gestión
- **Bloquea:** toda la planificación → [P-04](../00-proyecto/preguntas-abiertas.md#p-04)

#### E2 · Documentar el dataset de casos de prueba
- **Etiqueta:** 🔵 Desarrollo
- **Qué hay que hacer:** registrar cuál es, de dónde sale, cuántos registros tiene y si alcanza para entrenar o sólo para probar → [P-11](../00-proyecto/preguntas-abiertas.md#p-11)

#### E3 · Revisar en equipo el documento de requerimientos de FGR
- **Etiqueta:** 🟢 Producto
- **Qué hay que hacer:** decidir si se aprueba, se ajusta o se posterga hasta tener el research → [P-15](../00-proyecto/preguntas-abiertas.md#p-15)

#### E4 · Definir roles del equipo y rotación de Sprint Reviews
- **Etiqueta:** ⚫ Gestión
- **Origen:** [`docs/00-proyecto/equipo.md`](../00-proyecto/equipo.md#roles-a-repartir) → [P-08](../00-proyecto/preguntas-abiertas.md#p-08)

---

## Resumen

| Bloque | Tickets | Riesgo |
|---|---|---|
| A — Definición previa | 2 | Bajo, pero bloquea al resto |
| B — Design Thinking | 3 | Medio |
| C — User Research | 5 | 🔴 **Alto** — las 400 respuestas |
| D — Deuda anterior | 3 | Bajo |
| E — Gestión | 4 | Bajo |
| **Total** | **17** | |
