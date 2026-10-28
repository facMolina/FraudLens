# Registro del MVP y verificación del deploy — 2026-10-28

**Responsable del registro:** MDV. **Autor del commit consultado:** ML.

## Qué se hizo

Se registró en el centro de cómputos el repositorio separado del MVP y se distinguió de forma explícita del prototipo de FGR. La fuente fijada identifica un scaffold técnico: no acredita todavía flujos de fraude funcionales. Se documentaron el stack que declara el README, sus instrucciones de arranque (sin ejecutarlas) y los límites de la evidencia.

En una comprobación pública de solo lectura:

- `GET https://fraudlens-two.vercel.app/` respondió HTTP 200; título `FraudLens`, con el texto “MVP / PUNTO DE PARTIDA”, “La base está lista.” y “Versión inicial · 0.1”.
- `GET https://fraudlens-two.vercel.app/api/health` respondió HTTP 200 con `{"status":"ok","service":"fraudlens"}`.

Esto verifica disponibilidad HTTP básica, no conexión de servicios, funcionalidad de producto ni que el deploy corresponda al commit consultado. No se usaron credenciales de la aplicación, no se modificaron sus datos, no se levantó el MVP localmente y no se cambió el repositorio remoto. La actualización documental de Trello se hizo por separado con la conexión OAuth de MDV.

## Trello y pendientes

La tarjeta [`ec7Xd3xy`](https://trello.com/c/ec7Xd3xy#comment-6ae25085d167a230e2af985a) quedó con descripción actualizada y comentario de seguimiento verificados por el coordinador. Sigue en Backlog, abierta, sin marcar completa, sin fecha de vencimiento ni miembros asignados. El acceso del equipo, la decisión sobre stack y la relación/reutilización con el prototipo siguen pendientes.

Al terminar el registro, la documentación era local y los enlaces de publicación permanecían sin marcar. No se cerró el ticket. Después, MDV pidió «okey actualiza el origen», autorizando guardar y publicar este registro en `origin/main`; antes de publicar, `git fetch origin` confirmó que no había nuevos commits remotos.

## Verificación documental

- Se revisaron los siete archivos del cambio y se alinearon los comandos de arranque con el README fijado al commit consultado. No se ejecutó ese arranque local.
- El chequeo estructural pasó: cambios de preguntas limitados a P-05 (P-10 intacta), evidencia y comandos presentes, 11 aportes de MDV, una sola entrada de Pi en herramientas, bloques de código cerrados y destinos de enlaces locales existentes.
- `git diff --check` pasó; Git avisa que normalizará LF a CRLF en el historial de aportes.
- No aplica RED/GREEN de comportamiento porque solo se modificó documentación.
- La evaluación nativa no pudo evaluar el conjunto por los archivos nuevos sin seguimiento, que requieren declaración explícita de alcance. No se inició revisión nativa ni se afirma su aprobación.

## Archivos de registro

- [`mvp.md`](../docs/05-producto/mvp.md)
- [P-05](../docs/00-proyecto/preguntas-abiertas.md#p-05)
