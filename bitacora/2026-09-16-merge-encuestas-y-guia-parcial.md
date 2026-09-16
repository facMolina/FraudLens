# 2026-09-16 — Merge del research de ML, orden del tablero y guía para el 1° Parcial

| | |
|---|---|
| **Tipo** | Trabajo individual, con validación en el momento (con asistencia de Claude Code) |
| **Duración** | — |
| **Participantes** | Facundo Molina (FM) |

## Por qué esta sesión

Es el día del 1° Parcial. ML ejecutó research real (entrevistas + encuesta) pero no podía seguir
avanzando (ni abrir el PR ni tocar Trello); FGR ya había resuelto sus dos tareas asignadas (dataset
y tensión CU-07). Quedaba: mergear el trabajo de ML, ordenar el tablero contra la consigna real del
docente, y armar una guía de consulta rápida para la oral.

## PR #2 de ML — entrevistas y encuesta

ML pusheó a la rama `encuestas` (3 commits) sin abrir el Pull Request. Se revisó el contenido antes
de tocar nada:

- **Entrevistas reales ejecutadas:** Nicolás (Perfil A, analista de fraude) y Agustín (Perfil B,
  analista de producto en fintech). Hallazgos: falsos positivos, falta de explicabilidad, pedido de
  vista unificada del caso y panel configurable por perfil.
- **Encuesta del Perfil C difundida:** https://forms.gle/ZLfhijskphLA1Fxu9
- ML corrigió un exceso propio: había puesto un contacto puntual ("Tobías") para una encuesta que
  en realidad es abierta — lo sacó.
- **Cambió la definición del Perfil B** de "responsable de riesgo/producto" (decisión 0004) a
  "analista de producto" — el cargo real de su contacto. Se le preguntó a FM si aceptarlo: **sí,
  ML es quien tiene el contacto y el contexto real**, se deja tal cual sin revertir.

La rama estaba desactualizada respecto a los commits de FGR y MDV de las últimas 24 h. Se mergeó la
base en la rama de ML localmente, se resolvió el único conflicto real (`historial-aportes.md`, dos
filas nuevas casi simultáneas — se conservaron ambas) y se abrió y mergeó el
[PR #2](https://github.com/facMolina/FraudLens/pull/2).

## Orden del tablero contra la consigna del docente

- **"Encuestas y entrevistas"** → de 🚧 Bloqueado a 🔨 En curso: entrevistas A y B hechas, encuesta
  difundida; sólo falta recopilar y analizar respuestas — tarea que ya no depende de ML.
- **"Stakeholders y expertos consultados"** → actualizada con Nicolás y Agustín (estaba desactualizada).
- **"Modelos de IA a utilizar"** → de 🚧 Bloqueado a 🎯 Esta semana, con la referencia a la decisión
  0006 de FGR que la destrabó.
- **5 tarjetas diferidas a 📥 Backlog** (Documentar prototipo de FGR, Arrancar repo de código del
  MVP, User Persona, Mapa de Empatía, Problem Statement validado): no están en la lista explícita
  del docente para hoy, y varias dependen de trabajo que no es urgente para la oral. Quedan
  anotadas para retomar la próxima clase, no se pierden.
- **🚧 Bloqueado quedó en cero tarjetas.**

## Guía para la oral

[`docs/00-proyecto/guia-1er-parcial.md`](../docs/00-proyecto/guia-1er-parcial.md) — mapea cada uno
de los 16 ítems que pidió el docente contra el estado real del repo, con links directos y sin
inventar nada: marca explícitamente los 4 huecos reales (código del MVP, respuestas de la encuesta,
sombrero rojo incompleto, P&L pendiente) y sugiere cómo responder si preguntan por ellos.

## Archivos

- `docs/00-proyecto/guia-1er-parcial.md` *(nuevo)*
- `registro/historial-aportes.md`
- Tablero de Trello: 8 tarjetas actualizadas/movidas
