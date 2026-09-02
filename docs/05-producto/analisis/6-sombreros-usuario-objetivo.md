# 6 Sombreros — ¿Quién es el usuario de FraudLens?

| | |
|---|---|
| **Decisión** | Qué **3 perfiles de usuario** vamos a investigar (User Persona · Mapa de Empatía · Escenario Actual) |
| **Fecha** | 2026-09-02 |
| **Participantes** | Borrador armado por FM con asistencia de Claude Code — **a validar y corregir por el equipo** |
| **Tarjeta de Trello** | https://trello.com/c/IYegyoM6 |
| **Estado** | 🟡 En análisis — se cierra en la clase del 2/9 |

> ⚠️ **El 🔴 sombrero rojo lo tiene que escribir el equipo.** Lo que está abajo es un borrador de
> lo que se percibe desde afuera; corríjanlo con lo que sienten de verdad. Un rojo prestado no sirve.

## El problema, en una frase

**¿A qué tres personas concretas vamos a investigar, sabiendo que esa elección define el producto,
el research, el MVP y el pitch — y que hay que decidirla hoy?**

Es la decisión más cara del proyecto: todo lo que viene después se apoya acá.

---

## ⚪ Sombrero Blanco — Analista racional

### Lo que sabemos

| Hecho | Fuente |
|---|---|
| El problema está **aprobado por el docente** y no se cambia | FM, clase del 19/8 |
| El objetivo declarado es *"asistir en la decisión de **aprobar, rechazar o revisar** una operación"* | Planilla del docente |
| El enunciado dice **complementar** las reglas existentes, no reemplazarlas | Planilla del docente |
| El documento de requerimientos propone 4 actores: **sistema cliente, analista de fraude, administrador, FraudLens** | Requerimientos del MVP (ML) |
| De esos 4, **dos no son personas**: "sistema cliente" es software y "FraudLens" es el producto | Lectura del documento |
| **No hay User Research hecho.** Cero encuestas, cero entrevistas, cero observaciones | FM, 2026-09-02 |
| **ML propuso el tema, es el referente del rubro del equipo y tiene acceso a información de otros expertos** | FM, 2026-09-02 |
| Existe un prototipo funcionando con dashboard, hecho por FGR | [prototipo.md](../prototipo.md) |
| Hay 3 datasets candidatos, **ninguno analizado todavía** | [datos.md](../datos.md) |
| El docente exige **datos reales**; las 400 respuestas son una guía, no una obligación | Clase 4 + FM |
| El equipo es de **4 personas** para un trabajo dimensionado para 6-8 | Clase 1 + FM |
| Fechas que dependen de esta decisión: solución elegida **23/9**, MVP definido **30/9**, desarrollo desde **7/10** | [cronograma.md](../../00-proyecto/cronograma.md) |

### Lo que NO sabemos

> No se completa a ojo. Si falta, se marca como falta.

- **A cuántas personas del rubro puede llegar ML realmente.** ¿Uno, cinco, ninguno? Es el dato más
  importante de esta lista y es el único que se puede conseguir hoy mismo.
- **Qué columnas tienen los datasets candidatos.** Si no traen comercio, ubicación o dispositivo,
  hay funcionalidades del documento de requerimientos que son imposibles.
- **Cuánto cuesta el fraude** a cada perfil. No tenemos ni un número propio ni de terceros.
- **Cómo se resuelve hoy** el problema en la práctica, en cada perfil.
- Si el docente espera **3 perfiles distintos o 3 personas del mismo perfil** → [P-18](../../00-proyecto/preguntas-abiertas.md#p-18).
- Qué considera el docente un **Problem Statement "validado"** sin research previo → [P-21](../../00-proyecto/preguntas-abiertas.md#p-21).

---

## 🔴 Sombrero Rojo — Mente emocional

> Sin justificar. **Borrador — el equipo lo corrige.**

- **Ansiedad por la fecha.** La clase es hoy y no hay una sola entrevista hecha.
- **Incomodidad de fondo:** se escribieron los requerimientos y se armó un prototipo antes de saber
  para quién. Se siente como haber puesto el carro delante del caballo, y nadie lo dijo en voz alta.
- **Apego a lo hecho.** El prototipo anda y da orgullo. Da fastidio pensar que el research podría
  obligar a tirarlo.
- **Falsa sensación de ir adelantados.** Tener un documento largo y un prototipo funcionando da la
  impresión de estar avanzados. La realidad es que estamos atrasados justo en lo que se evalúa.
- **Miedo concreto:** que el docente pregunte *"¿a quién entrevistaron?"* y no haya respuesta.
- **Cansancio de ser cuatro** en un trabajo pensado para seis u ocho.
- **Tentación de elegir el usuario que le queda cómodo al prototipo** en vez del que conviene al
  proyecto. Es el sesgo más peligroso de esta decisión y hay que nombrarlo.

---

## ⚫ Sombrero Negro — Crítico estratégico

| Riesgo | Cómo se ve el fracaso |
|---|---|
| **El analista de fraude es el usuario más difícil de conseguir del mundo.** Trabaja en bancos y fintechs, y sus controles antifraude son información confidencial | Llegamos a octubre con cero entrevistas reales. El research se vuelve especulación y el docente lo detecta enseguida |
| **Si no conseguimos datos reales, la tentación es inventarlos** | Deja de ser un problema de nota y pasa a ser un problema de **honestidad académica**, que el cronograma dice explícitamente que se sanciona |
| **"Administrador" no es un usuario, es un rol de configuración** del propio sistema | Su User Persona y su Mapa de Empatía salen vacíos: no tiene un dolor propio, sólo mueve dos umbrales. Se nota en la entrega |
| **El prototipo condiciona la decisión.** Ya asume un analista mirando un dashboard | Elegimos el usuario que le sirve al prototipo, no el que sirve al proyecto. Es exactamente el sesgo que el método de los 6 sombreros existe para evitar |
| **Tres perfiles demasiado parecidos** | Los tres Mapas de Empatía terminan siendo el mismo documento escrito tres veces. Es visible a simple vista y devalúa el entregable |
| **El dataset puede no soportar el producto que definamos** | Definimos features que ningún dataset candidato tiene, y en octubre hay que rehacer el alcance con el desarrollo ya empezado |
| **ML es el único canal a expertos del rubro** | Si ML se satura, se enferma o no consigue los contactos, el proyecto entero se queda sin su fuente de datos reales. Es un punto único de falla |
| **Decidir hoy con cero evidencia** | Estamos eligiendo el usuario **antes** del research, que es justo el orden que la Clase 4 dice que hace fallar al 90% de las startups |

---

## 🟡 Sombrero Amarillo — Optimista estratégico

- **Tenemos algo que casi ningún equipo tiene: acceso real al rubro.** ML propuso el tema porque lo
  conoce y tiene contactos con expertos. En una materia que exige datos reales, eso es *el* activo
  diferencial. Bien usado, resuelve el punto más difícil de la cursada.
- **Hay un perfil infinitamente accesible.** Todos conocemos a alguien a quien le clonaron la
  tarjeta o le rechazaron una compra legítima. Se pueden juntar decenas de respuestas reales en
  días, sin depender de ningún contacto corporativo.
- **El prototipo ya existe.** Si el usuario elegido necesita un dashboard, tenemos demo desde el
  primer Sprint Review mientras otros equipos recién arrancan.
- **Decidir bien hoy ahorra octubre entero.** Cada semana que el usuario siga sin definir es una
  semana de desarrollo construyendo sobre supuestos.
- **El problema es genuinamente interesante y actual.** No cae en ninguna de las temáticas que el
  docente descartó, y el fraude digital es un tema que se defiende solo en un pitch.
- **La tensión "solución antes que problema" se puede convertir en fortaleza narrativa.** Contar en
  el pitch *"partimos de una hipótesis, la contrastamos con usuarios reales y esto es lo que
  cambiamos"* es mejor historia que haber acertado de casualidad. Pero sólo funciona **si de verdad
  cambiamos algo**.

---

## 🟢 Sombrero Verde — Pensamiento creativo

> Sin filtrar ni evaluar.

1. **Los tres niveles del dolor:** quien lo **sufre** (consumidor), quien lo **decide** (analista),
   quien lo **paga** (comercio). Tres perfiles naturalmente distintos, con mapas de empatía que no
   se van a parecer entre sí.
2. **Dueño de e-commerce o comercio chico** que come contracargos. Accesible en cualquier feria,
   local o grupo de emprendedores. Tiene dolor económico directo y ninguna herramienta.
3. **El consumidor al que le rechazaron una compra legítima.** El falso positivo tiene víctima, y esa
   víctima está en todas partes. Encuestable masivamente.
4. **El operador de atención al cliente** que atiende el reclamo del falso positivo. Ve el problema
   todos los días y es mucho más accesible que un analista de fraude.
5. **Dar vuelta el producto** (pensamiento lateral de la Clase 1): en vez de *detectar fraude*,
   **certificar transacciones legítimas**. Cambia el usuario, la métrica y el discurso.
6. **Contador o responsable administrativo de una PyME** que concilia movimientos y detecta cargos
   raros a mano.
7. **Cooperativas, mutuales y billeteras chicas** en vez de bancos grandes: mismo problema, mucho
   menos blindaje para hablar.
8. **Perfil proxy:** si el analista real es inaccesible, entrevistar a alguien de un rubro
   equivalente (prevención de pérdidas en retail, control de riesgo crediticio).
9. **Que ML sea entrevistado.** Es experto del rubro y está en el equipo — pero declarándolo como
   fuente interna, no disfrazándolo de research externo.
10. **Empezar por el dataset y no por el usuario:** ver qué datos existen realmente y elegir el
    usuario que se puede servir con eso.

---

## 🔵 Sombrero Azul — Director estratégico

### Puntos clave de cada sombrero

| Sombrero | Lo que aportó |
|---|---|
| ⚪ Blanco | No hay research. El dato decisivo —a cuántos expertos llega ML— **no lo tenemos y se puede conseguir hoy** |
| 🔴 Rojo | Existe un sesgo activo: elegir el usuario que le queda cómodo al prototipo. Nombrarlo es la mitad del trabajo |
| ⚫ Negro | El usuario más obvio (analista de fraude) es el menos accesible. Apostar todo a él es apostar a un punto único de falla |
| 🟡 Amarillo | Hay acceso real al rubro vía ML, y hay un perfil masivamente accesible que nadie está mirando |
| 🟢 Verde | Los tres niveles —sufre / decide / paga— resuelven de una sola vez el problema de tener tres perfiles genuinamente distintos |

### Contradicciones a resolver

**El negro dice que el analista de fraude es inaccesible; el amarillo dice que ML tiene acceso.**

No es una contradicción de opinión: es **una pregunta con respuesta**, y la respuesta la tiene ML.
No se resuelve discutiendo, se resuelve preguntándole hoy: *¿podés conseguir una o dos entrevistas
reales con analistas de fraude en las próximas dos semanas, sí o no?*

Es la bisagra de toda la decisión.

### Decisión propuesta

> **Tres perfiles en tres niveles distintos del mismo problema, elegidos con la accesibilidad como
> filtro duro:**
>
> | | Perfil | Rol en el problema | Cómo se investiga |
> |---|---|---|---|
> | **A** | **Analista de fraude** | El que **decide** | Entrevistas vía los contactos de ML — **sujeto a que ML confirme acceso hoy** |
> | **B** | **Dueño de comercio / e-commerce chico** | El que **paga** el fraude y los contracargos | Entrevistas — accesible sin contactos especiales |
> | **C** | **Consumidor con fraude o rechazo indebido** | El que lo **sufre** | Encuesta — masivamente accesible |
>
> **Se descarta "administrador"** como perfil de investigación: es un rol de configuración del
> propio sistema, no una persona con un dolor propio. Sigue existiendo como actor del software.
>
> **Plan B, si ML no puede confirmar acceso:** el perfil A pasa a ser un **proxy accesible** —
> operador de atención al cliente que atiende reclamos de fraude, o responsable de riesgo en una
> cooperativa o billetera chica. Se documenta que es un proxy y por qué.

### Qué la sostiene

- Los tres perfiles tienen dolores **estructuralmente distintos**, así que los tres Mapas de Empatía
  van a ser genuinamente diferentes.
- **Al menos dos de los tres son accesibles sin depender de nadie**, así que el research arranca hoy
  pase lo que pase.
- Cubre el enunciado aprobado sin cambiarlo: sigue siendo *aprobar, rechazar o revisar*, visto desde
  los tres lados.
- Deja explícito el sesgo del prototipo en vez de dejarlo actuar en silencio.

### Qué la haría cambiar

- Que ML confirme que **no** hay acceso a analistas de fraude → se activa el plan B.
- Que los datasets no permitan modelar nada útil para el perfil elegido → se revisa el alcance.
- Que el docente responda [P-18](../../00-proyecto/preguntas-abiertas.md#p-18) diciendo que son
  **3 personas del mismo perfil** y no 3 perfiles → cambia toda la estructura.
- Que el research diga que el dolor real está en un lugar donde no lo estamos buscando.

### Lo primero que hay que hacer

1. **Preguntarle a ML, hoy, antes de la clase:** ¿tenés acceso real a analistas de fraude para
   entrevistar en las próximas dos semanas?
2. **Preguntar [P-18](../../00-proyecto/preguntas-abiertas.md#p-18) al inicio de la clase**, no al final.
3. Recién con esas dos respuestas, cerrar los 3 perfiles.

---

## Verificación final

- [x] El problema se analizó desde múltiples perspectivas reales
- [x] El resultado **no** refleja un único sesgo emocional o racional — el rojo nombra el sesgo del
      prototipo y el azul lo contrarresta con el filtro de accesibilidad
- [x] La decisión del azul integra y equilibra todas las visiones anteriores
- [x] El blanco **no inventó** ningún dato: lo que falta está listado como falta
- [ ] ⬜ **El equipo validó el sombrero rojo** *(pendiente)*
- [ ] ⬜ **ML confirmó o descartó el acceso a expertos** *(pendiente — es la bisagra)*
