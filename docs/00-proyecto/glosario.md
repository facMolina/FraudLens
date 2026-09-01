# Glosario

Definiciones de referencia del proyecto. **Cada término indica de qué clase sale**, para poder
rastrearlo hasta la fuente.

Estado:
- ✅ **Visto** — el docente ya lo desarrolló, la definición es la de la clase.
- 🔜 **Anunciado** — aparece en el temario pero todavía no se dictó. La definición es provisoria.

---

## Marco general de la materia

### TIF / SIP ✅ *(Clase 1)*
Trabajo Integrador Final / Seminario Integrador Profesional. Una **instancia de aprendizaje que
funciona como puente entre la vida académica y la profesional**, ejecutando un proyecto informático
con nivel de exigencia cercano al del mundo profesional.

### MVP — Minimum Viable Product / Producto Mínimo Viable ✅ *(Clase 1)*
La **versión elemental** de un producto: aquella que reúne sus funcionalidades y atributos **básicos**
para ser lanzada al mercado.

Tres notas de la clase:
- Utiliza los **comentarios reales de los clientes** para mejorar las versiones posteriores.
- Sirve para **"probar las aguas"** antes de comprometer tiempo y dinero con un producto final complejo.
- No es "el producto con menos features". Es **el producto más chico que ya entrega valor**.

**Ejemplos de la clase:**

| Producto | MVP | NO MVP |
|---|---|---|
| Amazon | Tienda en línea para compra/venta de libros con entrega a domicilio | Prime, Prime Video, AWS, Kindle |
| Instagram | App para subir y compartir fotos con filtros básicos | Stories, Reels, Mensajes directos, Grupos |
| Uber | Reservar y pagar un viaje en auto vía iPhone/Smartphone, SMS o web — **sólo en San Francisco** | Ubicación en tiempo real, compartir ubicación, viajes compartidos, estimación de tarifas |

> 🎯 **Aplicado a FraudLens:** el MVP es *scorear una transacción y mostrar su riesgo*.
> NO son parte del MVP: reentrenamiento automático, multi-tenant, alertas por mail, panel de
> administración, integraciones con procesadores de pago reales.

### Producto ✅ *(Clase 1)*
Servicio que vamos a producir con el propósito de **satisfacer una necesidad del usuario**.

### User Research ✅ *(Clase 1)*
Acceso a información sobre el problema. Requisito explícito: **deben ser datos reales**.

Técnicas mencionadas para conocer un problema: **encuestas, entrevistas** (en persona u online),
**observación, reviews, focus group, analytics** y **reportes de otros departamentos**
(Marketing, Finanzas, etc.).

### Grupo vs. Equipo ✅ *(Clase 1)*

| Grupo | Equipo |
|---|---|
| Objetivos individuales | Objetivos compartidos |
| Responsabilidad individual | Responsabilidad individual **y mutua** |
| Éxito o fracaso individual | Éxito o fracaso **colectivo** |

### Brecha de innovación ✅ *(Clase 1 — "la paradoja de la maleta")*
La rueda existe desde el 3500 A.C. y la maleta desde el 600 D.C., pero la **maleta con ruedas**
recién apareció en **1970**. Dos piezas conocidas convivieron milenios sin que nadie las integrara.

> 🎯 **Aplicado a FraudLens:** el machine learning y los motores de reglas antifraude existen hace
> años por separado. El valor no está en inventar una pieza nueva, sino en **integrarlas bien**.

### Pensamiento lateral / El poder de lo opuesto ✅ *(Clase 1)*
Para cada idea lógica o "brillante", existe una idea **opuesta** que también puede ser válida,
desafiando las suposiciones fundamentales.

> *"El pensamiento lateral surge al reconocer que la verdad es una cuestión de perspectiva."*

Ejemplos de la clase: sistemas de direcciones (EE.UU. nombra calles / Japón nombra manzanas),
modelos de negocio en salud (se paga cuando hay enfermedad / los médicos cobran cuando estás sano),
y la ubicación del "uno" en un compás musical.

### Detective de problemas ✅ *(Clase 1)*
Un ingeniero no sólo debe saber programar: debe poder **enfrentar desafíos ambiguos con una
metodología sólida**. (Anécdota de la entrevista de Ann Hiatt con Jeff Bezos: *"¿cuántos paneles
de vidrio hay en Seattle?"*).

---

## Metodología ágil

### Sprint 🔜 *(Bloque 3)*
Iteración de trabajo de duración fija. El cursado tiene **4 sprints**.

### Sprint Review 🔜 *(Bloque 3)*
Instancia donde el equipo presenta los avances del sprint. **Los presentadores rotan semana a
semana.** Sólo se admite uno desaprobado y un ausente.

### Retrospectiva 🔜 *(Bloque 3)*
Reunión de fin de sprint donde el equipo revisa **cómo trabajó** (no qué construyó) y define mejoras.
Al cierre del cuatrimestre hay una **Big Retro**.

### Daily / Weekly ✅ *(Clase 1, mencionadas)*
Reuniones de seguimiento basadas en lineamientos ágiles.

### SCRUM · KANBAN · Historias de Usuario · Estimación de tareas 🔜 *(Bloque 2)*
Se dictan en el bloque de planificación. Definiciones a completar cuando se vean.

---

## Diseño y experiencia

### Design Thinking 🔜 *(Bloque 1)*
Metodología de diseño centrada en el usuario. Etapas del temario: **Research · Ideación · Prototipo**.

### UX / UI · Heurísticas 🔜 *(Bloque 2)*
Experiencia de usuario e interfaz. Hay un **Taller de Diseño UX/UI** en el Sprint 2.

### Segmentación de usuarios / Target 🔜 *(Clase 2)*
Definir a quién le hablamos.

---

## Estrategia y negocio

### Estrategia del Océano Azul 🔜 *(Bloque 1)*
Buscar mercados sin competencia directa en lugar de competir en mercados saturados.
Temas asociados: **Competencia** y **Diferenciación**.

### Benchmarking 🔜 *(Bloque 1)*
Comparación sistemática contra soluciones existentes.

### BMC — Business Model Canvas 🔜 *(Bloque 2)*
Lienzo de 9 bloques para describir el modelo de negocio.

### P&L — Profit & Loss 🔜 *(Bloque 2)*
Estado de resultados. En la materia: **estimación de costos** del proyecto.

### Roadmap 🔜 *(Bloque 1 / Management 3.0)*
Plan temporal de evolución del producto.

### Management 3.0 🔜
Enfoque de gestión centrado en las personas. Temas: **equipo de trabajo, roadmap, feedback**.

---

## Métricas

### KPI — Key Performance Indicator 🔜 *(Sprint 4)*
Indicador que mide el desempeño de algo que ya está ocurriendo.

### OKR — Objectives and Key Results 🔜 *(Sprint 4)*
Objetivo cualitativo + resultados clave medibles que indican si se alcanzó.

> Diferencia práctica: el **OKR** define a dónde querés llegar; el **KPI** mide cómo venís.

---

## Presentación

### The Pitch ✅ *(Clase 1)*
Presentación final: **presentación, defensa y demo con todos los integrantes del equipo**.
Hay un **Simulacro de The Pitch** previo. Quien no se presenta queda **ausente**.

### Storytelling · Oratoria · Demo 🔜 *(Bloque de presentaciones)*
Hay **Taller de Oratoria** y **Taller de Escritura** en el bloque de planificación.

---

## Términos del dominio (FraudLens)

> Estos **no** salen de las clases: son del dominio del problema. Se irán refinando con el
> User Research y las decisiones técnicas.

### Transacción
Operación individual a evaluar (monto, medio de pago, comercio, timestamp, ubicación, etc.).

### Score de riesgo
Valor que estima la probabilidad de que una transacción sea fraudulenta.

### Motor de reglas
Sistema tradicional de detección basado en condiciones predefinidas. El proyecto lo
**complementa**, no lo reemplaza.

### Falso positivo
Transacción legítima marcada como fraude. Molesta al cliente y le cuesta plata al comercio.

### Falso negativo
Fraude que pasa sin ser detectado.

> ⚠️ En detección de fraude los datos están fuertemente **desbalanceados** (los fraudes son una
> fracción mínima), por lo que *accuracy* no es una métrica válida. Habrá que decidir cuáles sí.
> Ver [P-06](preguntas-abiertas.md#p-06).
