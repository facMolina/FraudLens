# 6 Sombreros — ¿Con qué herramienta registramos el Product Backlog?

| | |
|---|---|
| **Decisión** | Dónde y con qué herramienta se registra el Product Backlog |
| **Fecha** | 2026-10-14 |
| **Participantes** | FM (propuesta). ⬜ Faltan MDV, FGR y ML |
| **Tarjeta de Trello** | [Decidir la herramienta donde se registra el Product Backlog](https://trello.com/c/kceMBbCj) |
| **Estado** | 🟡 **En análisis — borrador.** El sombrero rojo y la decisión final son del equipo |

> Análisis **liviano**, como pide la tarjeta. Blanco, negro, amarillo y verde son **borrador de Claude Code, a corregir por el equipo**. El rojo está **vacío a propósito**: lo escribe el equipo, no la IA.

## El problema, en una frase

¿Registramos el Product Backlog en **Trello** (en la misma lista Backlog, con una etiqueta HU), en un **archivo del repo**, o en **Miro/FigJam + Trello**?

---

## ⚪ Sombrero Blanco — Analista racional

### Lo que sabemos

| Hecho | Fuente |
|---|---|
| La Clase 10 pide *"decidir cuál va a ser la herramienta donde el equipo registrará su Backlog"* | [Clase 10](../../01-clases/clase-10-user-story-mapping-y-backlog.md) |
| El mismo deck muestra Miro, FigJam y Lucidspark como herramientas útiles | Clase 10 |
| La Clase 09 nombra a Trello como la herramienta para plasmar lo que se desarrolla en el sprint | [Clase 09](../../01-clases/clase-09-agile-scrum-kanban.md) |
| Los tableros de trabajo son ítem de evaluación de la materia | [`convencion-de-tickets.md`](../../04-metodologia/convencion-de-tickets.md) |
| El borrador del backlog de MDV (14 historias con criterios Dado/Cuando/Entonces) **ya existe como archivo del repo** | [`product-backlog-borrador.md`](../product-backlog-borrador.md) |
| El Product Backlog del 14/10 se entrega **sin estimar** | FM, [P-31](../../00-proyecto/preguntas-abiertas.md#p-31) |
| El tablero tenía 48 tarjetas el 2026-10-14: 15 en Backlog, 3 en Esta semana, 4 en En curso, 3 en En revisión, 23 en Hecho | Lectura de Trello del 2026-10-14 |
| El tablero tenía 6 etiquetas, solo 3 con nombre (Prioridad Alta, Prioridad Media, Diseño). **Ninguna se llama HU.** Las otras 3 (verde, violeta y amarilla) están sin nombre y sin uso | Lectura de Trello del 2026-10-15 |
| El conector de Trello **no puede crear etiquetas**: solo crea tableros y pone o saca etiquetas que ya existen. La etiqueta HU **se crea a mano** (por ejemplo, renombrando una de las 3 sin nombre) | Revisión de las herramientas del conector, 2026-10-15 |
| La convención de tickets propone **7 etiquetas de categoría** y exige **una por tarjeta**; ninguna es "HU". Esa convención **no está aprobada** | [`convencion-de-tickets.md`](../../04-metodologia/convencion-de-tickets.md), [P-22](../../00-proyecto/preguntas-abiertas.md#p-22) |
| Según el docente, el backlog es dinámico y las historias de mayor prioridad van más refinadas | Clase 10 |

### Lo que NO sabemos

- ⬜ Si el docente evalúa el backlog **en Trello o en otro formato**. No se le preguntó.
- ⬜ Cuántas historias van a quedar después de cruzar el borrador de MDV con el [mapa](../user-story-map.md).
- ⬜ Qué opinan MDV, FGR y ML.

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
| **Se mezclan historias con tickets de trabajo** en la misma lista | Las 14 historias se suman a los 15 tickets que ya hay en Backlog (unas 29 tarjetas). El orden de arriba hacia abajo, que en un backlog significa prioridad, queda compartido entre cosas de naturaleza distinta |
| **Etiqueta nueva fuera de la convención** | La etiqueta HU no está entre las 7 categorías propuestas, y esa convención todavía no está aprobada |
| **Dos fuentes de verdad** | El borrador en el repo y las tarjetas de Trello se desactualizan entre sí |
| **Criterios largos dentro de tarjetas** | Cada historia lleva Como/Quiero/Para y varios Dado/Cuando/Entonces: se leen peor en la descripción de una tarjeta que en un archivo |
| **La etiqueta no se puede crear desde el conector** *(verificado el 2026-10-15)* | Hay que hacerla a mano antes de cargar las historias; si se olvida, las tarjetas quedan sin etiqueta |

---

## 🟡 Sombrero Amarillo — Optimista estratégico *(borrador de Claude Code)*

- **Todo queda en el tablero que el docente evalúa**, sin abrir una segunda herramienta.
- **El equipo ya usa Trello** y la Clase 09 lo nombra para el sprint.
- **El orden de la lista funciona como prioridad**, que es lo que pide el docente (las más prioritarias arriba).
- Pasar del borrador en el repo a tarjetas es **mecánico**: ya están escritas con su fuente.

---

## 🟢 Sombrero Verde — Pensamiento creativo *(borrador de Claude Code)*

1. Filtrar el tablero por la etiqueta HU para ver **solo historias** y ocultar los tickets de trabajo.
2. Titular cada tarjeta **"HU-NN — …"** para ordenarlas y citarlas desde el repo.
3. Usar un **checklist** de la tarjeta para los criterios de aceptación.
4. Dejar el archivo del repo como **espejo** de lo que hay en Trello.
5. *(Alternativa que FM descartó)* Una lista **"Product Backlog"** aparte en el mismo tablero, para no compartir el orden con los tickets.

---

## 🔵 Sombrero Azul — Director estratégico

### Puntos clave de cada sombrero

| Sombrero | Lo que aportó |
|---|---|
| ⚪ Blanco | La cátedra nombra Trello para el sprint y evalúa el tablero; el borrador ya existe en el repo; no hay etiqueta HU (y el conector no puede crearla) ni convención aprobada |
| 🔴 Rojo | ⬜ Pendiente: las 4 voces |
| ⚫ Negro | Mezcla con los tickets, etiqueta fuera de convención y dos fuentes de verdad |
| 🟡 Amarillo | Un solo tablero evaluable, orden de la lista como prioridad |
| 🟢 Verde | Filtro por etiqueta, títulos "HU-NN", checklist, archivo como espejo |

### Contradicciones a resolver

- FM eligió la **misma lista Backlog con etiqueta**, sabiendo que las historias **comparten el orden de prioridad** con los tickets de trabajo (fue la advertencia que se le hizo). Falta ver si el equipo acepta ese costo.

### Decisión

> ⬜ **Del equipo.**
> **Propuesta de FM (2026-10-14):** registrar el Product Backlog en **Trello, en la misma lista Backlog, con una etiqueta HU**.

### Qué la sostiene

- La Clase 09 nombra Trello para el sprint y el tablero es ítem de evaluación.
- Un solo lugar para el docente y para el equipo.

### Qué la haría cambiar

- Que el docente pida otro formato para el backlog.
- Que la mezcla con los tickets haga confuso priorizar.
- Que el equipo prefiera una lista separada. (La etiqueta HU hay que crearla a mano: el conector no puede.)

---

## Verificación final

- [ ] El problema se analizó desde múltiples perspectivas reales *(falta el rojo del equipo)*
- [ ] El resultado **no** refleja un único sesgo emocional o racional
- [ ] La decisión del azul integra y equilibra todas las visiones anteriores
- [x] El blanco **no inventó** ningún dato
