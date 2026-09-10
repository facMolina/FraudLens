# Benchmarking con curva de valor

| | |
|---|---|
| **Estado** | 🟢 Primera vuelta hecha — **es continuo, se repite** |
| **Fecha** | 2026-09-10 |
| **Ticket** | [9. Benchmarking con curva de valor](https://trello.com/c/OCO21r8W) |
| **Entregable de** | Clase 6 remota (5/9) |
| **Método** | [Curva de valor / Océano Azul](../01-clases/clase-06-oceano-azul.md), Kim y Mauborgne |

> ⚠️ **Fuentes:** todo lo que sigue viene de búsqueda web hecha hoy (2026-09-10), citada al pie de
> cada afirmación. Donde la fuente no daba un dato preciso, queda marcado **❓ sin verificar** — no
> se completa a ojo.
>
> El benchmarking **es continuo**, según la propia clase — esta es la primera vuelta, no la única.

## Competidores relevados

| Empresa | Categoría | Enfoque | Fuente |
|---|---|---|---|
| **Sift** | Plataforma de puntuación (post-autorización) | Mercados digitales / marketplaces. $2K–10K/mes en mercado medio | [cside.com](https://cside.com/blog/best-fraud-detection-software) |
| **Feedzai** | Plataforma empresarial | Fraude **y** AML para bancos — un solo proveedor para las dos cosas | [cside.com](https://cside.com/blog/best-fraud-detection-software) |
| **Forter** | Plataforma de puntuación | Invierte el enfoque usual: optimiza **aprobar buenos clientes** en vez de bloquear más fraude | [cside.com](https://cside.com/blog/best-fraud-detection-software) |
| **Signifyd** | Modelo de garantía | #1 en protección de e-commerce según Digital Commerce 360 (5 años seguidos); garantía financiera 100% contra chargebacks de fraude | [cside.com](https://cside.com/blog/best-fraud-detection-software) |
| **Riskified** | Modelo de garantía | Grandes minoristas online enfocados en crecimiento; fraude sin intervención manual | [cside.com](https://cside.com/blog/best-fraud-detection-software) |
| **ClearSale** | Modelo de garantía, foco LatAm | Presencia activa en Argentina y LatAm; integración directa con **Tiendanube**; garantía de contracargo pensada para **PyMEs de e-commerce** | [es.clear.sale](https://es.clear.sale/proteccion-contra-el-fraude/como-funciona), [dplnews.com](https://dplnews.com/clearsale-expertise-y-productos-antifraude-mexico-2025/) |

**Modelos de precio, por categoría** (no por empresa individual, la fuente no discrimina tanto):
capas de señal desde $99–500/mes, plataformas de puntuación $2K–10K/mes, plataformas empresariales
desde $50K/año, modelos de garantía a 0.6–1.5% del GMV protegido.
[Fuente](https://cside.com/blog/best-fraud-detection-software)

## La curva de valor

**Eje X** — los factores en que compiten. **Eje Y** — nivel de oferta (Bajo · Medio · Alto).

| Factor | Sift | Feedzai | Forter | Signifyd | Riskified | ClearSale | **FraudLens (hipótesis)** |
|---|---|---|---|---|---|---|---|
| Precio / accesible para comercio chico | Medio | Bajo | ❓ | ❓ | Bajo | **Alto** | Alto |
| Foco específico en LatAm/Argentina | Bajo | Bajo | Bajo | Bajo | Bajo | **Alto** | Alto |
| Modelo de garantía (asume la pérdida) | Bajo | Bajo | Bajo | **Alto** | **Alto** | **Alto** | Bajo *(no es el modelo elegido)* |
| Cobertura AML + fraude en un solo producto | Bajo | **Alto** | Bajo | Bajo | Bajo | Bajo | Bajo *(fuera de alcance del MVP)* |
| Complementa un sistema antifraude existente, no lo reemplaza | ❓ | Bajo *(reemplaza)* | ❓ | Bajo *(reemplaza)* | Bajo *(reemplaza)* | Bajo *(reemplaza)* | **Alto** *(hipótesis P-07)* |
| Explicabilidad por transacción, dirigida al analista | ❓ | ❓ | Medio *(prioriza no rechazar clientes buenos, no está dicho que explique por qué)* | ❓ | ❓ | ❓ | Alto *(hipótesis, ver más abajo)* |

Las celdas ❓ no significan "cero" — significan que la búsqueda no trajo evidencia suficiente para
puntuar. Antes de usar esta tabla como definitiva, conviene revisar el sitio de cada competidor
directamente.

## 🔴 Lo que esta curva corrige de nuestra propia hipótesis

El [borrador de las 4 acciones](../01-clases/clase-06-oceano-azul.md#32-las-cuatro-acciones-aplicadas-a-fraudlens--borrador-para-discutir)
proponía la explicabilidad y el foco en comercio chico como posible espacio blanco. El benchmarking
**no lo confirma tal cual** — hay que ajustarlo:

1. **La explicabilidad ya es tendencia de toda la industria en 2026, no un hueco.** La regulación
   está empujando a que la IA de fraude sea auditable ("glass-box", no caja negra), con técnicas
   como SHAP para explicar cada transacción — esto aparece descrito como dirección general del
   mercado, no como diferencial de un competidor puntual.
   [Fuente](https://www.fluxforce.ai/blog/fraud-detection-benchmarks-2026-response)

   Consecuencia: si la identidad de marca y el dashboard prometen "explicabilidad" sin más, no es
   un océano azul — es alcanzar el estándar de la industria. Para que siga siendo diferencial,
   tiene que estar **dirigida a un analista sin equipo de ciencia de datos propio**, en una fintech
   chica — no a un banco con área de compliance.

2. **"Comercio chico + LatAm" ya lo cubre ClearSale**, con un modelo de garantía financiera y
   presencia confirmada en Argentina, integrado directo a Tiendanube — que es exactamente el canal
   de e-commerce chico que imaginábamos alcanzar. No es un hueco vacío: hay un jugador establecido.

### El espacio que sí queda sin cubrir en lo relevado

**Nadie de los 6 relevados se posiciona como complemento de un sistema antifraude que el cliente ya
tiene.** Los seis compiten para ser *el* sistema (o directamente asumen el riesgo, modelo de
garantía). Ninguna fuente describe una oferta que diga *"metete al lado de lo que ya tenés, sumá un
filtro más y un panel de revisión, sin reemplazar nada"*.

Eso coincide con la hipótesis de [P-07](../00-proyecto/preguntas-abiertas.md#p-07) (FraudLens como
complemento, no reemplazo, para un equipo de fraude de fintech) — pero el research con el perfil A
(analista) tiene que confirmar si ese dolor ("necesito un filtro extra, no otro sistema entero") es
real o es una hipótesis cómoda para el prototipo que ya existe. Mismo sesgo que ya nombró el
[sombrero rojo](analisis/6-sombreros-usuario-objetivo.md#-sombrero-rojo--mente-emocional).

## Qué falta para la próxima vuelta

- ⬜ Verificar directamente en los sitios de cada competidor las celdas marcadas ❓
- ⬜ Sumar 1-2 competidores más chicos / específicos de Argentina (más allá de ClearSale)
- ⬜ Repetir esta curva **después** de tener el research del perfil A — la fila de "complemento vs.
  reemplazo" es la más importante y hoy es una hipótesis, no un hallazgo
