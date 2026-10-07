# Encuesta Perfil C — respuestas (datos)

| | |
|---|---|
| **Estado** | 🟡 Datos tal como llegaron, **anonimizados**. Sin validar por el equipo |
| **Fuente** | Export de respuestas del Google Form [*Encuesta sobre experiencias de fraude en bancos y fintech*](https://forms.gle/ZLfhijskphLA1Fxu9), **aportado por FM el 2026-10-07** (`FraudLens_encuesta.xlsx`; los `.xlsx` no se versionan en este repo) |
| **Respuestas** | **28** |
| **Período** | 16/9 al 22/9/2026 *(según la marca temporal del Form)* |
| **Análisis** | [`encuesta-perfil-c-analisis.md`](encuesta-perfil-c-analisis.md) |

## Qué se hizo con los datos, y qué se sacó

- **Se numeraron las respuestas R01 a R28** en el orden del export.
- **Se omitió la marca temporal de cada fila**; solo queda el rango de fechas de arriba. La encuesta se difundió como anónima.
- **Una respuesta nombraba un club puntual** (R09, pregunta 10): se reemplazó por `[nombre de un club — omitido por anonimato]`. Es lo **único** que se tocó. El resto está
  **textual**, con sus errores de tipeo.
- **No se corrigió ninguna inconsistencia** entre respuestas (ver el análisis).
- ✅ **La estructura del formulario (opciones de cada pregunta) se confirmó el 2026-10-07** con un relevamiento hecho por otro chat de Claude con
  Claude in Chrome, que leyó los datos de la página pública del Form sin responderlo. Está en la sección siguiente. El export de Excel, por sí solo,
  trae únicamente lo que cada persona eligió.

## Estructura del formulario

> **Fuente:** relevamiento del 2026-10-07 hecho por otro chat de Claude con Claude in Chrome, **solo lectura** (no se respondió el Form). Lo leyó de los datos
> internos de la página pública. **No pudo ver la pestaña de Respuestas** (requiere acceso de editor), así que **el total de respuestas del Form no está
> verificado**: las 28 salen del export.

- **Título publicado:** *Encuesta sobre experiencias de fraude en bancos y fintech*. *(El nombre interno del archivo es "Formulario sin título". El diseño previo, en [`user-research.md`](user-research.md), lo llamaba "Encuesta sobre fraude y rechazos de operaciones".)*
- **Descripción:** *"No se te va a pedir nombre, documento, número de tarjeta ni datos bancarios"*. Es el único texto sobre anonimato. **No hay texto de consentimiento.**
- **Sin secciones y sin lógica condicional:** el formulario **no filtra** a nadie. **Solo las preguntas 1 y 2 son obligatorias**; por eso hay respuestas en blanco en las demás.
- **El formulario seguía aceptando respuestas** el 2026-10-07 (la página pública mostraba las preguntas y el botón de enviar, sin aviso de cierre).

| # | Pregunta | Tipo | Oblig. | Opciones, en orden *(entre paréntesis, cuántas de las 28 la marcaron)* |
|---|---|---|---|---|
| 1 | ¿Con qué frecuencia realizás compras o pagos usando tarjetas o billeteras virtuales? | Opción múltiple | **Sí** | Todos los días (14) · Varias veces por semana (12) · Algunas veces al mes (2) · Menos de una vez al mes (0) · No utilizo estos medios (0) |
| 2 | En los últimos 12 meses, ¿alguna vez te rechazaron una compra que considerabas legítima? | Opción múltiple | **Sí** | Sí (11) · No (12) · No estoy seguro (5) |
| 3 | Si te ocurrió, ¿con qué frecuencia pasó? | Opción múltiple | No | Una sola vez (4) · Dos o tres veces (7) · Varias veces (0) · No recuerdo (3) · No me ocurrió (12) · *(en blanco: 2)* |
| 4 | ¿Qué hiciste después de que rechazaran la compra? | Opción múltiple | No | Intenté nuevamente y funcionó (2) · Use otro medio de pago *(sin tilde, así figura)* (8) · Contacté al banco o billetera (5) · Abandoné la compra (0) · No me ocurrió (9) · **Otros** (texto libre) (0) · *(en blanco: 4)* |
| 5 | En los últimos 12 meses, ¿alguna vez detectaste un consumo o transferencia que no reconocías? | Opción múltiple | No | Sí (10) · No (17) · No estoy seguro (1) |
| 6 | Si te ocurrió, ¿cómo te enteraste? | Opción múltiple | No | Revisando el resumen o viendo la transacción en la aplicación (10) · Por una notificación (0) · Por un llamado o aviso de la entidad (2) · No me ocurrió (11) · **Otros** (texto libre) (0) · *(en blanco: 5)* |
| 7 | ¿Qué situación te generaría un mayor inconveniente? | Opción múltiple | No | Que rechacen una compra legítima (1) · Que se apruebe una operación que no hice (19) · Ambas por igual (8) · Ninguna de las dos (0) · No estoy seguro (0) |
| 8 | Cuando una operación es rechazada, ¿qué explicación recibís normalmente? | Opción múltiple | No | Una explicación poco clara (15) · **Una explicación clara (0)** · Ninguna explicación. *(con punto final)* (6) · No recuerdo (3) · Nunca me ocurrió (4) |
| 9 | ¿Qué información te gustaría recibir cuando una operación es rechazada por seguridad? | Párrafo | No | — |
| 10 | Contanos brevemente la última experiencia que hayas tenido con una compra rechazada o un consumo no reconocido. | Párrafo | No | — |
| 11 | ¿En qué rango de edad te encontrás? | Opción múltiple | No | Menos de 18 (0) · 18–24 (11) · 25–34 (11) · 35–44 (2) · 45–54 (2) · 55 o más (2) · Prefiero no responder (0) |

Los 11 textos y su orden **coinciden** con los del export de respuestas.

> ⚠️ La descripción de la encuesta en [`user-research.md`](user-research.md#encuesta--perfil-c-usuario-final-de-fintechbilleterapasarela) listaba **7 ítems** con
> otras opciones y un filtro inicial: es el **diseño previo a la difusión**. **Para lo que se respondió, vale esta estructura.**

## Respuestas cerradas (preguntas 1 a 8 y edad)


| R | P1 Frecuencia de compras | P2 Rechazo 12 m | P3 Cuántas veces | P4 Qué hizo | P5 Consumo no reconocido | P6 Cómo se enteró | P7 Mayor inconveniente | P8 Explicación recibida | Edad |
|---|---|---|---|---|---|---|---|---|---|
| R01 | Todos los días | Sí | Dos o tres veces | Contacté al banco o billetera | Sí | Por un llamado o aviso de la entidad | Que se apruebe una operación que no hice | Ninguna explicación. | 18–24 |
| R02 | Varias veces por semana | No | No me ocurrió | — | No | — | Que se apruebe una operación que no hice | Nunca me ocurrió | 18–24 |
| R03 | Todos los días | No estoy seguro | No recuerdo | Intenté nuevamente y funcionó | No | Revisando el resumen o viendo la transacción en la aplicación | Que se apruebe una operación que no hice | Una explicación poco clara | 18–24 |
| R04 | Todos los días | No estoy seguro | No me ocurrió | No me ocurrió | Sí | Revisando el resumen o viendo la transacción en la aplicación | Que se apruebe una operación que no hice | Una explicación poco clara | 18–24 |
| R05 | Varias veces por semana | Sí | Una sola vez | Use otro medio de pago | No | Revisando el resumen o viendo la transacción en la aplicación | Que se apruebe una operación que no hice | Una explicación poco clara | 18–24 |
| R06 | Varias veces por semana | No | No me ocurrió | No me ocurrió | No | No me ocurrió | Ambas por igual | No recuerdo | 18–24 |
| R07 | Todos los días | Sí | Dos o tres veces | Use otro medio de pago | No | No me ocurrió | Que se apruebe una operación que no hice | Una explicación poco clara | 18–24 |
| R08 | Varias veces por semana | No | No recuerdo | Intenté nuevamente y funcionó | No | No me ocurrió | Que se apruebe una operación que no hice | No recuerdo | 18–24 |
| R09 | Todos los días | No | No me ocurrió | — | Sí | Por un llamado o aviso de la entidad | Que se apruebe una operación que no hice | Una explicación poco clara | 45–54 |
| R10 | Algunas veces al mes | Sí | Una sola vez | Contacté al banco o billetera | No | No me ocurrió | Que rechacen una compra legítima | Una explicación poco clara | 35–44 |
| R11 | Varias veces por semana | Sí | Una sola vez | Use otro medio de pago | No | — | Que se apruebe una operación que no hice | Una explicación poco clara | 55 o más |
| R12 | Todos los días | No | No me ocurrió | No me ocurrió | Sí | Revisando el resumen o viendo la transacción en la aplicación | Que se apruebe una operación que no hice | Una explicación poco clara | 25–34 |
| R13 | Varias veces por semana | No | No me ocurrió | No me ocurrió | No | No me ocurrió | Que se apruebe una operación que no hice | Nunca me ocurrió | 45–54 |
| R14 | Varias veces por semana | Sí | Una sola vez | Use otro medio de pago | Sí | Revisando el resumen o viendo la transacción en la aplicación | Ambas por igual | Una explicación poco clara | 25–34 |
| R15 | Todos los días | Sí | Dos o tres veces | Use otro medio de pago | No | No me ocurrió | Que se apruebe una operación que no hice | Una explicación poco clara | 35–44 |
| R16 | Varias veces por semana | No | No me ocurrió | No me ocurrió | Sí | Revisando el resumen o viendo la transacción en la aplicación | Ambas por igual | Nunca me ocurrió | 25–34 |
| R17 | Todos los días | No estoy seguro | No recuerdo | Contacté al banco o billetera | Sí | Revisando el resumen o viendo la transacción en la aplicación | Que se apruebe una operación que no hice | No recuerdo | 18–24 |
| R18 | Varias veces por semana | No | No me ocurrió | No me ocurrió | No | No me ocurrió | Que se apruebe una operación que no hice | Ninguna explicación. | 25–34 |
| R19 | Todos los días | No estoy seguro | No me ocurrió | Use otro medio de pago | Sí | Revisando el resumen o viendo la transacción en la aplicación | Ambas por igual | Ninguna explicación. | 25–34 |
| R20 | Varias veces por semana | Sí | Dos o tres veces | Contacté al banco o billetera | No | No me ocurrió | Que se apruebe una operación que no hice | Ninguna explicación. | 25–34 |
| R21 | Algunas veces al mes | No | No me ocurrió | No me ocurrió | No | No me ocurrió | Que se apruebe una operación que no hice | Una explicación poco clara | 25–34 |
| R22 | Todos los días | No | No me ocurrió | No me ocurrió | Sí | Revisando el resumen o viendo la transacción en la aplicación | Ambas por igual | Una explicación poco clara | 25–34 |
| R23 | Varias veces por semana | Sí | Dos o tres veces | Use otro medio de pago | No estoy seguro | — | Que se apruebe una operación que no hice | Una explicación poco clara | 18–24 |
| R24 | Todos los días | No estoy seguro | — | — | No | — | Ambas por igual | Una explicación poco clara | 18–24 |
| R25 | Todos los días | No | No me ocurrió | No me ocurrió | No | No me ocurrió | Ambas por igual | Nunca me ocurrió | 55 o más |
| R26 | Todos los días | No | — | — | No | — | Que se apruebe una operación que no hice | Una explicación poco clara | 25–34 |
| R27 | Varias veces por semana | Sí | Dos o tres veces | Use otro medio de pago | Sí | Revisando el resumen o viendo la transacción en la aplicación | Ambas por igual | Ninguna explicación. | 25–34 |
| R28 | Todos los días | Sí | Dos o tres veces | Contacté al banco o billetera | No | No me ocurrió | Que se apruebe una operación que no hice | Ninguna explicación. | 25–34 |

*— = en blanco.* En las preguntas 3, 4 y 6 aparece **"No me ocurrió"** como respuesta: es una opción del Form, no un dato faltante.

## Respuestas abiertas (preguntas 9 y 10)

Textuales. Solo figuran las respuestas que tienen texto.

### R01 · 18–24
**P9 — información que le gustaría recibir:**
> que comercio, que monto y si mi tarjeta se bloqueó como medida de seguridad.

**P10 — última experiencia:**
> Estando de viaje, me rechazaron varias veces una compra. Fue muy molesto. Yo habia hecho denuncia pero tuve que llamar igual. No me daba nada de info de por que ocurria y fue muy tedioso
> 
> Despues tambien tuve unas compras fraudulentas. Se hicieron unas compras en brasil (nada que ver conmigo) y recien me di cuenta en el resumen. El banco se hizo cargo pero es increible que si no veia la fila en el resumen, no me daba cuenta

### R02 · 18–24
**P9 — información que le gustaría recibir:**
> Donde se hizo

### R03 · 18–24
**P9 — información que le gustaría recibir:**
> Informacion

**P10 — última experiencia:**
> Don´t Remember

### R04 · 18–24
**P9 — información que le gustaría recibir:**
> Principalmente el motivo, después que me llegue un mensaje o Mail o algún aviso del banco que pueda autorizarla o denegarla

**P10 — última experiencia:**
> Llame al banco y lo único que hicieron fue cancelarle la tarjeta y mandarme una nueva. Era todo un quilombo hacer el reclamo. Por suerte era un monto bajo

### R05 · 18–24
**P9 — información que le gustaría recibir:**
> Una explicación clara

**P10 — última experiencia:**
> Por usar una tarjeta de débito sin saldo. En general en esos casos la explicacion es clara, pero otras veces no sabés por qué rechaza.

### R06 · 18–24
**P9 — información que le gustaría recibir:**
> El motivo del por qué se me ha rechazado.

**P10 — última experiencia:**
> No recuerdo.

### R07 · 18–24
**P9 — información que le gustaría recibir:**
> Que me expliquen en detalle porque se rechazó y que tengo que hacer para que me la aprueben rápido

**P10 — última experiencia:**
> Varias veces que compré en Amazon me rechazaron el pago reiteradas veces sin motivo. Lo único que hacia era ir rotando entre 2 tarjetas el pago hasta que alguna la aprobaran y siempre funciokó

### R09 · 45–54

**P10 — última experiencia:**
> me drenaron la cuenta del banco cuando pague la cuota de [nombre de un club — omitido por anonimato], ese dinero luego fue utilizado para pagar las deudas del club

### R10 · 35–44
**P9 — información que le gustaría recibir:**
> Si es por monto alto o por compra en lugar poco frecuente

**P10 — última experiencia:**
> Al pagar pasajes me rechazaba el monto y tuve que contactar a la tarjeta para que lo autoricen y tenía miedo de perder el pasaje reservado

### R12 · 25–34
**P9 — información que le gustaría recibir:**
> El motivo de manera entendible y a su vez la solución

**P10 — última experiencia:**
> -

### R13 · 45–54
**P9 — información que le gustaría recibir:**
> Que me indiquen la causa

**P10 — última experiencia:**
> No tuve

### R14 · 25–34
**P9 — información que le gustaría recibir:**
> El motivo exacto del rechazo

**P10 — última experiencia:**
> Me rechazaron un pago en un restaurante pero no figuraba porqué. Probamos pasar la tarjeta varias veces y siempre se rechazaba. Finalmente abone a traves de mercadopago donde tenia esa tarjeta cargada y pasó bien (nunca se entendió porque el pago con la tarjeta directa no entraba)

### R15 · 35–44
**P9 — información que le gustaría recibir:**
> el porque (ejemplo, tarjeta vencida, bloqueada, etc)

**P10 — última experiencia:**
> compre y el resultado fue "pago rechazado"

### R16 · 25–34
**P9 — información que le gustaría recibir:**
> Mensaje por wpp o correo electrónico.

**P10 — última experiencia:**
> No recuerdo puntualmente.

### R17 · 18–24
**P9 — información que le gustaría recibir:**
> Tener un aviso previo al rechazo

**P10 — última experiencia:**
> No tuve por el momento

### R18 · 25–34
**P9 — información que le gustaría recibir:**
> El motivo, o en cuanto tiempo se podría "liberar" su uso

**P10 — última experiencia:**
> No me ocurrió, pero si a un familiar con un consumo no reconocido. 
> A través de compras en Mercado Libre, usaron sus datos de la tarjeta para realizar compras de electrodomésticos o comida, a través de Mercado Pago.
> Cómo habían usado esa tarjeta hace mucho por ML, me llegaban mails de confirmación de pago de dichos consumos a por Mercado Pago. Si no era por eso, nos enteramos con el resumen y no en el instante.

### R19 · 25–34
**P9 — información que le gustaría recibir:**
> Los motivos

### R20 · 25–34
**P9 — información que le gustaría recibir:**
> Motivo/que hacer para aprobarla

### R21 · 25–34
**P9 — información que le gustaría recibir:**
> Una manera facil de habilitar la compra. Siempre son mil vueltas

**P10 — última experiencia:**
> Una compra de un electrodomestico, por el monto, se me rechazó y tuve que llamar para habilitar.

### R22 · 25–34
**P9 — información que le gustaría recibir:**
> Motivo de rechazo, claro,ejemplo si es porque la cuenta bancaria donde hago la transferencia ya no está en uso, si es una transferencia a un usuario que no tengo agendado, etc

**P10 — última experiencia:**
> Compra que no hice, realicé el desconocimiento en el banco y lo resolvieron

### R23 · 18–24
**P9 — información que le gustaría recibir:**
> En detalle el motivo

**P10 — última experiencia:**
> Hace poco me rechazaron una compra con tarjeta de crédito de mercado pago, a través de coto digital. Sigo sin entender por qué, ya que ese mismo medio de pago, se puede utilizar en sucursales.

### R26 · 25–34
**P9 — información que le gustaría recibir:**
> Los motivos claros y los pasos a seguir

### R27 · 25–34
**P9 — información que le gustaría recibir:**
> Los motivos especificos del rechazo, y la opcion de autorizar la compra inmediatamente

**P10 — última experiencia:**
> Comsumo en tarjeta de credito de una compea que yo no realice, desconoci la compra, me anularon la tarjeta de credito e inmediatamente me tramitaron otra. En el resumen siguiente me devolvieron el dinero de la compra no realizada

### R28 · 25–34
**P9 — información que le gustaría recibir:**
> El detalle y como se soluciona

**P10 — última experiencia:**
> Compré, me rechazó el pago y tuve que llamar al banco para que me lo aprueben. Re intenté y funcionó
