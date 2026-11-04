# Los 3 perfiles de usuario a investigar

| | |
|---|---|
| **Estado** | ✅ **Decidido** por el equipo (2026-09-02) · Perfil B y C **redefinidos** el 2026-09-14 |
| **Ticket** | [1. Decidir los 3 perfiles de usuario](https://trello.com/c/IYegyoM6) |
| **Método** | [Análisis de 6 Sombreros (2/9)](analisis/6-sombreros-usuario-objetivo.md) · [Análisis de 6 Sombreros — enfoque fintech (14/9)](analisis/6-sombreros-enfoque-fintech.md) |
| **Bloquea a** | Plan de research · User Persona ×3 · Mapa de Empatía ×3 · Problem Statement |
| **User Persona y Mapas** | 🟡 [Borrador con huecos explícitos](#user-persona) (2026-11-04), **sin validar por el equipo** |

> 🔄 **2026-09-14 — Perfil B y C redefinidos.** El equipo decidió que el enfoque del proyecto es
> llegar a **empresas fintech y bancos tradicionales**, no comercio chico. Ver
> [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md). Lo que sigue abajo
> ya refleja esa redefinición; la versión original del 2/9 (comercio chico) queda documentada en el
> [análisis de 6 sombreros del 2/9](analisis/6-sombreros-usuario-objetivo.md) como parte del
> historial de la decisión.

## La decisión

**Tres perfiles en tres niveles distintos del mismo problema**, con la accesibilidad como filtro
duro.

No son tres variantes del mismo usuario: son tres personas que viven el fraude desde lugares
estructuralmente diferentes. Uno lo **sufre**, otro lo **decide**, otro lo **paga**. Por eso los
tres Mapas de Empatía van a salir genuinamente distintos, que es lo que pide la consigna.

| | Perfil | Rol en el problema | Cómo se investiga | Acceso |
|---|---|---|---|---|
| **A** | **Analista de fraude** (dentro de la fintech/banco cliente) | El que **decide**: revisa la cola de casos y aprueba, rechaza o escala | Entrevistas en profundidad | ✅ **Nicolás entrevistado** |
| **B** | **Analista de producto en una fintech, billetera virtual, pasarela de pago o banco tradicional** | El que **paga/decide integrar** FraudLens | Entrevistas | ✅ **Agustín identificado** |
| **C** | **Usuario final de una fintech, billetera virtual o pasarela de pago** (ej. Mercado Pago, Ualá, Modo) con fraude o rechazo indebido | El que lo **sufre**: le clonan la tarjeta, o le rechazan una compra legítima | Encuesta abierta | 🔄 **En difusión** |

### Perfil A — Analista de fraude

**Es el usuario directo del producto.** Es quien va a tener el dashboard abierto varias horas por
día y quien toma la decisión que FraudLens asiste.

- **Qué buscamos entender:** cómo es hoy su cola de trabajo, con qué herramientas decide, cuánto
  tarda por caso, qué información le falta en el momento de decidir, y qué pasa cuando se equivoca
  en cada dirección.
- **Acceso:** ✅ **ML confirmó que consigue entrevistas** en las próximas dos semanas. Es el activo
  más valioso del research y hay que usarlo bien: son pocas entrevistas y no se repiten.
- **Por qué importa que sea entrevista y no encuesta:** lo que necesitamos de él es el *proceso* y
  las *excepciones*, y eso no entra en un formulario.

### Perfil B — Analista de producto en una fintech o banco tradicional

**Es quien pone la plata.** Trabaja en una fintech, billetera virtual, pasarela de pago o banco
tradicional, y es quien evalúa e integra una solución antifraude como FraudLens.

> 🔄 **Redefinido el 2026-09-14** — antes era "dueño de comercio/e-commerce chico". Ver
> [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md) y el
> [análisis de 6 sombreros](analisis/6-sombreros-enfoque-fintech.md).

- **Qué buscamos entender:** cómo gestiona hoy el riesgo de fraude, qué le exige la normativa (las
  Comunicaciones "A" 8471 y "A" 8473 del BCRA obligan a tener una función de gestión de riesgo de
  fraude), y cuál de los dos errores le duele más — dejar pasar un fraude o rechazar un cliente
  bueno.
- **Por qué está:** es el perfil que conecta el problema con el **modelo de negocio**. Sirve
  directo para la Clase 6 (BMC).
- ✅ **Agustín entrevistado.**

### Perfil C — Usuario final de una fintech, billetera virtual o pasarela de pago

**Es quien sufre el problema en el cuerpo**, y el único perfil al que podemos llegar en volumen.

> 🔄 **Redefinido el 2026-09-14** — antes era "consumidor" genérico. Ahora es específicamente
> alguien que usa una fintech/billetera/pasarela (ej. Mercado Pago, Ualá, Modo). Ver
> [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md).

- **Qué buscamos entender:** la experiencia del fraude vivido, y sobre todo **el falso positivo** —
  que te rechacen una compra o transferencia legítima en el peor momento. Es el costo invisible que
  nadie mide.
- **Por qué está:** hace que el research tenga **datos reales en cantidad**, que es lo que el
  docente exige, sin depender de conseguir entrevistas.

> 🔎 **Primer dato de la encuesta (2026-10-07, 28 respuestas, sin validar):** a la pregunta de cuál situación genera más inconveniente, **19 de 28** eligieron *"que se apruebe una operación que no hice"*, **8** *"ambas por igual"* y **1** *"que rechacen una compra legítima"*. El texto de arriba ("sobre todo el falso positivo") **no se modificó**: lo tiene que revisar el equipo. Ver [`encuesta-perfil-c-analisis.md`](encuesta-perfil-c-analisis.md#5-qué-dice-esto-frente-a-lo-que-el-repo-daba-por-hipótesis).

## Qué se descartó y por qué

| Descartado | Motivo |
|---|---|
| **Administrador del sistema** | Es un **rol de configuración**, no una persona con un dolor propio. Su User Persona y su Mapa de Empatía saldrían vacíos: no sufre el problema, sólo opera la herramienta. Sigue existiendo como actor del software, pero no es sujeto de research. |
| **Sistema cliente** (la API que consume) | No es una persona. No se le puede hacer un mapa de empatía. |
| **Tres analistas de fraude** (3 personas del mismo perfil) | El docente confirmó que pide **3 perfiles distintos**, no 3 personas del mismo. Ver [P-18](../00-proyecto/preguntas-abiertas.md#p-18). |

## ⚠️ El sesgo que hay que vigilar

Del sombrero rojo del análisis, y queda escrito acá para que no actúe en silencio:

> **Hay tentación de elegir el usuario que le queda cómodo al prototipo que ya existe**, en vez del
> que le conviene al proyecto.

El equipo escribió los requerimientos y armó un prototipo **antes** de saber para quién — que es
exactamente lo que la Clase 4 advierte que hace fallar al 90% de las startups. Este research existe
para corregir eso, no para justificarlo.

**Regla que se desprende:** si el research contradice los
[requerimientos](requerimientos-funcionales-mvp.md) o la
[identidad visual](identidad/propuesta-canva.md), se corrigen **esos documentos**, no el research.

## Relación con P-07

El **tipo de cliente** (empresas fintech y bancos tradicionales, no comercio chico) quedó decidido
por el equipo el 2026-09-14 — ver [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md).

Pero esto **no cierra del todo** [P-07](../00-proyecto/preguntas-abiertas.md#p-07): falta confirmar
si *el* usuario objetivo del MVP (a quién se le diseña la interfaz, el dashboard, el pitch) es el
Perfil A (analista) o el Perfil B (quien decide integrarlo) — eso sigue siendo una conclusión que
sale **del research**, no de antes.

## User Persona

> 🟡 **Borrador del 2026-11-04, sin validar por el equipo.** Tarjeta
> [4. User Persona × 3 perfiles](https://trello.com/c/dlJzvQPi). Formato del docente:
> [Clase 4](../01-clases/clase-04-design-thinking.md#user-persona).

**Cómo leer esta sección y la siguiente:**

- **Solo está lo que tiene fuente.** `⬜ Sin dato` significa que el research no lo relevó. No se
  completó con supuestos ni se repreguntó a los entrevistados (decisión de MDV, 2026-11-04).
- **Los perfiles no llevan nombre ficticio:** sería un dato sin fuente.
- **Perfil A y Perfil B salen de una sola entrevista cada uno**, y de su resumen en
  [`user-research.md`](user-research.md#resultados-preliminares-de-entrevistas), no de una
  transcripción. Describen a una persona, no a un usuario tipo.
- **Perfil C es un agregado de 28 respuestas auto-seleccionadas**, no una persona. Los conteos y
  las citas salen de las [respuestas](encuesta-perfil-c-respuestas.md) y del
  [primer análisis](encuesta-perfil-c-analisis.md), que sigue sin validar. `P#` es la pregunta del
  Form y `R##` es la respuesta.

### Perfil A — Analista de fraude

**Fuente:** entrevista a Nicolás.

| Bloque | Dato |
|---|---|
| **Características** | **Edad:** ⬜ Sin dato · **Familia y relaciones:** ⬜ Sin dato · **Ocupación:** analista de fraude (entidad: ⬜ Sin dato) · **Intereses/Hobbies:** ⬜ Sin dato · **Localización:** ⬜ Sin dato |
| **Momento / Escenario** | Tiene que reunir y relacionar información distribuida entre distintas herramientas. Eso demora la investigación, puede generar revisiones repetidas y dificulta entender el contexto completo de una alerta. El motor actual detecta bien patrones conocidos, pero genera falsos positivos y no siempre explica por qué activó una alerta. Los casos ambiguos, los montos inusuales y los dispositivos nuevos suelen pasar a revisión manual |
| **Motivaciones** | **Laborales:** su mejora prioritaria sería una vista unificada del caso, con línea de tiempo, resumen de señales de riesgo, historial de operaciones, datos del dispositivo y antecedentes del cliente. **Personales y de carrera:** ⬜ Sin dato |

### Perfil B — Analista de producto

**Fuente:** entrevista a Agustín.

| Bloque | Dato |
|---|---|
| **Características** | **Edad:** ⬜ Sin dato · **Familia y relaciones:** ⬜ Sin dato · **Ocupación:** analista de producto en una fintech, según la [tarjeta del Plan de research](https://trello.com/c/EkjU3QyB) (entidad: ⬜ Sin dato) · **Intereses/Hobbies:** ⬜ Sin dato · **Localización:** ⬜ Sin dato |
| **Momento / Escenario** | Su desafío principal es reducir el fraude sin perjudicar a los usuarios legítimos. Su satisfacción con el motor actual es intermedia: responde bien ante patrones conocidos y permite aplicar controles rápidamente, pero necesita mayor precisión y adaptación. La interfaz actual fragmenta la información, dificulta comparar períodos y no siempre presenta indicadores claros |
| **Motivaciones** | **Laborales:** su funcionalidad prioritaria sería un panel configurable por perfil, con vistas para analistas, líderes operativos, riesgo y producto. **Personales y de carrera:** ⬜ Sin dato |

> ⚠️ **Hipótesis sin evidencia:** este documento define al Perfil B como *"el que paga/decide
> integrar"*. El resumen de la entrevista **no registra** presupuesto, decisión de compra ni
> disposición a pagar, así que ese rol no se cargó en la Persona.

### Perfil C — Usuario final

**Fuente:** encuesta, 28 respuestas.

| Bloque | Dato |
|---|---|
| **Características** | **Edad:** 22 de 28 tienen entre 18 y 34 años (P11) · **Familia y relaciones:** ⬜ Sin dato · **Ocupación:** ⬜ Sin dato · **Intereses/Hobbies:** ⬜ Sin dato · **Localización:** ⬜ Sin dato · **Uso de medios de pago:** 26 de 28 pagan con tarjeta o billetera todos los días o varias veces por semana (P1) |
| **Momento / Escenario** | En los últimos 12 meses, a 11 de 28 les rechazaron una compra que consideraban legítima (P2) y 10 de 28 detectaron un consumo o una transferencia que no reconocían (P5). A 18 de 28 les pasó al menos una de las dos cosas. 21 de 28 dicen que, cuando les rechazan una operación, reciben una explicación poco clara o ninguna (P8) |
| **Motivaciones** | Ante un rechazo por seguridad, 15 quieren saber el motivo, 8 quieren saber qué hacer, cómo habilitar la operación o cuánto tarda, y 4 quieren un aviso o un canal (P9, lectura manual). **Personales y de carrera:** ⬜ Sin dato |

> ⚠️ **Contradicción sin resolver:** a la pregunta de qué les generaría mayor inconveniente (P7),
> 19 de 28 eligieron *"que se apruebe una operación que no hice"*, 8 *"ambas por igual"* y 1 *"que
> rechacen una compra legítima"*. La descripción del Perfil C de arriba dice *"sobre todo el falso
> positivo"*. Ese texto no se modificó: lo tiene que revisar el equipo
> ([análisis, punto 5.1](encuesta-perfil-c-analisis.md#5-qué-dice-esto-frente-a-lo-que-el-repo-daba-por-hipótesis)).

## Mapa de Empatía

> 🟡 **Borrador del 2026-11-04, sin validar por el equipo.** Tarjeta
> [5. Mapa de Empatía × 3 perfiles](https://trello.com/c/8pJ24yzo). Cuadrantes del docente:
> [Clase 4](../01-clases/clase-04-design-thinking.md#mapa-de-empatía). Se aplican las reglas de
> lectura de [User Persona](#user-persona).
>
> **¿Qué OYE?** está sin dato en los 3 perfiles: ni las entrevistas ni la encuesta relevaron qué
> dicen sus amigos, su familia, su jefe, las personas influyentes o los medios.

### Perfil A — Analista de fraude

**Fuente:** entrevista a Nicolás.

| Cuadrante | Lo que consta | Sin dato |
|---|---|---|
| **¿Qué PIENSA Y SIENTE?** | La IA ayuda a detectar patrones complejos, priorizar alertas y analizar grandes volúmenes, pero requiere supervisión por riesgos de sesgo y falta de explicabilidad. No debería bloquear cuentas ni rechazar casos sensibles sin intervención humana | ⬜ Emociones · aspiraciones · lo que no dice |
| **¿Qué OYE?** | — | ⬜ Todo el cuadrante |
| **¿Qué VE?** | Información distribuida entre distintas herramientas · falsos positivos · alertas que no siempre explican por qué se activaron · casos ambiguos, montos inusuales y dispositivos nuevos en revisión manual | ⬜ Oferta del mercado · amigos |
| **¿Qué DICE Y HACE?** | **Dice** que su mayor dolor es reunir y relacionar la información. **Hace** esa reunión de información entre herramientas para investigar las alertas | ⬜ Actitud en público · trato con los demás · diferencias entre lo que dice y lo que piensa |
| **ESFUERZOS / ¿Qué lo FRUSTRA?** | Investigación demorada · revisiones repetidas · dificultad para entender el contexto completo de una alerta · falsos positivos · alertas sin explicación | ⬜ Miedos |
| **RESULTADOS / ¿Qué lo MOTIVA?** | Una vista unificada del caso, con línea de tiempo, resumen de señales de riesgo, historial de operaciones, datos del dispositivo y antecedentes del cliente | ⬜ Qué es el éxito para esta persona |

### Perfil B — Analista de producto

**Fuente:** entrevista a Agustín.

| Cuadrante | Lo que consta | Sin dato |
|---|---|---|
| **¿Qué PIENSA Y SIENTE?** | Su satisfacción con el motor actual es intermedia. La IA puede mejorar la detección de anomalías, automatizar análisis y adaptar controles | ⬜ Emociones · aspiraciones · lo que no dice |
| **¿Qué OYE?** | — | ⬜ Todo el cuadrante |
| **¿Qué VE?** | Información fragmentada en la interfaz actual · dificultad para comparar períodos · indicadores que no siempre son claros · un motor que responde bien ante patrones conocidos | ⬜ Oferta del mercado · amigos |
| **¿Qué DICE Y HACE?** | **Dice** que el motor necesita mayor precisión y adaptación, y que faltan simulación de cambios, explicabilidad y seguimiento más completo. **Hace:** el desafío se mide con pérdidas económicas, tasa de fraude, falsos positivos, operaciones rechazadas, tiempo de resolución, reclamos, confianza y abandono | ⬜ Actitud en público · trato con los demás · diferencias entre lo que dice y lo que piensa |
| **ESFUERZOS / ¿Qué lo FRUSTRA?** | Reducir el fraude sin perjudicar a los usuarios legítimos · falta de simulación, explicabilidad y seguimiento · obstáculos para la IA: calidad de datos, integración, regulación y falta de especialistas | ⬜ Miedos |
| **RESULTADOS / ¿Qué lo MOTIVA?** | Un panel configurable por perfil. En IA se exigirían trazabilidad, explicaciones comprensibles, monitoreo y supervisión humana en decisiones de alto impacto | ⬜ Qué es el éxito para esta persona, más allá de los indicadores que se miden |

### Perfil C — Usuario final

**Fuente:** encuesta, 28 respuestas. Las citas son textuales.

| Cuadrante | Lo que consta | Sin dato |
|---|---|---|
| **¿Qué PIENSA Y SIENTE?** | 19 de 28 eligen como mayor inconveniente que se apruebe una operación que no hicieron (P7) · *"tenía miedo de perder el pasaje reservado"* (R10) · *"es increible que si no veia la fila en el resumen, no me daba cuenta"* (R01) | ⬜ Aspiraciones · lo que no dice |
| **¿Qué OYE?** | — | ⬜ Todo el cuadrante |
| **¿Qué VE?** | 15 de 28 reciben una explicación poco clara y 6 ninguna; ninguno marcó *"Una explicación clara"* (P8) · de los 10 que detectaron un consumo ajeno, 8 lo vieron revisando el resumen o la aplicación, 2 por un llamado o aviso de la entidad y ninguno por una notificación (P6) · *"compre y el resultado fue \"pago rechazado\""* (R15) | ⬜ Entorno · amigos · oferta del mercado |
| **¿Qué DICE Y HACE?** | **Hace,** de los 11 con un rechazo: 7 usaron otro medio de pago y 4 contactaron al banco o billetera (P4). **Dice:** *"Siempre son mil vueltas"* (R21) · *"Era todo un quilombo hacer el reclamo"* (R04) | ⬜ Actitud en público · trato con los demás · diferencias entre lo que dice y lo que piensa |
| **ESFUERZOS / ¿Qué lo FRUSTRA?** | A 7 de esos 11 les pasó dos o tres veces (P3) · llamar al banco para habilitar una compra legítima (R01, R10, R21, R28) · no saber por qué se rechazó (R07, R14, R15, R23) · enterarse tarde de un consumo ajeno: *"nos enteramos con el resumen y no en el instante"* (R18, sobre un familiar) | — |
| **RESULTADOS / ¿Qué lo MOTIVA?** | Saber el motivo del rechazo (15) · saber qué hacer, cómo habilitar la operación o cuánto tarda (8) · recibir un aviso o tener un canal (4) · *"la opcion de autorizar la compra inmediatamente"* (R27) | ⬜ Qué es el éxito para esta persona |

## Qué falta para cerrar las tarjetas 4 y 5

| Criterio de la tarjeta | Estado |
|---|---|
| 3 User Persona con los 3 bloques | 🟡 Están los 3 bloques, pero **Características** tiene huecos en los 3 perfiles |
| 3 Mapas **sin cuadrantes vacíos** | 🔴 **No se cumple:** ¿Qué OYE? está vacío en los 3 perfiles, y otros cuadrantes están incompletos |
| Cargados en `usuarios.md` | ✅ |
| Validación del equipo | ⬜ Pendiente. El equipo tiene que aceptar estos huecos, o decidir cómo completarlos |

## Estado del ticket

| Ítem | Estado |
|---|---|
| ML respondió sobre el acceso a expertos | ✅ Hay acceso |
| P-18 preguntada al docente | ✅ Son 3 perfiles distintos |
| Los 3 perfiles escritos | ✅ Este documento |
| El equipo validó el sombrero rojo | 🟡 **3 de 4 voces** (MDV, FM, FGR). **Falta ML.** Tarjeta cerrada el 2026-09-30 por decisión de MDV sin la voz de ML — se completa cuando ML responda. Ver [puntos a debatir](analisis/6-sombreros-usuario-objetivo.md#-pendiente-el-equipo-tiene-que-escribir-el-sombrero-rojo) |
| Tarjeta de Trello | ✅ Movida a Hecho el 2026-09-30, con comentario de resolución |
