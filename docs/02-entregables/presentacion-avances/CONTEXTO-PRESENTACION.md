# Presentación «FraudLens — Avances»: contexto para editar

> Equipo FraudLens · Seminario de Gestión Tecnológica (UADE) · 2° Parcial, 2026-11-11
> Fuente de verdad del contenido: los documentos del repo que cita el pie de cada slide. Plan en
> [`../plan-presentacion-avances.md`](../plan-presentacion-avances.md).
> Última actualización: 2026-11-11 (versión 6 del artifact). Armada por MDV con Claude Code.

## 1. Piezas

| Pieza | Dónde | Formato |
|---|---|---|
| Deck (12 slides) | https://claude.ai/artifact/9YuGw3Cw2HDJkb5ncYuWPd | Artifact Slides de claude.ai |
| Design system | Ninguno instalado: tokens tomados de [`paleta.md`](../../05-producto/identidad/paleta.md) y del [logo](../../05-producto/identidad/logo/README.md) | — |

Impresión: ⬜ sin probar. Exportar el PDF desde el artifact y revisar las slides animadas.

## 2. Deck: estructura

Orden actual (versión 6). `*` = animación en loop.

| Sección | Slides (id) |
|---|---|
| Apertura | 01 `portada`* |
| Problema y usuarios | 02 `problema`* · 03 `usuarios`* |
| Evidencia del user research | 04 `research`* · 05 `hallazgos`* |
| Solución, alcance y mercado | 06 `alcance`* · 07 `mercado`* |
| El MVP construido | 08 `arquitectura`* · 09 `demo` (captura nativa + demo en vivo) |
| Cómo trabajamos y próximos pasos | 10 `proceso`* · 11 `pendientes`* · 12 `preguntas`* |

Tiempo total de las notas: ≈ 9 min 50 s (supuesto: exposición de 10 min, ⬜ a confirmar).

Reparto de oradores: ⬜ sin definir (la Clase 1 pide rotar).

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

- [ ] Que el equipo revise el deck y acuerde el reparto de oradores
- [ ] Ensayo cronometrado
- [ ] Probar la impresión (PDF del artifact) y revisar cada slide animada
- [ ] Plan B: PDF del deck descargado en la notebook
- [ ] Probar la demo en vivo antes de la clase (slide 9)
- [ ] Instalar Inter en la notebook que presenta (opcional)
