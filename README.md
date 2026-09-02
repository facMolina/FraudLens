# FraudLens — Centro de Cómputos

> Repositorio de trabajo, documentación y trazabilidad del Trabajo Integrador Final (TIF/SIP)
> de la materia **Seminario de Gestión Tecnológica** — UADE, Licenciatura en Sistemas — 2C 2026.

## ¿Qué es este repositorio?

Este repositorio **no es el producto final**. Es el **centro de cómputos** del equipo: el lugar
donde queda registrado todo lo que definimos, todo lo que hacemos y todo lo que decidimos.

Sirve para tres cosas:

1. **Dejar registro** — bitácora de sesiones de trabajo e historial de aportes por integrante.
2. **Consultar definiciones** — glosario, conceptos de cada clase y decisiones ya tomadas.
3. **Guiar el armado** — plantillas, flujo de trabajo y checklist de entregables.

El código del MVP (API + modelo de detección de fraude + interfaz web) vivirá en un
repositorio aparte. Ver [`docs/00-proyecto/preguntas-abiertas.md`](docs/00-proyecto/preguntas-abiertas.md).

## El proyecto en una línea

Prototipo capaz de analizar transacciones en tiempo real y estimar su nivel de riesgo de fraude
mediante un modelo de IA entrenado con datos históricos, para asistir en la decisión de
**aprobar, rechazar o revisar** una operación.

📋 Ficha completa: [`docs/00-proyecto/ficha-proyecto.md`](docs/00-proyecto/ficha-proyecto.md)
🗂️ Tablero Trello: https://trello.com/b/iUaTi33p/fraudlens-analizador-probabilidad-de-fraude

## Mapa del repositorio

| Carpeta | Qué contiene | Cuándo la usás |
|---|---|---|
| [`docs/00-proyecto/`](docs/00-proyecto/) | Ficha, equipo, materia, glosario y preguntas abiertas | Para saber "qué es esto" y "quién es quién" |
| [`docs/01-clases/`](docs/01-clases/) | Una nota por clase: resumen, conceptos y cómo se aplican a FraudLens | Cada vez que hay clase nueva |
| [`docs/01-clases/material/`](docs/01-clases/material/) | El deck del docente convertido a Markdown, tal cual | Para chequear la fuente original |
| [`docs/02-entregables/`](docs/02-entregables/) | Qué se entrega, cuándo y en qué estado está | Antes de cada entrega o Sprint Review |
| [`docs/03-decisiones/`](docs/03-decisiones/) | Decisiones del equipo, numeradas y con contexto | Cuando discutimos algo y hay que fijarlo |
| [`docs/04-metodologia/`](docs/04-metodologia/) | Cómo trabajamos: flujo, Trello, Graphify | Para arrancar o si tenés dudas de proceso |
| [`docs/05-producto/`](docs/05-producto/) | Definición del problema, usuarios, solución y producto | A medida que avanzamos con el MVP |
| [`bitacora/`](bitacora/) | Un archivo por sesión de trabajo | Cada vez que trabajamos |
| [`registro/`](registro/) | Historial de aportes por integrante | Se actualiza junto con la bitácora |

## Cómo arrancar (primera vez)

```bash
git clone <url-del-repo>
cd FraudLens
```

1. Leé este README.
2. Leé [`docs/04-metodologia/flujo-de-trabajo.md`](docs/04-metodologia/flujo-de-trabajo.md) — son 5 minutos y evita pisarnos.
3. Mirá [`docs/00-proyecto/preguntas-abiertas.md`](docs/00-proyecto/preguntas-abiertas.md) para ver qué falta definir.

Opcional pero recomendado — grafo de navegación con Graphify:

```bash
uv tool install graphifyy   # o: pipx install graphifyy
graphify install
```

Después se construye el grafo desde el asistente con `/graphify .`
(desde la terminal hace falta una API key, porque este repo es sólo documentación).

Detalle en [`docs/04-metodologia/graphify.md`](docs/04-metodologia/graphify.md).

## Reglas de oro

- **Todo lo que definimos, se documenta acá.** Si se habló en clase, en Discord o en un audio y no quedó en un `.md`, no existe.
- **Un archivo de bitácora por sesión de trabajo**, y actualizar el historial de aportes en la misma sesión.
- **Las decisiones se numeran** (`docs/03-decisiones/`). No se editan las viejas: se supersede con una nueva.
- **Español** para toda la documentación.
- **No se deduce.** Si falta un dato se pregunta y se deja el hueco marcado. Un documento con
  `⬜ A definir` es útil; uno con datos inventados es un riesgo en una entrega evaluada.

## 🚨 Material de clase: Markdown, no PDF

**No subas PDFs.** Convertí el deck acá 👉 **https://cloudconvert.com/pdf-to-md** y subí el `.md`
a [`docs/01-clases/material/`](docs/01-clases/material/) como `clase-NN-tema.md`.
