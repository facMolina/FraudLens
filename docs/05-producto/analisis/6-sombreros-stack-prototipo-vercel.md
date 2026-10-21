# 6 Sombreros — ¿MongoDB Atlas o PostgreSQL para el prototipo en un solo deploy en Vercel?

| | |
|---|---|
| **Decisión** | Al reconvertir el prototipo a Next.js en un solo deploy en Vercel, ¿la base pasa a MongoDB Atlas o se mantiene PostgreSQL? |
| **Fecha** | 2026-10-21 |
| **Participantes** | FGR, con asistencia de Claude Code. ⬜ Faltan las voces de MDV, ML y FM |
| **Tarjeta de Trello** | [Reconvertir stack de prototipo para modelo mejorado con un solo Deploy](https://trello.com/c/6LaBsgsa) |
| **Estado** | 🟡 **BORRADOR.** FGR decidió (ver azul y [decisión 0007](../../03-decisiones/0007-prototipo-postgresql-un-deploy-vercel.md)). ⬜ Falta el sombrero rojo y la validación del equipo |

> ⚠️ **Qué es de quién en este archivo** (regla 6 del repo):
> - ⚪ Blanco: hechos del repo del prototipo (relevados el 2026-10-21), de este repositorio y de la
>   tarjeta de Trello, con su fuente.
> - ⚫🟡🟢 Negro, amarillo y verde: **💡 borrador de Claude Code.** El equipo los corrige, completa o descarta.
> - 🔴 Rojo: **lo escribe el equipo.** Acá sólo están las preguntas.
> - 🔵 Azul: la decisión es **de FGR**; los puntos clave los resumió Claude Code.

## El problema, en una frase

Para tener el prototipo en un solo deploy en Vercel antes del 25/10, ¿migramos la base a MongoDB
Atlas como decía la tarjeta, o mantenemos PostgreSQL?

---

## ⚪ Sombrero Blanco — Analista racional

### Lo que sabemos

| Hecho | Fuente |
|---|---|
| El prototipo usa NestJS + Prisma + PostgreSQL en el backend y React + Vite en el frontend | [`prototipo.md`](../prototipo.md) |
| El esquema tiene 22 modelos de Prisma | `Backend/prisma/schema.prisma` del prototipo |
| El aislamiento entre organizaciones usa políticas RLS de PostgreSQL y `set_config('app.tenant_id', …)` | Migraciones del prototipo · `auth.guard.ts` · `tenant.interceptor.ts` |
| La idempotencia de transacciones y configuraciones usa `pg_advisory_xact_lock` | `transactions.service.ts` · `settings.service.ts` del prototipo |
| El dashboard usa SQL crudo y la configuración valida zonas horarias con `pg_timezone_names` | `dashboard.service.ts` · `settings.service.ts` del prototipo |
| Hay tests de RLS, privilegios, autenticación y fraude | `Backend/test/` del prototipo |
| El código del frontend web son unas 800 líneas | `Frontend/src/` del prototipo |
| La app móvil (Expo) consume la misma API `/api/v1` | `Frontend/mobile/api.js` del prototipo |
| El deploy actual es Vercel (front) + Render (back) + Supabase (base), con la regla de mantenerse en planes gratis | [`prototipo.md`](../prototipo.md#actualización-del-2026-10-21--esquema-de-privilegios-pr-3) |
| Según `DEPLOYMENT.md`, Supabase ya tiene las migraciones aplicadas | [`prototipo.md`](../prototipo.md#actualización-del-2026-10-21--esquema-de-privilegios-pr-3) |
| La tarjeta planteaba MongoDB Atlas; están asignados MDV, ML y FGR | Tarjeta de Trello (versión original) |
| FGR fijó el vencimiento de la tarjeta para el 25/10 | Tarjeta de Trello |
| La 2da Entrega (Prototipo v1) es el 28/10 | [`cronograma.md`](../../00-proyecto/cronograma.md) |
| El stack del MVP está abierto; hay una sugerencia (FastAPI + Python) que el equipo no revisó | [P-10](../../00-proyecto/preguntas-abiertas.md#p-10) |
| Supabase Free se pausa tras una semana sin uso | [P-10](../../00-proyecto/preguntas-abiertas.md#p-10) (fuente: selector de stack aportado por MDV) |

### Lo que NO sabemos

- ⬜ **Por qué la tarjeta planteaba MongoDB Atlas**: qué se buscaba con ese cambio.
- ⬜ Si MDV y ML están de acuerdo con mantener PostgreSQL.
- ⬜ Si la conexión con pooler funciona bien con el esquema actual de RLS dentro de funciones de Vercel. **No se probó.**
- ⬜ Los límites vigentes de Vercel Hobby, Supabase Free y Neon Free (duración de funciones, almacenamiento, conexiones). **No se verificaron.**
- ⬜ Si el MVP va a partir de este código ([P-05](../../00-proyecto/preguntas-abiertas.md#p-05)).

---

## 🔴 Sombrero Rojo — Mente emocional

> Emociones, miedos e intuiciones. **Sin justificar.** Lo escribe el equipo, no la IA.

Preguntas para cada integrante:
- ¿Qué te genera cambiar el stack a una semana de la entrega del Prototipo v1?
- ¿Te sentís cómodo/a defendiendo frente al docente un prototipo en Next.js + PostgreSQL? ¿Y en MongoDB?
- ¿Algo de MongoDB te entusiasmaba y se pierde con esta decisión?

- **FGR:** ⬜
- **MDV:** ⬜
- **ML:** ⬜
- **FM:** ⬜

---

## ⚫ Sombrero Negro — Crítico estratégico

> 💡 Borrador de Claude Code.

| Riesgo | Cómo se ve el fracaso |
|---|---|
| **Con MongoDB:** filtro de tenant olvidado | Una consulta sin `tenantId` muestra transacciones de otra organización. En un antifraude es el peor error |
| **Con MongoDB:** reescritura grande con poco tiempo | Al 25/10 la base nueva no está lista y se entrega el Prototipo v1 a medio migrar |
| **Con PostgreSQL:** conexiones agotadas en serverless | Sin pooler, cada función abre su conexión y la base rechaza pedidos bajo carga |
| **Con PostgreSQL:** base pausada | Supabase Free se pausa sin uso y la demo falla si nadie la despertó antes |
| **En las dos:** romper la app móvil | Las API routes cambian rutas o formatos y la app Expo deja de funcionar |
| **En las dos:** se confunde con la decisión del MVP | El equipo lee esto como "el MVP es Next + Postgres" cuando P-10 sigue abierta |

---

## 🟡 Sombrero Amarillo — Optimista estratégico

> 💡 Borrador de Claude Code.

- Un solo deploy y un solo panel: menos servicios gratis que se apagan y menos cosas que explicar en la demo.
- Se conserva todo lo construido y probado: esquema, migraciones, seguridad por tenant y tests.
- El trabajo se concentra en lo que pide la tarjeta (unificar), no en rehacer la base.
- Deja margen para pulir el prototipo antes del 28/10.

---

## 🟢 Sombrero Verde — Pensamiento creativo

> 💡 Borrador de Claude Code. Sin filtrar.

1. Migrar en una rama aparte y dejar el deploy actual como respaldo hasta que la versión nueva pase los tests.
2. Usar Neon en vez de Supabase para evitar la pausa por inactividad.
3. Si algún caso de uso necesita documentos flexibles, usar columnas `JSONB` de PostgreSQL en vez de sumar MongoDB.
4. Reevaluar MongoDB después del 28/10 con un caso concreto que lo justifique.

---

## 🔵 Sombrero Azul — Director estratégico

### Puntos clave de cada sombrero

| Sombrero | Lo que aportó |
|---|---|
| ⚪ Blanco | La seguridad entre organizaciones depende de PostgreSQL; quedan tres días entre el vencimiento y la entrega; no se sabe por qué se había planteado MongoDB |
| 🔴 Rojo | ⬜ Pendiente del equipo |
| ⚫ Negro | MongoDB suma riesgo de seguridad y de plazo; PostgreSQL exige pooler y cuidar la pausa de Supabase |
| 🟡 Amarillo | Un solo deploy conservando lo construido |
| 🟢 Verde | Rama aparte con respaldo; Neon; `JSONB`; reevaluar Mongo después |

### Contradicciones a resolver

- La tarjeta original decía MongoDB y la decisión dice PostgreSQL: falta saber qué se buscaba con MongoDB y confirmarlo con MDV y ML.
- P-10 tiene una sugerencia distinta para el MVP (FastAPI + Python). Esta decisión es sólo del prototipo y no la contradice, pero hay que dejarlo claro.

### Decisión

> **(FGR, 2026-10-21)** En esta fase el prototipo se reconvierte a Next.js en un solo deploy en
> Vercel y **mantiene PostgreSQL**. MongoDB Atlas queda descartado para esta fase.
> → [Decisión 0007](../../03-decisiones/0007-prototipo-postgresql-un-deploy-vercel.md)

### Qué la sostiene

- El aislamiento entre organizaciones lo garantiza la base.
- El plazo al 25/10.
- Se cumple igual el objetivo de un solo deploy.

### Qué la haría cambiar

- Que MDV o ML expliquen una necesidad concreta que sólo cubra MongoDB.
- Que la conexión de PostgreSQL desde funciones de Vercel no funcione en los planes gratis.

---

## Verificación final

- [ ] El problema se analizó desde múltiples perspectivas reales — ⬜ falta el rojo del equipo
- [x] El resultado **no** refleja un único sesgo emocional o racional
- [ ] La decisión del azul integra y equilibra todas las visiones anteriores — ⬜ falta el rojo
- [x] El blanco **no inventó** ningún dato
