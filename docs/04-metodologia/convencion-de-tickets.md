# Convención de tickets

Cómo se crea, se etiqueta y se cierra un ticket en el tablero de FraudLens.

🗂️ **Tablero:** https://trello.com/b/iUaTi33p/fraudlens-analizador-probabilidad-de-fraude

> **Por qué existe esta convención:** los tableros de trabajo son **ítem de evaluación de la
> materia**. Un tablero donde cada uno escribe como quiere no se entiende de un vistazo, y no
> demuestra proceso. Con esta convención, cualquiera —incluido el docente— abre una tarjeta y en
> diez segundos sabe de qué se trata, quién la tiene y en qué estado está.

---

## 1. Etiquetas: de qué se trata el ticket

> ⚠️ **PROPUESTA — a confirmar por el equipo.** Ver [P-22](../00-proyecto/preguntas-abiertas.md#p-22).

Cada ticket lleva **exactamente una etiqueta de categoría**. Si dudás entre dos, el ticket
probablemente son dos tickets.

| Color | Etiqueta | Qué incluye | Ejemplos reales del proyecto |
|---|---|---|---|
| 🟣 Violeta | **Negocio** | Decisiones de negocio y de alcance: problema, propuesta de valor, modelo de negocio, BMC, P&L, competencia | *Definir el Problem Statement* · *Business Model Canvas* · *Océano Azul* |
| 🟢 Verde | **Research** | Investigación de usuarios: encuestas, entrevistas, observación, User Persona, Mapa de Empatía, síntesis de hallazgos | *Plan de research* · *User Persona × 3* · *Difundir la encuesta* |
| 🔵 Azul | **Diseño** | Identidad visual, UX/UI, wireframes, user flows, prototipos, Figma | *Identidad visual de FraudLens* · *Prototipo clickeable* |
| 🟡 Amarillo | **Datos & Modelo** | Dataset, features, entrenamiento, métricas del modelo, evaluación | *Elegir el dataset* · *Definir métricas del modelo* |
| 🟠 Naranja | **Código** | Desarrollo del MVP: API, backend, frontend, testing | *Arrancar el repositorio del MVP* · *Endpoint de scoring* |
| 🔴 Rojo | **Entrega** | Lo que se entrega y se evalúa: parciales, Sprint Reviews, documento final, The Pitch | *1° Parcial* · *Entrega documentación final* |
| ⚫ Negro | **Gestión** | Coordinación del equipo y herramientas: tablero, repo, permisos, roles, preguntas al docente | *Sumar integrantes al tablero* · *Definir roles* |

### ¿Y la prioridad?

**La prioridad NO va en etiquetas.** Se lee de dos lugares que ya existen:

- **La lista**: 🎯 Esta semana es más urgente que 📥 Backlog.
- **La fecha de vencimiento**: si tiene fecha, es esa.

Poner prioridad *además* en etiquetas duplica la información y se desactualiza. Las etiquetas
responden **"¿de qué se trata?"**, no **"¿para cuándo?"**.

> ⚠️ **Hoy el tablero usa las etiquetas al revés**: tiene *Prioridad Alta* (roja) y *Prioridad
> Media* (naranja). Si el equipo aprueba esta propuesta, hay que renombrarlas.

---

## 2. Formato del ticket

### Título

```
[Verbo en infinitivo] + [objeto concreto]
```

| ✅ Bien | ❌ Mal |
|---|---|
| `Entrevistar a 5 analistas de fraude` | `User Research` |
| `Elegir el dataset de entrenamiento` | `Dataset` |
| `Definir la paleta de riesgo del dashboard` | `Colores` |

**Sin numerar**, salvo que sean pasos de una misma secuencia con dependencias (como los entregables
de una clase, que van `1.`, `2.`, `3.`).

### Descripción — estas secciones, en este orden

```markdown
## 🎯 Qué hay que hacer
Una o dos frases. Qué se espera que exista cuando esto esté terminado.

## 📋 Contexto
De dónde sale (clase, cronograma, decisión del equipo), y qué hay que saber
para no arrancar de cero.

## ✅ Listo cuando
- [ ] Criterio verificable 1
- [ ] Criterio verificable 2

## 🔗 Links
- Archivo en el repo: docs/...
- Tarjetas relacionadas:

## 🎩 Análisis 6 Sombreros
(sólo si es una decisión — ver más abajo)
```

**Los criterios de "Listo cuando" tienen que ser verificables.** *"Que quede bien"* no es un
criterio. *"3 User Persona con los 3 bloques cada una, cargadas en `usuarios.md`"* sí lo es.

### Responsable

Toda tarjeta fuera de 📥 Backlog tiene **una** persona asignada. *"El equipo"* no es un dueño.

> ⚠️ **El asistente no puede asignar miembros a tarjetas** (limitación del conector de Trello).
> Escribe el responsable en la descripción; **la persona tiene que darle "Unirme" a mano**.

---

## 3. ¿Lleva análisis de 6 Sombreros?

Consigna del docente. Ver [`seis-sombreros.md`](seis-sombreros.md).

| Categoría | ¿Análisis? |
|---|---|
| 🟣 Negocio · 🔵 Diseño · 🟡 Datos & Modelo | ✅ **Casi siempre** — son decisiones |
| 🔴 Entrega | ✅ Sí, si el entregable implica elegir algo |
| 🟢 Research | ⚠️ Depende: *diseñar* el plan sí, *difundir* la encuesta no |
| 🟠 Código · ⚫ Gestión | ❌ Normalmente no — son ejecución |

> Criterio: **"¿esto se puede hacer mal de más de una manera?"**

El análisis va en `docs/05-producto/analisis/6-sombreros-<tema>.md` y **la tarjeta linkea al archivo**.

---

## 4. 🔴 Al cerrar un ticket: el comentario de resolución

**Regla del equipo: ningún ticket se mueve a ✅ Hecho sin un comentario de resolución en Trello.**

No alcanza con dejarlo documentado en el repositorio. **Tiene que estar en las dos partes**:

| Dónde | Qué va | Para qué |
|---|---|---|
| **El repositorio** | El contenido: el documento, la decisión, el análisis | Es la fuente de verdad y alimenta el documento final |
| **El comentario en Trello** | **El proceso**: qué decidiste, qué descartaste y por qué | Es lo que el docente ve al mirar el tablero, y lo que el equipo lee sin abrir el repo |

### Plantilla del comentario

```markdown
## ✅ RESOLUCIÓN — AAAA-MM-DD — <alias>

### Qué se hizo


### Decisiones que tomé y por qué
| Decisión | Alternativas que descarté | Por qué |
|---|---|---|
|  |  |  |

### A qué conclusión llegué


### Qué quedó abierto
- 

### Dónde quedó documentado
- Archivo: `docs/...`
- Commit: `<hash o mensaje>`
```

### Por qué esto importa

El docente evalúa **"cumplimiento del problema-solución"** y **"conocimiento y dedicación demostrado
en el proyecto"**. Un tablero donde las tarjetas pasan a Hecho sin explicación no demuestra ninguna
de las dos cosas.

Y para el equipo: dentro de dos meses, cuando alguien pregunte *"¿por qué habíamos elegido esto?"*,
la respuesta está en el comentario y no en la memoria de quien lo hizo.

> **Las alternativas descartadas son la parte más valiosa.** Se reutilizan tal cual en el documento
> final y en el pitch.

---

## 5. Checklist para crear un ticket

- [ ] Título con **verbo + objeto concreto**
- [ ] **Una** etiqueta de categoría
- [ ] Las secciones de descripción completas
- [ ] Criterios de "Listo cuando" **verificables**
- [ ] Fecha de vencimiento si hay una fecha real
- [ ] Responsable escrito (y asignado a mano en Trello)
- [ ] Link al archivo del repo, si corresponde
- [ ] ¿Es decisión? → análisis de 6 Sombreros linkeado

## 6. Checklist para cerrar un ticket

- [ ] Los criterios de "Listo cuando" están todos cumplidos
- [ ] El contenido quedó en un `.md` del repositorio
- [ ] **Comentario de resolución escrito en la tarjeta de Trello**
- [ ] Bitácora e historial de aportes actualizados
- [ ] Commit pusheado con tu propio usuario de Git
- [ ] Tarjeta movida a ✅ Hecho
