# El problema

> Estado: 🟡 **Iniciado.** Lo que está acá viene de la planilla del docente y de la Clase 1.
> Falta todo el User Research, que es lo que le da sustento real.

## Cómo llegamos acá

| Clase | Qué pasó |
|---|---|
| **Clase 2** | El equipo expuso las ideas de problema que tenía. Todavía se evaluaban varios proyectos |
| **Clase 3** | Se decidió por este sistema. **El docente lo aprobó** |
| **Clase 4** | Se escribieron los [requerimientos funcionales del MVP](requerimientos-funcionales-mvp.md) y se definió el nombre **FraudLens** |

> ⚠️ El **User Research todavía no se hizo**. Las herramientas de la Clase 4 (User Persona, Mapa de
> Empatía, Escenario Actual) están pendientes, y son la consigna para la Clase 5.
> Ver [P-12](../00-proyecto/preguntas-abiertas.md#p-12).

## Enunciado (planilla del docente)

Los sistemas tradicionales de detección de fraude suelen apoyarse en **reglas predefinidas**, que
pueden resultar insuficientes para identificar comportamientos anómalos que no fueron contemplados
previamente.

Existe la oportunidad de **complementar** estas reglas mediante modelos de inteligencia artificial
capaces de analizar patrones históricos y características de cada transacción para detectar
operaciones potencialmente fraudulentas.

## Objetivo

Desarrollar un prototipo capaz de analizar transacciones **en tiempo real** y estimar su nivel de
riesgo de fraude mediante un modelo de IA entrenado con datos históricos, permitiendo identificar
comportamientos anómalos y **asistir en la decisión de aprobar, rechazar o revisar** una operación.

## Árbol de Problemas y 5 Por Qué

| | |
|---|---|
| **Estado** | ✅ Escrito |
| **Fecha** | 2026-09-14 |
| **Ticket** | [Árbol de Problemas y análisis 5 Por Qué de FraudLens](https://trello.com/c/G4UP8ERN) |
| **Método** | Árbol de Problemas y 5 Por Qué (5 Why) — [Clase 02](../01-clases/clase-02-segmentacion-y-problema.md#5-por-qué-5-why--análisis-de-causa-raíz) |

### Árbol de Problemas

**PROBLEMA CENTRAL** *(planilla del docente, textual)*:
> "Los sistemas tradicionales de detección de fraude se apoyan en reglas predefinidas, que pueden
> resultar insuficientes para identificar comportamientos anómalos que no fueron contemplados
> previamente."

**EFECTOS** *(consecuencias, una por perfil — ver [`usuarios.md`](usuarios.md))*:

| Perfil | Efecto |
|---|---|
| **A · Analista de fraude** | Revisa casos dudosos sin más ayuda que su propio criterio, sin poder explicar del todo por qué una transacción es riesgosa cuando alguien le pregunta |
| **B · Responsable de riesgo/producto en la fintech o banco** | Queda expuesto a un riesgo regulatorio real: las Comunicaciones "A" 8471 y "A" 8473 del BCRA (2026) exigen a PSP y entidades financieras tener una función de gestión de riesgo de fraude, autoevaluaciones y reportes periódicos — y a pérdidas financieras/reputacionales si el sistema actual no alcanza |
| **C · Usuario final de una fintech/billetera/pasarela** | Sufre el rechazo indebido de una compra o transferencia legítima, o le aprueban un cargo que no reconoce |

**CAUSAS:**
- Las reglas predefinidas no contemplan casos de uso nuevos, ni los movimientos de fraudulentos que buscan evadirlas.
- Dependen de un ser humano que razone y las reconfigure.
- La estrategia elegida no es reemplazar a ese humano por un modelo autónomo, sino que el modelo lo **asista** con hipótesis para crear reglas nuevas o detectar posibles casos de fraude — reforzado porque la normativa BCRA exige justamente una persona/función responsable, no un sistema sin supervisión.

### 5 Por qué

1. **¿Por qué se escapan fraudes (o se rechazan operaciones legítimas)?** → Hay casos de uso que las reglas típicas no contemplan. Esas reglas, en el sistema financiero y digital argentino, están marcadas por normativa del BCRA (Comunicaciones "A" 8471 y "A" 8473, 2026) y marcos internacionales de cumplimiento obligatorio para bancos y PSP.
2. **¿Por qué esas reglas no contemplan casos nuevos?** → Son definidas de antemano y no contemplan casos de uso nuevos, ni los movimientos ingeniosos de fraudulentos que buscan evadir el sistema ya conocido.
3. **¿Por qué depende de que alguien las actualice?** → Porque dependen de un ser humano que razone y reconfigure los casos no contemplados.
4. **¿Por qué reconfiguración manual en vez de un modelo autónomo?** → Porque la estrategia es que el modelo **asista** al analista — con hipótesis para crear reglas nuevas o detectar posibles casos de fraude — en vez de reemplazarlo. Reforzado por la normativa BCRA (Com. "A" 8471), que exige una persona/función responsable a cargo.

> Se cierra en 4 niveles: se llegó a una causa raíz sólida (decisión estratégica + mandato
> regulatorio). El material de la Clase 2 no exige un número fijo de "por qués" más allá del nombre
> de la técnica — se para cuando se llega al fondo, no antes ni después.

**Fuentes de cada afirmación:**

| Afirmación | Fuente |
|---|---|
| Enunciado del problema central | Planilla del docente |
| Normativa BCRA (Comunicaciones "A" 8471 y "A" 8473) | Búsqueda web, 2026-09-14 — [Bruchou & Funes de Rioja](https://bruchoufunes.com/nueva-regulacion-del-bcra-sobre-gestion-del-riesgo-de-fraude-com-a-8471/), [Tavarone Rovelli Salim Miani](https://tavarone.com/comunicaciones-bcra-a-8471-y-a-8473-gestion-y-prevencion-del-riesgo-de-fraude/) |
| Reglas estáticas, dependencia de reconfiguración manual, estrategia de modelo asistivo | Razonamiento del equipo (FM, con correcciones de FM en la sesión del 14/9) — no es una fuente documental externa |

## Hipótesis de trabajo sobre el usuario

> 📌 **Aportada por FM el 2026-09-02.** El **tipo de cliente** (empresas fintech y bancos
> tradicionales, no comercio chico) quedó **confirmado como decisión del equipo el 2026-09-14** —
> ver [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md). Sigue sin decidir
> **cuál perfil (A o B) es *el* usuario objetivo del MVP** — eso depende del research.

FraudLens sería un producto **B2B para empresas fintech y bancos tradicionales** que manejan
tráfico de transacciones: integran nuestro sistema como **complemento** de su antifraude actual,
sumando un filtro más específico gracias a la IA, más un **dashboard de revisión** para su equipo.

El **cliente** que paga es la fintech/banco (Perfil B); los **usuarios** que lo usan todos los días
son los analistas de su equipo de fraude (Perfil A).

Ver [P-07](../00-proyecto/preguntas-abiertas.md#p-07).

## Lo que todavía no sabemos

El enunciado describe una **oportunidad tecnológica**, no todavía un problema con dueño. Para que
sea un problema del TIF hace falta responder:

| Pregunta | Por qué importa |
|---|---|
| **¿A quién le duele?** ¿Un analista de fraude? ¿Un comercio chico? ¿Un banco? | Define el usuario, la interfaz y todo el User Research → [P-07](../00-proyecto/preguntas-abiertas.md#p-07) |
| **¿Cuánto duele?** ¿Cuánta plata o cuánto tiempo se pierde hoy? | Es la evidencia que justifica el proyecto |
| **¿Cómo lo resuelven hoy?** | Sin entender el sistema actual, no podemos decir que lo mejoramos |
| **¿Por qué no está resuelto?** | Si fuera fácil ya existiría. La respuesta es parte de la diferenciación |

Estas se responden con **User Research con datos reales** — exigencia explícita del docente.

## Reformular como "¿Cómo podríamos nosotros…?" *(Clase 4)*

El docente enseñó una fórmula para pasar de una descripción vaga a un problema específico:

| ❌ En lugar de | ✅ Definí |
|---|---|
| "Hacer una app de dietas" | "¿Cómo podríamos ayudar a **estudiantes universitarios sin tiempo** a planificar comidas saludables **con presupuesto limitado**?" |

Nuestro enunciado actual describe una **oportunidad tecnológica**, no un usuario con una restricción.

> ⚠️ **Por qué son 3 versiones y no una.** Esta fórmula normalmente se escribe **después** de
> Empatizar, como síntesis de entrevistas reales. Nosotros todavía tenemos **0 entrevistas hechas**,
> así que lo de abajo **no es un insight validado — es una hipótesis de trabajo**, construida sólo
> con lo que ya sabemos con certeza (la planilla del docente y la decisión de
> [los 3 perfiles](usuarios.md)), sin inventar dolores que todavía no confirmamos. Además,
> [P-07](../00-proyecto/preguntas-abiertas.md#p-07) —quién es *el* usuario objetivo del MVP— sigue
> abierta: elegir una sola reformulación hoy sería adelantar esa respuesta sin evidencia, que es
> justo el sesgo que nombró el
> [sombrero rojo](analisis/6-sombreros-usuario-objetivo.md#-sombrero-rojo--mente-emocional).
> Por eso hay una reformulación **por perfil**, igual que va a haber un User Persona por perfil.
>
> **Se corrige** en cuanto haya entrevistas reales — sobre todo la del perfil A, que depende de los
> contactos de ML.

### A — Analista de fraude *(el que decide)*

> **¿Cómo podríamos ayudar a analistas de fraude que deciden aprobar, rechazar o revisar
> transacciones a detectar los casos que las reglas predefinidas no contemplan?**

Fuente: planilla del docente (*"reglas predefinidas... insuficientes para identificar
comportamientos anómalos"*) + rol descripto en [usuarios.md](usuarios.md#perfil-a--analista-de-fraude).

### B — Responsable de riesgo/producto en una fintech o banco tradicional *(el que paga)*

> **¿Cómo podríamos ayudar a un responsable de riesgo o producto en una fintech, billetera virtual,
> pasarela de pago o banco tradicional a cumplir con la gestión de riesgo de fraude que le exige el
> BCRA, sin depender sólo de reglas que no contemplan casos nuevos?**

> 🔄 **Actualizada el 2026-09-14** — la reformulación original (FGR, 2/9) apuntaba a "dueño de
> comercio/e-commerce chico". Se ajustó al redefinirse el Perfil B —
> [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md) — conservando la
> autoría original de la fórmula y el criterio de FGR.

Fuente: [usuarios.md](usuarios.md#perfil-b--responsable-de-riesgoproducto-en-una-fintech-o-banco-tradicional).

### C — Usuario final de una fintech/billetera/pasarela *(el que lo sufre)*

> **¿Cómo podríamos evitar que al usuario final de una fintech, billetera virtual o pasarela de pago
> le rechacen una compra o transferencia legítima, o le aprueben una fraudulenta, sin que tenga
> forma de intervenir en esa decisión?**

> 🔄 **Actualizada el 2026-09-14** — la reformulación original (FGR, 2/9) hablaba de "consumidor" en
> general. Se ajustó al redefinirse el Perfil C —
> [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md).

Fuente: [usuarios.md](usuarios.md#perfil-c--usuario-final-de-una-fintech-billetera-virtual-o-pasarela-de-pago).

### Estado

✅ Reformuladas las 3 — pendiente de corregirse con entrevistas reales. El tipo de cliente (fintech/
bancos) ya se confirmó ([decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md));
sigue sin cerrar cuál perfil es *el* usuario objetivo del MVP → [P-07](../00-proyecto/preguntas-abiertas.md#p-07).

## Narrativa de la propuesta de solución

| | |
|---|---|
| **Estado** | 🟡 **Borrador — pendiente de validar con research** |
| **Fecha** | 2026-09-10 |
| **Ticket** | [11. Narrativa de la propuesta de solución](https://trello.com/c/dcgkOG5x) |
| **Método** | Estructura de 3 actos (Aristóteles) — [Clase 05](../01-clases/clase-05-oratoria-y-storytelling.md) |

> ⚠️ **Materia prima:** las 3 reformulaciones de arriba, ninguna hipótesis nueva. Por lo mismo que
> hay 3 reformulaciones y no 1 ([P-07](../00-proyecto/preguntas-abiertas.md#p-07) sigue abierta),
> hay **3 narrativas**, una por perfil — elegir una sola narrativa hoy adelantaría esa respuesta sin
> evidencia.

### 🔴 Dos trampas que esta narrativa tiene que esquivar

1. **Trampa 3 del océano rojo** — "confundir innovación de valor con tecnología". Ninguna de las
   tres narrativas puede arrancar por "usamos IA".
2. **Clave 2 de Robbins** — no se habla del MVP, se habla del problema que resuelve, con un número.
   Hoy **no tenemos ese número**: sale del User Research, todavía en cero. Cada narrativa lo deja
   marcado como hueco explícito en vez de inventarlo.

### A — Analista de fraude

**INICIO.** Todos los días llega una cola de transacciones para revisar. Las reglas predefinidas
atrapan lo conocido — pero el fraude que importa es el que **no** estaba contemplado, y ese pasa o
se atasca en una revisión manual sin más ayuda que el criterio propio.

**DESARROLLO.** Sin nada que cambie, cada caso dudoso sigue dependiendo de la experiencia individual
del analista, con la misma información limitada de siempre y sin poder explicar del todo por qué
una transacción es riesgosa cuando alguien pregunta. *⬜ Falta el número: cuánto tiempo o cuántos
casos mal decididos cuesta esto hoy — lo responde la entrevista del Perfil A.*

**CIERRE.** FraudLens no reemplaza ese criterio: lo asiste con un motivo explícito por transacción y
una cola priorizada, para que decidir un caso dudoso deje de depender sólo de la memoria de quien
lo revisa.

> **Test de los 10 segundos:** *"Ayudamos a analistas de fraude a decidir los casos que las reglas
> no contemplan, mostrándoles por qué cada transacción es riesgosa."*

### B — Responsable de riesgo/producto en una fintech o banco tradicional

> 🔄 **Actualizada el 2026-09-14** tras la redefinición del Perfil B —
> [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md). La versión original
> (dueño de comercio chico) queda en el historial de la sesión del 2026-09-10.

**INICIO.** Una fintech o banco maneja tráfico de transacciones bajo una exigencia regulatoria
concreta: las Comunicaciones "A" 8471 y "A" 8473 del BCRA (2026) obligan a tener una función de
gestión de riesgo de fraude, con autoevaluaciones y reportes periódicos.

**DESARROLLO.** Sin nada que cambie, esa gestión sigue dependiendo de reglas que no contemplan
casos nuevos y de la reconfiguración manual de un analista, con el riesgo regulatorio y financiero
recayendo sobre quien tiene que responder por el programa antifraude. *⬜ Falta el número: cuánto le
cuesta hoy el fraude o el incumplimiento regulatorio — lo responde la entrevista del Perfil B.*

**CIERRE.** FraudLens le da a esa fintech o banco un filtro adicional y explicable para su programa
antifraude, sin reemplazar lo que ya tienen ni requerir un equipo de ciencia de datos propio.

> **Test de los 10 segundos:** *"Ayudamos a fintechs y bancos a reforzar su gestión de riesgo de
> fraude con un filtro explicable, sin armar un equipo de ciencia de datos para eso."*

### C — Usuario final de una fintech/billetera/pasarela

> 🔄 **Actualizada el 2026-09-14** tras la redefinición del Perfil C —
> [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md). La versión original
> (consumidor genérico) queda en el historial de la sesión del 2026-09-10.

**INICIO.** A alguien le rechazan una compra o transferencia legítima en el peor momento, usando su
fintech, billetera virtual o pasarela de pago (ej. Mercado Pago, Ualá, Modo), o le aparece un cargo
que no reconoce. En los dos casos, no tiene ninguna forma de intervenir en esa decisión — la toma un
sistema que no ve.

**DESARROLLO.** Sin nada que cambie, sigue siendo una moneda al aire: unas veces el sistema lo deja
pasar sin problema, otras veces lo frena sin que pueda entender por qué. *⬜ Falta el número: con
qué frecuencia le pasa esto a la gente — lo responde la encuesta del Perfil C.*

**CIERRE.** FraudLens está del otro lado del sistema que decide por él: ayuda a que esa decisión
tenga un motivo explicable, no una moneda al aire.

> **Test de los 10 segundos:** *"Ayudamos a que rechazar una compra o aprobar un cargo dudoso deje
> de ser una moneda al aire — con un motivo explicable detrás."*

### Qué falta para converger en una sola

Estas 3 narrativas **no van a competir para siempre**: en algún momento (probablemente para The
Pitch, formato todavía sin confirmar — [P-19](../00-proyecto/preguntas-abiertas.md#p-19)) el equipo
va a tener que elegir una sola historia. Esa elección es la misma que resuelve
[P-07](../00-proyecto/preguntas-abiertas.md#p-07), y depende del research — no se adelanta acá.

## El ángulo del proyecto

De la Clase 1, la **brecha de innovación** (la paradoja de la maleta con ruedas): la rueda existe
desde el 3500 A.C. y la maleta desde el 600 D.C., pero la maleta con ruedas recién apareció en 1970.

FraudLens está en la misma situación: los **motores de reglas** antifraude existen hace décadas y el
**machine learning** también. No inventamos ninguna pieza. El valor está en **integrarlas** de una
forma que hoy no está resuelta para nuestro usuario.

Es un buen argumento para el pitch, y sale del propio material del docente.

## El ángulo opuesto (pensamiento lateral)

También de la Clase 1: *para cada idea lógica, existe una idea opuesta que también puede ser válida*.

| Enfoque lógico | Enfoque opuesto |
|---|---|
| **Detectar fraude** — buscar el 0,1% malo | **Certificar operaciones legítimas** — acelerar el 99,9% bueno |
| Métrica: fraudes detectados | Métrica: fricción evitada a clientes legítimos |
| Usuario: el que investiga | Usuario: el que quiere vender sin frenar la operación |

Vale ponerlo sobre la mesa antes de cerrar la solución. Puede que lo descartemos, pero **haberlo
considerado y documentado por qué lo descartamos suma** en el documento entregable.

## Alcance del MVP

> Se completa cuando definamos el usuario. Por ahora, la hipótesis de trabajo:

> 🔄 **2026-09-14 — El MVP es una simulación, no el sistema final.** Mientras no se resuelvan las
> cuestiones de negocio pendientes (P-07, acceso al Perfil B, dataset), el MVP demuestra el
> comportamiento del sistema (analizar, puntuar, decidir) sin construir las piezas que dependen de
> esas decisiones — ver [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md). CU-02 y CU-07
> de los [requerimientos](requerimientos-funcionales-mvp.md) pasan a ser **configuración fija al
> arrancar**, no un panel de administración en vivo.

**Sí es MVP:**
- Recibir una transacción y devolver un **score de riesgo**
- Mostrar las transacciones y su nivel de riesgo en una **pantalla**
- Un modelo entrenado con datos históricos

**No es MVP:**
- Reentrenamiento automático del modelo
- Múltiples clientes / multi-tenant
- Alertas por mail o notificaciones
- Panel de administración de usuarios y permisos
- Integraciones con procesadores de pago reales
- Explicabilidad avanzada del modelo

> Recordar el caso Uber de la Clase 1: el MVP no sólo recorta funciones, **recorta el alcance**.
> UberCab era una ciudad, una función.

## Líneas futuras / próximas versiones

Lo que queda **fuera del MVP** no se descarta — es la lista de por dónde seguir después:

- **Reentrenamiento automático del modelo** — hoy es manual/fijo; a futuro, aprendizaje continuo.
- **Multi-tenant** — hoy es un solo cliente; a futuro, varias fintechs/bancos en la misma
  plataforma.
- **Alertas por mail o notificaciones** en tiempo real para el analista.
- **Panel de administración** completo para el Perfil B, más allá de la configuración fija actual
  (ver [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md)).
- **Integraciones reales con procesadores de pago.**
- **Explicabilidad avanzada del modelo** (más allá de los 3 factores básicos de CU-03).
- **Cobertura AML + fraude en un solo producto** — hoy fuera de alcance, pero es lo que ya ofrece
  Feedzai según el [benchmarking](benchmarking.md); podría ser una línea de crecimiento si el
  research confirma demanda.
- **Verificar el espacio "complementa, no reemplaza"** con más research — es el hallazgo central
  del benchmarking, pero sigue siendo hipótesis (ver [P-07](../00-proyecto/preguntas-abiertas.md#p-07)).

## Chequeo contra "Problemas que NO"

El docente descartó explícitamente: reservas en general, estacionamiento, cómo viajar, filas y
turnos, pedidos y tiendas online, pagos de colegio o renta, calcular/dividir/medir gastos,
información de estudios médicos e historia clínica, gestores de biblioteca / taller mecánico /
edificio o cualquier ABM, mascotas perdidas y refugios, gimnasios, trackeo de camiones/perros/pedidos,
y qué cocinar con lo que hay en la heladera.

**FraudLens no cae en ninguna de esas categorías.** ✅
