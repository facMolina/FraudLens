# 0007 — El prototipo pasa a Next.js en un solo deploy en Vercel y mantiene PostgreSQL

| | |
|---|---|
| **Fecha** | 2026-10-21 |
| **Estado** | 🟡 Propuesta — decidida por FGR, **falta la validación de MDV y ML** (asignados a la tarjeta) |
| **Decidido por** | Guerrero Rojas, Francisco Daniel (FGR) |
| **Pregunta relacionada** | [P-10](../00-proyecto/preguntas-abiertas.md#p-10) (aporta un dato, **no la cierra**) · [P-05](../00-proyecto/preguntas-abiertas.md#p-05) |
| **Tarjeta de Trello** | [Reconvertir stack de prototipo para modelo mejorado con un solo Deploy](https://trello.com/c/6LaBsgsa) |
| **Análisis** | [6 Sombreros — stack del prototipo](../05-producto/analisis/6-sombreros-stack-prototipo-vercel.md) |

> ⚠️ **Alcance:** esta decisión es sobre el **prototipo** y **para esta fase** (hasta la 2da Entrega,
> Prototipo v1, del 28/10). **No es la decisión de stack del MVP**: eso sigue abierto en P-10.

## Contexto

- La tarjeta de Trello planteaba reconvertir el prototipo a un **solo deploy en Vercel**: Next.js
  (frontend + API routes como backend) y **MongoDB Atlas** como base de datos.
- Hoy el prototipo está repartido en tres servicios: el frontend (React + Vite) en Vercel, el backend
  (NestJS + Prisma) en Render y PostgreSQL en Supabase ([`prototipo.md`](../05-producto/prototipo.md)).
- Al relevar el código del prototipo (2026-10-21) se vio que **el aislamiento entre organizaciones
  (tenants) depende de funciones propias de PostgreSQL**:
  - políticas RLS (`CREATE POLICY tenant_isolation`) en las migraciones;
  - `set_config('app.tenant_id', …)` en el guard de autenticación y en el interceptor de tenant;
  - `pg_advisory_xact_lock` para evitar transacciones y configuraciones duplicadas;
  - SQL crudo en el dashboard y validación de zona horaria con `pg_timezone_names`.
- FGR fijó como vencimiento de la tarjeta el **25/10**, tres días antes de la entrega del Prototipo v1.

## Alternativas consideradas

| Opción | A favor | En contra |
|---|---|---|
| **A. Next.js en Vercel + MongoDB Atlas** *(plan original de la tarjeta)* | Era lo planteado originalmente | Hay que reimplementar en código el aislamiento entre tenants y la idempotencia; reescribir 22 modelos de Prisma y el SQL del dashboard; los tests de RLS dejan de servir. Riesgo de que una consulta sin filtro muestre datos de otra organización |
| **B. Next.js en Vercel + PostgreSQL** *(elegida)* | Se conservan Prisma, el esquema, las migraciones, RLS y los tests; Supabase ya tiene las migraciones aplicadas; el plan se achica | Hay que configurar la conexión con pooler para funciones serverless; los planes gratis tienen límites (Supabase Free se pausa tras una semana sin uso) |
| **C. No migrar: dejar Vercel + Render + Supabase** | Cero trabajo antes de la entrega | No cumple el objetivo de la tarjeta (un solo deploy); Render gratis se apaga sin uso |

## Decisión

**En esta fase el prototipo se reconvierte a Next.js (frontend + API routes) en un solo deploy en
Vercel y mantiene PostgreSQL (Supabase o Neon) como base de datos. MongoDB Atlas queda descartado
para esta fase** y se puede reevaluar después.

## Por qué

1. **Seguridad entre organizaciones.** El aislamiento por tenant lo garantiza la base (RLS), no el
   código. Con MongoDB eso tendría que hacerse a mano en cada consulta, y en un sistema antifraude
   que una organización vea datos de otra es el peor error posible.
2. **Plazo.** Con PostgreSQL desaparece el paso "cambiar la base" y el cambio de backend se limita a
   pasar los controladores de NestJS a API routes, reutilizando los servicios y Prisma. Así el 25/10
   es alcanzable.
3. **El objetivo de la tarjeta se cumple igual.** Ni PostgreSQL ni MongoDB corren dentro de Vercel:
   en los dos casos la base es un proveedor externo conectado al proyecto. *(Conocimiento general de
   Claude Code, sin verificar en documentación de Vercel.)*
4. **Lo ya probado sigue sirviendo.** Los tests de RLS, privilegios y fraude se pueden usar para
   verificar que la migración no rompió nada.

## Consecuencias

- **El plan de la tarjeta cambia:** el paso 3 pasa a ser "mantener PostgreSQL: conexión con pooler
  + `DIRECT_URL` para migraciones". Ya está actualizado en la descripción de la tarjeta.
- **Hay que respetar el contrato `/api/v1`**, porque la app móvil (Expo) lo consume.
- **Sigue abierto:**
  - la validación de MDV y ML (hasta entonces el estado es 🟡 Propuesta);
  - el sombrero rojo del análisis, que lo escribe el equipo;
  - el stack del MVP ([P-10](../00-proyecto/preguntas-abiertas.md#p-10)), donde hay una sugerencia
    distinta (FastAPI + Python) que el equipo no revisó;
  - si el MVP parte del código del prototipo ([P-05](../00-proyecto/preguntas-abiertas.md#p-05));
  - la conexión con TypeSafe/Jev ([P-26](../00-proyecto/preguntas-abiertas.md#p-26),
    [P-27](../00-proyecto/preguntas-abiertas.md#p-27)), que queda fuera del 25/10.
