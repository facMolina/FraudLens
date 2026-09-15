# 0005 — Recorte de alcance del MVP y aclaración de roles

| | |
|---|---|
| **Fecha** | 2026-09-14 |
| **Estado** | ✅ **Registrada de forma liviana** — 6 Sombreros formal pendiente para después del 1° Parcial (16/9), por tiempo |
| **Decidido por** | El equipo (FM, en la revisión de requerimientos) |
| **Ticket** | [Revisar en equipo los requerimientos funcionales del MVP](https://trello.com/c/eSWWYc7Z) |
| **Documento afectado** | [`requerimientos-funcionales-mvp.md`](../05-producto/requerimientos-funcionales-mvp.md) — "Puntos a discutir en equipo" |

## Contexto

El documento de requerimientos de ML tenía 6 puntos abiertos para revisión en equipo (ver el propio
documento). El 1° Parcial es el 16/9 — quedan 2 días — así que esta decisión se registra de forma
liviana en vez de con el análisis completo de 6 Sombreros que pide la
[decisión 0003](0003-metodo-seis-sombreros.md) para decisiones de alcance. El 6 Sombreros formal
queda pendiente para después del parcial.

## Decisión

**El actor "Administrador" del documento de requerimientos es el Perfil B** (responsable de
riesgo/producto en la fintech o banco): decide integrar FraudLens a nivel comercial, no revisa
casos uno por uno. **El actor "Analista de fraude" es el Perfil A**: usa el dashboard día a día
para revisar la cola de transacciones.

**CU-02 (regla de monto mínimo) y CU-07 (configurar reglas y umbrales) se recortan** de una función
viva y editable por un Administrador con su propio login, a una **configuración fija que se carga
al levantar el sistema** (seed inicial), sin pantalla de administración dedicada en el MVP.

**El Analista (Perfil A) hace las dos cosas**: revisa casos uno por uno (CU-05/CU-06) y ve los
reportes o señales agregadas que da el sistema. No hay una vista ni un login separado para el
Administrador en el MVP — su rol queda acotado a la configuración fija inicial. Por eso **no hace
falta autenticación con roles diferenciados** para el MVP: un solo tipo de usuario (Analista)
accede a todo el dashboard.

## Por qué

- **El MVP tiene que simular el sistema final, no serlo.** Mientras no se resuelvan las cuestiones
  de negocio pendientes (P-07, acceso al Perfil B, dataset), construir una pantalla de
  administración completa sería construir sobre supuestos que todavía pueden cambiar. Una
  configuración fija demuestra el mismo comportamiento (umbrales aplicados, decisión resultante) sin
  ese costo.
- Reduce el alcance de 7 casos de uso "vivos" a un núcleo demostrable (CU-01, CU-03, CU-04, CU-05,
  CU-06) más una configuración inicial fija (CU-02, CU-07 simplificados), más alineado con el
  criterio de MVP de la Clase 1 (UberCab: una ciudad, una función).
- **El punto 4 (métricas de evaluación del modelo) se marca bloqueante**, no se avanza en él hasta
  resolver [P-11](../00-proyecto/preguntas-abiertas.md#p-11) (qué dataset se usa) — elegir una
  métrica sin saber el dataset sería una decisión sin base.

## Consecuencias

- `requerimientos-funcionales-mvp.md` queda anotado con el estado de cada punto de revisión, sin
  reescribir el documento original de ML (sigue siendo su borrador, con las anotaciones de revisión
  claramente separadas).
- Falta: hacer el 6 Sombreros formal de este recorte de alcance después del 16/9.
- El MVP, mientras tanto, se documenta explícitamente como una **simulación** del sistema final —
  no como el sistema de producción de una fintech real.
