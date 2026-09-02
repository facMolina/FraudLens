# Trello

🗂️ **Tablero:** https://trello.com/b/iUaTi33p/fraudlens-analizador-probabilidad-de-fraude

## Por qué importa

Los **tableros de trabajo (Trello/Jira)** son un ítem explícito de evaluación de la materia. Un
tablero desordenado, con tarjetas sin dueño o listas abandonadas, resta nota. Un tablero prolijo es
evidencia de gestión.

## Estado

✅ **Tablero limpiado y rearmado el 2026-09-02.** Venía siendo la plantilla Kanban de Trello sin
tocar: 6 listas en inglés y 14 tarjetas de ejemplo (*"Feature ABC"*, *"Task 123"*, las tarjetas
`💬 Move a card to this stage…`).

Se archivaron las 14 tarjetas de plantilla (archivar es reversible), se renombraron las listas al
español y se cargaron las tarjetas reales del proyecto.

## Listas

| Lista | Qué contiene | Regla |
|---|---|---|
| **📥 Backlog** | Todo lo que hay que hacer en algún momento | Sin fecha ni dueño obligatorios |
| **🎯 Esta semana** | Comprometido para la clase de esta semana | **Toda tarjeta tiene dueño y fecha** |
| **🔨 En curso** | Se está trabajando ahora | Máximo 1-2 tarjetas por persona |
| **👀 En revisión** | Terminado, esperando que otro lo mire | Se asigna al revisor |
| **🚧 Bloqueado** | No se puede avanzar | La tarjeta dice **qué** lo bloquea y **quién** lo destraba |
| **✅ Hecho** | Terminado y revisado | |

## Etiquetas

El tablero tiene dos etiquetas con nombre, que usamos como prioridad:

| Etiqueta | Cuándo |
|---|---|
| 🔴 **Prioridad Alta** | Entregable de clase, parcial, o algo que bloquea a otros |
| 🟠 **Prioridad Media** | Importante pero no bloqueante |

Hay 4 etiquetas más sin nombre (verde, violeta, azul, amarilla) disponibles si el equipo quiere
sumar categorías por tipo de trabajo.

## ⚠️ Miembros del tablero

**Hoy el tablero tiene un solo miembro: Francisco Guerrero.**

Los tableros son ítem de evaluación, y con un solo miembro **no se puede demostrar la participación
individual de nadie más**. Hay que sumar a MDV, ML y FM, y asignar dueño a cada tarjeta que esté
fuera del Backlog.

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

## Cómo conectar Trello a Claude

Para que el asistente pueda **leer, crear, actualizar y mover tarjetas**, hay que conectar Trello
a la cuenta de claude.ai. El conector existe en el directorio oficial de Anthropic; sólo falta
activarlo.

### Pasos

1. Entrá a **https://claude.ai/settings/connectors** *(o: claude.ai → tu avatar → Settings → Connectors)*.
2. Buscá **Trello** en el directorio de conectores y tocá **Connect**.
3. Se abre la ventana de autorización de Atlassian/Trello. Iniciá sesión con la cuenta que tiene
   acceso al tablero y **aceptá los permisos**.
4. Volvé a la conversación con Claude y **activá Trello para ese chat**: en el selector de
   herramientas/conectores del chat, tildá Trello.
5. Avisale al asistente que ya está conectado, para que lo verifique.

> ⚠️ Los pasos 4 y 5 importan: un conector puede estar **autorizado a nivel cuenta** pero
> **apagado en el chat**. Si está apagado, el asistente no ve ninguna herramienta de Trello.

### Importante sobre la cuenta

El conector opera **con los permisos del usuario que autorizó**.

> ✅ **En nuestro caso:** el tablero lo creó **Francisco (FGR)**, pero **Facundo (FM) es admin**.
> Con eso alcanza: FM puede conectar desde su propia cuenta y el asistente va a ver el tablero
> con permisos de administrador.

### Qué va a poder hacer una vez conectado

Leer tableros, listas, tarjetas, checklists y miembros; y crear, actualizar y mover tarjetas.

### Mientras tanto

Sin el conector, el asistente **no puede ver el tablero**. Las opciones son pegarle el contenido en
el chat, o dejar los tickets redactados en Markdown para cargarlos a mano.

Ver [P-09](../00-proyecto/preguntas-abiertas.md#p-09).
