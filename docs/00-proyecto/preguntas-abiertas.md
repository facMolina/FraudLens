# Preguntas abiertas

Todo lo que falta definir. Cuando una pregunta se responde: se marca **✅ Resuelta**, se escribe la
respuesta, y si la respuesta cambia el rumbo del proyecto se registra además como
[decisión](../03-decisiones/).

**Prioridad:** 🔴 bloqueante · 🟡 importante · 🟢 puede esperar

| ID | Pregunta | Prioridad | Para quién | Estado |
|---|---|---|---|---|
| [P-01](#p-01) | ¿Cuál es el título oficial del proyecto? | 🟡 | Equipo | 🔲 Abierta |
| [P-02](#p-02) | ¿El problema ya está aprobado por los docentes? | 🔴 | Docente | 🔲 Abierta |
| [P-03](#p-03) | ¿El equipo queda con 4 integrantes? | 🔴 | Docente | 🔲 Abierta |
| [P-04](#p-04) | ¿Cuál es el calendario real de 2C 2026? | 🔴 | Docente | 🔲 Abierta |
| [P-05](#p-05) | ¿Dónde vive el código del MVP? | 🟡 | Equipo | 🔲 Abierta |
| [P-06](#p-06) | ¿Qué datos reales vamos a usar? | 🔴 | Equipo | 🔲 Abierta |
| [P-07](#p-07) | ¿Quién es el usuario objetivo? | 🔴 | Equipo | 🔲 Abierta |
| [P-08](#p-08) | ¿Qué roles toma cada integrante? | 🟡 | Equipo | 🔲 Abierta |
| [P-09](#p-09) | ¿Cómo se estructura el tablero de Trello? | 🟡 | Equipo | 🔲 Abierta |
| [P-10](#p-10) | ¿Qué stack tecnológico usamos? | 🟢 | Equipo | 🔲 Abierta |

---

## P-01
### ¿Cuál es el título oficial del proyecto?

La planilla del docente dice **"Sistema inteligente de detección de fraude en transacciones en
tiempo real"**. El tablero de Trello dice **"FraudLens - Analizador probabilidad de fraude"**.

Hay que elegir uno y usarlo en forma consistente en documentación, entregas y pitch.
Sugerencia: **FraudLens** como nombre de producto y la frase larga como descripción/subtítulo.

---

## P-02
### ¿El problema ya está aprobado por los docentes?

La planilla ya tiene el problema cargado, pero la Clase 1 dice que para la clase siguiente hay que
llevar **mínimo 2 propuestas de problema por integrante** y que junto a los docentes **se selecciona
uno**. La selección de problema figura en el cronograma de la **Clase 2**.

**Impacto si la respuesta es "no":** habría que preparar 8 propuestas (2 × 4 integrantes) y FraudLens
pasa a ser una candidata más, no un hecho.

**Tarea asociada:** *Narrativa de Propuestas de Problema* (Tarea de Teams) + *Presentación de Avance:
listado de problemas priorizados por relevancia, votado, en 1:30 minutos*.

---

## P-03
### ¿El equipo queda con 4 integrantes?

La Clase 1 indica equipos de **seis/ocho integrantes**. Somos **4**.

**Impacto:** si hay que fusionarse con otro equipo cambian los roles, el reparto de trabajo y
posiblemente el problema elegido. Conviene confirmarlo cuanto antes.

---

## P-04
### ¿Cuál es el calendario real de 2C 2026?

El deck de Clase 1 (v1.2) trae el cronograma del **primer cuatrimestre** (09/03 → 20/07). Nuestro
período es **2C 2026**.

Hace falta:
- Fecha de cada clase
- Fecha de la **Primera Entrega** y de la **Segunda Entrega**
- Fechas de inicio/fin de cada uno de los **4 Sprints**
- Fecha de **entrega de documentación final**, **Simulacro The Pitch** y **The Pitch**
- Fecha del **recuperatorio** (última clase del cuatrimestre)

**Impacto:** sin esto no se puede planificar nada. Es lo primero a completar en
[`docs/02-entregables/README.md`](../02-entregables/README.md).

---

## P-05
### ¿Dónde vive el código del MVP?

Este repo es el centro de cómputos, no el producto. El MVP (API + modelo + web) necesita su lugar.

Opciones:
1. **Repositorio aparte** — más prolijo, separa documentación de código. *(sugerido)*
2. **Carpeta dentro de este repo** — todo junto, más simple de encontrar.

Sea cual sea, hay que dejar el link acá y en el README.

---

## P-06
### ¿Qué datos reales vamos a usar?

El docente exige **datos reales** para el User Research. Para FraudLens esto se abre en dos frentes:

**a) Datos del problema (User Research):** ¿a quién entrevistamos? ¿Gente que sufrió fraude?
¿Alguien que trabaje en prevención de fraude en un banco, fintech o procesador de pagos? ¿Tenemos
un contacto en el rubro?

**b) Datos para entrenar el modelo:** ¿dataset público (tipo IEEE-CIS, PaySim, Credit Card Fraud
Detection de Kaggle) o datos sintéticos generados por nosotros? Cada opción tiene un costo en
credibilidad para el pitch.

**Decisión asociada:** también hay que definir con qué **métricas** se evalúa el modelo. Los datos de
fraude están muy desbalanceados, así que *accuracy* no sirve.

---

## P-07
### ¿Quién es el usuario objetivo?

FraudLens "asiste en la decisión de aprobar, rechazar o revisar". ¿Quién toma esa decisión?

- ¿Un **analista de fraude** que revisa una cola de casos? → el producto es un panel de revisión.
- ¿Un **sistema automático** del comercio? → el producto es una API y la web es secundaria.
- ¿El **dueño de un comercio chico** sin equipo antifraude? → el producto es otra cosa distinta.

**Impacto:** define la interfaz, el MVP y todo el User Research. Es la pregunta más importante de
la lista después del calendario. Se trabaja en la **Clase 2 (Segmentación de usuarios / Target)**.

---

## P-08
### ¿Qué roles toma cada integrante?

Ver la tabla de roles propuesta en [`equipo.md`](equipo.md#roles-a-repartir).
También hay que armar la rotación de presentadores de Sprint Reviews.

---

## P-09
### ¿Cómo se estructura el tablero de Trello?

El tablero **forma parte de la evaluación** ("Tableros de trabajo (Trello/Jira)"), así que no puede
estar desprolijo. Hay que definir listas, etiquetas y convención de tarjetas.

Propuesta inicial en [`docs/04-metodologia/trello.md`](../04-metodologia/trello.md) — falta validarla
contra el estado actual del tablero.

---

## P-10
### ¿Qué stack tecnológico usamos?

API, modelo e interfaz web. A definir cuando lleguemos al bloque de desarrollo, pero conviene
tenerlo pensado antes del Sprint 1 para no perder tiempo.

Criterio sugerido: **elegir lo que el equipo ya sabe usar**. El cuatrimestre es corto y la nota no
premia aprender un framework nuevo — premia tener un MVP funcionando.
