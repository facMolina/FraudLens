# Clase 10 — User Story Mapping · Backlog · User Flow · Historias de Usuario

| | |
|---|---|
| **Fecha** | ⬜ *No consta en el material — a confirmar por el equipo ([P-28](../00-proyecto/preguntas-abiertas.md#p-28))* |
| **Docente** | Daniel Britez *(deck firmado por la cátedra, ver Clase 09)* |
| **Material** | `010_-_Clase_09_SIPI_User_Story_Mapping_y_Backlog.md` → [`material/clase-10-user-story-mapping-backlog.md`](material/clase-10-user-story-mapping-backlog.md) |
| **Cargada por** | Facundo Molina (FM) |
| **Fecha de carga** | 2026-10-07 |

> ⚠️ **Numeración ([P-20](../00-proyecto/preguntas-abiertas.md#p-20)):** el nombre del archivo trae
> **dos números a la vez** (`010` y `Clase_09`), igual que pasó con la Clase 07. Se cargó como
> **Clase 10** por el prefijo y por orden, sin asumir cuál es "el correcto" para el docente.
> Tampoco se le asignó fecha ([P-28](../00-proyecto/preguntas-abiertas.md#p-28)).

---

## 1. De qué se trató

Es la clase que **baja el MVP a algo construible**. Arranca repasando Design Thinking y enseña, en
orden: **User Story Mapping** (armar visualmente el mapa de funcionalidades y separar qué entra al MVP
y qué a futuros releases), **Product Backlog**, **User Flow** (diagramas del camino del usuario),
**Historias de Usuario** con sus criterios de aceptación y, para ordenarlas y partirlas, **INVEST**,
**MoSCoW**, **Épicas** y el criterio **SPIDR**.

Importa porque el cronograma pide el **Product Backlog como entregable el 14/10** y el **prototipo
clickeable el 21/10**: esta clase es el "cómo" de ambos.

> ⚠️ **Calidad de la conversión.** Las diapositivas del User Story Mapping son un mapa que se va
> armando en pasos; al convertirlas quedó el texto **sin su posición** (qué tarea cuelga de qué
> actividad, y cuáles quedaron en MVP / R2 / R3). **No se reconstruyó esa disposición**: se lista lo que
> el deck dice, sin asignar columnas que el texto no permite asegurar.

---

## 2. Conceptos

### User Story Mapping (USM)
Manera **visual y colaborativa** de definir el **mapa de funcionalidades** de un producto. Ordena por
prioridad y permite establecer las necesidades del negocio **manteniendo el foco en el valor**.

Para qué sirve, según el deck:
- Tener en una sola mirada el **"big picture"** del sistema.
- **Descomponer** las ideas más generales en las más específicas.
- Identificar **qué entra en el MVP y qué en futuros releases**.

**Los 4 pasos** *(ejemplo del deck: "Comprar zapatillas para entrenar")*:

| Paso | Qué se hace | Ejemplo del deck |
|---|---|---|
| **1. Identificar el objetivo del usuario** | Se define la meta y se la parte en **actividades** | Objetivo: *comprar zapatillas para entrenar* → actividades **Buscar · Seleccionar · Checkout** |
| **2. Escribir el User Journey** | Los pasos concretos del recorrido, de izquierda a derecha | Buscar producto · Ver producto · Elegir · Confirmar carrito · Seleccionar delivery · Pagar |
| **3. Descomponer cada actividad en tareas** | Las tareas cuelgan debajo; el **eje vertical es prioridad**: **+ prioridad arriba, − prioridad abajo** | Filtrar por marca / color / talle / actividad deportiva · Ordenar por precio / por más comprado · Ver fotos · Elegir opciones · Ver composición · Ver valoración · Confirmar compra · Agregar dirección · Retirar en sucursal · Cupón de descuento · Pagar con tarjeta |
| **4. Definir MVP y Releases** | Se separan con una **línea punteada** horizontal: lo de arriba es el **MVP**, lo siguiente **R2**, **R3**… | El mapa termina dividido en MVP / R2 / R3 |

> ⬜ *Qué tarea del ejemplo cayó en MVP, en R2 y en R3 no se puede leer en la conversión. Y el orden
> exacto de los pasos del journey por actividad se infiere de cómo se va armando la diapositiva: no
> es textual. Si el docente lo toma como ejemplo, mirar el deck original.*

> 🎯 **Aplicado a FraudLens:** es la técnica que esta clase pide para armar la **propuesta de MVP**
> (ver sección 4). Ya tenemos material para el paso 1 y 2: el
> [flujo principal](../05-producto/requerimientos-funcionales-mvp.md#4-flujo-principal) y el
> recorrido de "MVP terminado" de los requerimientos de ML. **No es el mapa**: son los insumos.

### Product Backlog
La **lista de deseos o elementos** del producto. Es **dinámico**: puede crecer o decrecer.

- En cada iteración se planifican los **PBI** de **mayor prioridad**, que forman el **Sprint Backlog**.
- **Mayor prioridad → más refinados.** **Menor prioridad → menos refinados.**
- Si entran requerimientos nuevos, **se priorizan dentro del backlog existente**.
- Los PBI **pueden cambiar de prioridad** o **removerse** en cualquier momento.

**Herramientas** que muestra: **Miro**, **FigJam**, **Lucidspark** *(en la conversión el primer nombre
llegó como "mirteCo"; se lee Miro)*.

### User Flow
**El camino que un usuario sigue mientras interactúa con un producto o servicio**: empieza cuando
accede a la plataforma y termina cuando completa la acción deseada (comprar, registrarse, leer un
artículo, etc.).

**Por qué importa:** permite entender cómo interactúan los usuarios, **identificar obstáculos** que
les impiden completar una tarea y **determinar qué características son más importantes**.

**Cómo se representa:** con **diagramas de flujo** — representación gráfica de un proceso a través de
pasos estructurados y relacionados.
- Se tienen en cuenta **las decisiones del usuario y las decisiones del sistema**, que se dibujan
  **con formas diferentes**.
- Se hacen **de izquierda a derecha y de arriba a abajo**, **evitando el cruce de líneas**.

**Cómo se diseña (6 pasos del deck):**
1. Analizar las necesidades de los usuarios.
2. Diseñar la ruta según los objetivos.
3. Analizar a los clientes para definir su recorrido.
4. Definir otros caminos para el usuario.
5. Trazar el recorrido.
6. Refinar el flujo con comentarios y cambiar lo necesario.

*Ejemplos del deck:* compra de hosting, inicio de sesión (varias rutas: redes sociales o correo),
compra en un e-commerce.

> ⬜ *Los diagramas son imagen y no se extrajeron: las formas concretas para "decisión del usuario" y
> "decisión del sistema" **no figuran** en el texto. No se inventan.*

### Historia de Usuario (HU)
Descripción **breve** de algo que el cliente quiere: una necesidad del negocio.

- **Título:** verbo en infinitivo.
- **Formato:** **COMO** [rol o usuario], **QUIERO** [una funcionalidad], **PARA** [alcanzar un objetivo].

*Ejemplo del deck:* **HU — Ver campañas de Marketing.** *Como Gerente de Marketing, quiero ver
información histórica de las campañas realizadas, para identificar y repetir las que fueron exitosas.*

**Las 3 C's** — toda HU debe cumplirlas:

| C | Qué pide |
|---|---|
| **Card** | Suficientemente **pequeña para entrar en una tarjeta**, de lectura rápida y fácil comprensión |
| **Conversación** | Se completa **conversando** para obtener detalles y **que no haya ambigüedad**. *Ejemplo del deck:* "cancelar una reserva para obtener el reembolso" → ¿total o parcial?, ¿sobre la tarjeta o en crédito del sitio?, ¿hasta cuántos días antes?, ¿los usuarios frecuentes pueden cancelar a último momento? |
| **Confirmación** | Interactúan **Product Owner y Development Team** para **saber si terminamos de construir y si cumplimos lo esperado** |

**Criterios de aceptación:** requerimientos que deben cumplirse para dar por finalizada la HU.
Formato: **DADO** [una precondición], **CUANDO** [una acción que se produce], **ENTONCES** [una consecuencia].

*Ejemplo del deck (HU "Ver mis favoritos"):* **DADO** que guardé los hoteles que me gustaron,
**CUANDO** vea favoritos, **ENTONCES** se mostrará una lista con nombre, foto y precio por noche.

> ⚠️ **"No hay un único usuario."** *"Si diseñamos las HU pensando en un solo usuario entonces
> perderemos HU. ¡Error muy frecuente y que debemos evitar!"* — frase textual del deck.

### INVEST — cómo saber si una HU es buena

| Letra | Principio | Significado |
|---|---|---|
| **I** | Independiente | No debe depender de otra HU |
| **N** | Negociable | Puede cambiarse, reescribirse o eliminarse antes de empezar a trabajar en ella |
| **V** | Valorable | Debe dar valor al usuario final |
| **E** | Estimable | Se puede estimar su tamaño |
| **S** | Small | Lo más pequeña posible |
| **T** | Testeable | Provee la información necesaria para que el desarrollo y el test sean posibles |

### MoSCoW — prioridad de los ítems

| Categoría | Qué es *(según el deck)* |
|---|---|
| **MUST** | Ítems **necesarios en el sprint** |
| **SHOULD** | Ítems **importantes pero no necesarios** en el sprint |
| **COULD** | Ítems **deseables pero no necesarios**: pueden mejorar la experiencia o satisfacción **a bajo costo** |
| **WON'T** | Ítems de **menor criticidad, bajo valor, o no apropiados en este momento** (en un futuro, puede ser) |

### Épicas
Una **historia de usuario tan grande** que el equipo la **descompone** en historias de un tamaño
manejable para estimación y seguimiento.

### Criterio SPIDR — cómo partir una épica

| Letra | Cómo parte la historia | Ejemplo del deck *("comprar una aspiradora")* |
|---|---|---|
| **S — Spikes** | Cuando hay una duda técnica: se hace una **investigación** (leer documentación, hablar con proveedores, **prueba de concepto**) cuyo objetivo es **determinar qué hay que hacer en otra HU** | *Ya ofrecemos débito y crédito: ¿podemos integrarnos con Mercado Pago?* |
| **P — Paths** | Por **caminos** distintos del usuario | Usuario ya registrado vs. no registrado |
| **I — Interfaces** | Por **interfaz** | Portal web vs. app mobile |
| **D — Data** | Por **datos** | Residente en Argentina (envío el mismo día) vs. en el extranjero (hasta 10 días) |
| **R — Rules** | Por **reglas de negocio** | Solo productos para quien tenga TC → pagar con VISA / avisar que no se puede con Mastercard |

---

## 3. Aplicación a FraudLens

*Sección obligatoria.* Fuente de cada fila: **(D)** dice el docente · **(R)** hecho del repo ·
**(S)** sugerencia de Claude Code, sin aprobar por el equipo.

| Qué | Por qué | Dónde se refleja |
|---|---|---|
| **El entregable "Product Backlog" del 14/10 sale de esta clase** (D + R: cronograma) | Es la tarea concreta. Hoy el backlog **no existe**: lo más cercano son los casos de uso de ML | [`entregables/README`](../02-entregables/README.md) — fila "Planificación ágil" ⬜ |
| **Los requerimientos de ML no están en formato HU** (R) | Están como casos de uso con actor, flujo y criterios de aceptación **en lista**; la clase pide **Como / Quiero / Para** y criterios **Dado / Cuando / Entonces**. Hay que **reescribirlos**, no copiarlos | [`requerimientos-funcionales-mvp.md`](../05-producto/requerimientos-funcionales-mvp.md) §5 |
| **MoSCoW ya tiene un "Won't" casi armado** (R) | El repo tiene **dos listas** de "fuera del MVP" que no coinciden (la de `problema.md`, 6 ítems, y la de requerimientos §9, 11 ítems). Con MoSCoW hay que **unificarlas** en una sola. **Must / Should / Could no están decididos**: lo decide el equipo | [`problema.md`](../05-producto/problema.md) · [`requerimientos §9`](../05-producto/requerimientos-funcionales-mvp.md#9-fuera-del-alcance) |
| **"No hay un único usuario" choca con la [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md)** (D vs R) | La 0005 dejó **un solo tipo de usuario (Analista)** en el MVP y recortó al Administrador. Pero los requerimientos tienen otro actor: el **sistema cliente** (el que manda transacciones por API). Hay que decidir **qué roles escriben HU** — sin re-litigar la 0005, pero sin perder historias | [P-32](../00-proyecto/preguntas-abiertas.md#p-32) |
| **El spike de Jev ya existe, con otro nombre** (D + R) | SPIDR define un **Spike** como investigación / prueba de concepto *"para determinar qué hay que hacer en otra HU"*. La tarjeta **"Validar Jev con una muestra del dataset 3"** es exactamente eso. Conviene **reformularla como Spike** y que su resultado alimente una HU | [`typesafe-jev.md`](../05-producto/typesafe-jev.md) · [Validar Jev…](https://trello.com/c/EYxcS7tu) |
| **Definición de "MVP terminado" (8 pasos) = insumo del User Journey** (R) | Es un recorrido de punta a punta. Sirve como **primer borrador** de los pasos 1 y 2 del USM | [`requerimientos §10`](../05-producto/requerimientos-funcionales-mvp.md#10-definición-de-mvp-terminado) |
| **Épicas candidatas** (S) | Los casos de uso grandes (CU-01 *Analizar una transacción*, CU-03 *Calcular el riesgo*) probablemente sean épicas. **Sin decidir**: lo define el equipo con INVEST y SPIDR | — |
| **Herramienta del backlog** (D) | La clase pide **decidir** dónde se registra (muestra Miro / FigJam / Lucidspark para el mapa; Trello ya es nuestro tablero del sprint, Clase 09). **No elegimos por deducción** | [P-30](../00-proyecto/preguntas-abiertas.md#p-30) |
| **Prototipo y User Flow** (D + R) | Los User Flow se piden **para las funcionalidades del MVP**. El prototipo de FGR es una interfaz sin lógica: sirve de base para el flujo, no lo reemplaza | [`prototipo.md`](../05-producto/prototipo.md) |

> **Un borrador para empezar, marcado como tal (S):** el *flujo principal* de los requerimientos
> (enviar → validar → regla de monto → riesgo → umbrales → devolver → registrar y mostrar) podría
> ser la **columna vertebral** del mapa. Es un punto de partida para discutir, **no una decisión**.

---

## 4. Qué tenemos que hacer para la próxima

*Textual del deck:* **"Armar propuesta MVP usando User Story Mapping · Plantear los User Flow de las
funcionalidades que se incluyen en el MVP · Decidir cuál va a ser la herramienta donde el equipo
registrará su Backlog · Armar el backlog: comenzar a escribir las User Stories."**
Con esta regla de refinamiento: **las más prioritarias arriba, completas con criterios de aceptación ·
las próximas a trabajar con título y Como/Quiero/Para · las menos prioritarias, solo título.**

| Tarea | Responsable | Fecha límite | Trello |
|---|---|---|---|
| Armar la propuesta de MVP con User Story Mapping | ⬜ Sin asignar | ⬜ *(el cronograma pide el Product Backlog el 14/10)* | ⬜ **Crear tarjeta** |
| Plantear los User Flow de las funcionalidades del MVP | ⬜ Sin asignar | ⬜ | ⬜ **Crear tarjeta** |
| Decidir la herramienta donde se registra el Backlog | ⬜ Equipo | ⬜ | ⬜ **Crear tarjeta** ([P-30](../00-proyecto/preguntas-abiertas.md#p-30)) |
| Escribir el Product Backlog (HU con criterios de aceptación, refinadas por prioridad) | ⬜ Sin asignar | **14/10** *(entregable, según cronograma)* | ⬜ **Crear tarjeta** |

> ⚠️ Estas 4 tarjetas **no existen todavía** en el tablero. Se proponen en la
> [bitácora](../../bitacora/2026-10-07-clases-9-y-10.md); no se crearon sin que el equipo las revise.

---

## 5. Dudas que quedaron

- ¿Qué fecha tiene esta clase? → [P-28](../00-proyecto/preguntas-abiertas.md#p-28)
- ¿Qué actores escriben HU, dado "no hay un único usuario" y la decisión 0005? → [P-32](../00-proyecto/preguntas-abiertas.md#p-32)
- ¿Con qué herramienta se arma el backlog? → [P-30](../00-proyecto/preguntas-abiertas.md#p-30)
- ¿El Product Backlog del 14/10 se entrega ya estimado? → [P-31](../00-proyecto/preguntas-abiertas.md#p-31)
- El cronograma del 30/9 anuncia **"MVP Canvas"**; este deck **no lo define**. Si es una herramienta
  distinta del USM, **no está en el material cargado**.

---

## 6. Términos nuevos para el glosario

- [x] *User Story Mapping · Product Backlog · Sprint Backlog · User Flow · Diagrama de flujo ·
  Historia de Usuario · 3 C's · Criterios de aceptación · INVEST · MoSCoW · Épica · SPIDR · Spike* →
  agregados a [`glosario.md`](../00-proyecto/glosario.md)
