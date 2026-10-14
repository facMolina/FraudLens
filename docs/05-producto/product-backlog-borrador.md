# Product Backlog — borrador (CU-01 a CU-07)

> 🟡 **BORRADOR de MDV con asistencia de Claude Code (2026-10-14). No es definición del equipo.**
> Cubre los 7 casos de uso de los requerimientos de ML, con CU-02 y CU-07 en su versión recortada
> por la 0005. **Falta cruzar con el User Story Mapping de FM**
> ([tarjeta](https://trello.com/c/mxSfKQw6)), que puede cambiar cómo se agrupan o se nombran las historias.
>
> Tarjeta: [Escribir el Product Backlog del MVP](https://trello.com/c/MhuvgAQX) (entregable del **14/10**).

## Qué es esto y qué no

- **Formato:** el de la [Clase 10](../01-clases/clase-10-user-story-mapping-y-backlog.md) — título con
  verbo en infinitivo · **Como / Quiero / Para** · criterios **Dado / Cuando / Entonces**.
- **Sin estimar** (FM, 2026-10-07, [P-31](../00-proyecto/preguntas-abiertas.md#p-31)).
- **Prioridad / MoSCoW: ⬜ no decidida.** El equipo todavía no clasificó
  ([`alcance-mvp-moscow.md`](alcance-mvp-moscow.md)). Cada HU tiene la columna vacía a propósito.
- **Fuente de cada criterio:** *(R)* sale de los
  [requerimientos de ML](requerimientos-funcionales-mvp.md) (que son borrador de ML, no definición) ·
  *(D)* de la decisión 0005 · *(S)* sugerencia de Claude Code, sin aprobar.
- **Actor:** Analista de fraude (Perfil A), el único usuario **humano** del MVP según la
  [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md). Las historias HU-07 a HU-14 tienen
  otro actor (sistema cliente) o ninguno claro: **es [P-32](../00-proyecto/preguntas-abiertas.md#p-32),
  sigue abierta**. Donde un caso de uso tiene como actor a "FraudLens" (CU-03, CU-04), la historia está
  escrita desde el analista que ve el resultado *(S: reformulación de Claude Code, sin aprobar)*.

## Resumen

| ID | Historia | Origen | MoSCoW | Estado |
|---|---|---|---|---|
| HU-01 | Ver la lista de transacciones | CU-05 | ⬜ | Borrador completo |
| HU-02 | Filtrar transacciones | CU-05 | ⬜ | Borrador completo |
| HU-03 | Ordenar transacciones por fecha y riesgo | CU-05 | ⬜ | Borrador completo |
| HU-04 | Distinguir los riesgos altos y bloqueos | CU-05 | ⬜ | Borrador completo |
| HU-05 | Ver transacciones nuevas sin recargar | CU-05 | ⬜ | Borrador completo |
| HU-06 | Consultar el detalle de una transacción | CU-06 | ⬜ | **Criterios incompletos** (ver abajo) |
| HU-07 | Enviar una transacción para analizarla | CU-01 | ⬜ | Borrador · actor: sistema cliente (P-32) |
| HU-08 | Rechazar solicitudes con datos faltantes | CU-01 | ⬜ | Borrador · actor: sistema cliente (P-32) |
| HU-09 | Evitar registros duplicados | CU-01 | ⬜ | Borrador · actor: sistema cliente (P-32) |
| HU-10 | Calcular el riesgo de una transacción | CU-03 | ⬜ | Borrador · incluye "historial insuficiente" y "análisis no disponible" |
| HU-11 | Ver los factores que explican el riesgo | CU-03 | ⬜ | Borrador · se solapa con HU-06 (ver nota) |
| HU-12 | Recibir una decisión según los umbrales | CU-04 | ⬜ | Borrador · choca con la 0005 (ver nota) |
| HU-13 | Aprobar por regla las transacciones de monto bajo | CU-02 | ⬜ | Borrador · configuración fija (0005) |
| HU-14 | Cargar la configuración inicial del sistema | CU-07 | ⬜ | Borrador · **actor sin definir** (P-32) |

> **¿Por qué 5 historias para CU-05?** El caso de uso es una sola pantalla con seis cosas distintas.
> Juntas serían una épica (INVEST: no Small); partidas por **SPIDR** (reglas / interfaz) cada una
> se puede construir y probar sola. *(S: es una propuesta; el equipo puede juntarlas.)*

---

## HU-01 — Ver la lista de transacciones

**Como** analista de fraude, **quiero** ver una lista de las transacciones analizadas con su riesgo y
decisión, **para** saber qué operaciones revisar sin abrirlas una por una.

**Criterios de aceptación**

- **Dado** que hay transacciones analizadas, **cuando** abro el dashboard, **entonces** veo una lista
  con: fecha y hora · identificador · usuario · monto y moneda · puntaje de riesgo · nivel de riesgo ·
  decisión · estado del análisis. *(R: CU-05)*
- **Dado** que no hay transacciones para mostrar, **cuando** abro el dashboard, **entonces** veo un
  estado vacío claro y no una tabla en blanco. *(R: CU-05)*
- **Dado** que una transacción tiene datos sensibles, **cuando** aparece en la lista, **entonces** no
  se muestran completos. *(R: requerimientos no funcionales §7)*

⬜ *Qué datos cuentan como "sensibles" no está definido en los requerimientos. Preguntar a ML.*

## HU-02 — Filtrar transacciones

**Como** analista de fraude, **quiero** filtrar la lista, **para** encontrar rápido las transacciones
que me interesan.

**Criterios de aceptación**

- **Dado** que estoy viendo la lista, **cuando** aplico un filtro por rango de fechas, nivel de riesgo,
  decisión, identificador de usuario o identificador de transacción, **entonces** la lista muestra solo
  las que cumplen. *(R: CU-05, "filtros mínimos")*
- **Dado** que apliqué un filtro, **cuando** ninguna transacción lo cumple, **entonces** veo el estado
  vacío claro. *(R: CU-05)*

⬜ *No está definido si se combinan varios filtros a la vez. Los requerimientos solo listan "filtros mínimos".*

## HU-03 — Ordenar transacciones por fecha y riesgo

**Como** analista de fraude, **quiero** ordenar la tabla por fecha y por riesgo, **para** empezar por
lo más reciente o lo más riesgoso.

**Criterios de aceptación**

- **Dado** que estoy viendo la lista, **cuando** elijo ordenar por fecha o por riesgo, **entonces** la
  tabla se reordena según ese campo. *(R: CU-05)*

⬜ *No está definido el orden por defecto ni si se puede ordenar por otras columnas.*

## HU-04 — Distinguir los riesgos altos y bloqueos

**Como** analista de fraude, **quiero** que los riesgos altos y los bloqueos se vean distintos del
resto, **para** detectarlos de un vistazo.

**Criterios de aceptación**

- **Dado** que la lista tiene transacciones de distinto nivel, **cuando** la miro, **entonces** las de
  riesgo alto y las bloqueadas se distinguen visualmente de las demás. *(R: CU-05)*
- **Dado** el nivel de riesgo, **cuando** se muestra, **entonces** usa la clasificación Bajo / Medio /
  Alto / Crítico. *(R: requerimientos §6, "clasificación visual sugerida", con rangos 0–39 · 40–59 ·
  60–84 · 85–100, que deben adaptarse a los umbrales configurados)*

⬜ *"Se distinguen visualmente" no dice cómo (color, ícono, etiqueta). Es decisión de diseño, con el
prototipo y el taller UX/UI del 21/10. Ojo accesibilidad: no depender solo del color (S).*

## HU-05 — Ver transacciones nuevas sin recargar

**Como** analista de fraude, **quiero** que las transacciones nuevas aparezcan solas, **para** no
perder operaciones mientras trabajo.

**Criterios de aceptación**

- **Dado** que estoy en el dashboard, **cuando** llega una transacción nueva, **entonces** aparece sin
  que yo recargue la página, o mediante una actualización periódica. *(R: CU-05)*

⬜ *Los requerimientos aceptan las dos opciones. No se define cada cuánto se actualiza. Decisión
técnica de FGR.*

## HU-06 — Consultar el detalle de una transacción

**Como** analista de fraude, **quiero** abrir el detalle de una transacción, **para** entender por qué
el sistema recomendó esa decisión y poder resolverla.

**Criterios de aceptación**

- **Dado** que veo una transacción en la lista, **cuando** abro su detalle, **entonces** veo: los datos
  recibidos · puntaje y nivel de riesgo · decisión recomendada · reglas aplicadas · factores que
  elevaron el riesgo · resumen del historial utilizado · fecha y hora del análisis · configuración de
  umbrales vigente al analizarla. *(R: CU-06)*
- **Dado** que el modelo no pudo analizar la transacción, **cuando** abro su detalle, **entonces** veo
  el estado explícito "análisis no disponible" y no una aprobación. *(R: requerimientos §7)*

> 🔴 **Criterios incompletos.** CU-06 **no trae criterios de aceptación propios** en los
> requerimientos: solo lista qué muestra el detalle. Los de arriba son esa lista reescrita en formato
> Dado/Cuando/Entonces. Faltan, **sin inventarlos**: ⬜ si el analista puede tomar una acción desde el
> detalle (aprobar o bloquear a mano) — los requerimientos no lo dicen — y ⬜ cuántos "factores" se
> muestran (CU-03 dice "hasta tres").

---

## Historias del motor de análisis (CU-01 a CU-04, CU-02 y CU-07 recortados)

## HU-07 — Enviar una transacción para analizarla

**Como** sistema cliente de la fintech o el banco, **quiero** enviar una transacción a FraudLens y
recibir una decisión, **para** saber si aprobarla, revisarla o bloquearla antes de procesarla.

**Criterios de aceptación**

- **Dado** que envío una transacción con los datos obligatorios, **cuando** FraudLens la procesa,
  **entonces** recibo una respuesta con: identificador · puntaje de riesgo · nivel de riesgo ·
  decisión · si la analizó el modelo · motivos. *(R: CU-01, "resultado esperado")*
- **Dado** cualquier transacción válida, **cuando** recibo la respuesta, **entonces** siempre trae una
  decisión. *(R: CU-01)*
- **Dado** que la transacción fue procesada, **cuando** el analista abre el dashboard, **entonces** la
  transacción aparece. *(R: CU-01)*
- **Dado** el resultado, **cuando** lo recibo, **entonces** el riesgo está entre 0 y 100. *(R: CU-01)*
- **Dado** que la solicitud se hace, **cuando** FraudLens responde, **entonces** lo hace en pocos
  segundos. *(R: requerimientos no funcionales §7)*

⬜ *"Pocos segundos" no tiene un número. Definirlo con FGR.* ⬜ *Los datos obligatorios exactos no
están definidos: la "entrada mínima" lista 10 campos y uno es "cuando esté disponible".*

## HU-08 — Rechazar solicitudes con datos faltantes

**Como** sistema cliente, **quiero** que me indiquen qué datos faltan cuando mi solicitud está
incompleta, **para** corregirla y reenviarla.

**Criterios de aceptación**

- **Dado** que envío una transacción sin algún dato obligatorio, **cuando** FraudLens la recibe,
  **entonces** la rechaza e indica cuáles datos faltan. *(R: CU-01)*
- **Dado** que la solicitud fue rechazada, **cuando** reviso el dashboard, **entonces** no aparece como
  transacción analizada. *(S: no está en los requerimientos; confirmar con ML)*

## HU-09 — Evitar registros duplicados

**Como** sistema cliente, **quiero** que reenviar una transacción no genere un segundo registro,
**para** no contaminar el historial por un reintento.

**Criterios de aceptación**

- **Dado** que ya se procesó una transacción, **cuando** envío otra con el mismo identificador,
  **entonces** no se crea un registro duplicado. *(R: CU-01)*

⬜ *No está definido qué se devuelve en ese caso (¿el resultado anterior? ¿un error?). "Transacción
duplicada" figura en los casos excepcionales (§8) sin detalle.*

## HU-10 — Calcular el riesgo de una transacción

**Como** analista de fraude, **quiero** que cada transacción tenga un puntaje de riesgo, **para** poder
priorizar cuáles revisar. *(S: CU-03 tiene como actor a FraudLens; acá se escribe desde quien usa el resultado)*

**Criterios de aceptación**

- **Dado** una transacción que debe analizarse, **cuando** el modelo la evalúa, **entonces** produce un
  puntaje entre 0 y 100. *(R: CU-03)*
- **Dado** un usuario con poco o ningún historial, **cuando** se evalúa su transacción, **entonces** el
  sistema igual funciona y el resultado indica **"historial insuficiente"**. *(R: CU-03)*
- **Dado** que el modelo falla o no está disponible, **cuando** se evalúa una transacción, **entonces**
  el resultado es un estado explícito de **"análisis no disponible"** y no una aprobación. *(R: §7)*

⬜ *El modelo concreto no está decidido ([Modelos de IA a utilizar](https://trello.com/c/HgigLF8C),
Jev). Esta historia no depende de cuál se elija, pero su construcción sí. Candidata a **épica** (S):
se puede partir por SPIDR — primero una regla simple, después el modelo.*

## HU-11 — Ver los factores que explican el riesgo

**Como** analista de fraude, **quiero** ver los factores principales que elevaron el riesgo, **para**
entender por qué el sistema recomendó esa decisión sin necesitar explicaciones avanzadas del modelo.

**Criterios de aceptación**

- **Dado** una transacción analizada, **cuando** veo su resultado, **entonces** aparecen hasta tres
  factores relevantes. *(R: CU-03)*

> **Solapamiento con HU-06:** el detalle (HU-06) ya incluye "factores que elevaron el riesgo". Una de
> las dos sobra o se fusionan. Decide el equipo con el User Story Mapping.

## HU-12 — Recibir una decisión según los umbrales

**Como** analista de fraude, **quiero** que cada transacción tenga una decisión (aprobar, revisar o
bloquear) según su riesgo, **para** saber qué hacer con ella. *(S: CU-04 tiene como actor a FraudLens)*

**Criterios de aceptación**

- **Dado** un riesgo menor al umbral de revisión, **cuando** se determina la decisión, **entonces** es
  aprobar. *(R: CU-04, ejemplo 60 %)*
- **Dado** un riesgo igual o mayor al umbral de revisión y menor al de bloqueo, **cuando** se determina
  la decisión, **entonces** es revisar. *(R: CU-04)*
- **Dado** un riesgo igual o mayor al umbral de bloqueo, **cuando** se determina la decisión,
  **entonces** es bloquear. *(R: CU-04, ejemplo 85 %)*
- **Dado** cualquier decisión, **cuando** la veo, **entonces** se muestra qué regla o umbral la
  produjo. *(R: CU-04)*
- **Dado** que el umbral de bloqueo debe ser mayor que el de revisión, **cuando** se cargan los
  umbrales, **entonces** una configuración inconsistente se rechaza. *(R: CU-04)*

> ⚠️ **Choque con la [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md):** CU-04 dice que
> "los umbrales deben poder modificarse" y que "un cambio de configuración se aplica solo a nuevas
> evaluaciones". La 0005 los dejó en **configuración fija** (seed). Se omitieron esos dos criterios y
> queda como pregunta. Los valores 60 % y 85 % son un **ejemplo** de los requerimientos, no una
> decisión.

## HU-13 — Aprobar por regla las transacciones de monto bajo

**Como** analista de fraude, **quiero** que las transacciones de monto bajo se aprueben por regla sin
pasar por el modelo, **para** concentrarme en las que importan. *(S: CU-02 tiene como actor a FraudLens)*

**Criterios de aceptación**

- **Dado** una transacción con monto inferior al mínimo de análisis, **cuando** se procesa, **entonces**
  se aprueba por regla. *(R: CU-02)*
- **Dado** que se aprobó por regla, **cuando** veo el resultado, **entonces** indica que el modelo no
  fue ejecutado y figura como "no evaluada por el modelo", no con un riesgo de 0 %. *(R: CU-02 y §4)*
- **Dado** que se aprobó por regla, **cuando** abro el dashboard, **entonces** la transacción se
  registra y se muestra igual. *(R: CU-02)*

⬜ *El monto mínimo del requerimiento es un ejemplo (ARS 10.000). Con la 0005 es **configuración fija**:
el criterio "el monto mínimo debe ser configurable" de CU-02 queda cubierto por HU-14.*

## HU-14 — Cargar la configuración inicial del sistema

**Como** ⬜ *(actor sin definir: ¿quien despliega el sistema?)*, **quiero** cargar al levantar el sistema
los valores de monto mínimo y umbrales, **para** que el análisis use una configuración conocida.

**Criterios de aceptación**

- **Dado** que se levanta el sistema, **cuando** carga su configuración inicial, **entonces** quedan
  definidos: si la regla de monto mínimo está activa · el monto mínimo · el umbral de revisión · el
  umbral de bloqueo. *(R: CU-07, "configuraciones mínimas"; D: 0005, configuración fija por seed)*
- **Dado** valores fuera de 0 a 100 o inconsistentes, **cuando** se cargan, **entonces** se rechazan.
  *(R: CU-07)*
- **Dado** el resultado de una transacción, **cuando** la analizo, **entonces** se conserva la
  configuración con la que se evaluó. *(R: CU-06 y §7: "configuración de umbrales vigente al
  analizarla")*

> Se omitieron de CU-07: "solo un administrador puede modificar" y "registrar quién cambió qué": la
> 0005 recortó el rol Administrador y la pantalla de configuración. **Esta historia entera depende de
> [P-32](../00-proyecto/preguntas-abiertas.md#p-32).**

---

## Preguntas que este borrador deja abiertas

| # | Pregunta | Para quién |
|---|---|---|
| 1 | ¿Qué datos de la transacción se consideran sensibles y no se muestran completos? (HU-01) | ML |
| 2 | ¿Se combinan filtros? ¿Cuál es el orden por defecto? (HU-02, HU-03) | ML · FM |
| 3 | ¿El analista puede actuar sobre una transacción desde el detalle? (HU-06) | ML |
| 4 | ¿Cada cuánto se actualiza la lista? (HU-05) | FGR |
| 5 | ¿Cómo se anota que los requerimientos de ML todavía dan por adentro la configuración de umbrales desde el dashboard, que la 0005 recortó? | Equipo ([`alcance-mvp-moscow.md`](alcance-mvp-moscow.md)) |
| 6 | ¿Qué actores escriben HU? HU-07 a HU-09 salen del sistema cliente y HU-14 no tiene actor | Equipo ([P-32](../00-proyecto/preguntas-abiertas.md#p-32)) |
| 7 | ¿Se fusionan HU-06 y HU-11 (ambas muestran los factores)? | Equipo · FM (User Story Mapping) |
| 8 | ¿Cuál es el número de "pocos segundos" de respuesta, y qué se devuelve ante un duplicado? (HU-07, HU-09) | FGR · ML |
| 9 | ¿Qué hacemos con los criterios de CU-04 y CU-07 que la 0005 dejó sin sentido (umbrales modificables, solo un administrador)? | Equipo |

## Qué falta para entregarlo el 14/10

- ⬜ **MoSCoW** de cada HU, decidido por el equipo.
- ⬜ **Herramienta** donde se registra el backlog ([P-30](../00-proyecto/preguntas-abiertas.md#p-30)).
- ⬜ Cruzar con el **User Story Mapping de FM**, para no duplicar ni contradecir.
- ⬜ Pasar las HU a la herramienta elegida, ordenadas: las prioritarias completas, las siguientes con
  título y Como/Quiero/Para, las últimas solo con título (regla de la Clase 10).
