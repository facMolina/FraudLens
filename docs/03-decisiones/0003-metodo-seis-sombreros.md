# 0003 — Adoptar el método de los 6 Sombreros para las decisiones del proyecto

| | |
|---|---|
| **Fecha** | 2026-09-02 |
| **Estado** | ✅ Aceptada |
| **Decidido por** | **Consigna del docente** (no es una elección del equipo) |
| **Pregunta relacionada** | — |

## Contexto

El docente pidió aplicar el **método de los 6 Sombreros para Pensar** (Edward de Bono) a los temas
del proyecto, y entregó un prompt específico para hacerlo con asistencia de IA.

El equipo viene tomando decisiones de manera informal: el problema se eligió en clase, los
requerimientos los escribió una persona, el prototipo lo armó otra. Ninguna de esas decisiones quedó
con su razonamiento escrito, y el docente evalúa **"cumplimiento del problema-solución"** — que es
exactamente eso.

## Alternativas consideradas

| Opción | A favor | En contra |
|---|---|---|
| **Aplicarlo a toda decisión relevante** | Es lo que pidió el docente; deja el razonamiento escrito y reutilizable en el documento final | Cuesta tiempo |
| Aplicarlo sólo a la decisión final del proyecto | Menos trabajo | No es lo que se pidió, y llegaríamos sin práctica a la decisión que más importa |
| Aplicarlo a **todas** las tarjetas, incluidas las operativas | Cumplimiento literal | Un análisis de 6 sombreros sobre *"invitar gente al tablero"* es ruido, y el ruido tapa lo que sí importa |

## Decisión

Se adopta el método de los 6 Sombreros **para toda decisión y todo entregable de la materia**, con
un criterio explícito de cuándo aplica y cuándo no.

**Criterio:** *"¿esto se puede hacer mal de más de una manera?"* Si la respuesta es sí, lleva
análisis. Las tareas de pura ejecución, no.

| Tipo de tarjeta | ¿Análisis? |
|---|---|
| Decisión entre opciones (usuario, dataset, alcance, stack) | ✅ Sí |
| Entregable de la materia (Problem Statement, solución elegida, MVP Canvas) | ✅ Sí |
| Tarea operativa (invitar gente, crear un repo, cargar un documento) | ❌ No |

## Por qué

- **Es consigna del docente**, no una preferencia del equipo.
- Obliga a separar **hechos** de **miedos** de **críticas**, que es justo donde este equipo se venía
  mezclando: el prototipo se defendía por apego, no por evidencia.
- El sombrero **blanco** obliga a listar **qué datos faltan**, lo que conecta directo con la regla
  del repositorio de no deducir.
- El análisis escrito **es material del documento final**: el razonamiento ya queda redactado.

## Consecuencias

- Se crea [`docs/04-metodologia/seis-sombreros.md`](../04-metodologia/seis-sombreros.md) con el
  método y el prompt del docente textual.
- Los análisis viven en [`docs/05-producto/analisis/`](../05-producto/analisis/) y **cada tarjeta de
  Trello linkea al suyo**.
- **Tres salvaguardas al usar IA para esto:**
  1. El sombrero **blanco** sólo usa hechos que aportamos nosotros. **No rellena.** Un dato inventado
     en un documento evaluado es un riesgo, no un atajo.
  2. El sombrero **rojo** lo escribe **el equipo**. Las emociones son nuestras, no de un modelo.
  3. **La decisión la firma el equipo.** En la defensa nos van a preguntar por qué decidimos algo, y
     *"lo dijo la IA"* no es una respuesta.
- Primer análisis hecho:
  [¿Quién es el usuario de FraudLens?](../05-producto/analisis/6-sombreros-usuario-objetivo.md)
