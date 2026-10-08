# Alcance del MVP — qué queda afuera y borrador de MoSCoW

| | |
|---|---|
| **Estado** | 🟡 **Borrador — no hay ninguna clasificación decidida** |
| **Fecha** | 2026-10-08 |
| **Responsable** | Facundo Molina (FM) |
| **Ticket** | [Unificar las listas de "fuera del MVP" y armar el MoSCoW](https://trello.com/c/5dkWRPUy) |
| **Armado con** | Claude Code, **compilando lo que ya está escrito en el repo**. No se agregó ninguna funcionalidad ni ninguna clasificación nueva |
| **Método** | MoSCoW, [Clase 10 (30/9)](../01-clases/clase-10-user-story-mapping-y-backlog.md) |

## Qué es esto y qué no

- **Es una compilación.** Junta en un solo lugar las listas de "fuera del MVP" que hoy están repartidas en cuatro documentos, y marca dónde se contradicen.
- **No decide nada.** Cuáles ítems son *Must / Should / Could / Won't* lo decide el equipo. Donde figura *"⬜ el equipo decide"* es porque **falta esa decisión**.
- Fuentes: **(R)** lo dice un documento del repo, con su link · **(S)** sugerencia de Claude Code, sin aprobar.

### MoSCoW, según la Clase 10

| Categoría | Qué es *(según el deck)* |
|---|---|
| **MUST** | Ítems necesarios en el sprint |
| **SHOULD** | Ítems importantes pero no necesarios en el sprint |
| **COULD** | Ítems deseables pero no necesarios: pueden mejorar la experiencia o satisfacción a bajo costo |
| **WON'T** | Ítems de menor criticidad, bajo valor o no apropiados en este momento (en un futuro, puede ser) |

## 1. De dónde sale cada lista

| Fuente | Qué dice | Ítems |
|---|---|---|
| **Lista corta** — [`problema.md`](problema.md#alcance-del-mvp), *"No es MVP"* | Es la *"hipótesis de trabajo"* del alcance en `problema.md`, que *"se completa cuando definamos el usuario"* | 6 |
| **Lista larga** — [`requerimientos-funcionales-mvp.md` §9](requerimientos-funcionales-mvp.md#9-fuera-del-alcance), *"Fuera del alcance"* | Borrador de ML, revisado en equipo | 11 |
| **Decisión [0005](../03-decisiones/0005-recorte-alcance-mvp.md)** (14/9) | Recorta CU-02 y CU-07 y deja un solo tipo de usuario | 3 recortes (ver sección 3) |
| **Líneas futuras** — [`problema.md`](problema.md#líneas-futuras--próximas-versiones) | *"Lo que queda fuera del MVP no se descarta"* | 8 |

## 2. Lista unificada de lo que queda fuera del MVP

**14 ítems distintos** salen de las dos listas (6 + 11, con 3 que aparecen en ambas). Los 2 últimos vienen de otras fuentes y **no están en ninguna de las dos listas**.

| # | Ítem | Lista corta | Lista larga | Otras fuentes | Notas |
|---|---|---|---|---|---|
| 1 | Reentrenamiento automático del modelo | ✓ *"Reentrenamiento automático del modelo"* | ✓ *"Entrenamiento automático o continuo del modelo"* | Líneas futuras: *"hoy es manual/fijo; a futuro, aprendizaje continuo"* | ⬜ **Redactado distinto**: confirmar si es lo mismo |
| 2 | Reentrenamiento basado en acciones del analista | — | ✓ | — | Solo en la larga. ⬜ ¿Es parte del 1 o es aparte? |
| 3 | Múltiples clientes (multi-tenant) | ✓ *"Múltiples clientes / multi-tenant"* | — | Líneas futuras: *"hoy es un solo cliente"* | Solo en la corta |
| 4 | Alertas y notificaciones | ✓ *"Alertas por mail o notificaciones"* | ✓ *"Notificaciones por correo o mensajería"* | Líneas futuras: *"en tiempo real para el analista"* | ⬜ **Redactado distinto**: confirmar si es lo mismo |
| 5 | Panel de administración de usuarios y permisos | ✓ | — | **0005**: sin pantalla de administración ni roles diferenciados. Líneas futuras: *"panel de administración completo para el Perfil B, más allá de la configuración fija actual"* | Solo en la corta, pero la 0005 la respalda |
| 6 | Integraciones con procesadores de pago reales | ✓ | — | Líneas futuras | Solo en la corta |
| 7 | Explicabilidad avanzada | ✓ *"Explicabilidad avanzada del modelo"* | ✓ *"Explicabilidad avanzada"* | Líneas futuras: *"más allá de los 3 factores básicos de CU-03"* | En las dos, mismo sentido |
| 8 | Modelos avanzados o múltiples modelos especializados | — | ✓ | — | Solo en la larga. **Jev no está ubicado** (sección 5) |
| 9 | Investigación completa de casos de fraude | — | ✓ | — | Solo en la larga |
| 10 | Gestión de reclamos o contracargos | — | ✓ | — | Solo en la larga |
| 11 | Modificación manual de la decisión desde el dashboard | — | ✓ | — | Solo en la larga |
| 12 | Integraciones con listas externas de fraude | — | ✓ | — | Solo en la larga |
| 13 | Grafos de relaciones entre usuarios, comercios o dispositivos | — | ✓ | — | Solo en la larga |
| 14 | **Bloqueo real de dinero**: FraudLens solo devuelve una recomendación | — | ✓ | — | Solo en la larga |
| 15 | Cobertura AML + fraude en un solo producto | — | — | Líneas futuras: *"hoy fuera de alcance, pero es lo que ya ofrece Feedzai"* ([benchmarking](benchmarking.md)) | **No figura en ninguna de las dos listas**, solo en líneas futuras |
| 16 | Autenticación con roles diferenciados (login de Administrador) | — | — | **0005**: *"no hace falta autenticación con roles diferenciados para el MVP: un solo tipo de usuario (Analista) accede a todo el dashboard"* | **No figura en las listas**: sale de la 0005 |

**MoSCoW de estos 16 ítems:** los 16 ya están declarados fuera del MVP por el equipo, así que **por la definición de la Clase 10 corresponden a *Won't* ("no apropiados en este momento; en un futuro, puede ser")**. Eso es lo que dice el repo; **⬜ falta que el equipo lo confirme como clasificación MoSCoW**, y confirmar los 3 pares redactados distinto (ítems 1, 2 y 4).

## 3. Recortes de la decisión 0005: no están "fuera", se simplifican

| Qué | Antes | Después (decisión 0005) |
|---|---|---|
| **CU-02** — regla de monto mínimo | Función viva, editable por un Administrador con login propio | **Configuración fija que se carga al levantar el sistema** (seed inicial) |
| **CU-07** — configurar reglas y umbrales | Ídem | Ídem, **sin pantalla de administración dedicada** |
| **Actor Administrador** | Rol con su propia vista | **Sin vista ni login separado**: lo hace el Analista; su rol queda acotado a la configuración fija inicial |

## 4. Lo que está adentro, según el repo

Según la 0005, el MVP queda con un **"núcleo demostrable"** de CU-01, CU-03, CU-04, CU-05 y CU-06, más CU-02 y CU-07 simplificados. **Eso no es una clasificación MoSCoW.**

| CU | Título | Estado según el repo | MoSCoW |
|---|---|---|---|
| [CU-01](requerimientos-funcionales-mvp.md#cu-01--analizar-una-transacción) | Analizar una transacción | Núcleo (0005) | ⬜ el equipo decide |
| [CU-02](requerimientos-funcionales-mvp.md#cu-02--aplicar-la-regla-de-monto-mínimo) | Aplicar la regla de monto mínimo | Simplificado a configuración fija (0005) | ⬜ el equipo decide |
| [CU-03](requerimientos-funcionales-mvp.md#cu-03--calcular-el-riesgo-de-fraude) | Calcular el riesgo de fraude | Núcleo (0005) | ⬜ el equipo decide |
| [CU-04](requerimientos-funcionales-mvp.md#cu-04--determinar-la-decisión) | Determinar la decisión | Núcleo (0005) | ⬜ el equipo decide |
| [CU-05](requerimientos-funcionales-mvp.md#cu-05--monitorear-transacciones) | Monitorear transacciones | Núcleo (0005) | ⬜ el equipo decide |
| [CU-06](requerimientos-funcionales-mvp.md#cu-06--consultar-el-detalle-de-una-transacción) | Consultar el detalle de una transacción | Núcleo (0005) | ⬜ el equipo decide |
| [CU-07](requerimientos-funcionales-mvp.md#cu-07--configurar-reglas-y-umbrales) | Configurar reglas y umbrales | Simplificado a configuración fija (0005) | ⬜ el equipo decide |

`problema.md` resume el MVP en tres cosas: **recibir una transacción y devolver un score**, **mostrarlas en una pantalla** y **un modelo entrenado con datos históricos**.

## 5. Ítems sin ubicar

- **Jev (modelo externo de TypeSafe).** La lista larga deja fuera *"modelos avanzados o múltiples modelos especializados"* (ítem 8); **no dice si un modelo externo cae ahí**. Hoy no está ni adentro ni afuera. Depende del [análisis de 6 Sombreros de Jev](analisis/6-sombreros-jev.md) y de [P-25](../00-proyecto/preguntas-abiertas.md#p-25). **Se le preguntó a MDV en su tarjeta.**
- **Los ítems 15 y 16** no están en ninguna lista de "fuera del MVP": hay que decidir si se suman a la lista única.

## 6. Contradicciones entre documentos *(para resolver, sin decidir acá)*

1. **Los requerimientos todavía dan por adentro algo que la 0005 recortó.** El [§2 de los requerimientos](requerimientos-funcionales-mvp.md#2-alcance-del-mvp) lista *"Configuración de umbrales desde el dashboard"* como parte del alcance, y la [definición de "MVP terminado" (§10)](requerimientos-funcionales-mvp.md#10-definición-de-mvp-terminado) incluye *"el administrador modifica los umbrales"*. La 0005 los pasó a configuración fija por seed. Por regla del repo, el documento de ML **no se reescribe**; conviene que el equipo decida cómo anotarlo.
2. **Tres ítems están redactados distinto en las dos listas** (1, 2 y 4). No se dio por hecho que son iguales.
3. **El MVP promete "un modelo entrenado con datos históricos"** (`problema.md` y §2 de los requerimientos). **El prototipo de FGR no tiene un modelo entrenado**: calcula el riesgo con reglas ponderadas ([relevamiento del 2026-10-07](prototipo.md#qué-muestra-el-repo--relevamiento-del-2026-10-07), segunda mano, sin ejecutar). Entonces ese ítem *"adentro"* hoy **no existe** en el código.
4. **El prototipo implementa cosas que la 0005 recortó o que las listas dejan afuera:** CU-02 y CU-07 como funciones vivas, tres roles por API key y el registro de una revisión humana de cada transacción. *(Según el relevamiento; no es lo mismo que el ítem 11, "modificación manual de la decisión", y no se equiparó.)*

## 7. Qué falta para dar esto por cerrado

- [ ] Confirmar los **3 ítems redactados distinto** (1, 2 y 4)
- [ ] Decidir si los ítems **15 y 16** se suman a la lista única
- [ ] **Clasificar con MoSCoW** cada ítem, incluidos los CU (secciones 2 y 4). Requiere análisis de 6 Sombreros ([tarjeta](https://trello.com/c/vxWQiPIz)), con el sombrero rojo de las 4 voces
- [ ] **Ubicar a Jev** (sección 5)
- [ ] Decidir cómo se anota la contradicción 1 en los requerimientos
- [ ] Registrar la **lista única** como decisión numerada y hacer que las dos listas viejas apunten a ella *(recién después de la decisión)*

## Fuentes

[`problema.md`](problema.md) · [`requerimientos-funcionales-mvp.md`](requerimientos-funcionales-mvp.md) · [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md) · [Clase 10](../01-clases/clase-10-user-story-mapping-y-backlog.md) · [`prototipo.md`](prototipo.md) · [`typesafe-jev.md`](typesafe-jev.md)
