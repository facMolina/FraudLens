# Base técnica del MVP

> **Estado (2026-11-11):** 🟡 en desarrollo. En `main` ya están integrados el alta y el historial de evaluaciones (CU-01) y la decisión con IA (Groq) y la interfaz web migrada del prototipo (PRs #7 a #9, integrados el 11/11). Ver [Avance al 2026-11-11](#avance-al-2026-11-11). Las secciones siguientes son el registro original del 2026-10-28 y describen el scaffold inicial.
>
> **Autor del commit consultado:** Mateo Lewinzon (ML). **Registro documental y chequeos públicos:** MDV, 2026-10-28.

## Avance al 2026-11-11

**(R) Relevado de GitHub el 2026-11-11 por MDV**, sin ejecutar el código en esta sesión. Lo que dice cada PR es lo que declara su descripción.

### Integrado en `main`

| PR | Autor | Merge | Qué agrega (según la descripción del PR) |
|---|---|---|---|
| [#1](https://github.com/mateolewinzon/fraudlens/pull/1) | ML | 30/10, por ML | CU-01: `POST /api/transaction-evaluations` valida y persiste la transacción en MongoDB; `GET` devuelve el historial paginado (`limit`, `offset`, `has_more`). El resultado era fijo (`BLOCK`, 0.6), sin IA ni reglas. Colección de Postman actualizada |
| [#4](https://github.com/mateolewinzon/fraudlens/pull/4) | MDV | 4/11, por ML | Contrato propio `DecisionModel` para usar cualquier modelo de IA y adapter de **Groq** (AI SDK), con 7 pruebas simuladas. No conecta la IA a los endpoints |
| [#5](https://github.com/mateolewinzon/fraudlens/pull/5) | MDV | 4/11, por ML | Documentación: `docs/architecture.md` (mapa de la arquitectura actual) y `docs/design/ai-integration.md` (propuesta de integración de IA) |
| [#6](https://github.com/mateolewinzon/fraudlens/pull/6) | ML | 4/11, por ML | El `POST` reemplaza el resultado fijo por una decisión de Groq: `APPROVED` o `REJECTED`, con motivos, señales y puntaje estimado. Usa como contexto hasta 50 transacciones aprobadas anteriores del mismo usuario y compara el país de la transacción con el de la tarjeta (`card_country`, obligatorio). Sin umbrales de score. Devuelve 503 si falla la IA. Los registros viejos con `BLOCK` se conservan como históricos |

### Migración de la interfaz — integrada el 2026-11-11

Migración de la interfaz del [prototipo de FGR](prototipo.md) al MVP, en 3 PRs encadenados. **MDV los integró el 11/11 (14:46, hora de Argentina) sin revisión de otro integrante** (0 revisiones en GitHub). Se verificó que los commits de la migración (`8025c46`, `62170ee`, `0f3e259`) están en `main` (merge `78a2a6d`).

| PR | Rama → base | Qué agrega |
|---|---|---|
| [#7](https://github.com/mateolewinzon/fraudlens/pull/7) | `feat/frontend-migration` → `main` | Seguimiento de la migración |
| [#8](https://github.com/mateolewinzon/fraudlens/pull/8) | `feat/frontend-migration-01-client` → #7 | Cliente de evaluaciones compatible con la API actual |
| [#9](https://github.com/mateolewinzon/fraudlens/pull/9) | `feat/frontend-migration-02-ui` → #8 | Pantalla de evaluación e historial conectada al backend, con la identidad visual del prototipo, modo claro y oscuro, y diseño adaptable |

> ⚠️ **CI de `main` en rojo después del merge, sin relación con el código.** GitHub no arrancó el job: *"The job was not started because your account is locked due to a billing issue"*. Lo resuelve el dueño del repo (ML) desde la facturación de GitHub. Antes del merge, los 3 PRs tenían los checks en verde.

### Qué no está probado

- Los 2 tests de integración real (MongoDB e inferencia) quedaron **salteados a propósito**: no hay evidencia de una evaluación real de punta a punta registrada en este repo.
- El deploy público (`https://fraudlens-two.vercel.app`) responde 200 (verificado el 11/11), pero no se verificó que corresponda al último commit de `main`.
- El stack implementado (MongoDB) **no coincide** con la [decisión 0007](../03-decisiones/0007-prototipo-postgresql-un-deploy-vercel.md) (PostgreSQL para el prototipo) ni con la tarjeta [Reconvertir stack](https://trello.com/c/6LaBsgsa). P-10 sigue abierta.
- La decisión 0006 prevé un modelo entrenado con 3 datasets. El MVP hoy decide con un LLM (Groq) y no tiene ninguna pieza de entrenamiento. Falta decisión del equipo en [Modelos de IA a utilizar](https://trello.com/c/HgigLF8C).

## Dónde está

| Recurso | Enlace / evidencia |
|---|---|
| Repositorio | [mateolewinzon/fraudlens](https://github.com/mateolewinzon/fraudlens) |
| Commit consultado | [`4cba6107b1770534b6ce22058e44558618838e79`](https://github.com/mateolewinzon/fraudlens/commit/4cba6107b1770534b6ce22058e44558618838e79), rama `main`; mensaje `chore: bootstrap FraudLens MVP stack`; autor Mateo Lewinzon; 2026-10-22 00:29:23 UTC |
| Deploy público | [fraudlens-two.vercel.app](https://fraudlens-two.vercel.app/) |
| Salud HTTP | [`/api/health`](https://fraudlens-two.vercel.app/api/health) |
| Guía de origen | [README del repositorio, fijado al commit consultado](https://github.com/mateolewinzon/fraudlens/blob/4cba6107b1770534b6ce22058e44558618838e79/README.md) |

La fecha `pushed_at` del repositorio no identifica un commit nuevo de ese día. No se verificó que el deploy corresponda al SHA citado.

## Qué hay, según las fuentes

**(R) README del repositorio, revisado en el commit indicado:** scaffold e infraestructura inicial para empezar a construir; declara explícitamente que todavía no contiene entidades de dominio, esquemas, reglas de negocio, autenticación ni flujos de IA. El stack declarado es:

- Next.js App Router, React y TypeScript estricto.
- Route Handlers sobre Node.js.
- MongoDB Atlas en producción y MongoDB 8 en Docker para desarrollo local, con conexión compartida mediante Mongoose.
- AI SDK y proveedor oficial TypeSafe Jev.
- npm workspaces en `apps/web`, Node.js 24; ESLint, chequeo de tipos y build en GitHub Actions.

La guía requiere Node.js 24, npm y Docker con Compose v2 o superior. Desde la raíz del repo del MVP, indica:

```bash
nvm use
npm ci
cp apps/web/.env.example apps/web/.env.local
npm run db:up
npm run dev
```

Las variables locales van en `apps/web/.env.local`, no en la raíz. No publiques credenciales. Seguí el README fijado para los detalles vigentes. **Estos comandos no se ejecutaron en esta sesión.** El README informa que se habían realizado chequeos iniciales de lint, tipos, build y Mongo local, pero eso es evidencia declarada upstream, no una ejecución nuestra; Atlas e inferencia no estaban probados allí.

## Verificación pública de solo lectura

**(O) Comprobado el 2026-10-28, 19:42 UTC, sin credenciales ni modificaciones en la aplicación:**

| Recurso | Resultado observado |
|---|---|
| `GET https://fraudlens-two.vercel.app/` | HTTP 200, `text/html`; título `FraudLens`. La página muestra “MVP / PUNTO DE PARTIDA”, “La base está lista.” y “Versión inicial · 0.1”. |
| `GET https://fraudlens-two.vercel.app/api/health` | HTTP 200, `application/json`; cuerpo exacto `{"status":"ok","service":"fraudlens"}`. |

El endpoint de salud confirma liveness HTTP básico; **no** prueba conexión a MongoDB, Jev ni funcionalidad de negocio. Tampoco se verificaron autenticación, clasificación de fraude, datos/modelo entrenado, seguridad, aceptación funcional ni correspondencia entre el deploy y el SHA.

## Pendiente de confirmar

- Acceso y capacidad de colaboración de los cuatro integrantes.
- Si este MVP reutiliza componentes del [prototipo de FGR](prototipo.md) o ambos repositorios continúan independientes. El prototipo documentado allí es distinto y no debe confundirse con este scaffold.
- Aprobación del equipo sobre stack y alcance. La tecnología publicada describe la implementación, pero **no cierra P-10** ni constituye una decisión del equipo.
- Implementación y verificación de los flujos de producto tras User Research y definición del alcance.

Ver [P-05](../00-proyecto/preguntas-abiertas.md#p-05) y [P-10](../00-proyecto/preguntas-abiertas.md#p-10).
