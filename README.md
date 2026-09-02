# FraudLens — Centro de Cómputos

> Repositorio de trabajo, documentación y trazabilidad del Trabajo Integrador Final (TIF/SIP)
> **Seminario de Gestión Tecnológica** — UADE, Lic. en Sistemas — **2C 2026** — Lic. Daniel Britez

---

# 👋 ¿Sos del equipo y es tu primera vez acá? Leé esto

## Qué es este repositorio

Es el **centro de cómputos** del TIF: el lugar donde queda registrado **todo** lo que definimos,
hacemos y decidimos.

**No es el producto final.** El código del MVP (API + modelo + web) vive en otro lado.

Sirve para tres cosas:

| | |
|---|---|
| 📌 **Dejar registro** | Bitácora de sesiones e historial de aportes por integrante |
| 📖 **Consultar** | Glosario, notas de clase, decisiones ya tomadas, cronograma |
| 🧭 **Guiar** | Plantillas, flujo de trabajo y checklist de entregables |

## Arrancar una sesión de trabajo con Claude Code o Codex

**Regla del equipo: toda sesión de trabajo arranca desde un ticket de Trello.**

🗂️ **Tablero:** https://trello.com/b/iUaTi33p/fraudlens-analizador-probabilidad-de-fraude

### ⚠️ Requisito obligatorio: conectá Trello antes de empezar

**No arranques una sesión sin el conector de Trello activo.** Sin él, el asistente no puede leer los
tickets, no puede mover tarjetas y no puede dejar registro de lo que hiciste — y el tablero es
**ítem de evaluación de la materia**.

| Paso | Qué hacer |
|---|---|
| 1 | Entrá a **https://claude.ai/settings/connectors** *(o: claude.ai → avatar → Settings → Connectors)* |
| 2 | Buscá **Trello** y tocá **Connect** |
| 3 | Autorizá con la cuenta de Trello que tenga acceso al tablero |
| 4 | **Activá Trello en el chat**, en el selector de conectores de la conversación |
| 5 | Pedile al asistente que liste los tickets, para confirmar que lo ve |

> 🔑 El paso 4 es el que más se saltea: un conector puede estar **autorizado en la cuenta** pero
> **apagado en el chat**. Si está apagado, el asistente no ve ninguna herramienta de Trello.
>
> Si no sos miembro del tablero todavía, pedile a **FGR** que te invite: sin eso no vas a ver nada
> aunque conectes.

### Los 6 pasos

```bash
# 1. Traer lo último
git pull

# 2. Abrir el asistente en la raíz del repo
claude          # o: codex
```

**3. Leé el tablero y tomá un ticket.** Pegale este arranque al asistente:

```
Leé README.md y CLAUDE.md para tomar contexto.
Después leé docs/00-proyecto/cronograma.md y docs/00-proyecto/preguntas-abiertas.md.

Soy <tu nombre> (<alias: MDV / FGR / ML / FM>).

Listame los tickets del tablero de Trello agrupados por lista, marcando
cuáles están sin dueño y cuáles vencen primero.
```

**4. Asignate el ticket.** Elegí uno de **🎯 Esta semana** o **📥 Backlog**, entrá a la tarjeta en
Trello y dale **Unirme**.

> ⚠️ **Asignarse la tarjeta es obligatorio, no opcional.** El docente evalúa **participación
> individual**, y un tablero donde nadie es dueño de nada no demuestra nada. Además evita que dos
> trabajen lo mismo.
>
> Reglas del tablero:
> - Toda tarjeta fuera del Backlog tiene **una** persona asignada. *"El equipo"* no es un dueño.
> - Máximo **1 o 2 tarjetas por persona** en 🔨 En curso. Si tenés más, no estás trabajando: estás
>   acumulando.
> - Movela a **🔨 En curso** cuando arranques y a **✅ Hecho** cuando termine.
> - Si te trabás, movela a **🚧 Bloqueado** y escribí en la tarjeta **qué** te bloquea y **quién**
>   lo destraba.

**5. Trabajá.** Decile al asistente en qué ticket estás. Ya sabe las reglas del repo porque están
en `CLAUDE.md`.

> 🎩 Si el ticket es una **decisión** (elegir entre opciones, definir alcance), lleva análisis de
> **[6 Sombreros](docs/04-metodologia/seis-sombreros.md)** — es consigna del docente.
> Criterio: *"¿esto se puede hacer mal de más de una manera?"*

**6. Cerrá la sesión:**

- [ ] Lo que definiste quedó escrito en un `.md`
- [ ] Creaste o actualizaste tu archivo del día en [`bitacora/`](bitacora/)
- [ ] Sumaste tu fila en [`registro/historial-aportes.md`](registro/historial-aportes.md)
- [ ] **Moviste la tarjeta en Trello** al estado que corresponde
- [ ] Commiteaste **con tu propio usuario de Git** y pusheaste

> ⚠️ **Commiteá siempre con tu usuario.** El historial por autor (`git log --author="Tu Nombre"`)
> es evidencia de participación individual, y **el docente la evalúa**.
>
> ```bash
> git config user.name "Tu Nombre"
> git config user.email "tu-email@ejemplo.com"
> ```

> 💡 **Sobre `/init`:** no hace falta. Este repo ya tiene un `CLAUDE.md` escrito a mano con las
> reglas del proyecto. Si corrés `/init` lo vas a **pisar** con un resumen automático y peor.
> Si el asistente te propone correrlo, decile que no.

---

## 🔴 Lo que hay que saber ya

| | |
|---|---|
| **Cursada** | Miércoles 18:45 a 22:15 |
| **Próxima clase** | Ver [`cronograma.md`](docs/00-proyecto/cronograma.md) |
| **Clase remota sincrónica** | **Sábado 5/9, 9 a 13 hs** ⚠️ fuera del horario habitual |
| **1° Parcial** | Miércoles **16/9** |
| **2° Parcial** | Miércoles **11/11** |
| **Entrega documentación final** | **18/11** y **2/12** |

📅 Cronograma completo: [`docs/00-proyecto/cronograma.md`](docs/00-proyecto/cronograma.md)

---

## El proyecto en una línea

Prototipo capaz de analizar transacciones en tiempo real y estimar su nivel de riesgo de fraude
mediante un modelo de IA entrenado con datos históricos, para asistir en la decisión de
**aprobar, rechazar o revisar** una operación.

**FraudLens** es el nombre de producto. El título académico de la planilla es
*"Sistema inteligente de detección de fraude en transacciones en tiempo real"*.

📋 Ficha completa: [`docs/00-proyecto/ficha-proyecto.md`](docs/00-proyecto/ficha-proyecto.md)

## El equipo

| Integrante | Legajo | Alias |
|---|---|---|
| Diaz Valdez, Mateo | 1192969 | `MDV` |
| Guerrero Rojas, Francisco Daniel | 1042529 | `FGR` |
| Lewinzon, Mateo | 1151641 | `ML` |
| Molina, Facundo Roman | 1115862 | `FM` |

---

## Mapa del repositorio

| Necesito… | Voy a… |
|---|---|
| Saber qué es el proyecto | [`docs/00-proyecto/ficha-proyecto.md`](docs/00-proyecto/ficha-proyecto.md) |
| **Fechas, parciales, entregas** | [`docs/00-proyecto/cronograma.md`](docs/00-proyecto/cronograma.md) |
| Una definición | [`docs/00-proyecto/glosario.md`](docs/00-proyecto/glosario.md) |
| **Saber qué falta definir** | [`docs/00-proyecto/preguntas-abiertas.md`](docs/00-proyecto/preguntas-abiertas.md) |
| Ver qué se dio en una clase | [`docs/01-clases/`](docs/01-clases/) |
| Ver el deck original del docente | [`docs/01-clases/material/`](docs/01-clases/material/) |
| Saber qué se entrega y cuándo | [`docs/02-entregables/`](docs/02-entregables/) |
| Saber por qué se decidió algo | [`docs/03-decisiones/`](docs/03-decisiones/) |
| Saber cómo trabajamos | [`docs/04-metodologia/flujo-de-trabajo.md`](docs/04-metodologia/flujo-de-trabajo.md) |
| **Analizar una decisión (6 Sombreros)** | [`docs/04-metodologia/seis-sombreros.md`](docs/04-metodologia/seis-sombreros.md) |
| Ver los análisis ya hechos | [`docs/05-producto/analisis/`](docs/05-producto/analisis/) |
| Cómo usamos Trello | [`docs/04-metodologia/trello.md`](docs/04-metodologia/trello.md) |
| **Cómo se crea y se cierra un ticket** | [`docs/04-metodologia/convencion-de-tickets.md`](docs/04-metodologia/convencion-de-tickets.md) |
| El problema, usuarios y producto | [`docs/05-producto/`](docs/05-producto/) |
| Ver qué hizo cada uno | [`registro/historial-aportes.md`](registro/historial-aportes.md) |
| Ver qué se hizo un día | [`bitacora/`](bitacora/) |

---

## Reglas de oro

1. **Si no está en un `.md`, no existe.** Lo que se habló en clase, en un audio o en un mensaje
   suelto tiene que terminar escrito acá.
2. **Cada sesión deja rastro:** bitácora + historial de aportes, en la misma sesión.
3. **Las decisiones se numeran y no se editan.** Para cambiar una vieja, se escribe una nueva que
   la supersede.
4. **No se deduce.** Si falta un dato se pregunta y se deja el hueco marcado `⬜ A definir`.
   Un documento con huecos es útil; uno con datos inventados es un riesgo en una entrega evaluada.
5. **Borrador ≠ definición.** Lo que alguien pasó "para revisar" se guarda marcado como borrador
   hasta que el equipo lo apruebe.
6. **Español** para toda la documentación.

## 🚨 Material de clase: Markdown, nunca PDF

**No subas PDFs.** Son pesados, no tienen diff útil en Git y muchas veces no se les puede extraer
el texto.

👉 Convertí el deck en **https://cloudconvert.com/pdf-to-md** y subí el `.md` a
[`docs/01-clases/material/`](docs/01-clases/material/) como `clase-NN-tema.md`.

---

## Graphify (opcional)

Capa de lectura del repo — [decisión 0002](docs/03-decisiones/0002-graphify-como-capa-de-lectura.md).
**El repo se lee perfectamente sin esto.**

```bash
uv tool install graphifyy   # o: pipx install graphifyy
graphify install
```

Después, desde el asistente: `/graphify .`
(desde la terminal pide API key, porque este repo es sólo documentación).

Detalle: [`docs/04-metodologia/graphify.md`](docs/04-metodologia/graphify.md)
