# 6 Sombreros — ¿Qué entra al MVP y dónde va la línea R1 / R2 / R3?

| | |
|---|---|
| **Decisión** | Qué entra al MVP, según el [User Story Mapping](../user-story-map.md): usuario del mapa, recorrido y línea de releases |
| **Fecha** | 2026-10-15 |
| **Participantes** | FM (propuesta). ⬜ Faltan MDV, FGR y ML |
| **Tarjeta de Trello** | [Armar la propuesta de MVP con User Story Mapping](https://trello.com/c/mxSfKQw6) |
| **Estado** | 🟡 **En análisis — borrador.** El sombrero rojo y la decisión final son del equipo |

> Es una decisión de alcance, así que lleva análisis (lo pide la tarjeta). Blanco, negro, amarillo y verde son **borrador de Claude Code, a corregir por el equipo**. El blanco usa **solo hechos que ya están en el repo**. El rojo está **vacío a propósito**: lo escribe el equipo, no la IA.

## El problema, en una frase

¿Aceptamos el mapa propuesto por FM —**un solo mapa del Analista, 5 pasos, las 9 tareas en R1 y nada del recorrido para R2**— o lo cambiamos?

---

## ⚪ Sombrero Blanco — Analista racional

### Lo que sabemos

| Hecho | Fuente |
|---|---|
| FM propuso: **un solo mapa, desde el Analista de fraude**; recorrido de **5 pasos**; **R1 = los 5 pasos completos (9 tareas)**; R2 = alertas, explicabilidad avanzada, umbrales en vivo y reentrenamiento automático; el resto, R3 o más adelante | [`user-story-map.md`](../user-story-map.md), respuestas de FM del 2026-10-14 |
| FM aclaró que **la entrega llega solo hasta R1** | FM, 2026-10-14 |
| El mapa cubre **9 de las 14 historias** del borrador de MDV. **Quedan sin carril** HU-07, HU-08, HU-09, HU-10 y HU-14 | [`product-backlog-borrador.md`](../product-backlog-borrador.md), [`user-story-map.md`](../user-story-map.md) |
| La decisión 0005 dejó **un solo tipo de usuario (Analista)** y un *"núcleo demostrable"* de CU-01, CU-03, CU-04, CU-05 y CU-06, más CU-02 y CU-07 simplificados a configuración fija | [Decisión 0005](../../03-decisiones/0005-recorte-alcance-mvp.md) |
| La Clase 10 dice que **"no hay un único usuario"** y que perder historias es un error frecuente | [Clase 10](../../01-clases/clase-10-user-story-mapping-y-backlog.md) |
| La Clase 1 pide un MVP chico (*"UberCab: una ciudad, una función"*) | [`user-story-map.md`](../user-story-map.md#cautelas), cita de la Clase 1 |
| **Ninguna tarea tiene MoSCoW**: lo decide el equipo. Los 16 ítems que ya están fuera del MVP corresponderían a *Won't* por la definición de la Clase 10, **sin confirmar** | [`alcance-mvp-moscow.md`](../alcance-mvp-moscow.md) |
| MDV marcó que **HU-12 choca con la 0005** y que **HU-06 y HU-11 se solapan** | [`product-backlog-borrador.md`](../product-backlog-borrador.md) |
| El relevamiento del prototipo de FGR (de segunda mano, sin ejecutar) dice que implementa CU-02 y CU-07 como funciones vivas, tres roles por API key y un registro de revisión humana | [`prototipo.md`](../prototipo.md) |
| El Product Backlog se entrega **sin estimar** | FM, [P-31](../../00-proyecto/preguntas-abiertas.md#p-31) |

### Lo que NO sabemos

- ⬜ **Cuánto trabajo lleva construir las 9 tareas** (no se estimó) ni si entra en el tiempo disponible. Es lo que puede responder FGR.
- ⬜ Si el docente considera que 9 tareas es un MVP chico.
- ⬜ Cómo se llevan al backlog las 5 historias sin carril ([P-32](../../00-proyecto/preguntas-abiertas.md#p-32)).
- ⬜ El MoSCoW de cada tarea.
- ⬜ Qué opinan MDV, FGR y ML (ML es el referente de producto según `equipo.md`).

---

## 🔴 Sombrero Rojo — Mente emocional

> Emociones, miedos e intuiciones. **Sin justificar.** Lo escribe el equipo, no la IA.

- ⬜ **MDV:**
- ⬜ **FGR:**
- ⬜ **ML:**
- ⬜ **FM:**

---

## ⚫ Sombrero Negro — Crítico estratégico *(borrador de Claude Code)*

| Riesgo | Cómo se ve el fracaso |
|---|---|
| **Todo el recorrido entra en R1** | No queda margen: si algo se atrasa, no hay una tarea que se pueda mover a un release posterior sin romper el recorrido. Es el error clásico de irse de alcance |
| **Se pierden historias sin carril** | HU-07 a HU-10 y HU-14 hacen falta para que exista lo que el analista ve, pero no están en el mapa. Si nadie las lleva al backlog, el MVP se arma sin ellas |
| **El objetivo dice "decidir" y el sistema solo recomienda** | El mapa promete algo que la herramienta no hace dentro de FraudLens |
| **Solapes y choques sin resolver** | HU-06 y HU-11 muestran lo mismo; HU-12 choca con la 0005. El mapa los deja como están |
| **Prioridad sin MoSCoW** | El orden vertical del mapa no es prioridad; sin MoSCoW no se sabe qué sacar primero si hay que recortar |

---

## 🟡 Sombrero Amarillo — Optimista estratégico *(borrador de Claude Code)*

- **Un solo mapa, claro**, con un usuario y un objetivo que coinciden con lo que dice el repo (el Analista *"monitorea operaciones y revisa sus resultados"*).
- **El recorrido coincide con el núcleo de la 0005**: CU-05, CU-06, CU-03, CU-04 y CU-02.
- **Cada tarea tiene su historia y su caso de uso**, así que se puede rastrear de punta a punta.
- **Lo que queda afuera está registrado** (R2 y R3), no descartado, y sale de la lista unificada de 16 ítems.
- Ya hay **5 User Flow** armados sobre este mismo recorrido.

---

## 🟢 Sombrero Verde — Pensamiento creativo *(borrador de Claude Code)*

1. **Partir R1 en dos tramos** (por ejemplo, ver y filtrar la cola primero; detalle y recomendación después), sin cambiar el mapa.
2. **Sumar un segundo mapa corto** para el sistema cliente (HU-07 a HU-10), sin tocar el del analista.
3. **Tratar HU-07 a HU-10 y HU-14 como historias técnicas de soporte**, dentro del mismo backlog.
4. **Fusionar HU-06 y HU-11** para achicar el recorrido de 5 a 4 pasos.
5. **Hacer el MoSCoW antes de cerrar R1**, y dejar que el MoSCoW decida el orden vertical.
6. **Llevar el mapa a una versión visual** (por ejemplo, FigJam) para revisarlo en la clase.

---

## 🔵 Sombrero Azul — Director estratégico

### Puntos clave de cada sombrero

| Sombrero | Lo que aportó |
|---|---|
| ⚪ Blanco | La propuesta de FM cubre 9 de 14 historias; la 0005 respalda el usuario y el núcleo; no hay MoSCoW ni estimación |
| 🔴 Rojo | ⬜ Pendiente: las 4 voces |
| ⚫ Negro | Todo en R1, historias sin carril, "decidir" vs "recomendar", solapes sin resolver |
| 🟡 Amarillo | Un mapa claro, alineado con la 0005, con lo que queda afuera registrado |
| 🟢 Verde | Partir R1, un segundo mapa, historias de soporte, fusionar HU-06 y HU-11, MoSCoW primero |

### Contradicciones a resolver

- **"MVP chico" (Clase 1) contra "todo el recorrido en R1"** (propuesta de FM). Falta ver si el equipo lo acepta o parte R1.
- **El mapa es solo del Analista** y la Clase 10 advierte que perder historias es un error frecuente: P-32 sigue abierta.

### Decisión

> ⬜ **Del equipo.**
> **Propuesta de FM (2026-10-14):** el mapa de la [`user-story-map.md`](../user-story-map.md), con las 9 tareas en R1.

### Qué la sostiene

- La decisión 0005 y los requerimientos de ML coinciden con el usuario, el objetivo y el núcleo.
- Los 5 User Flow ya están armados sobre este recorrido.

### Qué la haría cambiar

- Que FGR diga que las 9 tareas no entran en el tiempo disponible.
- Que el docente pida un MVP más chico.
- Que el equipo decida sumar otro actor al mapa (P-32).

---

## Verificación final

- [ ] El problema se analizó desde múltiples perspectivas reales *(falta el rojo del equipo)*
- [ ] El resultado **no** refleja un único sesgo emocional o racional
- [ ] La decisión del azul integra y equilibra todas las visiones anteriores
- [x] El blanco **no inventó** ningún dato
