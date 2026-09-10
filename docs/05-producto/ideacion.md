# Ideación y Grilla de Priorización

| | |
|---|---|
| **Estado** | 🟡 **Borrador — ideación pre-research, ninguna idea está validada** |
| **Fecha** | 2026-09-10 |
| **Ticket** | [10. Ideación y Grilla de Priorización](https://trello.com/c/3ULARKgX) |
| **Entregable de** | Clase 6 remota (5/9) — vencido |
| **Método** | [Las 4 acciones (ERRC)](../01-clases/clase-06-oceano-azul.md#-las-cuatro-acciones-la-herramienta-central), Kim y Mauborgne |

## ⚠️ Sobre qué se está ideando

La propia tarjeta lo señala: la ideación normalmente parte de un **Problem Statement cerrado**, y el
nuestro sigue abierto (ticket 6, depende de [P-07](../00-proyecto/preguntas-abiertas.md#p-07)). Se
ideó igual, sobre lo que ya está documentado — el
[borrador ERRC de la Clase 6](../01-clases/clase-06-oceano-azul.md#32-las-cuatro-acciones-aplicadas-a-fraudlens--borrador-para-discutir),
los [requerimientos de ML](requerimientos-funcionales-mvp.md) y el
[benchmarking](benchmarking.md) — para no perder el tiempo esperando. **Si el Problem Statement
cambia con el research, esto se revisa.**

## 🔴 Hueco del material, y cómo se llenó

El deck **nombra** la Grilla de Priorización pero no explica cómo se arma (ejes, criterios). En
ausencia de esa definición, se usó una técnica estándar de priorización — **Impacto × Esfuerzo** —
que **no viene del material del docente**, es una elección del equipo para no quedar frenados.
Queda como [P-24](../00-proyecto/preguntas-abiertas.md#p-24): preguntarle al docente si tiene un
formato específico en mente. Si la respuesta cambia el criterio, esta grilla se rehace.

## Sesión de ideación

Sin filtrar en esta etapa (sombrero verde: generar, no criticar). Cada idea nace de algo ya
documentado, no de nada inventado — el link a la fuente va al lado de cada una.

### ✕ Eliminar

| Idea | De dónde sale |
|---|---|
| La configuración manual de reglas y umbrales que hoy le come tiempo al analista | [Borrador ERRC](../01-clases/clase-06-oceano-azul.md#32-las-cuatro-acciones-aplicadas-a-fraudlens--borrador-para-discutir) |

> ⚠️ **Tensión con lo ya escrito:** los [requerimientos de ML](requerimientos-funcionales-mvp.md#cu-07--configurar-reglas-y-umbrales)
> (CU-07) incluyen la configuración de umbrales como parte del MVP, con un actor **administrador**
> dedicado a eso. "Eliminar" la configuración manual entra en conflicto directo con ese documento.
> No se resuelve acá — queda anotado para la revisión en equipo de los requerimientos (ticket
> "Revisar en equipo los requerimientos funcionales del MVP").

### ⊖ Reducir

| Idea | De dónde sale |
|---|---|
| El volumen de casos que llegan a revisión humana | [Borrador ERRC](../01-clases/clase-06-oceano-azul.md#32-las-cuatro-acciones-aplicadas-a-fraudlens--borrador-para-discutir) |
| Los falsos positivos (rechazar una compra legítima) | Mismo borrador + [Perfil C en `usuarios.md`](usuarios.md#perfil-c--consumidor-con-fraude-o-rechazo-indebido) — es el costo invisible que el equipo ya identificó |

### ⊕ Incrementar

| Idea | De dónde sale |
|---|---|
| La explicabilidad de cada decisión — por qué este caso es riesgoso | [Borrador ERRC](../01-clases/clase-06-oceano-azul.md#32-las-cuatro-acciones-aplicadas-a-fraudlens--borrador-para-discutir) |

> 🔴 **El benchmarking ya corrigió el alcance de esta idea** (ver
> [`benchmarking.md`](benchmarking.md#-lo-que-esta-curva-corrige-de-nuestra-propia-hipótesis)): la
> explicabilidad genérica ya es tendencia de toda la industria en 2026, no un diferencial. Para que
> siga siendo una idea con espacio blanco, tiene que estar **dirigida específicamente a un analista
> sin equipo de ciencia de datos propio**, no a una explicabilidad "para cualquiera".

### ◆ Crear

| Idea | De dónde sale |
|---|---|
| Un dashboard que no sólo puntúa sino que **cuenta la historia** de la transacción | [Borrador ERRC](../01-clases/clase-06-oceano-azul.md#32-las-cuatro-acciones-aplicadas-a-fraudlens--borrador-para-discutir) + [Clase 05, Storytelling con Datos](../01-clases/clase-05-oratoria-y-storytelling.md#34--storytelling-con-datos-es-literalmente-el-pliego-del-dashboard) |
| Un producto que se integra **al lado** del sistema antifraude existente, sin reemplazarlo | El único espacio sin cubrir en el [benchmarking](benchmarking.md#el-espacio-que-sí-queda-sin-cubrir-en-lo-relevado) — ninguno de los 6 competidores relevados se posiciona así. Coincide con la hipótesis de [P-07](../00-proyecto/preguntas-abiertas.md#p-07), sin confirmar todavía |

## La grilla de priorización (Impacto × Esfuerzo)

**Eje X — Esfuerzo** de construirlo para el MVP académico. **Eje Y — Impacto** percibido para quien
decide, paga o sufre el fraude (no impacto técnico).

Los cuadrantes son la lectura estándar de esta técnica: **Alto impacto / Bajo esfuerzo** = hacer
primero; **Alto impacto / Alto esfuerzo** = planificarlo; **Bajo impacto / Bajo esfuerzo** = si
sobra tiempo; **Bajo impacto / Alto esfuerzo** = descartar.

| Idea | Impacto | Esfuerzo | Cuadrante |
|---|---|---|---|
| Reducir falsos positivos | Alto | Alto | Planificarlo — es central al valor pero requiere ajustar el modelo, no sólo la interfaz |
| Explicabilidad dirigida al analista sin equipo de datos | Alto *(si se confirma con research)* | Medio | Hacer primero, condicionado a validar con el Perfil A |
| Dashboard que cuenta la historia de la transacción | Medio-Alto | Medio | Hacer primero — ya está en el alcance del MVP (CU-06, detalle de transacción) como base |
| Complementar en vez de reemplazar el sistema existente | Alto *(hipótesis)* | Bajo *(es una decisión de posicionamiento, no de desarrollo)* | Hacer primero — barato de decidir, alto impacto potencial en el diferencial |
| Reducir volumen de casos a revisión humana | Medio | Alto | Planificarlo — depende de la calidad del modelo, no es trivial |
| Eliminar configuración manual de reglas | ❓ *(en conflicto con CU-07)* | Medio | **No priorizar todavía** — resolver primero la tensión con los requerimientos |

> ⚠️ Las columnas "Impacto" son **estimaciones del equipo**, no medidas. Las marcadas *(hipótesis)*
> o *(si se confirma)* dependen directamente del research de los perfiles A y B — están para
> ordenar la conversación, no para cerrarla.

## Qué queda pendiente

- ⬜ Confirmar con el docente el formato esperado de la Grilla de Priorización ([P-24](../00-proyecto/preguntas-abiertas.md#p-24))
- ⬜ Resolver la tensión entre "Eliminar configuración manual" y el CU-07 de los requerimientos
- ⬜ Revalidar impacto y esfuerzo una vez haya datos del Perfil A y B
- ⬜ El equipo tiene que revisar esta ideación — es tan borrador como el ERRC del que parte
