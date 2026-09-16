# 0006 — Usar 3 datasets distintos, cada uno con un rol en el pipeline del modelo

| | |
|---|---|
| **Fecha** | 2026-09-15 |
| **Estado** | ✅ **Registrada de forma liviana** — 6 Sombreros formal pendiente para después del 1° Parcial (16/9), por tiempo. Mismo criterio que la [decisión 0005](0005-recorte-alcance-mvp.md). |
| **Decidido por** | Francisco Guerrero (FGR) |
| **Ticket** | [Documentar el dataset de casos de prueba](https://trello.com/c/4oV9jmrT) |
| **Pregunta relacionada** | [P-11](../00-proyecto/preguntas-abiertas.md#p-11) |
| **Documento afectado** | [`datos.md`](../05-producto/datos.md) |

## Contexto

El equipo tenía 3 notebooks de Kaggle pre-seleccionados y la tarea pendiente era elegir **uno** para
el MVP ([P-11](../00-proyecto/preguntas-abiertas.md#p-11)). Al investigar qué dataset usa cada
notebook, quedó claro que los 3 candidatos no son intercambiables: uno es real y anonimizado, otro
es sintético y sin anonimizar, y el tercero es sintético con reparto train/test ya hecho por el
autor. Elegir uno solo hubiera significado resignar alguna de esas tres propiedades.

## Alternativas consideradas

| Opción | A favor | En contra |
|---|---|---|
| Elegir 1 solo dataset (plan original) | Más simple de documentar y de justificar en el pitch | Ningún candidato cubre entrenamiento + explicabilidad + test hold-out al mismo tiempo |
| Usar los 3, cada uno con un rol distinto | Cubre entrenar con datos reales, explicar el modelo con datos sin anonimizar, y testear con datos nunca vistos | Más trabajo de integración (unificar columnas/formatos entre 3 fuentes distintas) y más superficie para citar correctamente |

## Decisión

Se usan **3 datasets de Kaggle**, cada uno con un rol fijo:

1. **Entrenamiento** — [Credit Card Fraud Detection Dataset 2023](https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023): ~500.000 registros reales, anonimizados excepto monto, id y clasificación. Aporta datos reales etiquetados sin exponer información sensible.
2. **Validación y explicabilidad** — [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/miadul/credit-card-fraud-detection-dataset): datos sintéticos, sin anonimizar. Al no estar anonimizado permite explicar qué atributos o combinación de factores llevan a sugerir fraude — algo que el dataset 1 (con columnas PCA anonimizadas) no permite.
3. **Test final** — [Credit Card Transactions Fraud Detection Dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection): datos que no participan del entrenamiento ni de la validación, para confirmar que el modelo generaliza a casos nunca vistos.

## Por qué

- El objetivo del MVP no es sólo entrenar un modelo que clasifique bien sobre su propio dataset —
  también hay que poder **explicar** una decisión (dashboard de revisión para el analista de
  fraude) y demostrar que el modelo **generaliza**. Un solo dataset no cubre las tres necesidades.
- Separar explícitamente los datos de test de los de entrenamiento/validación es una buena práctica
  metodológica más allá de este proyecto — evita el riesgo de sobreajuste al medir el modelo con
  datos que ya vio.

## Consecuencias

- [`datos.md`](../05-producto/datos.md) queda reestructurado: ya no es "elegir 1 de 3 candidatos"
  sino "3 datasets, cada uno con su rol", con lo verificado y lo pendiente marcado explícitamente.
- **Queda pendiente, antes de citar los 3 en el documento final**: confirmar registros exactos y
  licencia del dataset 1, y registros/columnas/licencia del dataset 2 (miadul) — Kaggle bloqueó el
  scraping con un reCAPTCHA a mitad de la investigación y no hay navegador automatizado disponible
  en esta sesión.
- Falta mapear columna por columna qué requerimiento del MVP cubre cada dataset, y confirmar si el
  dataset 2 permite construir historial por usuario (el 1 no tiene identificador de usuario real por
  estar anonimizado).
- **6 Sombreros formal pendiente** para después del 16/9, igual que la decisión 0005.
