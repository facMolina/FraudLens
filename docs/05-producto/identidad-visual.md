# Identidad visual de FraudLens

| | |
|---|---|
| **Responsable** | Facundo Molina (FM) |
| **Tarjeta** | https://trello.com/c/ncNYKzbF |
| **Estado** | 🔨 En curso — brief cerrado, falta generar y elegir |
| **Última actualización** | 2026-09-02 |

---

## ⚠️ Sobre qué se apoya este brief

La identidad depende de **para quién es el producto**, y eso todavía **no está decidido en equipo**
([P-07](../00-proyecto/preguntas-abiertas.md#p-07)).

Lo que sigue se apoya en una **hipótesis de trabajo aportada por FM**, no en una decisión del equipo
ni en User Research:

> FraudLens es un producto **B2B para empresas fintech** que manejan tráfico de transacciones y
> necesitan **integrar nuestro sistema como complemento** de su sistema antifraude existente,
> aportando un filtro más específico y eficaz gracias a la IA, más un **dashboard de revisión** para
> que su equipo tome decisiones.

**Si el User Research contradice esta hipótesis, la identidad se revisa.** Queda escrito para que la
dependencia sea explícita y no una sorpresa en octubre.

### Qué implica esta hipótesis para el diseño

| Implicancia | Consecuencia de diseño |
|---|---|
| **Es B2B, no consumidor final** | La marca le habla a un equipo técnico y a quien firma el contrato. No necesita ser simpática, necesita ser **creíble** |
| **Se integra a un sistema existente** | Convive visualmente con el producto del cliente. Conviene una identidad **sobria**, que no pelee |
| **El uso diario es un dashboard** | La identidad se juega sobre todo en **UI**, no en packaging ni marketing |
| **Quien lo mira son analistas, muchas horas** | Fatiga visual y densidad de datos son criterios reales, no detalles |

---

## Decisiones tomadas

| Decisión | Valor | Quién |
|---|---|---|
| **Tono** | **Agilidad fintech moderna** | FM |
| **Referencias** | Stripe / Nubank · Datadog / Grafana · Linear / Vercel | FM |
| **Concepto de logo** | Generar varias direcciones y comparar sobre imagen | FM |
| **Modo** | **Claro y oscuro**, los dos | FM |
| **Color de marca** | Generar opciones en varias familias y comparar | FM |
| **Formato del logo** | **Sólo isotipo** generado por IA; el nombre se monta con tipografía real | FM |

### El territorio que definen las referencias

Las tres referencias elegidas se cruzan en un lugar bastante preciso:

- **Stripe / Nubank** → mucho aire, gradientes sutiles, tipografía impecable, se siente caro
- **Datadog / Grafana** → denso en datos, oscuro, funcional antes que decorativo
- **Linear / Vercel** → minimalismo geométrico, blanco y negro con un acento

> **El cruce:** *fintech premium con alma de herramienta técnica.* Sobrio, geométrico, con un solo
> color de acento fuerte y muchísimo gris bien usado. **Nada de ilustración, nada de degradés
> ruidosos, nada de íconos redonditos.**

---

## El problema técnico central: marca vs. escala de riesgo

Es la restricción más dura de este trabajo y conviene tenerla presente todo el tiempo.

El dashboard clasifica transacciones en **bajo · medio · alto · crítico**, y esa escala usa
naturalmente verde → amarillo → naranja → rojo. Entonces:

| Si el color de marca es… | Problema |
|---|---|
| 🔴 Rojo | Se lee como "crítico". La marca grita peligro todo el tiempo |
| 🟢 Verde | Se lee como "aprobado". La marca se confunde con un estado |
| 🟡 Naranja / amarillo | Se lee como "alto riesgo" |

**Conclusión:** el color de marca tiene que vivir **fuera de la escala de riesgo** — azul, cian,
violeta o teal. Por eso los prompts generan opciones en esas familias.

### Y además: accesibilidad

La escala de riesgo **no puede depender sólo del color**. Cerca del 8% de los varones tiene alguna
forma de daltonismo, y el rojo-verde es justamente el eje más afectado.

**Regla:** todo estado de riesgo se comunica con **color + forma o texto**. Un ícono distinto, una
etiqueta, un patrón. Si alguien ve el dashboard en escala de grises, tiene que seguir entendiéndolo.

---

## Tipografía: requisitos

| Requisito | Por qué |
|---|---|
| **Números tabulares** (`tabular-nums`) | El dashboard muestra montos, puntajes e IDs en columna. Sin esto, los números bailan y la tabla se lee mal |
| **0 y O bien diferenciados** · **1, l e I distinguibles** | Se leen IDs de transacción. Confundir un carácter es un error real de trabajo |
| Buena legibilidad en tamaños chicos | Las tablas densas usan 12-14px |
| Licencia libre | Es un trabajo académico y el código puede quedar público |

---

## Entregables

| # | Entregable | Estado |
|---|---|---|
| 1 | Propuestas de isotipo (3 direcciones) | 🔲 |
| 2 | Paletas de color, claro y oscuro | 🔲 |
| 3 | Mockup del dashboard con la identidad aplicada | 🔲 |
| 4 | Lámina de tipografía | 🔲 |
| 5 | Elección del equipo | 🔲 |
| 6 | Board de presentación en Canva | 🔲 |

**Prompts para generar 1 a 4:** [`prompts-nano-banana.md`](prompts-nano-banana.md)

---

## Preguntas abiertas de este trabajo

| # | Pregunta |
|---|---|
| 1 | ¿El nombre se escribe **FraudLens** (con L mayúscula intercalada), **Fraudlens** o **fraudlens**? |
| 2 | ¿Lleva **tagline**? Si sí, ¿cuál? |
| 3 | ¿La UI del producto está en **español o inglés**? |
| 4 | ¿Tipografías de **Google Fonts** está bien? *(licencia libre, sin costo)* |
| 5 | ¿Quién **aprueba** la identidad? ¿La presentás y decide el equipo, o decidís vos? |
| 6 | ¿Hay algún color **vetado** por alguien del equipo? |
