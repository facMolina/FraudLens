# Requerimientos funcionales del MVP — BORRADOR

> ⚠️ **ESTO NO ESTÁ APROBADO.**
>
> | | |
> |---|---|
> | **Autor** | Francisco Daniel Guerrero Rojas (FGR) |
> | **Origen** | `FraudLens - Requerimientos funcionales del MVP.docx` |
> | **Estado** | 🟡 **Borrador para revisión del equipo** |
> | **Incorporado al repo** | 2026-09-02 por FM |
>
> Francisco lo pasó **para que el equipo lo revise**, no como definición cerrada. Nada de lo que
> está acá debe tomarse como decidido hasta que el equipo lo valide y quede registrado como
> [decisión](../03-decisiones/).
>
> Se transcribe completo y sin cambios de contenido para poder discutirlo sobre algo concreto.

---

## 1. Objetivo

FraudLens permitirá recibir una transacción mediante una API, analizarla utilizando datos del
usuario y su historial transaccional, y devolver:

- Un nivel de riesgo de fraude entre 0 % y 100 %.
- Una clasificación de riesgo.
- Una decisión recomendada: **aprobar, revisar o bloquear**.
- Los principales motivos que influyeron en el resultado.

Las transacciones y sus resultados podrán consultarse en un **dashboard en tiempo real**.

## 2. Alcance del MVP

- Recepción de transacciones mediante API.
- Consulta del historial disponible del usuario.
- Estimación de riesgo con un modelo simple entrenado con datos históricos.
- Aplicación de reglas configurables.
- Recomendación automática de una decisión.
- Dashboard de monitoreo.
- Consulta del detalle de cada transacción.
- Configuración de umbrales desde el dashboard.

## 3. Actores

| Actor | Rol |
|---|---|
| **Sistema cliente** | Envía transacciones para analizar |
| **Analista de fraude** | Monitorea operaciones y revisa sus resultados |
| **Administrador** | Configura los umbrales de decisión |
| **FraudLens** | Analiza la transacción y genera una recomendación |

## 4. Flujo principal

1. Un sistema cliente envía una transacción.
2. FraudLens valida que los datos obligatorios estén presentes.
3. Evalúa la regla de monto mínimo.
4. Si corresponde, consulta el historial del usuario y calcula el riesgo mediante el modelo.
5. Aplica los umbrales configurados.
6. Devuelve el resultado al sistema cliente.
7. Registra la transacción y la muestra en el dashboard.

### Decisiones posibles

| Condición | Resultado |
|---|---|
| Monto inferior al mínimo de análisis | Aprobar por regla, sin ejecutar el modelo |
| Riesgo inferior al umbral de revisión | Aprobar |
| Riesgo igual o superior al umbral de revisión | Revisar |
| Riesgo igual o superior al umbral de bloqueo | Bloquear |

> Conviene que una transacción no analizada por estar debajo del monto mínimo se marque como
> **"no evaluada por el modelo"**, en lugar de asignarle artificialmente un riesgo de 0 %.

## 5. Casos de uso

### CU-01 — Analizar una transacción

**Actor:** sistema cliente.

**Entrada mínima:** identificador único de la transacción · identificador del usuario · fecha y hora ·
monto · moneda · tipo o categoría de operación · comercio o destinatario · país o ubicación · canal
utilizado · dispositivo o identificador de sesión (cuando esté disponible).

**Flujo:**

1. El cliente envía la transacción.
2. FraudLens valida los datos.
3. Verifica si la transacción ya fue procesada.
4. Aplica la regla de monto mínimo.
5. Si debe analizarse, obtiene el historial del usuario.
6. Calcula el riesgo.
7. Determina la decisión recomendada.
8. Guarda y devuelve el resultado.

**Resultado esperado:**

```json
{
  "transaction_id": "trx-123",
  "risk_score": 78,
  "risk_level": "alto",
  "decision": "revisar",
  "analyzed_by_model": true,
  "reasons": [
    "Monto superior al habitual",
    "Ubicación no frecuente"
  ]
}
```

**Criterios de aceptación:**

- El riesgo debe expresarse entre 0 y 100.
- Toda respuesta debe contener una decisión.
- La transacción debe aparecer en el dashboard.
- El mismo identificador no debe generar registros duplicados.
- Si faltan datos obligatorios, la API debe rechazar la solicitud indicando cuáles faltan.

### CU-02 — Aplicar la regla de monto mínimo

**Actor:** FraudLens.
**Objetivo:** evitar ejecutar el análisis para operaciones de poco valor.
**Ejemplo:** *"No analizar transacciones menores a ARS 10.000"*.

**Criterios de aceptación:**

- El monto mínimo debe ser configurable.
- Si el monto es inferior, la operación se aprueba por regla.
- El resultado debe indicar que el modelo no fue ejecutado.
- La transacción igualmente debe registrarse y mostrarse en el dashboard.

### CU-03 — Calcular el riesgo de fraude

**Actor:** FraudLens.

El modelo deberá utilizar información simple de la transacción y del comportamiento histórico del
usuario, por ejemplo: diferencia respecto del monto habitual · frecuencia reciente de operaciones ·
países o ubicaciones habituales · comercios o categorías utilizadas previamente · horario habitual
de operación · uso de un dispositivo nuevo · cantidad de operaciones recientes.

**Criterios de aceptación:**

- Debe producir un puntaje entre 0 y 100.
- Debe funcionar aunque el usuario tenga poco o ningún historial.
- En usuarios nuevos, el resultado debe indicar **"historial insuficiente"**.
- Debe devolver hasta tres factores relevantes, sin requerir explicaciones avanzadas del modelo.

### CU-04 — Determinar la decisión

**Actor:** FraudLens.

**Configuración de ejemplo:** riesgo menor a 60 % → aprobar · desde 60 % → revisar · desde 85 % → bloquear.

**Criterios de aceptación:**

- Los umbrales deben poder modificarse sin alterar el modelo.
- El umbral de bloqueo debe ser mayor que el de revisión.
- La respuesta debe mostrar qué regla o umbral produjo la decisión.
- Un cambio de configuración debe aplicarse solamente a nuevas evaluaciones.

### CU-05 — Monitorear transacciones

**Actor:** analista de fraude.

El dashboard mostrará una lista actualizada de transacciones con: fecha y hora · identificador ·
usuario · monto y moneda · puntaje de riesgo · nivel de riesgo · decisión · estado del análisis.

**Filtros mínimos:** rango de fechas · nivel de riesgo · decisión · identificador de usuario ·
identificador de transacción.

**Criterios de aceptación:**

- Las transacciones nuevas deben aparecer sin recargar manualmente la página, o mediante actualización periódica.
- Los riesgos altos y bloqueos deben distinguirse visualmente.
- La tabla debe poder ordenarse por fecha y riesgo.
- Si no existen resultados, debe mostrarse un estado vacío claro.

### CU-06 — Consultar el detalle de una transacción

**Actor:** analista de fraude.

El detalle mostrará: datos recibidos · puntaje y nivel de riesgo · decisión recomendada · reglas
aplicadas · factores que elevaron el riesgo · resumen del historial utilizado · fecha y hora del
análisis · configuración de umbrales vigente al analizarla.

### CU-07 — Configurar reglas y umbrales

**Actor:** administrador.

**Configuraciones mínimas:** activar o desactivar la regla de monto mínimo · monto mínimo de
análisis · umbral de revisión · umbral de bloqueo.

**Criterios de aceptación:**

- Sólo un administrador puede modificar estos valores.
- El sistema debe validar valores entre 0 y 100.
- No debe permitir configuraciones inconsistentes.
- Debe registrar quién realizó el cambio, cuándo y cuáles eran los valores anteriores.

## 6. Clasificación visual sugerida

| Puntaje | Nivel | Acción |
|---|---|---|
| 0–39 | Bajo | Aprobar |
| 40–59 | Medio | Aprobar o monitorear |
| 60–84 | Alto | Revisar |
| 85–100 | Crítico | Bloquear |

> Los rangos deben adaptarse automáticamente a los umbrales configurados.

## 7. Requerimientos no funcionales

- El análisis debe responder en pocos segundos para no interrumpir el flujo de la operación.
- Toda transacción debe poder rastrearse por su identificador.
- Los resultados deben conservar los valores de configuración utilizados en el momento del análisis.
- La información sensible no debe mostrarse completa en el dashboard.
- El acceso al dashboard debe requerir autenticación.
- Los errores del modelo **no deben producir aprobaciones silenciosas**: deben devolver un estado
  explícito de *"análisis no disponible"*.
- El sistema debe registrar errores y eventos relevantes para diagnóstico.

## 8. Casos excepcionales

Transacción duplicada · usuario sin historial · datos incompletos o inválidos · moneda desconocida ·
modelo temporalmente no disponible · puntaje exactamente igual a un umbral · monto exactamente igual
al mínimo de análisis · historial insuficiente · transacción recibida con fecha futura o demasiado antigua.

## 9. Fuera del alcance

Para mantener el MVP simple, quedarán fuera:

- Entrenamiento automático o continuo del modelo.
- Modelos avanzados o múltiples modelos especializados.
- Investigación completa de casos de fraude.
- Gestión de reclamos o contracargos.
- Modificación manual de la decisión desde el dashboard.
- Notificaciones por correo o mensajería.
- Integraciones con listas externas de fraude.
- Grafos de relaciones entre usuarios, comercios o dispositivos.
- Reentrenamiento basado en acciones del analista.
- Explicabilidad avanzada.
- **Bloqueo real de dinero**: FraudLens sólo devuelve una recomendación.

## 10. Definición de "MVP terminado"

El MVP estará completo cuando pueda demostrarse este recorrido:

1. Se carga un conjunto de transacciones históricas.
2. Se envía una nueva transacción a la API.
3. FraudLens devuelve riesgo, nivel, decisión y motivos.
4. La transacción aparece en el dashboard.
5. El usuario abre su detalle.
6. El administrador modifica los umbrales.
7. Una nueva transacción utiliza la configuración actualizada.
8. Se demuestran los tres resultados: **aprobar, revisar y bloquear**.

---

# Puntos a discutir en equipo

> Esta sección **no es de Francisco**: son observaciones para la revisión. Se resuelven en equipo.

| # | Punto | Por qué revisarlo |
|---|---|---|
| 1 | El documento **asume el usuario objetivo** (analista de fraude + administrador) | Es justamente lo que la materia pide validar con User Research antes de definir. Está por delante de [P-07](../00-proyecto/preguntas-abiertas.md#p-07) |
| 2 | El alcance incluye **7 casos de uso, dashboard, autenticación y configuración de umbrales** | Hay que contrastarlo contra el criterio de MVP de la Clase 1 (UberCab = una ciudad, una función). Puede ser más grande que un MVP |
| 3 | Autenticación + roles (admin vs analista) están **dentro** del alcance | ¿Es necesario para demostrar valor, o es NO MVP? |
| 4 | No hay **métricas de evaluación del modelo** | En fraude los datos están desbalanceados; hay que decidir cómo se mide que el modelo sirve |
| 5 | Los umbrales de ejemplo (60 / 85) y los rangos de la tabla de clasificación **no coinciden entre sí** | La tabla marca "medio" hasta 59 y "alto" desde 60; conviene unificar el criterio |
| 6 | Está escrito **antes del User Research** | La materia exige que el producto salga de la evidencia. Habrá que poder explicar cómo esto se valida (o se corrige) con los datos |

**Ninguno de estos puntos dice que el documento esté mal.** Está muy completo y sirve como base.
Son los temas a cerrar antes de convertirlo en definición.
