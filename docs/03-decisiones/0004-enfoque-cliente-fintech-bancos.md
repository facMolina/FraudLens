# 0004 — Enfoque de cliente: fintechs y bancos tradicionales, no comercio chico

| | |
|---|---|
| **Fecha** | 2026-09-14 |
| **Estado** | ✅ Aceptada |
| **Decidido por** | El equipo (charlado en equipo, según FM) |
| **Pregunta relacionada** | [P-07](../00-proyecto/preguntas-abiertas.md#p-07) |
| **Análisis** | [6 Sombreros — ¿A qué tipo de cliente apunta FraudLens?](../05-producto/analisis/6-sombreros-enfoque-fintech.md) |
| **Supersede a** | La parte de [`usuarios.md`](../05-producto/usuarios.md) (2026-09-02) que definía el Perfil B como "dueño de comercio / e-commerce chico" |

## Contexto

El 2/9 el equipo había decidido tres perfiles de usuario: analista de fraude (decide), dueño de
comercio/e-commerce chico (paga), consumidor (sufre). Ese Perfil B ya tenía research planeado
(`user-research.md`), ideación (`ideacion.md`) y una narrativa escrita (`problema.md`).

El equipo charló y decidió que el enfoque real del proyecto **no es comercio chico**: es llegar a
**empresas fintech y bancos tradicionales** — billeteras virtuales, pasarelas de pago, entidades
financieras. Esto además es coherente con la hipótesis de FM en P-07 (FraudLens B2B para fintechs)
y con la identidad visual, que ya se había construido sobre esa hipótesis.

Se encontró además normativa real y reciente que sostiene el enfoque: las Comunicaciones "A" 8471
(27/08/2026) y "A" 8473 (03/09/2026) del BCRA obligan a entidades financieras y Proveedores de
Servicios de Pago a tener una función de gestión de riesgo de fraude, con autoevaluaciones y
reportes periódicos — es decir, el problema que resuelve FraudLens tiene ahora una exigencia
regulatoria concreta detrás, no sólo una necesidad de negocio.

## Alternativas consideradas

| Opción | A favor | En contra |
|---|---|---|
| **Mantener "comercio chico" como Perfil B** | Ya tenía documentos escritos; accesible sin contactos especiales | No es el enfoque real del proyecto; contradice la identidad visual y la hipótesis de FM |
| **Sacar el Perfil B y quedar con 2 perfiles** | Menos trabajo de reescritura | Contradice [P-18](../00-proyecto/preguntas-abiertas.md#p-18) (el docente confirmó 3 perfiles distintos) y rompe la estructura decide/paga/sufre |
| **Redefinir el Perfil B como responsable de riesgo/producto en fintech o banco** *(elegida)* | Mantiene los 3 perfiles y la estructura decide/paga/sufre; coherente con identidad e hipótesis; tiene respaldo regulatorio real (BCRA) | Ningún contacto de acceso confirmado todavía — mismo riesgo que tuvo el Perfil A antes del 2/9 |

## Decisión

**El Perfil B pasa de "dueño de comercio/e-commerce chico" a "responsable de riesgo o producto en
una fintech, billetera virtual, pasarela de pago o banco tradicional"** — sigue siendo "el que
paga/decide integrar" la solución, ahora en un rol corporativo.

**El Perfil C pasa de "consumidor" genérico a "usuario final de una fintech, billetera virtual o
pasarela de pago"** (ej. alguien que usa Mercado Pago, Ualá, Modo).

El Perfil A (analista de fraude) no cambia, pero se confirma como definición del equipo —ya no sólo
hipótesis de FM— que es un analista que trabaja **dentro de** la fintech o banco cliente.

## Por qué

- Es coherente con la identidad visual y con la hipótesis de FM (P-07), que ya apuntaban a fintechs.
- Tiene respaldo regulatorio real y verificable (BCRA, Comunicaciones "A" 8471 y "A" 8473).
- Mantiene la estructura de tres niveles del dolor (decide / paga / sufre) que pidió el docente.
- El análisis de 6 Sombreros identificó el riesgo principal (cero acceso confirmado al nuevo Perfil
  B) sin que eso invalide la decisión — es un pendiente a resolver, no un motivo para no decidir.

## Consecuencias

- `usuarios.md` se actualiza para reflejar los nuevos Perfil B y C, con una nota que apunta acá.
- `problema.md` (reformulación B y narrativa B), `user-research.md` (guía de entrevista Perfil B) y
  `benchmarking.md` (el ángulo "comercio chico + LatAm") se actualizan para no quedar inconsistentes.
- `identidad/propuesta-canva.md` no cambia de fondo — su hipótesis ya apuntaba a esto — pero su nota
  de dependencia se actualiza para reflejar que ya no es sólo la hipótesis de FM.
- Queda pendiente: conseguir un contacto real para entrevistar al nuevo Perfil B, y escribir el
  sombrero rojo del análisis (ambos, tarea del equipo).
