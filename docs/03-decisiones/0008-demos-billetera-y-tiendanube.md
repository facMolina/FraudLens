# 0008 — Para la presentación del MVP se construyen dos demos cliente: billetera virtual y e-commerce en Tiendanube

| | |
|---|---|
| **Fecha** | 2026-11-25 |
| **Estado** | 🟡 Propuesta — decidida por FGR, **falta la validación de MDV, ML y FM** |
| **Decidido por** | Guerrero Rojas, Francisco Daniel (FGR) |
| **Pregunta relacionada** | — |
| **Tarjeta de Trello** | [Armar la demo de integración de FraudLens para la presentación del MVP](https://trello.com/c/LqVQdkQu) |
| **Análisis** | **No se hizo 6 Sombreros** — ver "Por qué" |

## Contexto

- Para la presentación del MVP, FGR quiere mostrar a FraudLens **integrado en el flujo de un sistema
  cliente**, y no sólo su panel (`fraudlens-two.vercel.app`).
- El 2026-11-25 se redactaron con Claude Code dos specs en **borrador**:
  - [`spec-billetera-demo.md`](../05-producto/spec-billetera-demo.md): billetera virtual mínima que
    consulta FraudLens antes de cada pago.
  - [`spec-ecommerce-tiendanube-demo.md`](../05-producto/spec-ecommerce-tiendanube-demo.md): tienda en
    Tiendanube que consulta FraudLens, vía un middleware, antes de confirmar la compra.
- 📘 La API de FraudLens-MVP hoy sólo admite `operation_type: "PURCHASE"` (según las specs, tomadas de
  la documentación del repo del MVP).
- FGR fijó como fecha límite el **9/12/2026** (Final regular, según el [cronograma](../00-proyecto/cronograma.md)).

## Alternativas consideradas

| Opción | A favor | En contra |
|---|---|---|
| **A. Sólo la billetera** | Coincide con el segmento objetivo, fintechs y billeteras ([decisión 0004](0004-enfoque-cliente-fintech-bancos.md)) | Muestra un solo tipo de cliente |
| **B. Sólo Tiendanube** | Es una plataforma de e-commerce real, no una app armada para la demo | No es el segmento objetivo de la decisión 0004 |
| **C. Las dos** *(elegida)* | Muestra la misma API consumida por dos clientes distintos | Duplica el trabajo de construcción y de ensayo antes del 9/12 |

> Las columnas "a favor" y "en contra" salen de lo que dicen las specs. **No son una evaluación del equipo.**

## Decisión

**Para la presentación del MVP se construyen las dos demos, la billetera virtual y el e-commerce en
Tiendanube, con fecha límite el 9/12/2026.** Las dos son **clientes de demostración**: no forman
parte del MVP ni cambian el segmento objetivo de la decisión 0004.

## Por qué

1. **Se decidió en clase que hay que tener un video de la demo que presente a FraudLens desde el
   punto de vista de sus clientes, que pueden ser fintechs y comercios chicos.** *(Según FGR,
   2026-11-26. ⬜ Fecha de la clase: a confirmar.)* Por eso hay una demo para cada tipo de cliente:
   - **Fintech** → la billetera virtual;
   - **Comercio chico** → la tienda en Tiendanube.
2. **Como se construyen las dos**, no hay que elegir entre alternativas, y FGR resolvió **no hacer el
   análisis de 6 Sombreros** ([decisión 0003](0003-metodo-seis-sombreros.md)).

> 📝 *El punto 1 se completó el 2026-11-26, con el dato que aportó FGR. Antes estaba marcado como
> hueco (⬜).*

## Consecuencias

- La tarjeta de Trello exige que **cada demo** corra contra la API desplegada y muestre los 3 casos:
  `APPROVED`, `REJECTED` con alerta y motivos, y falla de la API (fail-closed).
- El video ya existe: [`fraudlens-demo-40s.mp4`](../05-producto/demo/fraudlens-demo-40s.mp4) (40 s),
  y muestra la billetera y la tienda de Tiendanube.
- **Sigue abierto:**
  - la validación de MDV, ML y FM (hasta entonces el estado es 🟡 Propuesta);
  - ⬜ **si los comercios chicos pasan a ser clientes objetivo.** La [decisión 0004](0004-enfoque-cliente-fintech-bancos.md)
    pone el foco en fintechs y bancos. Si lo que se dijo en clase amplía el segmento, hace falta una
    decisión nueva que lo diga; esta decisión no lo cambia;
  - la revisión de las dos specs, que siguen en **borrador** (regla 8);
  - contrastar las dos demos con la lista "NO MVP" y el [MoSCoW](../05-producto/alcance-mvp-moscow.md)
    ([decisión 0005](0005-recorte-alcance-mvp.md));
  - coordinar con MDV, responsable de la slide de demo en vivo del
    [guion de la presentación de avances](../02-entregables/presentacion-avances/guion.md), si la
    presentación del 9/12 reusa esa estructura.
