# 2026-09-14 — Árbol de Problemas, pivot a fintechs, revisión de requerimientos y logo

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

## Archivos (primera parte)

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

---

## Segunda parte — Revisión de requerimientos funcionales del MVP

Mismo día, se retomó la revisión en equipo del documento de ML (`requerimientos-funcionales-mvp.md`),
trabajando los 6 puntos abiertos punto por punto con FM.

### Lo que se resolvió

- **Punto 1 (actores):** Administrador = Perfil B (decide e integra a nivel comercial). Analista =
  Perfil A (revisa casos día a día). En realidad ya coincidía con el documento de ML (CU-05/06 usan
  "analista", CU-07 usa "administrador") — el conflicto estaba en no tener los actores mapeados
  contra los perfiles.
- **Puntos 2 y 3 (alcance):** CU-02 y CU-07 se recortan de funciones vivas del Administrador a
  **configuración fija al arrancar el sistema**, sin panel de administración en el MVP. FM remarcó
  algo importante para dejar dicho en el documento: **el MVP tiene que decir explícitamente que
  simula el sistema final**, hasta que se resuelvan las cuestiones de negocio pendientes (P-07,
  dataset, acceso al Perfil B).
  - Punto 3 ✅ **resuelto**: el Analista (Perfil A) hace las dos cosas — revisa casos (CU-05/CU-06)
    y ve los reportes/señales agregadas del sistema. No hay login ni vista separada para el
    Administrador en el MVP. Por lo tanto, **no hace falta autenticación con roles diferenciados**.
- **Punto 4 (métricas del modelo):** se deja explícitamente **bloqueante** — no se avanza hasta
  resolver [P-11](../docs/00-proyecto/preguntas-abiertas.md#p-11) (qué dataset se usa).
- **Punto 5 (inconsistencia de umbrales):** corregido directo — la tabla de clasificación decía
  "Aprobar o monitorear" para el nivel Medio, pero CU-04 sólo define 3 resultados (aprobar/revisar/
  bloquear). Se ajustó a "Aprobar", consistente con el resto del documento.
- **Punto 6:** sigue como regla permanente (si el research contradice, gana el research).

### Registro

- [`requerimientos-funcionales-mvp.md`](../docs/05-producto/requerimientos-funcionales-mvp.md) —
  tabla de "Puntos a discutir" con el estado de cada punto, y la corrección de la sección 6. El
  documento original de ML **no se reescribió** — las anotaciones de revisión quedan claramente
  separadas, seguimos la regla de "borrador ≠ definición".
- [`docs/03-decisiones/0005-recorte-alcance-mvp.md`](../docs/03-decisiones/0005-recorte-alcance-mvp.md) —
  decisión registrada de forma **liviana** (no el 6 Sombreros completo que pide la decisión 0003):
  el 1° Parcial es en 2 días (16/9), así que se prioriza avanzar y se deja el análisis formal para
  después del parcial.
- Trello: resolución en la `desc` de la tarjeta (mismo workaround de siempre) y movida a
  **✅ Hecho** — los 6 puntos están resueltos o explícitamente dispuestos (el punto 4 queda como
  dependencia externa de P-11, no bloquea el documento en sí).

---

## Tercera parte — Assets oficiales del logo (PNG)

FM subió el pptx de la Propuesta de Identidad Visual (el board de Canva exportado) y pidió armar
PNG oficiales: el logo solo, el logo con texto, y variaciones.

### Cómo se hizo

En vez de recortar capturas del pptx, se **extrajo la geometría vectorial exacta** (`custGeom`) del
slide 14 ("Logo Final") y se reconstruyó el isotipo con un script Python — así los PNG son nítidos
en cualquier tamaño. La extracción confirmó, coordenada por coordenada, la especificación que ya
estaba en `propuesta-canva.md`: grilla 3×3 en columnas/filas 22-50-78 (viewBox 100×100), círculos
r=8 regulares y r=12 en la anomalía (78, 22).

También se descubrió que el pptx usa **dos tratamientos de color según el fondo** (no estaba
documentado antes con este nivel de detalle):

| | Dots regulares | Anomalía |
|---|---|---|
| Modo claro | `#6B21A8` | `#9333EA` |
| Modo oscuro | `#7E22CE` | `#C084FC` |

### Assets generados

`docs/05-producto/identidad/logo/`: isotipo (claro/oscuro/monocromo blanco), logo completo con
wordmark (claro/oscuro), favicon/ícono de app — más el script (`make_logo_assets.py`) y un
`README.md` documentando fuente, paleta y una sustitución declarada: el pptx usa **Arimo Bold**,
no instalada en este entorno, así que se usó **Liberation Sans Bold** (métricamente compatible).

⚠️ **El pptx en sí no se sube al repo** — `.gitignore` excluye `*.pptx` (regla ya existente del
proyecto para material pesado). Sólo los PNG resultantes y el script generador quedan versionados.

### Registro en Trello

Nota agregada a la tarjeta de identidad visual (ya en ✅ Hecho, no se mueve) con el mismo workaround
de `desc` — `add_comment` se probó de nuevo en esta tarjeta (que sí tiene comentarios nativos de
sesiones anteriores) y **sigue fallando**.

## Qué queda pendiente (todo el día)

| Tarea | Responsable | Urgencia |
|---|---|---|
| Escribir el sombrero rojo de los dos análisis de 6 sombreros | Equipo | 🟡 |
| Conseguir contacto real para entrevistar al nuevo Perfil B | Equipo | 🔴 Antes del 16/9 |
| Resolver P-11 (dataset) para destrabar las métricas del modelo | Equipo | 🔴 |
| Hacer el 6 Sombreros formal del recorte de alcance del MVP | Equipo | 🟢 Después del 16/9 |
| Validar visualmente los PNG del logo | Equipo | 🟢 |

## Archivos (segunda y tercera parte)

- `docs/05-producto/requerimientos-funcionales-mvp.md`
- `docs/03-decisiones/0005-recorte-alcance-mvp.md` *(nuevo)*
- `docs/05-producto/problema.md` — nota de "MVP es simulación" en Alcance del MVP
- `docs/05-producto/identidad/logo/` *(nuevo: README.md, 6 PNG, make_logo_assets.py)*
- `docs/05-producto/identidad/propuesta-canva.md` — link a los assets
- `registro/historial-aportes.md`
