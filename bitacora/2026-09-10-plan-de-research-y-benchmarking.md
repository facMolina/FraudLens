# 2026-09-10 — Plan de research, benchmarking, ideación y narrativa

| | |
|---|---|
| **Tipo** | Trabajo individual (con asistencia de Claude Code) |
| **Duración** | — |
| **Participantes** | Facundo Molina (FM) |

## Por qué esta sesión

De los tickets sin bloqueo identificados el 9/9, estos dos eran los más urgentes: la tarjeta 2
(Plan de research) llevaba **8 días vencida** y es la raíz que bloquea User Persona, Mapa de
Empatía y Problem Statement; la tarjeta 9 (Benchmarking) era el único de los 4 entregables del 5/9
que no depende de conseguir entrevistas.

## Qué se hizo

### Plan de research (`docs/05-producto/user-research.md`)

Documento nuevo que define **cómo** se investiga, no los resultados — el research en sí sigue en
cero (0 entrevistas, 0 encuestas):

- Guía de entrevista para el **Perfil A** (analista de fraude, vía ML) — 5 temas, marcada como la
  más valiosa y la más escasa porque la ventana de ML se cierra ~16/9.
- Guía de entrevista para el **Perfil B** (dueño de comercio chico) — 4 temas centrados en costo
  real y disposición a pagar.
- Borrador de encuesta para el **Perfil C** (consumidor) — 7 preguntas, aplicando las buenas
  prácticas ya cargadas en el ticket (rangos impares, "Otros"/NS-NC, sin inducir respuesta).
- Propuesta de volumen: **80-100 respuestas de encuesta + 2-3 entrevistas por perfil**, justificado
  explícitamente contra [P-17](../docs/00-proyecto/preguntas-abiertas.md#p-17) (400 es guía, no
  obligación) — no se busca significancia estadística, sólo evidencia de que el problema existe.
- Canales de difusión, cronograma atado al 16/9, y la regla ya escrita en `usuarios.md` de que el
  research corrige los documentos existentes si los contradice, no al revés.

### Benchmarking con curva de valor (`docs/05-producto/benchmarking.md`)

Primera vuelta de benchmarking, con investigación real vía búsqueda web (no inventada):

- **6 competidores relevados con fuente citada**: Sift, Feedzai, Forter, Signifyd, Riskified,
  ClearSale — categorizados en capas de señal / plataformas de puntuación / modelos de garantía.
- **Curva de valor en 6 factores** (precio, foco LatAm, modelo de garantía, cobertura AML+fraude,
  complementa-vs-reemplaza, explicabilidad), puntuando cada competidor y la hipótesis de FraudLens.
- 🔴 **Corrección honesta de la propia hipótesis del equipo**: el borrador ERRC de la Clase 6
  proponía "explicabilidad + comercio chico" como espacio blanco. El benchmarking **no lo
  confirma**: la explicabilidad ya es tendencia regulatoria de toda la industria en 2026 (no un
  diferencial), y ClearSale ya cubre "comercio chico + LatAm" con garantía financiera e integración
  a Tiendanube.
- El único hallazgo que sobrevive: **ninguno de los 6 relevados se posiciona como complemento** de
  un sistema antifraude existente (todos compiten para *ser* el sistema, o asumen la pérdida). Esto
  coincide con la hipótesis de [P-07](../docs/00-proyecto/preguntas-abiertas.md#p-07), pero queda
  marcado explícitamente como **hipótesis sin confirmar** hasta tener el research del Perfil A —
  mismo sesgo que ya nombró el sombrero rojo.

## Qué se definió

- El plan de research y la primera vuelta de benchmarking quedan escritos, pero **ninguno de los
  dos tickets pasa a Hecho todavía**: el plan de research no reemplaza al research ejecutado, y el
  benchmarking es continuo por definición de la propia clase.
- Ambas tarjetas se movieron a **👀 En revisión** — a la del plan de research le falta que otro
  integrante la revise (su propio checklist lo pide); a la de benchmarking, que el equipo vea el
  hallazgo de corrección de hipótesis antes de darla por cerrada.

## ⚠️ Nota sobre Trello

El comentario de resolución **no se pudo cargar como comentario nativo**: la acción `add_comment`
de la herramienta de Trello sigue fallando con un error de validación server-side (mismo problema
ya documentado el 9/9). Se aplicó el mismo workaround: el comentario de resolución quedó escrito
dentro de la **descripción** de cada tarjeta, bajo un encabezado `## 📋 RESOLUCIÓN`, con fecha y
autor. Pierde los metadatos de comentario nativo (autor/fecha separados), pero mantiene la
transparencia que pide la regla del proyecto.

## Qué quedó pendiente (primera parte)

| Tarea | Responsable | Urgencia |
|---|---|---|
| Revisar el plan de research (checklist propio de la tarjeta lo pide) | Equipo | 🟡 Antes del 16/9 |
| **Ejecutar** el plan: difundir la encuesta y conseguir las entrevistas | Equipo / ML | 🔴 Antes del 16/9 — se cierra la ventana de ML |
| Verificar en los sitios de cada competidor las celdas ❓ del benchmarking | Equipo | 🟢 |
| Repetir la curva de valor después del research del Perfil A | Equipo | 🟢 |
| Re-testear si `add_comment` de Trello ya funciona, para volver a comentarios nativos | FM | 🟢 |

---

## Segunda parte — Ideación y Narrativa de la propuesta

Mismo día, se encararon los otros dos entregables vencidos del 9/9: la tarjeta 10 (Ideación y
Grilla de Priorización) y la tarjeta 11 (Narrativa de la propuesta de solución).

### Ideación (`docs/05-producto/ideacion.md`)

Se amplió el borrador ERRC de la Clase 6 con fuente citada por idea (el borrador mismo, el
benchmarking, los requerimientos), y se armó una **grilla de priorización Impacto × Esfuerzo** con
6 ideas.

🔴 **Dos hallazgos, no sólo un entregable cumplido:**

1. El deck nombra la Grilla de Priorización pero no explica cómo se arma. Se usó Impacto×Esfuerzo
   como criterio **propio del equipo, no del docente** — queda como
   [P-24](../docs/00-proyecto/preguntas-abiertas.md#p-24), a confirmar.
2. La idea "eliminar la configuración manual de reglas" (borrador ERRC) **choca directo con el
   CU-07** de los requerimientos de ML, que define un actor administrador justamente para eso. No
   se resolvió acá — queda anotado para cuando el equipo revise los requerimientos funcionales.

### Narrativa de la propuesta (nueva sección en `docs/05-producto/problema.md`)

Se escribieron **3 narrativas en 3 actos** (estructura de Aristóteles, Clase 5), una por perfil —
mismo criterio que las 3 reformulaciones de FGR: elegir una sola hoy adelantaría
[P-07](../docs/00-proyecto/preguntas-abiertas.md#p-07) sin evidencia. Cada narrativa:

- Esquiva las dos trampas que la propia tarjeta señalaba (arrancar por la tecnología / no dar el
  número).
- Deja marcado explícitamente **el número que falta** en cada perfil (tiempo perdido del analista,
  plata perdida del comercio, frecuencia del rechazo indebido) como hueco a completar con el
  research — no se inventó ningún dato.
- Pasa un test de 10 segundos, escrito al final de cada una.

Queda pendiente decidir **cuándo converge en una sola historia** para The Pitch — no se fuerza acá.

### Registro en los dos lugares

Mismo patrón que el resto de la sesión: resolución escrita en la `desc` de cada tarjeta (workaround
por el bug de `add_comment`) y ambas movidas a **👀 En revisión** — son borradores sobre un Problem
Statement todavía abierto, y falta la validación del equipo.

## Qué quedó pendiente (segunda parte)

| Tarea | Responsable | Urgencia |
|---|---|---|
| Resolver la tensión "eliminar config. manual" vs. CU-07 | Equipo | 🟡 Al revisar los requerimientos |
| Confirmar con el docente el formato de Grilla de Priorización (P-24) | Equipo → Docente | 🟢 |
| Validar las 3 narrativas y decidir cuándo convergen en una sola | Equipo | 🟡 Antes de The Pitch |
| Revalidar la ideación con los resultados del research | Equipo | 🟢 |

## Archivos

- `docs/05-producto/user-research.md` *(nuevo)*
- `docs/05-producto/benchmarking.md` *(nuevo)*
- `docs/05-producto/ideacion.md` *(nuevo)*
- `docs/05-producto/problema.md` — nueva sección "Narrativa de la propuesta de solución"
- `docs/00-proyecto/preguntas-abiertas.md` — P-24 nueva
- `registro/historial-aportes.md`
