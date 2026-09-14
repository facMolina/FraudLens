# 2026-09-14 — Árbol de Problemas, 5 Por Qué y pivot a fintechs/bancos

| | |
|---|---|
| **Tipo** | Trabajo individual, iterativo con validación en el momento (con asistencia de Claude Code) |
| **Duración** | — |
| **Participantes** | Facundo Molina (FM) |

## Cómo se trabajó

A pedido de FM, esta sesión se armó en modo **mostrar → validar/corregir → recién ahí dejar el
status**: cada pieza (Árbol de Problemas, 5 Por Qué, redefinición de Perfil B/C) se mostró en el
chat, FM la corrigió punto por punto, y sólo después de la validación se escribió al repo y se
actualizó Trello.

## Árbol de Problemas y 5 Por Qué (`docs/05-producto/problema.md`)

Se armó el árbol (efectos por perfil / problema central / causas) y la cadena de 5 Por Qué, con
correcciones de FM en cada paso:

- El punto 1 se enriqueció con un dato real: el **BCRA emitió las Comunicaciones "A" 8471
  (27/08/2026) y "A" 8473 (03/09/2026)**, que obligan a entidades financieras y PSP a tener una
  función de gestión de riesgo de fraude, autoevaluaciones y reportes periódicos. Se buscó por web
  a pedido de FM y se citó con fuente.
- El punto 4 se corrigió para reflejar la estrategia real: FraudLens no busca un modelo 100%
  autónomo, sino uno que **asista** al analista con hipótesis para crear reglas nuevas o detectar
  casos de fraude no contemplados — reforzado porque la propia normativa BCRA exige una persona
  responsable, no un sistema sin supervisión.
- Se cerró en 4 niveles (no 5): el material de la Clase 2 no exige un número fijo más allá del
  nombre de la técnica, y se llegó a una causa raíz sólida.

## 🔄 Pivot: el enfoque de cliente pasa a fintechs y bancos tradicionales

En el medio de la consulta, FM señaló dos cosas que cambian una decisión ya tomada:

1. **Perfil A (analista)** se confirma como definición del equipo —ya no sólo hipótesis de FM— que
   trabaja *dentro de* la fintech/banco cliente.
2. **Perfil B deja de ser "dueño de comercio chico".** El equipo charló y decidió que el enfoque
   real del proyecto es llegar a **empresas fintech y bancos tradicionales** (billeteras virtuales,
   pasarelas de pago, entidades financieras).

Esto es una decisión real del equipo, no una hipótesis de sesión, así que se registró con el
proceso completo que exige el proyecto:

### 6 Sombreros (nuevo análisis)

[`analisis/6-sombreros-enfoque-fintech.md`](../docs/05-producto/analisis/6-sombreros-enfoque-fintech.md) —
por la [decisión 0003](../docs/03-decisiones/0003-metodo-seis-sombreros.md), toda decisión de
"usuario objetivo" lleva este análisis. El hallazgo más importante del blanco: la normativa BCRA
(mismo hallazgo del 5 Por Qué) sostiene el pivot con evidencia real, no sólo con coherencia interna.
El negro marca el riesgo más importante: **a diferencia del Perfil A, nadie confirmó todavía un
contacto real** para entrevistar al nuevo Perfil B. El 🔴 sombrero rojo queda pendiente — lo tiene
que escribir el equipo.

### Decisión 0004

[`docs/03-decisiones/0004-enfoque-cliente-fintech-bancos.md`](../docs/03-decisiones/0004-enfoque-cliente-fintech-bancos.md) —
registra la redefinición: **Perfil B** pasa a "responsable de riesgo/producto en una fintech,
billetera virtual, pasarela de pago o banco tradicional"; **Perfil C** pasa a "usuario final de una
fintech, billetera virtual o pasarela de pago" (ej. Mercado Pago, Ualá, Modo).

### Actualización en cascada

Se actualizaron todos los documentos que quedaban inconsistentes con la redefinición:

- [`usuarios.md`](../docs/05-producto/usuarios.md) — Perfil B y C reescritos, con nota apuntando a
  la decisión 0004; el análisis del 2/9 queda como historial, no se reescribe.
- [P-07](../docs/00-proyecto/preguntas-abiertas.md#p-07) — marcada 🟡 Parcial: el tipo de cliente ya
  está confirmado, sigue abierto cuál perfil (A o B) es *el* usuario objetivo del MVP.
- [`problema.md`](../docs/05-producto/problema.md) — reformulación B y narrativa B reescritas para
  el nuevo perfil (conservando la autoría original de FGR con una nota de actualización); lo mismo
  para la reformulación y narrativa C.
- [`benchmarking.md`](../docs/05-producto/benchmarking.md) — el hallazgo "comercio chico + LatAm ya
  lo cubre ClearSale" se marcó como ya no aplicable directo al nuevo enfoque; queda abierto verificar
  si algún competidor cubre específicamente fintechs chicas.
- [`user-research.md`](../docs/05-producto/user-research.md) — guía de entrevista del Perfil B
  reescrita para el nuevo rol, con la normativa BCRA como gancho de entrevista; el canal de difusión
  anterior (grupos de vendedores de Tiendanube) se marcó como ya no aplicable, **sin inventar uno
  nuevo** — queda como tarea abierta.
- [`identidad/propuesta-canva.md`](../docs/05-producto/identidad/propuesta-canva.md) — nota de
  dependencia actualizada: el enfoque fintech ya no es sólo hipótesis de FM, es decisión del equipo.

## Registro en Trello

- **Árbol de Problemas y 5 Por Qué** — resolución en la `desc` de la tarjeta (workaround por el bug
  de `add_comment`, todavía sin arreglar) y movida a 👀 En revisión.
- **Ticket 1 (3 perfiles)** — se agregó una nota de actualización en la `desc` apuntando a la
  decisión 0004; queda donde estaba (En revisión), porque ahora tiene **dos** sombreros rojos
  pendientes de que el equipo los escriba, no uno.

## Qué queda pendiente

| Tarea | Responsable | Urgencia |
|---|---|---|
| Escribir el sombrero rojo de **ambos** análisis de 6 sombreros | Equipo | 🟡 |
| Conseguir un contacto real para entrevistar al nuevo Perfil B (fintech/banco) | Equipo | 🔴 Antes del 16/9 |
| Verificar si algún competidor cubre "fintech chica + LatAm" en el benchmarking | Equipo | 🟢 |
| Re-testear si `add_comment` de Trello ya funciona | FM | 🟢 |

## Archivos

- `docs/05-producto/problema.md` — nueva sección Árbol de Problemas/5 Por Qué, reformulaciones y
  narrativas B/C actualizadas
- `docs/05-producto/analisis/6-sombreros-enfoque-fintech.md` *(nuevo)*
- `docs/03-decisiones/0004-enfoque-cliente-fintech-bancos.md` *(nuevo)*
- `docs/05-producto/usuarios.md`
- `docs/05-producto/analisis/6-sombreros-usuario-objetivo.md` — nota de continuidad, sin reescribir
- `docs/00-proyecto/preguntas-abiertas.md` — P-07 actualizada
- `docs/05-producto/benchmarking.md`
- `docs/05-producto/user-research.md`
- `docs/05-producto/identidad/propuesta-canva.md`
- `registro/historial-aportes.md`
