# Datos y dataset del modelo

> **Estado:** ✅ **Decidido por FGR (2026-09-15)** — no se elige un único dataset: se usan **3**,
> cada uno con un rol distinto en el pipeline del modelo. Ver [decisión 0006](../03-decisiones/0006-tres-datasets-para-el-modelo.md).
> Referencia: [P-11](../00-proyecto/preguntas-abiertas.md#p-11) — ✅ resuelta.

## Los 3 datasets y su rol

| Rol | Dataset | Por qué este rol |
|---|---|---|
| **1. Entrenamiento** | [Credit Card Fraud Detection Dataset 2023](https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023) (`nelgiriyewithana`) | Datos **reales anonimizados** pero **etiquetados** — permite entrenar el modelo contra casos reales sin exponer datos sensibles |
| **2. Validación y explicabilidad** | [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/miadul/credit-card-fraud-detection-dataset) (`miadul`) | Datos **sintéticos** (no reales) y **sin anonimizar** — permite explicar qué atributos o combinación de factores llevan a sugerir fraude, algo que un dataset anonimizado (PCA) no permite |
| **3. Test final** | [Credit Card Transactions Fraud Detection Dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection) (`kartik2112`) | Datos que **no participaron** del entrenamiento ni de la validación — hold-out final para confirmar que el modelo generaliza |

> 🤖 **Fuente de esta sección:** la elección de los 3 datasets y sus roles **los decidió FGR**
> (2026-09-15) — no fue una sugerencia del asistente. Claude Code investigó y dejó marcado qué de
> las características de cada dataset está **confirmado con fuente** y qué es una **descripción de
> FGR sin verificación independiente**, siguiendo la regla del repo de no completar a ojo.

## Detalle de cada dataset

| Ítem | 1 — 2023 (entrenamiento) | 2 — miadul (validación) | 3 — kartik2112 (test final) |
|---|---|---|---|
| Cantidad de registros | **500.000** *(cifra de FGR — coincide con "+550.000" que reportan fuentes de terceros; no hay página oficial abierta para el número exacto)* | ⬜ **sin confirmar** — no encontramos el número de filas ni en la página del dataset ni en fuentes secundarias | **~1,3M transacciones** (1.000 clientes × 800 comercios a lo largo de 6 meses), con **train y test ya separados** por el propio autor — [fuente: paper *Fraud Dataset Benchmark*, Grover et al.](https://arxiv.org/abs/2208.14417) |
| Columnas / features | `id`, `V1`...`V28` (PCA, anonimizadas), `Amount`, `Class` — **anonimizado excepto monto, id y clasificación**, tal como lo describió FGR ✅ consistente con lo público del dataset | Sin anonimizar (según FGR) — columnas puntuales ⬜ sin confirmar | **23 features**: fecha/hora, número de tarjeta, comercio, categoría, monto, nombre, domicilio, género, entre otras — [fuente: mismo paper] |
| ¿Trae etiqueta de fraude? | Sí — columna `Class` | Sí (según FGR) | Sí |
| ¿Real o sintético? | Real, anonimizado | **Sintético** (según FGR) | Sintético — generado con la herramienta **Sparkov** |
| Licencia de uso | ⬜ sin confirmar | ⬜ sin confirmar | **CC0** (dominio público) — [fuente: mismo paper] |

⚠️ **Lo que queda pendiente de verificación** (no bloquea seguir, pero hay que cerrarlo antes de citar
estos datasets en el documento final, por honestidad académica):
- Registros exactos y licencia del dataset 1 (2023).
- Registros, columnas exactas y licencia del dataset 2 (miadul).
- Se resuelve en un minuto abriendo cada página de Kaggle logueado — Claude Code no pudo esta vez
  porque Kaggle empezó a devolver un reCAPTCHA a mitad de la investigación anterior y no hay
  navegador automatizado disponible en esta sesión.

## Qué tiene que confirmar cada uno antes de usarse

1. **¿Tiene las columnas que necesita nuestro MVP?**
   El [documento de requerimientos](requerimientos-funcionales-mvp.md) pide: identificador de
   transacción, identificador de usuario, fecha y hora, monto, moneda, tipo de operación, comercio,
   país/ubicación, canal y dispositivo. Con 3 datasets distintos, es esperable que **cada uno cubra
   un subconjunto distinto** — falta mapear columna por columna cuál cubre qué.
2. **¿Permite construir historial por usuario?** El modelo propuesto compara cada transacción contra
   el comportamiento histórico del usuario. El dataset 1 no tiene identificador de usuario real (es
   anonimizado); el 3 sí (1.000 clientes identificados). Falta confirmar el 2.
3. **Licencia.** Que se puedan usar y citar los 3 — ver pendientes arriba.

## ⚠️ Métricas: *accuracy* no sirve

En detección de fraude los datos están **fuertemente desbalanceados** — los fraudes suelen ser menos
del 1% de las transacciones. Un modelo que diga *"nada es fraude"* para todo acierta el 99% de las
veces y **no sirve para nada**.

Hay que decidir con qué se evalúa. Falta definirlo → 🔲 pendiente.

También hay que decidir **qué error duele más**:

| | Qué es | Qué cuesta |
|---|---|---|
| **Falso positivo** | Transacción legítima marcada como fraude | Molesta al cliente, el comercio pierde la venta |
| **Falso negativo** | Fraude que pasa sin detectarse | Pérdida directa de plata |

Esa decisión es de **producto**, no de modelo, y sale del User Research: depende de a quién le duele
más cada cosa.

## Reglas del repositorio

- **Los datasets NO se versionan.** `data/` y `*.csv` están en `.gitignore`.
  Se documenta **de dónde bajarlo**, no el archivo.
- **Nunca subir datos de transacciones reales** al repositorio ni al grafo de Graphify.

## Honestidad académica

Los 3 datasets van **citados con autor y link** en el documento final y en el pitch. Ver
[`prototipo.md`](prototipo.md#️-honestidad-académica--hay-que-dejarlo-escrito).
