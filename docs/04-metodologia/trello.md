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

## Etiquetas, formato de tarjeta y cierre

👉 Todo eso vive en **[`convencion-de-tickets.md`](convencion-de-tickets.md)**:

- Las **7 etiquetas de categoría** (Negocio · Research · Diseño · Datos & Modelo · Código · Entrega · Gestión)
- El **formato de título y descripción** de una tarjeta
- Cuándo lleva **análisis de 6 Sombreros**
- El **comentario de resolución obligatorio** al cerrar

> 🔴 **Regla clave:** ningún ticket pasa a ✅ Hecho sin un **comentario de resolución** en Trello que
> explique qué se decidió, qué se descartó y por qué. No alcanza con documentarlo en el repo:
> tiene que estar **en los dos lugares**.

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

Leer tableros, listas, tarjetas, checklists y miembros; y crear, actualizar, mover y archivar
tarjetas, poner vencimientos y etiquetas.

### ⚠️ Lo que NO puede hacer

Tres cosas que el conector **no** permite y que hay que hacer a mano en Trello:

| No puede | Consecuencia |
|---|---|
| **Asignar miembros a tarjetas** | El responsable queda escrito en la descripción; la persona tiene que darle **"Unirme"** |
| **Crear o renombrar etiquetas** | Las 7 etiquetas de categoría hay que crearlas a mano una vez |
| **Editar la descripción del tablero** | Hoy sigue con el texto de la plantilla *"Amazing Kanban"* en inglés — hay que reemplazarlo a mano |

### 🔴 Es requisito para trabajar, no una comodidad

**Ninguna sesión de trabajo arranca sin el conector activo.** Sin él el asistente no ve los tickets,
no puede mover tarjetas y no queda registro de lo que hiciste. Y el tablero es **ítem de
evaluación**.

### Mientras tanto

Sin el conector, el asistente **no puede ver el tablero**. Las opciones son pegarle el contenido en
el chat, o dejar los tickets redactados en Markdown para cargarlos a mano.

Ver [P-09](../00-proyecto/preguntas-abiertas.md#p-09).
