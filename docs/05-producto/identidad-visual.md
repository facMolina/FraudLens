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
| **Color de marca** | 🟣 **Violeta** — `#9333EA` claro / `#A855F7` oscuro | FM |
| **Formato del logo** | **Sólo isotipo** generado por IA; el nombre se monta con tipografía real | FM |
| **Escritura del nombre** | **FraudLens** — una palabra, L mayúscula intercalada | FM |
| **Idioma de la UI** | **Inglés** | FM |
| **Tipografía** | **Google Fonts** — licencia libre, sin costo | FM |
| **Quién aprueba** | **El equipo + el docente** | FM |
| **Colores vetados** | Ninguno *(más allá de la restricción de la escala de riesgo)* | FM |
| **Tagline** | ⬜ **Sin definir** — ver abajo | — |

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
| 1 | Primera generación (27 isotipos, 2 paletas, 2 mockups, tipografía) | ✅ [Análisis](identidad/analisis-generacion-01.md) |
| 2 | Paleta verificada con contraste WCAG | ✅ [`identidad/paleta.md`](identidad/paleta.md) |
| 3 | Color de marca elegido | ✅ Violeta |
| 4 | Shortlist de 3 isotipos | ✅ Embudo · Grilla con anomalía · Prisma |
| 5 | Variaciones de los 3 isotipos en violeta | 🔲 Prompt 5 |
| 6 | Mockups regenerados en violeta (claro y oscuro) | 🔲 Prompts 6 y 7 |
| 7 | Tipografía real elegida y verificada | 🔲 |
| 8 | Board de presentación | 🔲 |
| 9 | Elección del equipo + docente | 🔲 |

**Prompts para generar 1 a 4:** [`prompts-nano-banana.md`](prompts-nano-banana.md)

---

## Nota: UI en inglés, entrega en español

El **producto** va en inglés; el **documento final y el pitch** son en español, porque son de la
materia. Es una combinación normal en B2B fintech, pero conviene tenerla presente:

- Los **mockups** llevan textos en inglés (`Transactions`, `Risk`, `Decision`, `Approve`, `Review`, `Block`)
- La **documentación del proyecto** sigue toda en español
- En el pitch conviene **explicar la decisión** en una línea, para que no parezca un descuido

## Tagline: pendiente

FM todavía no lo definió. **No hace falta para generar las imágenes** — el isotipo se genera sin
texto igual.

Tres direcciones posibles para cuando se decida, según qué se quiera subrayar:

| Si se quiere subrayar… | Dirección |
|---|---|
| Que **complementa**, no reemplaza | Algo del orden de *"tu antifraude, con más foco"* |
| La **precisión** del filtro | Algo del orden de *"menos falsos positivos, más fraude detectado"* |
| La **decisión asistida** | Algo del orden de *"aprobar, revisar o bloquear, con fundamento"* |

⚠️ **No son propuestas cerradas**: son territorios. El tagline conviene escribirlo **después** del
User Research, cuando sepamos qué le duele de verdad al usuario. Un tagline inventado antes del
research es exactamente lo que la Clase 4 advierte.

## Preguntas abiertas de este trabajo

Todas resueltas salvo el **tagline**, que se pospone al User Research.
