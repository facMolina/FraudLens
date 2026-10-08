# 2026-10-08 — Borrador de alcance del MVP y MoSCoW

| | |
|---|---|
| **Tipo** | Documentación de producto, con asistencia de Claude Code |
| **Duración** | — |
| **Participantes** | Facundo Molina (FM) |

## Qué se hizo

- FM tomó la tarjeta [Unificar las listas de "fuera del MVP" y armar el MoSCoW](https://trello.com/c/5dkWRPUy) (queda a su nombre y pasa a 🔨 En curso).
- Se armó [`alcance-mvp-moscow.md`](../docs/05-producto/alcance-mvp-moscow.md): **compilación** de lo que ya estaba escrito, **sin decidir nada**.
  - Una lista única de **16 ítems** que quedan fuera del MVP, con la fuente de cada uno (las dos listas del repo, la decisión 0005 y las líneas futuras).
  - Los recortes de la 0005 (CU-02 y CU-07 pasan a configuración fija, sin roles diferenciados).
  - Los 7 casos de uso con su estado según el repo y la columna MoSCoW **vacía**: la decide el equipo.
- Se corrigió en [`docs/05-producto/README.md`](../docs/05-producto/README.md) una atribución mal puesta: los requerimientos funcionales son un **borrador de ML**, no de FGR.

## Qué se definió

Nada. Lo que el borrador deja a la vista:

- **Los 16 ítems ya están declarados fuera del MVP por el equipo**, así que por la definición de la Clase 10 corresponden a *Won't*. **Falta que el equipo lo confirme como MoSCoW.**
- **Tres ítems están redactados distinto** en las dos listas (reentrenamiento, reentrenamiento por acciones del analista y alertas/notificaciones): no se dio por hecho que son iguales.
- **Jev sigue sin ubicar** (ni adentro ni afuera).
- Los requerimientos de ML **todavía dan por adentro** la configuración de umbrales desde el dashboard, que la 0005 recortó.
- El MVP promete *"un modelo entrenado con datos históricos"* y **el prototipo de FGR no tiene uno** (según el relevamiento, de segunda mano, sin ejecutar).

## Qué quedó pendiente

| Tarea | Responsable | Para cuándo |
|---|---|---|
| Confirmar los 3 ítems redactados distinto | Equipo | ⬜ |
| Decidir si los ítems 15 (AML + fraude) y 16 (roles diferenciados) se suman a la lista única | Equipo | ⬜ |
| Clasificar con MoSCoW cada ítem y cada CU, con 6 Sombreros ([tarjeta](https://trello.com/c/vxWQiPIz)) y el sombrero rojo de las 4 voces | Equipo | ⬜ |
| Ubicar a Jev (pregunta hecha a MDV en su tarjeta) | MDV | ⬜ |
| Decidir cómo se anota la contradicción con los requerimientos de ML | Equipo | ⬜ |

## Dudas que surgieron

- ¿Los ítems 1, 2 y 4 son lo mismo en las dos listas?
- ¿Se suman los ítems 15 y 16 a la lista única?

## Archivos tocados

- Nuevo: `docs/05-producto/alcance-mvp-moscow.md`
- Modificados: `docs/05-producto/README.md` · `registro/historial-aportes.md`
- **Trello:** tarjeta #44 a nombre de FM, en En curso, con un comentario que enlaza el borrador.
