# Ficha del Proyecto

> Fuente: planilla `TIF_2C2026_Clase1597_Britez.xlsx` (relevamiento inicial de propuestas TIF – 2C 2026),
> cargada por Mateo Diaz Valdez.

## Identificación

| Campo | Valor |
|---|---|
| **Nombre de trabajo** | FraudLens |
| **Título tentativo (planilla)** | Sistema inteligente de detección de fraude en transacciones en tiempo real |
| **Materia** | Seminario de Gestión Tecnológica |
| **N.º de clase** | 1597 |
| **Docente** | Daniel Britez |
| **Período** | 2C 2026 |
| **Tipo de entregable previsto** | Prototipo funcional de software |

> ⚠️ **Discrepancia de nombre a resolver:** la planilla dice *"Sistema inteligente de detección de
> fraude en transacciones en tiempo real"*, el tablero de Trello dice *"FraudLens - Analizador
> probabilidad de fraude"*. Hay que unificar el título oficial.
> Ver [`preguntas-abiertas.md`](preguntas-abiertas.md#p-01).

## Problema / necesidad / oportunidad

Los sistemas tradicionales de detección de fraude suelen apoyarse en **reglas predefinidas**, que
pueden resultar insuficientes para identificar comportamientos anómalos que no fueron contemplados
previamente.

Existe la oportunidad de **complementar** esas reglas mediante modelos de inteligencia artificial
capaces de analizar patrones históricos y características de cada transacción para detectar
operaciones potencialmente fraudulentas.

> Nota: el enunciado dice **complementar**, no reemplazar. Es una distinción importante para el
> discurso del proyecto y para el pitch final.

## Objetivo del proyecto

Desarrollar un prototipo capaz de:

- analizar transacciones **en tiempo real**,
- estimar su **nivel de riesgo de fraude** mediante un modelo de IA entrenado con datos históricos,
- identificar comportamientos anómalos,
- y **asistir en la decisión** de aprobar, rechazar o revisar una operación.

## Entregable previsto

Prototipo funcional de software compuesto por:

1. **API de análisis de transacciones**, integrada con
2. un **modelo de detección de fraude**, y
3. una **interfaz web** para visualizar las operaciones y su nivel de riesgo.

## Estado

| Ítem | Estado |
|---|---|
| Problema cargado en la planilla del docente | ✅ Hecho |
| Problema aprobado/seleccionado por los docentes | ❓ A confirmar — ver [P-02](preguntas-abiertas.md#p-02) |
| User Research sobre el problema | ⬜ Pendiente |
| Definición de la solución | ⬜ Pendiente |
| Desarrollo del MVP | ⬜ Pendiente |

## Chequeo contra la lista de "Problemas que NO" (Clase 1)

El docente listó temáticas descartadas (reservas, estacionamiento, colas/turnos, tiendas online,
gestión de gastos, historia clínica, ABMs varios, mascotas, gimnasios, trackeo, recetas).

**FraudLens no cae en ninguna de esas categorías.** ✅
