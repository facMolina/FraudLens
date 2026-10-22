# Wireframes de FraudLens

> **Estado:** 🟡 En curso — 1 de 9 pantallas hecha. **Borrador de MDV, sin revisar por el equipo.**
> **Autor:** Mateo Diaz Valdez (MDV), con Claude Code y el conector de Figma. Iniciado el 2026-10-21.
> **Figma:** [01 · Panel de control](https://www.figma.com/design/5m4zALoaJXwDa2TkXjbEOb/Sin-t%C3%ADtulo?node-id=7-141)
> **Tarjeta de Trello relacionada:** [Crear Wireframes y mockups con diseños](https://trello.com/c/wtVScuzd) *(en 📥 Backlog, sin dueño a la fecha)*

## Para qué son

Son wireframes **de concepto**: muestran la estructura de cada pantalla (qué bloques hay y dónde
van), no el diseño final. MDV lo pidió así: *"es para mostrar el concepto de wireframe, no es para
aplicación práctica"*. El cronograma pone Wireframes en la clase del 21/10 (Taller UX/UI, ver
[`cronograma.md`](../00-proyecto/cronograma.md)).

## Criterios *(pedido de MDV)*

| Criterio | Valor |
|---|---|
| Fidelidad | **Baja (low-fi).** Cajas, rayas grises en lugar de texto y una X donde va una imagen o un mapa. Solo llevan palabras los títulos, el menú, los botones y los nombres de las secciones |
| Formato | **Desktop first**, ancho 1440 px, **sin versión responsive** |
| Colores | Blanco, negro y gris. Sin paleta de marca ni sombras |
| Idioma | Español, con los textos de la traducción del prototipo (`es-419.json`) |
| Ritmo | Una pantalla a la vez, empezando por las que mejor explican el sitio |

## De dónde sale cada cosa *(distinguir fuentes)*

- **Qué hay en cada pantalla y en qué orden:** del código del frontend web del
  [prototipo de FGR](prototipo.md) (`Frontend/src/App.jsx`, `Auth.jsx`, `Administration.jsx`,
  `Heatmap.jsx`), en el commit `99386f5` de `main`. La app móvil no se usó.
- **El estilo low-fi** (rayas, cajas con X, grises): elección de Claude Code dentro del pedido de
  MDV. **No viene del docente**: el material de la clase del 21/10 no está cargado en el repo.

## Pantallas

| # | Pantalla | Qué muestra | Estado |
|---|---|---|---|
| 01 | **Panel de control** | Barra de sesión, menú lateral, 4 métricas, tabla de transacciones recientes con filtros y paginación, mapa de riesgo | ✅ [Hecha](https://www.figma.com/design/5m4zALoaJXwDa2TkXjbEOb/Sin-t%C3%ADtulo?node-id=7-141) |
| 02 | Detalle de una transacción | Panel a la derecha: decisión, puntaje, factores de riesgo, datos, revisión humana, caso de fraude | 🔲 Siguiente |
| 03 | Nueva transacción | Modal con el formulario para analizar una transacción | 🔲 |
| 04 | Transacciones | Tabla completa con paginación | 🔲 |
| 05 | Reglas y umbrales | Modal: regla de monto mínimo y umbrales de revisión y bloqueo | 🔲 |
| 06 | Inicio de sesión | Correo, contraseña, idioma y tema | 🔲 |
| 07 | Elegir organización | Estado vacío cuando no hay organización activa | 🔲 |
| 08 | Administración | Organizaciones, miembros, reporte e historial | 🔲 |
| 09 | Ayuda | Modal con las indicaciones de uso | 🔲 |

El orden es una propuesta de Claude Code: primero lo que explica el producto (monitorear, ver por qué
una transacción es riesgosa, cargar una), después lo de soporte.

## Para revisar en equipo *(no son decisiones)*

1. **Los wireframes copian el prototipo, no el MVP.** El prototipo trae cosas que la
   [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md) sacó del MVP (varias organizaciones,
   roles, Administración). Hay que contrastar cada pantalla con la lista "NO MVP" de
   [`problema.md`](problema.md) antes de usarlas en una entrega.
2. **El archivo de Figma se llama "Sin título"** y es de la cuenta de MDV. Hay que renombrarlo y
   compartirlo con el equipo para que lo puedan abrir.
3. **Falta cargar el material de la clase del 21/10** (Taller UX/UI) para ver si el docente pidió un
   formato de wireframe en particular.
