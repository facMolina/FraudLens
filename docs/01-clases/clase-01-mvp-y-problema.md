# Clase 01 — Presentación de la materia · MVP · Problema · Equipos

| | |
|---|---|
| **Fecha** | ⬜ *(completar)* |
| **Docente** | Daniel Britez |
| **Material** | `001__SIP_Clase__01Vp_MVP_v1.2_1.pdf` (51 diapositivas) |
| **Cargada por** | Facundo Molina |
| **Fecha de carga** | 2026-09-01 |

---

## 1. De qué se trató

Clase de apertura. El docente define qué es el TIF/SIP, cuál es el objetivo de la materia
(**construir un MVP**), cómo se va a trabajar durante el cuatrimestre, cómo se evalúa, y arranca con
el primer tema de fondo: **qué es un problema y cómo se define uno**.

El mensaje central de la clase es que esta materia **no enseña contenido nuevo**: integra todo lo que
ya vimos en la carrera para gestionar un proyecto tecnológico real, con exigencia profesional. Y que
el trabajo **no se hace sólo en el horario de clase**.

Dos ideas conceptuales cierran la clase: la **brecha de innovación** (la paradoja de la maleta) y el
**pensamiento lateral** (el poder de lo opuesto).

---

## 2. Conceptos

### TIF / SIP
Una **instancia de aprendizaje que se convierte en el puente entre la vida académica y la
profesional**. El aprendizaje se fomenta mediante la **ejecución de un proyecto informático**, con
nivel de exigencia muy cercano al que enfrentaremos en el mundo profesional.

### Objetivo de la materia
Construir un **MVP de un producto digital**, con funcionalidades que aporten valor a una empresa o a
una necesidad general, como un emprendimiento.

### MVP — Minimum Viable Product
La **versión elemental** de un producto: aquella que reúne sus funcionalidades y atributos básicos
para ser lanzada al mercado.

- Utiliza los **comentarios reales de los clientes** para mejorar versiones posteriores.
- Sirve para **"probar las aguas"** antes de comprometer tiempo y dinero con un producto final complejo.

**Ejemplos que dio la clase:**

| | MVP | NO MVP |
|---|---|---|
| **Amazon** | Tienda en línea para compra/venta de **libros** con entrega a domicilio | Prime · Prime Video · AWS · Kindle |
| **Instagram** | App para subir y compartir fotos con **filtros básicos** | Stories · Reels · Mensajes directos · Grupos |
| **Uber (UberCab)** | Reservar y pagar un viaje en auto vía iPhone/Smartphone, SMS o web — **sólo disponible en San Francisco** | Ubicación en tiempo real de conductores · Compartir ubicación con contactos · Viajes compartidos · Estimación de tarifas |

El caso Uber es el más ilustrativo: el MVP no sólo recorta funcionalidades, **recorta el alcance
geográfico**. Una ciudad, una función.

> 🎯 **Aplicado a FraudLens:** nuestro MVP tiene que ser *"recibir una transacción y devolver su
> nivel de riesgo, y poder verlo en una pantalla"*. Todo lo demás —reentrenamiento automático,
> múltiples clientes, alertas, integraciones con procesadores reales, panel de administración— es
> **NO MVP**. Escribir esa lista explícita nos protege de la ambición: es el error clásico de esta
> materia.

### Los cuatro ejes: Producto, Metodología, Seguimiento, User Research

| Eje | Definición del docente |
|---|---|
| **Producto** | Servicio que vamos a producir con el propósito de **satisfacer una necesidad del usuario** |
| **Metodología** | Planificamos el desarrollo de la idea enmarcada en **lineamientos ágiles** |
| **Seguimiento** | Reuniones basadas en lineamientos ágiles (Daily, Weekly, Review, Retrospectivas) |
| **User Research** | Acceso a información sobre el problema — **deben ser datos reales** |

> 🎯 **Aplicado a FraudLens:** "datos reales" es la exigencia que más nos puede complicar. El fraude
> es un dominio donde los datos son sensibles y las empresas no los comparten. Hay que resolver
> temprano de dónde salen los datos del User Research **y** los datos de entrenamiento del modelo.
> Ver [P-06](../00-proyecto/preguntas-abiertas.md#p-06).

### Pasos para definir el producto

1. **Problema** — mínimo **1 problema por integrante**; junto a los docentes se selecciona 1. Puede ser
   una problemática de una empresa pública, privada, un problema propio o de terceros.
2. **User Research** — investigar más sobre la problemática con diversas técnicas de UX.
3. **Solución** — se proponen ideas y se selecciona una para trabajar **todo el cuatrimestre**.
4. **Producto** — proceso de creación del producto digital.

### Cómo se conoce un problema
Encuestas · Entrevistas (en persona u online) · Observación · Reviews · Focus Group · Analytics ·
Reportes de otros departamentos (Marketing, Finanzas, etc.).

### Grupo vs. Equipo

| Grupo | Equipo |
|---|---|
| Objetivos individuales | Objetivos compartidos |
| Responsabilidad individual | Responsabilidad individual **y mutua** |
| Éxito o fracaso individual | Éxito o fracaso **colectivo** |

### La brecha de innovación — la paradoja de la maleta
La rueda existe desde **3500 A.C.** La maleta, desde **600 D.C.** La **maleta con ruedas** apareció
recién en **1970**. Dos tecnologías conocidas convivieron milenios sin que nadie las integrara para
resolver el esfuerzo de cargar peso.

> 🎯 **Aplicado a FraudLens:** este es literalmente nuestro caso y conviene usarlo en el pitch. Los
> motores de reglas antifraude existen hace décadas. El machine learning también. Nuestro aporte no
> es inventar una pieza: es **integrarlas** de una forma que hoy no está resuelta para el usuario
> que elijamos. Es un argumento fuerte y sale directamente del material del docente.

### El poder de lo opuesto — pensamiento lateral
Para cada idea lógica o "brillante", existe una idea **opuesta** que también puede ser válida,
desafiando las suposiciones fundamentales.

> *"El pensamiento lateral surge al reconocer que la verdad es una cuestión de perspectiva."*

Ejemplos de la clase: sistemas de direcciones (EE.UU. nombra las calles / Japón nombra las manzanas);
modelos de negocio en salud (se paga cuando hay enfermedad / los médicos cobran cuando estás sano y
dejan de cobrar cuando enfermás); la ubicación del "uno" en un compás musical.

> 🎯 **Aplicado a FraudLens:** el enfoque lógico es *"detectar fraude"*. El opuesto es
> *"certificar transacciones legítimas"* — en vez de buscar al 0,1% malo, acelerar al 99,9% bueno.
> Cambia el usuario, la métrica y el discurso. Vale la pena ponerlo sobre la mesa antes de cerrar la
> solución, aunque después lo descartemos.

### Detective de problemas
Un ingeniero no sólo debe saber programar: debe ser un **"detective de problemas"**, capaz de
enfrentarse a desafíos ambiguos con una **metodología sólida**. (Anécdota de Ann Hiatt en su
entrevista con Jeff Bezos: *"¿cuántos paneles de vidrio hay en la ciudad de Seattle?"*).

---

## 3. Aplicación a FraudLens

| Qué | Por qué | Dónde se refleja |
|---|---|---|
| Escribir el **MVP y el NO MVP** explícitos | Es el criterio con que se evalúa el producto y evita que nos vayamos de alcance | [`docs/05-producto/problema.md`](../05-producto/problema.md) |
| Definir **de dónde salen los datos reales** | Exigencia explícita del docente, y en fraude es lo más difícil de conseguir | [P-06](../00-proyecto/preguntas-abiertas.md#p-06) |
| Preparar las **propuestas de problema** | La Clase 1 pide mínimo 1-2 por integrante aunque ya hayamos cargado la planilla | [P-02](../00-proyecto/preguntas-abiertas.md#p-02) |
| Confirmar el **tamaño del equipo** | La clase pide 6-8 integrantes y somos 4 | [P-03](../00-proyecto/preguntas-abiertas.md#p-03) |
| Cargar el **calendario 2C 2026** | El deck trae fechas de 1C; sin fechas reales no se planifica | [P-04](../00-proyecto/preguntas-abiertas.md#p-04) |
| Ordenar el **tablero de Trello** | Los tableros son un ítem de evaluación | [`docs/04-metodologia/trello.md`](../04-metodologia/trello.md) |
| Usar la **paradoja de la maleta** en el relato del proyecto | Es un argumento del propio docente que encaja perfecto con FraudLens | Pitch / Primera Entrega |

**Chequeo contra "Problemas que NO":** el docente descartó reservas, estacionamiento, viajes,
colas/turnos, tiendas online, pagos de colegio/renta, gestión de gastos, historia clínica, ABMs
(biblioteca, taller, edificio), mascotas/refugios, gimnasios, trackeo y recetas de cocina.
**FraudLens no cae en ninguna.** ✅

---

## 4. Qué tenemos que hacer para la próxima

Tal como lo pidió la clase:

| Tarea | Responsable | Fecha límite | Trello |
|---|---|---|---|
| **Tarea de Teams:** Narrativa de Propuestas de Problema (al menos **2 por integrante**) | Cada uno | ⬜ | ⬜ |
| **Conformar los equipos de trabajo** | Equipo | ⬜ | ⬜ |
| **Presentación de Avance:** listado de problemas priorizados por relevancia (votar), en **1:30 min** | Equipo | ⬜ | ⬜ |

---

## 5. Dudas que quedaron

- ¿La planilla ya cargada reemplaza la entrega de propuestas de problema, o hay que llevarlas igual?
  → [P-02](../00-proyecto/preguntas-abiertas.md#p-02)
- ¿El equipo de 4 es válido o hay que fusionarse? → [P-03](../00-proyecto/preguntas-abiertas.md#p-03)
- ¿Cuáles son las fechas reales del 2C 2026? → [P-04](../00-proyecto/preguntas-abiertas.md#p-04)

---

## 6. Términos nuevos para el glosario

- [x] TIF/SIP
- [x] MVP
- [x] Producto · Metodología · Seguimiento · User Research
- [x] Grupo vs. Equipo
- [x] Brecha de innovación
- [x] Pensamiento lateral / El poder de lo opuesto
- [x] Detective de problemas
- [x] The Pitch
