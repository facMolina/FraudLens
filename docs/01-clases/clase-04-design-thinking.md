# Clase 04 — Design Thinking · User Research

| | |
|---|---|
| **Fecha** | ⬜ *(completar)* |
| **Docente** | Daniel Britez |
| **Material crudo** | [`material/clase-04-design-thinking.md`](material/clase-04-design-thinking.md) |
| **Cargada por** | Facundo Molina |
| **Fecha de carga** | 2026-09-02 |

> ✅ El material de esta clase se convirtió bien. Es la clase **más densa y más aplicable** de las
> cuatro, y de acá salen los pendientes para la Clase 5.

---

## 1. De qué se trató

Agenda del deck:

| # | Bloque |
|---|---|
| 01 | Repaso — ¿qué vimos la clase pasada? |
| 02 | **Presentaciones** — los equipos presentan la problemática elegida |
| 03 | **Design Thinking** — User Persona, Mapa de Empatía, Escenario Actual, User Journey Map |
| 04 | **User Research** — encuestas, entrevistas y observaciones |
| 05 | Teamwork MVP |
| 06 | Entregable para la próxima clase |

Es la clase que baja el "hay que investigar al usuario" a **herramientas concretas**.

**Qué pasó en esta clase con nuestro equipo:** trabajamos en el **documento de requerimientos
funcionales del MVP** (el que escribió Francisco) y definimos el nombre **FraudLens**.

> ⚠️ Esto significa que **las herramientas de Design Thinking de esta clase todavía no se aplicaron
> a FraudLens**. Es el pendiente más grande del proyecto.

---

## 2. Conceptos

### Design Thinking

> Metodología **centrada en el usuario** para la resolución de problemas complejos, que busca
> generar soluciones innovadoras mediante un enfoque **iterativo y no lineal**. Se basa en la
> **empatía**, la **creatividad** y la **experimentación** para entender las necesidades de las
> personas y crear productos o servicios que realmente las satisfagan.

**Relación con User Research:**

> Design Thinking es la **metodología completa**. User Research es la **herramienta clave** para
> conocer al usuario y tomar decisiones basadas en evidencia. **User Research es la base de la
> etapa "EMPATIZAR"** en Design Thinking.

### El proceso — no es una línea recta

**Empatizar** (Entender) → **Definir** (Enfocar) → **Idear** (Explorar) → **Prototipar** (Construir) → **Testear** (Aprender)

### Por qué importa

> **El 90% de las startups fallan no por mal código, sino por crear algo que nadie necesita.**

> Construir la cosa correcta *(eficiencia)* sin saber si es la cosa adecuada *(eficacia)* =
> **esfuerzo desperdiciado**.

### La Trinidad del Desarrollo de Software

| Eje | Pregunta |
|---|---|
| **Deseabilidad** (Humanos) | ¿Lo quieren? |
| **Factibilidad** (Tecnología) | ¿Podemos programarlo? |
| **Viabilidad** (Negocio) | ¿Tiene sentido financiero? |

La intersección de las tres = **Innovación / Tu MVP**.

### Design Thinking · Lean Startup · Agile

| | Design Thinking | Lean Startup | Agile |
|---|---|---|---|
| **Rol** | Explorar el Problema | Validar el Negocio | Construir la Solución |
| **Qué hace** | Descubrir **QUÉ** construir a través de la empatía | Validar **SI TIENE SENTIDO** mediante experimentos (MVP) | Ejecutar **CÓMO** construirlo con excelencia (Sprints) |

> **Design Thinking asegura que estás construyendo el producto correcto; Agile asegura que lo estás
> construyendo correctamente.**

### Las 5 etapas

#### 1. Empatizar: "Salí de tu IDE"

> **Tu usuario no es un algoritmo.**

- Olvidá la base de datos por un momento.
- Observá, escuchá e interactuá **sin juzgar**.
- Identificá los verdaderos puntos de dolor (*pain points*).

> 🎯 **Misión MVP del deck:** *"Entrevistá a 5 personas reales que sufran el problema que intenta
> resolver tu proyecto. **Escuchá el 80% del tiempo.**"*

#### 2. Definir: "Encontrá la aguja en el pajar"

- Sintetizá el ruido de tus entrevistas.
- Encontrá patrones en las frustraciones.
- Definí un **problema específico**.

**La fórmula mágica: "¿Cómo podríamos nosotros…?"**

| ❌ En lugar de | ✅ Definí |
|---|---|
| "Hacer una app de dietas" | "¿Cómo podríamos ayudar a **estudiantes universitarios sin tiempo** a planificar comidas saludables **con presupuesto limitado**?" |

#### 3. Idear: "Pensá fuera de la consola"

- **Cantidad sobre calidad.** Cero código, máxima creatividad.
- Generá soluciones **descabelladas** antes de aplicar filtros de factibilidad técnica.
- Combiná ideas divergentes.

#### 4 y 5. Prototipar y Testear

> **Fallá antes de programar.**

- Prototipo = mockups (por ejemplo en Figma). **No es software terminado.**
- Buscá feedback **brutalmente honesto**.

> Un prototipo te cuesta **días**. Un MVP programado te cuesta **meses**.
> Descubrí si tu idea es mala **en días**.

### IA generativa como co-piloto de diseño

| Fase | Herramienta | Acción |
|---|---|---|
| 1 — Empatizar | LLMs (ChatGPT / Claude) | Sintetizar horas de transcripciones de entrevistas en patrones clave |
| 2 — Definir | IA analítica | Agrupar puntos de dolor y generar variaciones de la pregunta "¿Cómo podríamos…?" |
| 3 — Idear | ChatGPT | Compañero de brainstorming: 100 variaciones de tu MVP en 30 segundos |
| 4 — Prototipar | *(herramientas de diseño)* | Pasar de boceto en papel a pantalla |

> **La IA acelera la síntesis y la creación, pero la empatía y la validación final siempre requieren
> humanos reales.**

### Los gigantes también lo hacen

| Empresa | Qué hizo |
|---|---|
| **Apple** | Centró el diseño del iPhone original en la **intuición humana** (interfaz táctil fluida), no en las especificaciones brutas del hardware |
| **Airbnb** | Pasó de estar al borde de la quiebra a valer miles de millones al **dejar la pantalla**, volar a Nueva York y rediseñar la experiencia fotográfica del huésped |
| **IBM** | Invirtió masivamente en Enterprise Design Thinking: **ROI del 300%** y tiempo de salida al mercado a la mitad (**75% más rápidos**) |

---

### User Persona

Representación del usuario tipo. **¿Qué información completamos?**

- ¿Cómo es? ¿Cómo es su día a día?
- ¿Cuáles son sus gustos y disgustos?
- ¿Cuáles son sus miedos y fortalezas?
- ¿Qué es lo que más le importa en su vida? ¿A qué aspira?
- ¿Cómo es su tiempo de ocio/esparcimiento? ¿Qué le gusta hacer?

**Ejemplo del deck — "Chiara":**

| Bloque | Contenido |
|---|---|
| **Características** | Edad: 23 años · Soltera, vive con sus padres, tiene un hermano · Estudiante de Lic. en Comercialización · Intereses: viajar, aprender cosas nuevas, emprender, hacer deporte · Localización: CABA |
| **Momento / Escenario** | Mantuvo sus estudios con ahorros de una herencia familiar. Está en el último año y quiere dedicarle la mayor parte del tiempo. Necesita conocer estrategias de mercadeo emergentes para su nuevo emprendimiento. Los fondos se están acabando |
| **Motivaciones** | Le gusta viajar y ser independiente. Quisiera tener su propio emprendimiento y ser su propia jefa. Poner en práctica lo aprendido. Necesita una entrada de dinero para independizarse |

> Nótese que el ejemplo tiene **tres bloques**: características, momento/escenario y motivaciones.
> Ese es el formato que espera el docente.

### Mapa de Empatía

> Herramienta que nos ayuda a entender y empatizar en profundidad con nuestras
> personas/potenciales clientes/usuarios. Nos permite **"ponernos en los zapatos"** de la persona
> que definimos, relacionándonos con sus sentimientos y emociones.

**Los cuadrantes:**

| Cuadrante | Qué se responde |
|---|---|
| **¿Qué PIENSA Y SIENTE?** | Lo que realmente le importa · principales preocupaciones · inquietudes y aspiraciones · lo que no dice |
| **¿Qué OYE?** | Lo que dicen sus amigos y su familia · lo que dice el jefe · las personas influyentes · a qué medios presta atención |
| **¿Qué VE?** | Su entorno · sus amigos · **la oferta del mercado** · qué tipo de problemas enfrenta |
| **¿Qué DICE Y HACE?** | Actitud en público · comportamiento hacia los demás · **si hay diferencias entre lo que dice y lo que piensa** |
| **ESFUERZOS / ¿Qué lo FRUSTRA?** | Miedos · frustraciones · obstáculos en su camino |
| **RESULTADOS / ¿Qué lo MOTIVA?** | Deseos y necesidades · qué es el éxito para él o ella · qué quiere conseguir |

### Escenario Actual / AS-IS

> Nos sirve para entender **cómo se comporta nuestra persona con el proceso** e identificar sus
> **puntos de dolor**.
>
> **¡La solución que seleccionemos debe pasar por estos puntos de dolor!**
>
> Nos muestra cómo se siente, qué hace y qué dice el usuario en términos de experiencia.

Se arma por etapas (Etapa 1 → Etapa 2 → Etapa 3 → Etapa 4).

### User Journey Map

> También llamado **Customer Journey Map**. Es un mapa donde se plasman **todas las etapas por las
> cuales pasa nuestro usuario/cliente durante todo un ciclo de compra / potencial compra**.
>
> Aunque parece obvio, analizar en detalle cada etapa del proceso permite **identificar puntos de
> dolor y mejoras**. Tiene como objetivo **determinar cómo se sienten los clientes**.

Ejemplo del deck (ir al cine): Llegada → Fila de espera → Registro → Entrada → Golosinas → Baños →
Retirar película → Inicio de la película.

---

### User Research: encuestas

#### El orden de las preguntas importa

- **Preguntas demográficas**: al principio o al final. Elegirlas cuidadosamente. **Preferir evitarlas.**
- **Chequear la pregunta de la "respuesta ideal"** — preguntas que inducen la respuesta:
  - ❌ *"El café es rico"*
  - ❌ *"La atención es mala"*

#### Buenas prácticas

**Elegir bien las respuestas.** Agregar *"Otros"* y *"NS/NC"*.

| ❌ Pobre | ✅ Mejor |
|---|---|
| ¿Tomás café? Sí / No | Todos los días / Algunas veces a la semana / Algunas veces al mes / Cada algunos meses / Nunca |

> **NS/NC** significa *"No Sabe / No Contesta"*. Es una opción de respuesta usada cuando el
> encuestado desconoce la información (NS) o prefiere no responder (NC), permitiendo finalizar la
> encuesta sin forzar una opinión — lo cual **mejora la calidad de los datos** al evitar respuestas
> aleatorias.

**Limitar las preguntas abiertas:**
- Hacerlas opcionales
- Dificultad de análisis
- Consumen mucho tiempo de quien responde
- Dan lugar a que la gente "se desubique"

**No agregar información que desvíe la atención de la pregunta.**

**Rangos de respuestas impares (3, 5 o 7 opciones):**
- Muy satisfecho / Algo satisfecho / Ni satisfecho ni insatisfecho / Algo insatisfecho / Muy insatisfecho
- De acuerdo / Ni de acuerdo ni en desacuerdo / En desacuerdo

Permiten **"balance"**: puntos extremos y punto medio neutro. **Ordenar** las respuestas y mantener ese orden.

#### Recomendaciones

- **Anonimizar** las respuestas.
- **Crear "clases" de variables continuas:**
  - Edad: menor de 18 · 19 a 25 · 26 a 35 · 36 a 45…
  - Puntajes: 1 a 3 · 4 a 7 · 7 a 10…
- **Agrupar "outliers" en "otros"**: Doctor/a (10), Ingeniero/a (5), Biólogo/a marino/a (1), Físico/a cuántico/a (1) → Otros (2)
- **Ser claro con la persona encuestada** al respecto → mejora cantidad y calidad de respuestas.

### Entrevistas y observación

El deck dedica secciones a **entrevistas** y **observación** pero son casi enteramente visuales;
no hay texto de definición recuperable.

> ⚠️ **Hueco:** las buenas prácticas de entrevista y observación no se pueden reconstruir del
> material. **A completar con apuntes de clase.**

---

## 3. Aplicación a FraudLens

| Qué | Por qué | Estado |
|---|---|---|
| **Entrevistar a 5 personas reales que sufran el problema** | Es la consigna literal del deck para la etapa Empatizar | 🔲 |
| Reformular el problema como **"¿Cómo podríamos nosotros…?"** | Obliga a nombrar al usuario y su restricción concreta. Hoy nuestro enunciado describe una oportunidad tecnológica, no un usuario con un dolor | 🔲 |
| **User Persona** de al menos 3 posibles usuarios | Consigna para la Clase 5 | 🔲 |
| **Mapa de Empatía** de esos 3 usuarios | Consigna para la Clase 5 | 🔲 |
| **Escenario Actual / AS-IS** | *"La solución que seleccionemos debe pasar por estos puntos de dolor"* — es el puente entre el research y el producto | 🔲 |
| **Encuesta difundida — 400 respuestas** | Consigna para la Clase 5 | 🔲 |

> ⚠️ **Punto a mirar de frente.** El deck dice que Design Thinking sirve para
> *"resolver problemas complejos **antes de escribir la primera línea de código**"*, y que el 90% de
> las startups fallan **por construir algo que nadie necesita**.
>
> Nuestro equipo, en esta clase, escribió los **requerimientos funcionales del MVP** — es decir,
> definió **la solución** antes de hacer el research que define **el problema**.
>
> Esto no está "mal" y el documento de Francisco es bueno y detallado. Pero hay que decidir
> conscientemente qué hacemos: si el User Research contradice lo que asumimos ahí, **el research
> gana** — esa es la lógica que el docente evalúa. Es el punto 6 de la lista de revisión del
> [documento de requerimientos](../05-producto/requerimientos-funcionales-mvp.md#puntos-a-discutir-en-equipo).

---

## 4. Qué pidió para la próxima clase

Textual del deck:

| Tarea | Detalle |
|---|---|
| **Armar y realizar la difusión de encuestas, entrevistas y observaciones** | **400 respuestas en total** |
| **Design Thinking de al menos 3 posibles usuarios** | User Persona · Mapa de Empatía · Escenario Actual |

> 🔴 **Estos son los pendientes para la Clase 5.** Ninguno está hecho.
> **400 respuestas no se juntan en dos días** — la difusión de la encuesta tiene que arrancar ya.

---

## 5. Dudas que quedaron

- ¿Las 400 respuestas son **sólo de la encuesta** o suman encuestas + entrevistas + observaciones?
  → [P-17](../00-proyecto/preguntas-abiertas.md#p-17)
- ¿Los 3 usuarios del Design Thinking son 3 **personas entrevistadas** o 3 **perfiles/segmentos** distintos?
  → [P-18](../00-proyecto/preguntas-abiertas.md#p-18)
- Buenas prácticas de entrevista y observación *(hueco del material)*

---

## 6. Términos nuevos para el glosario

- [x] Design Thinking (5 etapas)
- [x] La Trinidad: Deseabilidad · Factibilidad · Viabilidad
- [x] User Persona
- [x] Mapa de Empatía
- [x] Escenario Actual / AS-IS
- [x] User Journey Map / Customer Journey Map
- [x] "¿Cómo podríamos nosotros…?"
- [x] NS/NC
