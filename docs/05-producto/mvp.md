# Base técnica del MVP

> **Estado:** 🟡 punto de partida técnico público; los flujos propios de FraudLens todavía no están implementados ni verificados. Este registro distingue lo que afirma el repositorio, lo observado en el deploy y lo que queda pendiente de decisión del equipo.
>
> **Autor del commit consultado:** Mateo Lewinzon (ML). **Registro documental y chequeos públicos:** MDV, 2026-10-28.

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
