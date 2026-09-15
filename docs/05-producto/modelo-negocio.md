# Modelo de negocio — Business Model Canvas

| | |
|---|---|
| **Estado** | 🟡 **Hipótesis del equipo — no validado con research** |
| **Fecha** | 2026-09-15 |
| **Método** | Business Model Canvas (Osterwalder) — mencionado en Clase 6 |
| **Depende de** | [P-07](../00-proyecto/preguntas-abiertas.md#p-07) (usuario objetivo) y [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md) (enfoque fintech/bancos) |

> ⚠️ **Nada de esto está validado.** No hicimos entrevistas de modelo de negocio, no hablamos con
> ningún cliente potencial sobre precio ni sobre canales. Es un punto de partida construido con lo
> que **ya está confirmado** en el proyecto (perfiles, propuesta de valor, benchmarking) más
> supuestos razonables marcados como tales — no se inventa como si fuera un hallazgo.

## Los 9 bloques

### 1. Segmentos de clientes

- **Cliente que paga (Perfil B):** fintechs, billeteras virtuales, pasarelas de pago y bancos
  tradicionales — confirmado en la [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md).
- **Usuario directo (Perfil A):** el analista de fraude dentro de esa empresa.
- **Afectado indirecto (Perfil C):** el usuario final de esa fintech/banco — no paga, pero su
  experiencia (rechazo indebido, fraude sufrido) es la métrica de éxito del producto.

### 2. Propuesta de valor

*(Fuente: [`problema.md` — Narrativa](problema.md#narrativa-de-la-propuesta-de-solución) y
[`benchmarking.md`](benchmarking.md))*

- Un filtro de fraude que **complementa** el sistema antifraude que la fintech/banco ya tiene, sin
  reemplazarlo — el único espacio que el benchmarking encontró sin cubrir por los 6 competidores
  relevados.
- Explicabilidad por transacción, pensada para un analista **sin equipo de ciencia de datos
  propio** — no una explicabilidad genérica (esa ya es estándar de industria, según el propio
  benchmarking).
- Ayuda a la fintech/banco a sostener su programa de gestión de riesgo de fraude exigido por el
  BCRA (Comunicaciones "A" 8471 y 8473).

### 3. Canales — ⬜ hipótesis, sin confirmar

- Venta directa B2B, vía los contactos del rubro que ya tiene ML.
- Presencia en eventos o comunidades fintech de Argentina.
- ⬜ No sabemos si esto es realista para una empresa recién empezando — no hay research de canales.

### 4. Relación con clientes — ⬜ hipótesis, sin confirmar

- Onboarding asistido (integrar FraudLens a un sistema existente no es trivial).
- Soporte técnico continuo, dado que es un complemento y no un reemplazo — la integración tiene que
  ser confiable para que la fintech no dude en sumarlo.

### 5. Fuentes de ingreso — ⬜ hipótesis, sin confirmar

- Modelo de **suscripción o licencia** (SaaS), **no** de garantía financiera (ese es el modelo de
  ClearSale/Signifyd/Riskified, explícitamente descartado — ver
  [`benchmarking.md`](benchmarking.md#la-curva-de-valor), fila "Modelo de garantía").
- Posiblemente escalonado por volumen de transacciones analizadas — es la práctica común del rubro
  según lo relevado (capas de señal desde USD 99-500/mes, plataformas de puntuación USD 2K-10K/mes),
  pero **no tenemos ninguna validación de que un cliente pagaría esto**.

### 6. Recursos clave

- El modelo de IA/ML entrenado (hoy: bloqueado por [P-11](../00-proyecto/preguntas-abiertas.md#p-11), qué dataset se usa).
- El equipo y su conocimiento del dominio (el acceso de ML al rubro es, según el propio
  [análisis de 6 sombreros](analisis/6-sombreros-usuario-objetivo.md), el activo más escaso del proyecto).
- La marca e identidad visual, ya cerradas.

### 7. Actividades clave

- Desarrollo y mejora continua del modelo de detección.
- Soporte e integración con los sistemas existentes de cada cliente.
- Mantenerse alineados a la normativa BCRA (que además es un argumento de venta, no sólo un costo).

### 8. Socios clave — ⬜ hipótesis, sin confirmar

- Fintechs o bancos piloto, dispuestos a probar la integración antes de un lanzamiento comercial.
- ⬜ No identificamos todavía ningún socio real — depende de conseguir acceso al Perfil B (mismo
  pendiente señalado en la [decisión 0004](../03-decisiones/0004-enfoque-cliente-fintech-bancos.md)).

### 9. Estructura de costos

- Desarrollo y mantenimiento del software.
- Infraestructura (cómputo para entrenar y correr el modelo).
- Equipo (los 4 integrantes, en la etapa académica; sin costo laboral real todavía).
- Cumplimiento regulatorio, si se sigue de cerca la normativa BCRA que aplica al rubro del cliente.

## Cómo crece con el tiempo *(sostenibilidad)*

⬜ **Hipótesis, sin validar.** Un camino posible: empezar con 1-2 clientes piloto (vía los contactos
de ML), cobrar por volumen de transacciones analizadas, y usar la explicabilidad como diferencial
para escalar a clientes más grandes (bancos tradicionales) una vez probado con fintechs chicas.
No hay evidencia todavía de que este camino sea el correcto — es el tipo de pregunta que el
research con el Perfil B tiene que responder.

## Qué falta para que esto deje de ser hipótesis

- ⬜ Conseguir la primera entrevista real con el Perfil B (bloqueante, ver decisión 0004).
- ⬜ Preguntar directamente por precio, canal y disposición a pagar en esa entrevista — ya está en
  la [guía de entrevista del Perfil B](user-research.md#entrevista--perfil-b-responsable-de-riesgoproducto-en-fintech-o-banco).
- ⬜ Revisar este documento entero después de esa entrevista — probablemente cambie más de un bloque.
