# 2026-09-15 — Decisión: 3 datasets, cada uno con un rol distinto

| | |
|---|---|
| **Tipo** | Decisión de producto (con asistencia de Claude Code) |
| **Duración** | — |
| **Participantes** | Francisco Guerrero (FGR) |

## Por qué esta sesión

FGR tomó la tarjeta [**"Documentar el dataset de casos de prueba"**](https://trello.com/c/4oV9jmrT).
El punto de partida era [P-11](../docs/00-proyecto/preguntas-abiertas.md#p-11): elegir **uno** de los
3 notebooks de Kaggle pre-seleccionados. Al investigar qué dataset hay detrás de cada notebook, quedó
claro que los 3 candidatos no son intercambiables — uno es real y anonimizado, otro sintético y sin
anonimizar, el tercero sintético con train/test ya separados por el autor.

## La decisión

**FGR decidió no elegir uno solo: usar los 3, cada uno con un rol fijo en el pipeline del modelo.**
Registrada como [decisión 0006](../docs/03-decisiones/0006-tres-datasets-para-el-modelo.md):

1. **Entrenamiento** — [Credit Card Fraud Detection Dataset 2023](https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023): ~500.000 registros reales, anonimizados excepto monto, id y clasificación.
2. **Validación y explicabilidad** — [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/miadul/credit-card-fraud-detection-dataset): sintético, sin anonimizar — permite explicar qué atributos combinados sugieren fraude.
3. **Test final** — [Credit Card Transactions Fraud Detection Dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection): datos no vistos en los otros dos, para verificar que el modelo generaliza.

## Qué hizo Claude Code

Investigación web para confirmar las características de cada dataset (registros, columnas,
etiqueta, licencia), marcando explícitamente qué quedó **confirmado con fuente** y qué es
**descripción de FGR sin verificación independiente** (regla del repo: no completar a ojo). El
dataset 3 quedó bien documentado gracias a un paper académico que lo cita (*Fraud Dataset
Benchmark*, Grover et al.); el dataset 2 (`miadul`) quedó con registros/licencia sin confirmar
porque Kaggle bloqueó el scraping con un reCAPTCHA y no hay navegador automatizado disponible en
esta sesión (el usuario declinó instalar la extensión de Chrome).

Detalle completo en [`docs/05-producto/datos.md`](../docs/05-producto/datos.md).

## Qué quedó pendiente

- Confirmar registros exactos y licencia del dataset 1 (2023), y registros/columnas/licencia del
  dataset 2 (miadul) — abriendo cada página de Kaggle logueado.
- Mapear columna por columna qué requerimiento del MVP cubre cada uno de los 3 datasets.
- Confirmar si el dataset 2 permite construir historial por usuario (el 1 no tiene identificador de
  usuario real, por estar anonimizado).
- **6 Sombreros formal** de esta decisión, después del 1° Parcial (16/9) — se registró de forma
  liviana por el mismo criterio que la [decisión 0005](../docs/03-decisiones/0005-recorte-alcance-mvp.md).
- Cerrar el ticket de Trello (comentario de resolución + mover a Hecho) cuando FGR lo confirme.

## Nota de método

FGR pidió explícitamente decidir él mismo cuáles datasets usar y el motivo de cada uno. El asistente
se limitó a investigar y dejar la información verificada, sin proponer ni adelantar la decisión.

## Archivos

- [`docs/05-producto/datos.md`](../docs/05-producto/datos.md) — reestructurado
- [`docs/03-decisiones/0006-tres-datasets-para-el-modelo.md`](../docs/03-decisiones/0006-tres-datasets-para-el-modelo.md) — nuevo
- [`docs/00-proyecto/preguntas-abiertas.md`](../docs/00-proyecto/preguntas-abiertas.md) — P-11 resuelta
- [`docs/00-proyecto/declaracion-uso-ia.md`](../docs/00-proyecto/declaracion-uso-ia.md) — nueva fila de uso de IA
