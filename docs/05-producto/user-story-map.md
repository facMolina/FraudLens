# User Story Mapping — borrador del MVP

| | |
|---|---|
| **Estado** | 🟡 **Borrador — propuesta de FM, pendiente del equipo** |
| **Fecha** | 2026-10-14 |
| **Responsable** | Facundo Molina (FM) |
| **Ticket** | [Armar la propuesta de MVP con User Story Mapping](https://trello.com/c/mxSfKQw6) |
| **Método** | User Story Mapping, [Clase 10 (30/9)](../01-clases/clase-10-user-story-mapping-y-backlog.md): objetivo del usuario → User Journey → tareas → MVP y releases |
| **Cómo se armó** | FM respondió **6 preguntas, una por vez**. Claude Code ordenó las respuestas y las cruzó con lo que ya está escrito en el repo |

Fuentes: **(FM)** respuesta de FM del 2026-10-14 · **(R)** documento del repo, con link · **(S)** sugerencia de Claude Code, sin aprobar.

> ⚠️ **Todo lo que dice "FM" es una propuesta suya, no una decisión del equipo.** Nada de esto cierra [P-32](../00-proyecto/preguntas-abiertas.md#p-32) ni el MoSCoW.

## Paso 1 — El objetivo del usuario

- **Usuario del mapa:** el **Analista de fraude** (Perfil A). **Un solo mapa.** *(FM)* Es el único usuario humano del MVP según la [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md) *(R)*.
- **Objetivo:** **decidir qué hacer con cada caso.** *(FM)* Es coherente con los requerimientos, donde el Analista *"monitorea operaciones y revisa sus resultados"* ([§3](requerimientos-funcionales-mvp.md#3-actores)) *(R)*.
- **Aclaración de FM:** dentro de FraudLens el analista **solo ve la recomendación** (aprobar, revisar o bloquear) y **actúa por fuera**. *(FM)* Es coherente con la lista de fuera del alcance: el *"bloqueo real de dinero"* y la *"modificación manual de la decisión"* no entran ([§9](requerimientos-funcionales-mvp.md#9-fuera-del-alcance)) *(R)*. Con esto FM respondió, como propuesta, la pregunta 3 que MDV le dejó a ML en su [borrador del backlog](product-backlog-borrador.md).

## Paso 2 — El User Journey

Los 5 pasos del analista, **confirmados por FM**:

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| **Ver la cola** de transacciones | **Encontrar los casos que importan** | **Abrir un caso** | **Entender por qué** se marcó | **Leer la recomendación** y actuar por fuera |

## Pasos 3 y 4 — Tareas y línea del MVP

Las tareas salen de las historias del [borrador de MDV](product-backlog-borrador.md) *(R)*. **El orden vertical NO es prioridad**: la prioridad es el MoSCoW, que el equipo todavía no decidió.

| 1. Ver la cola | 2. Encontrar los casos | 3. Abrir un caso | 4. Entender por qué | 5. Leer la recomendación |
|---|---|---|---|---|
| Ver la lista de transacciones *(HU-01 · CU-05)* | Filtrar *(HU-02 · CU-05)* | Consultar el detalle de una transacción *(HU-06 · CU-06)* | Ver los factores que explican el riesgo *(HU-11 · CU-03)* | Ver la decisión según los umbrales *(HU-12 · CU-04)* |
| Ver transacciones nuevas sin recargar *(HU-05 · CU-05)* | Ordenar por fecha y riesgo *(HU-03 · CU-05)* | | | |
| | Distinguir riesgos altos y bloqueos *(HU-04 · CU-05)* | | | |

### Dónde va la línea punteada *(FM)*

| Release | Qué entra | ¿Se entrega? |
|---|---|---|
| **R1 — el MVP** | **Los 5 pasos completos: las 8 tareas de la tabla** | ✅ **Es lo que se entrega.** *"El MVP llega a la R1 no más"* (FM) |
| **R2** | Alertas y notificaciones · Explicabilidad avanzada · Configurar umbrales en vivo (panel de administración) · Reentrenamiento automático | ❌ **No entra en la entrega.** Se registra como lo que viene después |
| **R3 o más adelante** | El resto de lo que hoy está fuera del MVP: multi-tenant, integraciones con procesadores de pago reales, modelos avanzados, investigación completa de casos, gestión de reclamos y contracargos, modificación manual de la decisión, integraciones con listas externas de fraude, grafos de relaciones, bloqueo real de dinero y cobertura AML + fraude | ❌ No entra |

Los ítems de R2 y R3 son los **16 de la [lista unificada](alcance-mvp-moscow.md#2-lista-unificada-de-lo-que-queda-fuera-del-mvp)** *(R)*: los ítems 1, 2, 4, 5, 7 y 16 van a R2 y los otros 10 a R3.

## Lo que el mapa deja sin carril

Como el mapa es solo del Analista *(FM)*, **no tienen lugar en él** las historias de MDV que no son del analista:

| Historias | Qué son | Qué falta decidir |
|---|---|---|
| HU-07, HU-08, HU-09 | Enviar una transacción, rechazar solicitudes con datos faltantes, evitar duplicados *(actor: sistema cliente)* | Son **necesarias para que exista lo que el analista ve**, pero no son del analista |
| HU-10 | Calcular el riesgo | Ídem |
| HU-13, HU-14 | Aprobar por regla los montos bajos y cargar la configuración inicial | Ídem; HU-14 además **no tiene actor** |

⬜ **Cómo se llevan al backlog es [P-32](../00-proyecto/preguntas-abiertas.md#p-32)**, y sigue abierta: ¿historias técnicas de soporte, o historias de otro actor? No se decidió.

## Cautelas

1. **Todo el recorrido entra en R1.** La Clase 1 pide que el MVP sea chico (*"UberCab: una ciudad, una función"*) y acá no queda nada del recorrido del analista para un release posterior. No se cuestiona; queda a la vista para que el equipo lo mire.
2. **El objetivo dice "decidir" y FraudLens solo recomienda.** La decisión ocurre fuera del sistema. Si el equipo quiere que FraudLens registre el veredicto del analista, es otro caso (el prototipo de FGR tiene un endpoint de revisión humana, [según el relevamiento](prototipo.md#qué-muestra-el-repo--relevamiento-del-2026-10-07)). No se agregó.
3. **La HU-12 de MDV choca con la decisión 0005** (él mismo lo marcó). No se resolvió acá.
4. **MDV también marcó que HU-06 y HU-11 se solapan** (ambas muestran los factores). El mapa las deja en pasos distintos (3 y 4) porque así lo confirmó FM; fusionarlas queda para el equipo.

## Qué falta para dar el mapa por cerrado

- [ ] **El equipo valida el mapa** (hoy es propuesta de FM)
- [ ] **MoSCoW** de cada tarea ([tarjeta](https://trello.com/c/5dkWRPUy)), que además da el orden vertical
- [ ] **Responder P-32** de forma definitiva: qué pasa con las historias que no son del analista
- [ ] **Una versión visual** del mapa, si el equipo la quiere (hoy es una tabla)
- [ ] Ajustar el [borrador del backlog](product-backlog-borrador.md) a este mapa (qué historias quedan dentro y cuáles son soporte)

## Fuentes

[Clase 10](../01-clases/clase-10-user-story-mapping-y-backlog.md) · [`product-backlog-borrador.md`](product-backlog-borrador.md) · [`alcance-mvp-moscow.md`](alcance-mvp-moscow.md) · [`requerimientos-funcionales-mvp.md`](requerimientos-funcionales-mvp.md) · [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md) · [`user-research.md`](user-research.md)
