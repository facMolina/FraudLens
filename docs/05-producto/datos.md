# Datos y dataset del modelo

> **Estado:** 🟡 hay **3 candidatos pre-seleccionados**, falta elegir uno y documentarlo.
> Responsable: ⬜ · Referencia: [P-11](../00-proyecto/preguntas-abiertas.md#p-11)

## Candidatos pre-seleccionados

> ⚠️ **Ojo: los tres links son NOTEBOOKS de Kaggle (`/code/`), no datasets (`/datasets/`).**
> Cada notebook usa un dataset por debajo. **Lo que necesitamos identificar es el dataset**, que es
> el dato en sí; el notebook es el análisis que otra persona hizo sobre él.

| # | Notebook | Autor | Nota |
|---|---|---|---|
| 1 | [Fraud Detection Full Project in Spanish](https://www.kaggle.com/code/carmencastrogonzlez/fraud-detection-full-project-in-spanish) | `carmencastrogonzlez` | **Es el que usó FGR** como base del [prototipo](prototipo.md) |
| 2 | [Fraud Detection using Deep Learning](https://www.kaggle.com/code/oscarmatiastorres/fraud-detection-using-deep-learning) | `oscarmatiastorres` | |
| 3 | [Detección de fraudes en transacciones](https://www.kaggle.com/code/christianmontenegro/detecci-n-de-fraudes-en-transacciones) | `christianmontenegro` | |

## Qué hay que completar para cada candidato

| Ítem | 1 | 2 | 3 |
|---|---|---|---|
| **Dataset que usa** (nombre + link al dataset) | ⬜ | ⬜ | ⬜ |
| Cantidad de registros | ⬜ | ⬜ | ⬜ |
| Columnas / features disponibles | ⬜ | ⬜ | ⬜ |
| ¿Trae etiqueta de fraude? | ⬜ | ⬜ | ⬜ |
| % de casos fraudulentos (desbalanceo) | ⬜ | ⬜ | ⬜ |
| ¿Alcanza para **entrenar** o sólo para **probar**? | ⬜ | ⬜ | ⬜ |
| Licencia de uso | ⬜ | ⬜ | ⬜ |

## Criterios para elegir

1. **¿Tiene las columnas que necesita nuestro MVP?**
   El [documento de requerimientos](requerimientos-funcionales-mvp.md) pide: identificador de
   transacción, identificador de usuario, fecha y hora, monto, moneda, tipo de operación, comercio,
   país/ubicación, canal y dispositivo. **Si el dataset no las tiene, o cambia el dataset o cambian
   los requerimientos.**
2. **¿Permite construir historial por usuario?** El modelo propuesto compara cada transacción contra
   el comportamiento histórico del usuario. Si el dataset no permite agrupar por usuario, eso no se
   puede hacer.
3. **¿Está en español o es fácil de explicar?** El documento final y el pitch son en español.
4. **Licencia.** Que se pueda usar y citar.

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

Sea cual sea el dataset y el notebook que usemos, va **citado con autor y link** en el documento
final y en el pitch. Ver [`prototipo.md`](prototipo.md#️-honestidad-académica--hay-que-dejarlo-escrito).
