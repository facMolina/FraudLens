# Guía para la oral del 1° Parcial (16/9)

> Uso: consulta rápida durante la presentación. Un ítem por sección, con el estado real y el
> link al archivo del repo. Si el docente pregunta algo puntual, acá está la respuesta y de dónde
> sale — no hay que buscarla en vivo.
> Armada por FM (con Claude Code) el mismo día del parcial, con el estado del repo a esa fecha.
> Referencia: tarjeta [🔴 1° PARCIAL](https://trello.com/c/3w2I0Een) en Trello.

Leyenda: ✅ listo · 🟡 parcial/en curso · 🔴 no empezado o hueco real.

---

## 1. Repositorio, con carpetas organizado ✅

`github.com/facMolina/FraudLens` — es el **centro de cómputos** del proyecto (decisión
[0001](../03-decisiones/0001-repo-como-centro-de-computos.md)), no el código del MVP.

Estructura: `docs/00-proyecto` (equipo, cronograma, preguntas abiertas) · `docs/01-clases` (notas
de cada clase) · `docs/02-entregables` (calendario y estado) · `docs/03-decisiones` (decisiones
numeradas) · `docs/04-metodologia` (cómo trabajamos) · `docs/05-producto` (problema, usuarios,
research, negocio) · `bitacora/` (registro día a día) · `registro/` (historial de aportes).

## 2. Kanban, con actividades ya iniciadas ✅

Tablero: https://trello.com/b/iUaTi33p — 4 integrantes sumados, tarjetas organizadas en 5 listas
(Backlog, Esta semana, En curso, En revisión, Bloqueado, Hecho), varias ya en Hecho o En curso.
Hoy quedó reordenado contra esta misma consigna del docente.

## 3. Documento de equipo (nombre, legajos, tareas, qué hace, a qué apunta) ✅

- **Nombre:** [`ficha-proyecto.md`](ficha-proyecto.md) — FraudLens (marca) / "Sistema inteligente
  de detección de fraude en transacciones en tiempo real" (título académico de la planilla).
- **Integrantes + legajo + rol:** [`equipo.md`](equipo.md) — tabla con los 4, roles asignados y
  justificados (ML: referente de producto, FGR: referente técnico, FM: referente de
  documentación, MDV: referente de proceso).
- **Qué hace / a qué apunta:** `ficha-proyecto.md` — sección "Problema / necesidad / oportunidad"
  y "Objetivo del proyecto": complementar (no reemplazar) las reglas de detección de fraude
  existentes con un modelo de IA que asiste al analista.

## 4. Declaración de uso de IA ✅

[`declaracion-uso-ia.md`](declaracion-uso-ia.md) — armada en base a los Lineamientos de Uso de IA
de la UADE (sección TIF/TFI/PFI). Cubre herramientas por persona, alcance por etapa, procesos de
validación (regla de no deducir, sombrero rojo siempre del equipo, decisiones numeradas,
`Co-Authored-By` en cada commit) y responsabilidad sobre el contenido.

## 5. Stakeholders, clientes, profesionales, expertos consultados 🟡

[`usuarios.md`](../05-producto/usuarios.md) — 3 perfiles con investigación real:

- **Perfil A · Analista de fraude** — ✅ entrevistado: **Nicolás**.
- **Perfil B · Analista de producto** (fintech/banco) — ✅ entrevistado: **Agustín**.
- **Perfil C · Usuario final** (fintech/billetera/pasarela) — encuesta difundida.

🟡 Falta: recopilar y analizar las respuestas de la encuesta del Perfil C.

## 6. Encuestas 🟡

[`user-research.md`](../05-producto/user-research.md#encuesta--perfil-c-usuario-final-de-fintechbilleterapasarela) —
7 preguntas, buenas prácticas de la Clase 4 aplicadas (sin preguntas inductivas, opción "Otros"
y "NS/NC", anonimizada). **Difundida:** https://forms.gle/ZLfhijskphLA1Fxu9
🟡 Respuestas y análisis: pendientes de recopilar.

## 7. Entrevistas ✅

[`user-research.md`](../05-producto/user-research.md#resultados-preliminares-de-entrevistas) — 2
entrevistas reales ejecutadas y analizadas:

- **Nicolás** (Perfil A): dolor principal es información dispersa entre herramientas; falsos
  positivos y falta de explicabilidad en las alertas; pide una vista unificada del caso.
- **Agustín** (Perfil B): mide éxito en pérdidas/falsos positivos/tiempo de resolución/confianza;
  pide explicabilidad, simulación de cambios y un panel configurable por perfil.
- Síntesis: ambos coinciden en reducir falsos positivos, explicar las alertas y centralizar
  información.

## 8. Investigaciones ✅

- **Benchmarking / Océano Azul:** [`benchmarking.md`](../05-producto/benchmarking.md) —
  competidores reales (ClearSale, Signifyd, Riskified), curva de valor, diferenciación.
- **Árbol de Problemas y 5 Por Qué:** [`problema.md`](../05-producto/problema.md) — causa raíz
  citando normativa BCRA (Comunicaciones "A" 8471/8473) sobre gestión de riesgo de fraude.
- **Ideación:** [`ideacion.md`](../05-producto/ideacion.md) — ERRC + grilla de priorización.

## 9. Estudio de plataformas/herramientas para el MVP ✅

[`datos.md`](../05-producto/datos.md) — decisión [0006](../03-decisiones/0006-tres-datasets-para-el-modelo.md):
**3 datasets de Kaggle**, cada uno con un rol distinto:

1. **Entrenamiento** — [Credit Card Fraud Detection Dataset 2023](https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023) (real, anonimizado, etiquetado).
2. **Validación y explicabilidad** — [dataset de miadul](https://www.kaggle.com/datasets/miadul/credit-card-fraud-detection-dataset) (sintético, sin anonimizar).
3. **Test final** — [dataset de kartik2112](https://www.kaggle.com/datasets/kartik2112/fraud-detection) (hold-out, nunca visto por el modelo).

🟡 Falta cerrar antes del documento final: registros exactos y licencia de los datasets 1 y 2
(bloqueado por un reCAPTCHA de Kaggle a mitad de la investigación).

## 10. Logo, imagen de marca ✅

[`identidad/propuesta-canva.md`](../05-producto/identidad/propuesta-canva.md) — Opción elegida:
**"Anomalía en grilla"** (grilla de puntos violeta con una irregularidad resaltada — metáfora
directa de detectar fraude). Assets PNG en [`identidad/logo/`](../05-producto/identidad/logo/):
isotipo, logo completo con wordmark, favicon, en modo claro y oscuro.
Presentación completa: [Canva, 17 páginas](https://canva.link/s167eweo67bw2la).

## 11. Estudio de colores ✅

[`identidad/paleta.md`](../05-producto/identidad/paleta.md) — violeta como color de marca
(`#9333EA` modo claro / `#A855F7` modo oscuro), **contrastes medidos con fórmula WCAG** (no
estimados), escala de riesgo con valores distintos para modo claro y oscuro.

## 12. Carpeta con el proyecto, si ya hay código 🔴

**Hueco real, hay que decirlo así.** FGR armó un **prototipo** (no el MVP): backend con Claude,
frontend con Codex, sobre el notebook de Kaggle [*Fraud Detection Full Project in
Spanish*](https://www.kaggle.com/code/carmencastrogonzlez/fraud-detection-full-project-in-spanish)
(`carmencastrogonzlez`), citado. Ver [`prototipo.md`](../05-producto/prototipo.md).

No está en un repo propio todavía, ni linkeado. Discurso sugerido: *"Existe un prototipo de
validación técnica sobre un dataset y un notebook público citados; el repositorio del MVP en sí
arranca recién el 7/10 según el cronograma, después de cerrar el alcance con el User Research."*
Decisión [0005](../03-decisiones/0005-recorte-alcance-mvp.md) — el MVP es explícitamente una
**simulación**, no el sistema final.

## 13. Modelos de IA, si se utilizarán ✅

Tarjeta [Modelos de IA a utilizar](https://trello.com/c/HgigLF8C). Estrategia definida en
[`problema.md`](../05-producto/problema.md) (Árbol de Problemas, punto 4 del 5 Por Qué): el modelo
**asiste** al analista con hipótesis para crear reglas nuevas o detectar posibles casos de
fraude — **no reemplaza su criterio**. Tipo de modelo y métricas concretas: 🟡 pendiente, recién
posible después de mapear qué requerimiento cubre cada uno de los 3 datasets (`datos.md`).

## 14. Modelo de negocio — sostenibilidad y crecimiento ✅

[`modelo-negocio.md`](../05-producto/modelo-negocio.md) — Business Model Canvas completo (9
bloques), marcado explícitamente qué es hipótesis y qué está confirmado. Ingresos: suscripción/
licencia (no garantía financiera, para diferenciarse de ClearSale/Signifyd/Riskified). Sección
"Cómo crece con el tiempo" cubre escalabilidad.
🟡 Falta el **P&L** (Profit & Loss, en Horas-Hombre) — pendiente para la próxima clase, no crítico
para hoy.

## 15. Líneas futuras / próximas versiones ✅

[`problema.md` — Líneas futuras / próximas versiones](../05-producto/problema.md#líneas-futuras--próximas-versiones):
reentrenamiento automático, multi-tenant, alertas, panel de administración completo,
integraciones reales, explicabilidad avanzada, cobertura AML + fraude (hallazgo del
benchmarking), verificar la hipótesis "complementa, no reemplaza" con el research.

## 16. Otros documentos que complementan el MVP ✅

- [`requerimientos-funcionales-mvp.md`](../05-producto/requerimientos-funcionales-mvp.md) — casos
  de uso del MVP (borrador de ML, revisado en equipo).
- [`glosario.md`](glosario.md) — términos de la materia y del proyecto.
- [`preguntas-abiertas.md`](preguntas-abiertas.md) — lo que el equipo marca explícitamente como
  sin definir, en vez de inventarlo.
- [`03-decisiones/`](../03-decisiones/) — 6 decisiones numeradas, con contexto y alternativas
  descartadas.
- [`analisis/6-sombreros-usuario-objetivo.md`](../05-producto/analisis/6-sombreros-usuario-objetivo.md)
  y [`analisis/6-sombreros-enfoque-fintech.md`](../05-producto/analisis/6-sombreros-enfoque-fintech.md)
  — 🟡 sombrero rojo con la voz de MDV cargada, falta FGR, ML y FM.

---

## Si preguntan por los huecos, la respuesta honesta es

- **Código del MVP:** no existe como repo propio — hay un prototipo de validación técnica,
  citado, y el MVP real arranca el 7/10 por decisión de alcance.
- **Encuesta del Perfil C:** difundida, respuestas todavía sin recopilar.
- **Sombrero rojo:** parcialmente escrito (MDV), falta el resto del equipo — es la única sección
  del proyecto que la reglas del repo dicen que no puede escribir una IA.
- **P&L:** pendiente, para la próxima clase.

No hay datos inventados en ningún bloque — donde falta algo, el repo lo marca explícito.
