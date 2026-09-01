# Trello

🗂️ **Tablero:** https://trello.com/b/iUaTi33p/fraudlens-analizador-probabilidad-de-fraude

## Por qué importa

Los **tableros de trabajo (Trello/Jira)** son un ítem explícito de evaluación de la materia. Un
tablero desordenado, con tarjetas sin dueño o listas abandonadas, resta nota. Un tablero prolijo es
evidencia de gestión.

## Estado

> ⚠️ Esta página describe una **propuesta** de organización. Falta contrastarla contra cómo está
> armado hoy el tablero y ajustarla. Ver [P-09](../00-proyecto/preguntas-abiertas.md#p-09).

## Propuesta de listas

| Lista | Qué contiene | Regla |
|---|---|---|
| **📥 Backlog** | Todo lo que hay que hacer en algún momento | Sin fecha ni dueño obligatorios |
| **🎯 Sprint actual** | Comprometido para el sprint en curso | **Toda tarjeta tiene dueño y fecha** |
| **🔨 En curso** | Se está trabajando ahora | Máximo 1-2 tarjetas por persona |
| **👀 En revisión** | Terminado, esperando que otro lo mire | Se asigna al revisor |
| **✅ Hecho** | Terminado y revisado | Se archiva al cerrar cada sprint |
| **🚧 Bloqueado** | No se puede avanzar | La tarjeta dice **qué** lo bloquea y **quién** lo destraba |

## Etiquetas

| Etiqueta | Para qué |
|---|---|
| 🔴 `Entrega` | Tarea que forma parte de una instancia evaluable |
| 🟠 `Documentación` | Escribir o actualizar documentos del TIF |
| 🟡 `User Research` | Encuestas, entrevistas, observación, análisis |
| 🟢 `Producto` | Definición de producto, UX/UI, prototipos |
| 🔵 `Desarrollo` | Código del MVP (API, modelo, web) |
| 🟣 `Clase` | Preparar algo puntual para la próxima clase |
| ⚫ `Gestión` | Coordinación, reuniones, tablero, repositorio |

## Convención de tarjetas

**Título:** verbo + objeto concreto.

✅ `Entrevistar a analista de fraude de fintech`
❌ `User Research`

**Descripción** — cada tarjeta debería tener:

```
## Qué hay que hacer
...

## Cómo sabemos que está listo
- [ ] ...

## Links
- Documento en el repo: docs/...
```

**Dueño:** toda tarjeta fuera del Backlog tiene **una** persona asignada. "El equipo" no es un dueño.

## Relación con este repositorio

Las dos herramientas se complementan y **se linkean entre sí**:

| | Trello | Repositorio |
|---|---|---|
| **Para qué** | Qué hay que hacer, quién y para cuándo | Qué definimos y por qué |
| **Vida útil** | La tarjeta se archiva al terminar | Queda para siempre |
| **Ejemplo** | Tarjeta *"Definir usuario objetivo"* | Documento `docs/05-producto/usuarios.md` |

**Regla:** cuando una tarjeta produce una definición, la definición va al repositorio y la tarjeta
linkea al archivo. Cuando un documento genera trabajo, se abre la tarjeta y el documento la linkea.

## Acceso desde Claude

Para que el asistente pueda leer, crear, actualizar y mover tarjetas hace falta habilitar el
**conector de Trello** en claude.ai (Configuración → Conectores) y activarlo en la conversación.
Sin eso, el asistente puede ver el tablero sólo si alguien le pega el contenido.

Ver [P-09](../00-proyecto/preguntas-abiertas.md#p-09).
