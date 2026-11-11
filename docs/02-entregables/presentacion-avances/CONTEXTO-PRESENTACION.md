# Presentación «FraudLens — Avances»: contexto para editar

> Equipo FraudLens · Seminario de Gestión Tecnológica (UADE) · 2° Parcial, 2026-11-11
> Fuente de verdad del contenido: los documentos del repo que cita el pie de cada slide. Plan en
> [`../plan-presentacion-avances.md`](../plan-presentacion-avances.md).
> Última actualización: 2026-11-11 (versión 12 del artifact). Armada por MDV con Claude Code.

## 1. Piezas

| Pieza | Dónde | Formato |
|---|---|---|
| Deck (16 slides) | https://claude.ai/artifact/9YuGw3Cw2HDJkb5ncYuWPd | Artifact Slides de claude.ai |
| Guion por slide y reparto | [`guion.md`](guion.md) (mismo texto que las notas del orador) | Markdown |
| Design system | Ninguno instalado: tokens tomados de [`paleta.md`](../../05-producto/identidad/paleta.md) y del [logo](../../05-producto/identidad/logo/README.md) | — |

Impresión: ⬜ sin probar. Exportar el PDF desde el artifact y revisar las slides animadas.

## 2. Deck: estructura

Orden actual (versión 9). `*` = animación en loop.

| Sección | Slides (id) |
|---|---|
| Apertura | 01 `portada`* · 02 `avance`* (del 1° Parcial a hoy) |
| Problema y usuarios | 03 `problema`* · 04 `usuarios`* |
| Evidencia del user research | 05 `research`* · 06 `hallazgos`* |
| Solución, alcance y mercado | 07 `alcance`* · 08 `backlog`* · 09 `mercado`* · 10 `oceano`* · 11 `ux`* |
| El MVP construido | 12 `arquitectura`* · 13 `demo` (captura nativa + demo en vivo) |
| Cómo trabajamos y próximos pasos | 14 `proceso`* · 15 `pendientes`* · 16 `preguntas`* |

Tiempo total de las notas: ≈ 12 min 50 s (⬜ tiempo oficial sin confirmar).

Reparto de oradores (según el historial de aportes, acordado por MDV el 11/11): ML → 1–5 (3:30) ·
FM → 6–8 (2:50) · FGR → 9–12 (3:20) · MDV → 13–15 (3:10) · Todos → 16.

Slide 02 `avance`: compara el estado del 16/9 (según `guia-1er-parcial.md`) con el de hoy. Solo muestra
lo nuevo; lo que ya estaba el 16/9 (entrevistas, benchmarking, BMC, identidad) va en una línea al pie.

Slide 08 `backlog` (pedido de FM): User Flow, Product Backlog y MoSCoW como **propuesta del equipo**,
con lo que falta para cerrarlo. Alcance (06) quedó solo con el User Story Mapping, para no repetir.

Etiquetas de concepto: cada slide de contenido lleva arriba a la izquierda los conceptos de la materia
que aplica (por ejemplo «Árbol de Problemas · 5 Por Qué»). **No llevan número de clase**: la
numeración de los decks no coincide con la del cronograma (P-14) y varias fechas no están confirmadas.

Cambios del 11/11 por feedback del equipo: el stack pasó a definido (MDV); «P&L del modelo de negocio»
pasó a «P&L: costos en horas-hombre e ingresos», porque el BMC sí está hecho; se sumaron las slides
de Océano Azul y UX/UI, las etiquetas de concepto (pedido de FM) y la tarjeta «Registrar
retrospectivas y Sprint Reviews».

### Slides retiradas

| Slide | Retirada | Respaldo | Qué tenía |
|---|---|---|---|
| — | — | — | — |

### Plantilla de slide

Eyebrow violeta en mayúsculas, título de 60 px, logo arriba a la derecha (versión clara u oscura según
el fondo), pie con la fuente a la izquierda y el número escrito a mano a la derecha. Sin isotipo de
fondo: las animaciones ocupan esa zona y lo taparían.

### Estilo (tokens de la marca)

| Rol | Hex |
|---|---|
| Fondo claro / oscuro | `#FAFAFA` / `#0D0D10` |
| Marca sobre claro / sobre oscuro | `#9333EA` / `#C084FC` |
| Violeta profundo (puntos del isotipo) | `#6B21A8` claro · `#7E22CE` oscuro |
| Texto secundario | `#475569` · pies `#64748B` |
| Pendiente (slide 11) | `#FBBF24`, siempre acompañado del texto «pendiente» |

Tipografía: **Inter** (supuesto: `paleta.md` la deja sin decidir entre Inter e IBM Plex Sans). El
wordmark de la portada usa Arial Bold, métricamente igual a Arimo, la fuente del logo. Las animaciones
no cargan fuentes web: muestran Inter solo si está instalada en la notebook; si no, Segoe UI.

### Assets subidos (blob ids)

| Archivo | src |
|---|---|
| Captura del MVP (`fraudlens-two.vercel.app`, 11/11) | `/_blob/9dc6c2b179c247298172f5f3033a27ca` |
| `logo-completo-modo-claro.png` | `/_blob/59270333cb4084ad250e3b45f8500cb7` |
| `logo-completo-modo-oscuro.png` | `/_blob/2d8e9d65c7d20bb93ec727fd4febab93` |
| `isotipo-modo-claro.png` | `/_blob/d63d851e4e87eb0e78aa733aaa160984` (sin usar) |

### Cómo editar el deck

Seguir la skill `presentacion-viva`: estilos inline del subconjunto del formato, embeds opacos con el
fondo de la slide, sin `prefers-reduced-motion`, renumerar los pies con `scripts/renumerar.py` si
cambia el orden, correr `scripts/check_embeds.py` y releer el índice antes de publicar.

## 3. Pendientes

- [ ] Que el equipo revise el deck y el [guion](guion.md), y confirme el reparto
- [ ] Ensayo cronometrado
- [ ] Probar la impresión (PDF del artifact) y revisar cada slide animada
- [ ] Plan B: PDF del deck descargado en la notebook
- [ ] Probar la demo en vivo antes de la clase (slide 9)
- [ ] Instalar Inter en la notebook que presenta (opcional)
