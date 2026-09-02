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

## Segmentación y problema *(Clases 2 y 3)*

### Segmentación demográfica ✅ *(Clase 2)*
Responde a la pregunta **¿quién es nuestro cliente?** Se basa en variables como **edad, género,
tamaño de familia, ingresos, ocupación, religión, raza y nacionalidad**.

> El docente muestra que **no alcanza sola**, con el contraste **Príncipe Carlos vs. Ozzy Osbourne**:
> mismos datos demográficos, personas completamente distintas.

### Segmentación por comportamiento ✅ *(Clase 2)*
Divide a la población según su **comportamiento, uso y hábitos**.

> 🎯 **Aplicado a FraudLens:** es la segmentación que nos sirve. Nuestro usuario no se define por
> edad ni ingresos, sino por **qué hace** con las transacciones.

### Segmentación geográfica ✅ *(Clase 2)*
Divide según ubicación. Ejemplo del deck: las ediciones locales de **Vogue**.

### Árbol de Problemas ✅ *(Clases 2 y 3)*
Herramienta que separa **causas** → **problema central** → **efectos/consecuencias**.

Ejemplo del deck: *Frecuentes accidentes de ómnibus* como problema central, con causas
(conductores imprudentes, vehículos en malas condiciones, calles en mal estado) y efectos
(pérdida de confianza, pasajeros heridos, pasajeros que llegan tarde).

### Fuentes de un problema ✅ *(Clases 2 y 3)*
Necesidades insatisfechas · Debilidades de la competencia · Feedback de usuarios · Innovación/Tecnología.

### 5 Por Qué (5 Why) ✅ *(Clases 2 y 3)*
Análisis de causa raíz proveniente de **Lean**: preguntar "¿por qué?" repetidamente hasta llegar a
la causa de fondo.

> *"No debemos dejarnos engañar por lo que a primera vista parece la causa de un problema.
> Nuestra solución sería ineficaz."*

### Criterios de evaluación de un problema ✅ *(Clase 3)*
Cuatro ejes: **áreas a las que afecta** · **gravedad** · **duración** · **número de problemas
simultáneos**. Ver [nota de la Clase 3](../01-clases/clase-03-seleccion-problema.md#ejercicio-identifica-tu-problema).

---

## Design Thinking y User Research *(Clase 4)*

### Design Thinking ✅ *(Clase 4)*
Metodología **centrada en el usuario** para la resolución de problemas complejos, que busca generar
soluciones innovadoras mediante un enfoque **iterativo y no lineal**. Se basa en la **empatía**, la
**creatividad** y la **experimentación**.

**Las 5 etapas:** Empatizar (Entender) → Definir (Enfocar) → Idear (Explorar) → Prototipar
(Construir) → Testear (Aprender). **No es una línea recta.**

> *"Design Thinking asegura que estás construyendo el producto correcto; Agile asegura que lo estás
> construyendo correctamente."*

### La Trinidad del Desarrollo de Software ✅ *(Clase 4)*
La intersección de tres ejes es la **innovación / tu MVP**:

| Eje | Pregunta |
|---|---|
| **Deseabilidad** (Humanos) | ¿Lo quieren? |
| **Factibilidad** (Tecnología) | ¿Podemos programarlo? |
| **Viabilidad** (Negocio) | ¿Tiene sentido financiero? |

### User Persona ✅ *(Clase 4)*
Representación del usuario tipo. El formato del docente tiene tres bloques:
**Características** (edad, familia, ocupación, intereses, localización) · **Momento/Escenario** ·
**Motivaciones**.

### Mapa de Empatía ✅ *(Clase 4)*
Herramienta para **"ponernos en los zapatos"** del usuario. Cuadrantes: **¿Qué piensa y siente?** ·
**¿Qué oye?** · **¿Qué ve?** · **¿Qué dice y hace?** · **Esfuerzos** (miedos, frustraciones,
obstáculos) · **Resultados** (deseos, medida del éxito).

### Escenario Actual / AS-IS ✅ *(Clase 4)*
Cómo se comporta la persona con el proceso **hoy**, para identificar sus **puntos de dolor**.

> *"¡La solución que seleccionemos debe pasar por estos puntos de dolor!"*

### User Journey Map / Customer Journey Map ✅ *(Clase 4)*
Mapa con **todas las etapas** por las que pasa el usuario durante un ciclo de compra o potencial
compra. Objetivo: **determinar cómo se sienten los clientes** e identificar puntos de dolor.

### "¿Cómo podríamos nosotros…?" ✅ *(Clase 4)*
Fórmula para redactar el problema en la etapa **Definir**. Obliga a nombrar al usuario y su
restricción concreta.

| ❌ | ✅ |
|---|---|
| "Hacer una app de dietas" | "¿Cómo podríamos ayudar a **estudiantes universitarios sin tiempo** a planificar comidas saludables **con presupuesto limitado**?" |

### NS/NC ✅ *(Clase 4)*
**"No Sabe / No Contesta"**. Opción de respuesta para cuando el encuestado desconoce la información
(NS) o prefiere no responder (NC). Evita forzar una opinión y **mejora la calidad de los datos**.

### Buenas prácticas de encuesta ✅ *(Clase 4)*
Evitar preguntas de **"respuesta ideal"** (que inducen la respuesta) · limitar las preguntas
abiertas y hacerlas opcionales · usar **rangos impares** (3, 5 o 7 opciones) con punto medio neutro ·
**ordenar** las respuestas y mantener el orden · agregar *"Otros"* y *"NS/NC"* · **anonimizar** ·
agrupar variables continuas en clases y outliers en *"otros"*.

---

## Método de trabajo exigido por el docente

### 6 Sombreros para Pensar ✅ *(consigna del docente)*
Método de **Edward de Bono** para analizar un problema desde seis perspectivas separadas, evitando
que se mezclen en una sola discusión. **No pienses como una persona; pensá como un equipo.**

| Sombrero | Rol | Qué aporta |
|---|---|---|
| ⚪ **Blanco** | Analista racional | Sólo hechos verificables **y qué datos faltan** |
| 🔴 **Rojo** | Mente emocional | Emociones, miedos, intuiciones — **sin justificar** |
| ⚫ **Negro** | Crítico estratégico | Riesgos y escenarios donde la decisión **fracasa** |
| 🟡 **Amarillo** | Optimista estratégico | Oportunidades y valor si funciona |
| 🟢 **Verde** | Pensamiento creativo | Ideas nuevas **sin filtrar** |
| 🔵 **Azul** | Director estratégico | Integra todo y **propone la decisión** |

Método completo y prompt del docente: [`docs/04-metodologia/seis-sombreros.md`](../04-metodologia/seis-sombreros.md).
Decisión de adopción: [0003](../03-decisiones/0003-metodo-seis-sombreros.md).

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

### UX / UI · Heurísticas 🔜 *(Bloque 2)*
Experiencia de usuario e interfaz. Hay un **Taller de Diseño UX/UI** en el Sprint 2.

### Segmentación de usuarios / Target ✅ *(Clase 2)*
Definir a quién le hablamos. Ver la sección [Segmentación y problema](#segmentación-y-problema-clases-2-y-3).

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
