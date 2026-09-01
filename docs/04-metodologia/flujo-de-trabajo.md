# Flujo de trabajo

Cómo trabajamos en este repositorio. Cinco minutos de lectura, y evita que nos pisemos.

## La regla base

> **Si no está en un `.md`, no existe.**

Lo que se habló en clase, en una reunión, en un audio de WhatsApp o en un mensaje suelto tiene que
terminar escrito acá. No importa si está prolijo: importa que esté.

## Ciclo de una sesión de trabajo

Una "sesión" es cualquier rato en que alguien trabaja en el proyecto: una clase, una reunión de
equipo, o dos horas solo un martes a la noche.

1. **Antes de empezar** — `git pull`
2. **Trabajar** — editar los `.md` que corresponda
3. **Registrar** — crear el archivo de bitácora del día (o agregar a uno existente si ya hay uno de hoy)
4. **Sumar el aporte** — una fila en [`registro/historial-aportes.md`](../../registro/historial-aportes.md)
5. **Actualizar Trello** — mover las tarjetas que correspondan
6. **Commitear y pushear**

## Ramas

| Situación | Qué hacer |
|---|---|
| Editar documentación, cargar una clase, sumar bitácora | Directo a `main` |
| Cambio grande que quieras que revisen (reestructurar el repo, redefinir el problema) | Rama `docs/<tema>` + Pull Request |

Para documentación, trabajar directo en `main` es lo más práctico. Los conflictos en Markdown son
fáciles de resolver y no rompen nada.

## Commits

Formato: `<tipo>: <qué cambió>`

| Tipo | Cuándo |
|---|---|
| `clase` | Cargar o actualizar una nota de clase |
| `docs` | Documentación de proyecto, producto o metodología |
| `decision` | Agregar o cambiar el estado de una decisión |
| `bitacora` | Registro de sesión de trabajo |
| `chore` | Estructura, configuración, mantenimiento |

Ejemplos:

```
clase: cargar notas de la Clase 2 - Segmentación de usuarios
docs: definir usuario objetivo de FraudLens
decision: 0003 - dataset de entrenamiento
bitacora: sesion 2026-09-08 - definicion de target
```

> **Commiteá con tu propio usuario de Git.** El historial por autor es parte de la evidencia de
> participación individual, que el docente evalúa.

Configuración por única vez:

```bash
git config user.name "Tu Nombre"
git config user.email "tu-email@ejemplo.com"
```

## Quién hizo qué

Dos registros que se complementan:

| Registro | Qué muestra | Cómo se consulta |
|---|---|---|
| **Historial de Git** | Cambios exactos, automático, no se puede falsear | `git log --author="Nombre" --oneline` |
| **[`registro/historial-aportes.md`](../../registro/historial-aportes.md)** | Aportes que no dejan rastro en Git: presentar en clase, hacer entrevistas, contactar gente, armar el pitch | Se lee directo |

El segundo existe porque **buena parte del trabajo del TIF no pasa por el repositorio**. Si hiciste
tres entrevistas de User Research, eso no aparece en `git log` pero es trabajo del proyecto.

## Cuando hay clase nueva

1. Copiar [`docs/01-clases/_plantilla-clase.md`](../01-clases/_plantilla-clase.md) → `clase-NN-tema.md`
2. Completar el resumen y los conceptos
3. **Completar "Aplicación a FraudLens"** — es la sección que le da sentido a la nota
4. Sumar los términos nuevos al [glosario](../00-proyecto/glosario.md), marcados ✅ con la clase de origen
5. Pasar las tareas de "para la próxima" al Trello
6. Agregar la fila al [índice de clases](../01-clases/README.md)
7. Revisar [`preguntas-abiertas.md`](../00-proyecto/preguntas-abiertas.md): ¿la clase respondió alguna? ¿abrió alguna nueva?

## Cuando hay que decidir algo

Si la charla lleva más de diez minutos o afecta el rumbo del proyecto, se registra:

1. Copiar [`docs/03-decisiones/_plantilla-decision.md`](../03-decisiones/_plantilla-decision.md)
2. Numerarla correlativa: `0003-...`, `0004-...`
3. Anotar **las alternativas que descartamos y por qué** — esa parte se reutiliza tal cual en el
   documento entregable y en el pitch
4. Agregarla al [índice de decisiones](../03-decisiones/README.md)

## Cuando aparece una duda

Va a [`preguntas-abiertas.md`](../00-proyecto/preguntas-abiertas.md) con un ID (`P-11`, `P-12`…),
prioridad y a quién hay que preguntarle. Cuando se responde: se marca resuelta y se escribe la
respuesta. Si la respuesta cambia el rumbo, además se registra como decisión.

## Antes de cada entrega

Checklist completo en [`docs/02-entregables/README.md`](../02-entregables/README.md#checklist-previo-a-cada-entrega).
