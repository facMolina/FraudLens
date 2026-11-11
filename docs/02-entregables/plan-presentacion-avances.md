# Plan: presentación de avances e informe con la marca

> **Estado:** 🟡 deck construido el 2026-11-11 (12 slides, [artifact](https://claude.ai/artifact/9YuGw3Cw2HDJkb5ncYuWPd)),
> falta la revisión del equipo. Contexto para editarlo en
> [`presentacion-avances/CONTEXTO-PRESENTACION.md`](presentacion-avances/CONTEXTO-PRESENTACION.md). El informe en LaTeX no se empezó.
> **Fuente de la consigna:** el docente **no pidió nada en particular** para el 2° Parcial (11/11): mostrar
> todo lo que tenemos *(dicho por MDV, 2026-11-11)*. La estructura de abajo es **propuesta del equipo**, no
> consigna de la cátedra.

## 1. Presentación de avances

### Decisiones tomadas

| Decisión | Elegido | Descartado y por qué |
|---|---|---|
| Herramienta | Skill `presentacion-viva` → **artifact Slides de claude.ai**: gráficos animados que entran solos y quedan en loop, marca en cada slide, notas del orador, exporta a PDF y PPTX | **Beamer**: no anima (un PDF no se mueve; el paquete `animate` solo anda en Adobe Reader). **Canva**: diseño duplicado con el informe y el conector se cortó 3 veces en septiembre |
| Plan B | Si el deck no convence, se rehace en **HTML** | — |
| Demo del MVP | En vivo, en el navegador: `https://fraudlens-two.vercel.app` | Incrustarla en el deck obliga a pasarlo a HTML estático y se pierde el editor del artifact |

### Guion propuesto (≈10 min, a confirmar)

| # | Slide | Qué muestra | Fuente |
|---|---|---|---|
| 1 | Portada | Logo, nombre, integrantes | [`identidad/logo/`](../05-producto/identidad/logo/README.md), [`equipo.md`](../00-proyecto/equipo.md) |
| 2 | El problema | Fraude en transacciones, foco fintech y bancos (decisión 0004), Árbol de Problemas | [`problema.md`](../05-producto/problema.md) |
| 3 | Qué aprendimos de los usuarios | Entrevistas A y B, encuesta C (28 respuestas), User Persona y Mapas de Empatía con huecos explícitos | [`user-research.md`](../05-producto/user-research.md), [`usuarios.md`](../05-producto/usuarios.md) |
| 4 | Solución y alcance | Recorte del MVP (decisión 0005), MoSCoW, Story Map | [`alcance-mvp-moscow.md`](../05-producto/alcance-mvp-moscow.md), [`user-story-map.md`](../05-producto/user-story-map.md) |
| 5 | Negocio y competencia | BMC como hipótesis, benchmarking | [`modelo-negocio.md`](../05-producto/modelo-negocio.md), [`benchmarking.md`](../05-producto/benchmarking.md) |
| 6 | **Demo del MVP** | Alta de transacción → decisión de la IA → historial | [`mvp.md`](../05-producto/mvp.md) |
| 7 | Cómo está hecho | Next.js, MongoDB, Groq detrás del contrato `DecisionModel` | [`mvp.md`](../05-producto/mvp.md) |
| 8 | Cómo trabajamos | Repo como centro de cómputos, Trello, 7 decisiones numeradas, 7 análisis de 6 Sombreros, declaración de uso de IA | [`03-decisiones/`](../03-decisiones/), [`analisis/`](../05-producto/analisis/) |
| 9 | Lo que falta y plan al 18/11 | Decisiones abiertas (modelo de IA, stack), Problem Statement, OKR/KPI, P&L | [Bitácora 11/11](../../bitacora/2026-11-11-relevamiento-avance-presentacion.md) |

### Riesgos a preparar

- **La demo (slide 6) no está probada de punta a punta.** Los tests de integración real (MongoDB e IA) se
  saltearon a propósito. Antes de presentar: hacer una evaluación real desde la interfaz.
- Preguntas incómodas probables, con respuesta honesta:
  - CI de `main` en rojo → bloqueo de facturación de GitHub, no el código.
  - Interfaz integrada sin revisión de otro integrante.
  - Groq (implementado) vs. modelo entrenado (decisión 0006); MongoDB (implementado) vs. PostgreSQL (decisión 0007).

### Pendiente de definir

| Qué | Estado |
|---|---|
| Duración real de la exposición | ⬜ supuesto: 10 min |
| Quién presenta cada bloque (rotación de la Clase 1) | ⬜ |

## 2. Informe con la marca (LaTeX)

| Paso | Detalle |
|---|---|
| Capítulos | ⬜ a definir; base: los bloques del [documento entregable](README.md#contenido-del-documento-entregable) |
| Plantilla `.tex` con la marca | Hay que crearla: logo (`identidad/logo/`) y paleta ([`paleta.md`](../05-producto/identidad/paleta.md)). No existe ningún `.tex` en el repo |
| Fuente | Un `.md` armado con los docs del repo |
| Conversión | Skill `md-to-latex`, respetando la plantilla |
| Compilación | MiKTeX local (`pdflatex`, `xelatex`, `latexmk` instalados) |
| Para cuándo | ⬜ (¿documentación final del 18/11?) |

## Orden de trabajo

1. Guion definitivo del deck (confirmar duración y oradores).
2. Deck con `presentacion-viva`.
3. Probar la demo del MVP de punta a punta.
4. Plantilla LaTeX con la marca → informe.
