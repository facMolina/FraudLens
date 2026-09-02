# Paleta de FraudLens — valores verificados

| | |
|---|---|
| **Color de marca** | 🟣 **Violeta** — decidido por FM el 2026-09-02 |
| **Modos** | Claro y oscuro |
| **Estado** | 🟡 Propuesta técnica — el equipo y el docente aprueban |

> Todos los contrastes están **medidos con la fórmula WCAG**, no estimados.
> Mínimos: **4.5** para texto normal · **3.0** para texto grande e iconos.

---

## Fondos

| Rol | Modo claro | Modo oscuro |
|---|---|---|
| Fondo de página | `#FAFAFA` | `#0D0D10` |
| Fondo de panel | `#FFFFFF` | `#16161A` *(a definir)* |

## Color de marca — violeta

| Uso | Hex | Contraste | ✓ |
|---|---|---|---|
| Marca sobre **fondo claro** | `#9333EA` | 5.16 | ✅ |
| Marca sobre **fondo oscuro** | `#A855F7` | 4.90 | ✅ |
| Texto blanco sobre botón violeta `#9333EA` | `#FFFFFF` | 5.38 | ✅ |

> ⚠️ **Ojo:** `#9333EA` sobre fondo oscuro da **3.61** — alcanza para iconos y texto grande, pero
> **no para texto normal**. Por eso en modo oscuro la marca sube a `#A855F7`.
>
> Es el tipo de detalle que separa un dashboard que se lee de uno que cansa la vista a las dos horas.

## Escala de riesgo

**Cada modo necesita valores distintos.** Los colores vivos que funcionan sobre fondo oscuro
fracasan sobre fondo claro.

| Nivel | Modo oscuro | Contraste | Modo claro | Contraste |
|---|---|---|---|---|
| 🟢 **LOW** | `#16A34A` | 5.89 ✅ | `#15803D` | 4.81 ✅ |
| 🟡 **MEDIUM** | `#FBBF24` | 11.62 ✅ | `#B45309` | 4.81 ✅ |
| 🟠 **HIGH** | `#F97316` | 6.92 ✅ | `#C2410C` | 4.96 ✅ |
| 🔴 **CRITICAL** | `#DC2626` | 4.02 ⚠️ | `#B91C1C` | 6.20 ✅ |

### Por qué cambian los valores en modo claro

| Nivel | El valor "vivo" sobre claro | Problema |
|---|---|---|
| MEDIUM `#FBBF24` | **1.60** | Amarillo sobre blanco es prácticamente invisible |
| HIGH `#F97316` | **2.69** | Insuficiente incluso para iconos |
| LOW `#16A34A` | **3.16** | Sirve para iconos, no para texto |

⚠️ **CRITICAL en modo oscuro** (`#DC2626`, 4.02) queda por debajo del mínimo para texto normal.
Sirve para el chip y el icono. Si se va a usar como **texto**, hay que aclarar el tono.

## 🔴 Regla no negociable: el color nunca va solo

Cerca del **8% de los varones** tiene alguna forma de daltonismo, y el eje **rojo-verde** es
justamente el más afectado — que es exactamente nuestra escala.

**Todo estado de riesgo se comunica con color + una forma distinta.** El mockup claro que generamos
ya lo hace bien:

| Nivel | Color | + Forma |
|---|---|---|
| LOW | verde | ✓ círculo con check |
| MEDIUM | ámbar | ⚠ triángulo |
| HIGH | naranja | ◆ rombo |
| CRITICAL | rojo | ● círculo lleno |

**Prueba de verdad:** poné una captura del dashboard en escala de grises. Si seguís sabiendo cuál
es crítica, la paleta funciona. Si no, no.

## Neutros

| Rol | Hex |
|---|---|
| Gris casi blanco | `#F1F5F9` |
| Gris claro-medio | `#CBD5E1` |
| Gris medio-oscuro | `#94A3B8` |
| Gris oscuro | `#475569` |

## Tipografía

⬜ **Sin decidir.** Candidatas: **Inter** o **IBM Plex Sans**, más una monoespaciada
(**IBM Plex Mono** o **JetBrains Mono**) para los `TRANSACTION ID`.

**Verificar en el archivo real** —no en una lámina generada— que `0/O` y `1/l/I` se distinguen.
