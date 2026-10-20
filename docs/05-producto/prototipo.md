# Prototipo de FraudLens

> **Estado:** 🟡 existe en un **repositorio propio**, **relevado el 2026-10-07** y **actualizado el 2026-10-18** con multi-tenant, autenticación,
> identidad visual y app móvil ([ver abajo](#actualización-del-2026-10-18--commits-de-fgr)). Todo leído del código, **sin ejecutar**: falta correrlo para confirmar que anda.
> **Autor:** Francisco Daniel Guerrero Rojas (FGR)
> **Registrado acá:** 2026-09-02 por FM, a partir de lo que FGR compartió por WhatsApp. **Link y relevamiento:** 2026-10-07 por FM.
> **Actualización:** 2026-10-20 por FGR.

## Dónde vive

**Repositorio (público):** https://github.com/fguerrero2/FraudLens-prototipo

- **Desde el 2026-10-20 es público** *(FGR)*: cualquiera puede leerlo, pero **solo los colaboradores pueden hacer cambios**.
  Antes era privado, y el relevamiento del 2026-10-07 se hizo con la sesión de GitHub de FM (ver abajo).
- El público ve todo el contenido commiteado. Revisá los puntos de seguridad en
  [Detalles a revisar con FGR](#detalles-a-revisar-con-fgr-no-se-deduce-nada).

> ✅ **Corrección (2026-10-07).** Acá se había escrito que el prototipo era *"solo interfaz, sin lógica"* y que *"no hay un modelo ni reglas
> funcionando detrás"* (aclaración del equipo del 17/9). **El relevamiento del repo muestra otra cosa:** hay un backend con un **motor de reglas
> ponderadas y determinista** que calcula el riesgo, base de datos y tests. **Lo que no hay es un modelo de ML entrenado.** Esa es la diferencia
> exacta. La frase vieja quedó superada; el detalle está abajo.
>
> **No es el repositorio del MVP** (eso sigue abierto, ver [P-05](../00-proyecto/preguntas-abiertas.md#p-05)).

## Qué hay

Francisco armó un prototipo funcional de FraudLens:

| Parte | Cómo se hizo |
|---|---|
| **Backend** | Generado con **Claude** |
| **Frontend** | Generado con **Codex** y después ajustado al backend ya desarrollado |
| **Base técnica** | Notebook de Kaggle: [*Fraud Detection Full Project in Spanish*](https://www.kaggle.com/code/carmencastrogonzlez/fraud-detection-full-project-in-spanish), de `carmencastrogonzlez` |
| **Especificación** | Se le pasó el documento [*FraudLens — Requerimientos funcionales del MVP*](requerimientos-funcionales-mvp.md) (escrito por ML) y de ahí salió todo |

## Qué muestra el repo — relevamiento del 2026-10-07

> **Fuente y cómo leerlo.** Lo relevó **otro chat de Claude con Claude in Chrome**, en **solo lectura**, sobre el commit `5f6528c` de `main`, con la
> sesión de GitHub de FM (en ese momento el repo era privado). **No se ejecutó la aplicación ni los tests**: los estados "implementado" se basan en la lectura del
> código. Cada dato trae su archivo de evidencia en el informe original. Es información de segunda mano para esta sesión: **no la verificamos nosotros**.

### Resumen

| | |
|---|---|
| **Stack** | **Backend:** NestJS + TypeScript, Prisma `^6.19.3`, PostgreSQL (`postgres:17-alpine` en Docker). **Frontend:** React + Vite (JSX). Las versiones de NestJS, React y Vite figuran como `"latest"` |
| **Modelo de ML** | **No hay.** Ni archivos de modelo (`.pkl`, `.joblib`, `.onnx`…), ni notebooks, ni librerías de ML |
| **Cómo se calcula el riesgo** | Con un **motor de reglas ponderadas y determinista** (`Backend/src/risk/risk.service.ts`): desvío del monto (hasta 35 pts), país no habitual (20), dispositivo nuevo (13), categoría o comercio no habitual (12), horario inusual (10), ráfaga de operaciones (10) e historial insuficiente (15 a 45). El README del backend lo dice: *"heurística ponderada y determinista (no ML)"* |
| **Se usa al entrar una transacción** | Sí: `POST /transactions` llama al motor, calcula nivel y decisión y guarda el resultado |
| **Endpoints** | `POST` y `GET /transactions`, `GET /transactions/:id`, `PUT /transactions/:id/review`, `GET /dashboard/metrics`, `GET` y `PUT /settings/thresholds`, `GET /settings/thresholds/history`, `GET /health`. Autenticación por **API key fija por rol** (`client`, `analyst`, `admin`) |
| **Frontend** | Dashboard y Transactions, con detalle de la transacción y revisión humana, panel *Rules & thresholds* y *New transaction*. **Interfaz en inglés** |
| **Datos** | **No hay ningún dataset en el repo.** Los datos de demostración los genera `prisma/seed.ts` (con `Math.random`) |
| **Evaluación offline** | `Backend/evaluation/`: 1.800 eventos sintéticos con semilla fija y un modelo estadístico de anomalías (media y desvío por moneda) que **solo corre en ese script** y no está conectado al servidor (`report.json`: *"No model deployed"*) |
| **Tests** | 12 en el backend (`node --test`) + un test de integración con Docker. En el frontend, ninguno |
| **Historial** | 7 commits, un solo autor (`fguerrero2`), del 31/8 al 16/9 (último: 21:15, el día del parcial) |

### Casos de uso — según el código, sin ejecutar

| CU | Estado |
|---|---|
| CU-01 Analizar una transacción | Implementado |
| CU-02 Regla de monto mínimo | Implementado (si hay 5 o más operaciones en 60 minutos, no aplica la exención) |
| CU-03 Calcular el riesgo | Implementado **con reglas, no con ML** |
| CU-04 Decisión por umbrales | Implementado (valores por defecto: monto mínimo 10.000, revisión 60, bloqueo 85) |
| CU-05 Monitorear transacciones | Implementado (el dashboard se refresca cada 15 segundos) |
| CU-06 Detalle de una transacción | Implementado |
| CU-07 Configurar reglas y umbrales | Implementado (valida y guarda historial de cambios) |

El botón **New transaction** del dashboard **sí llama al backend**: manda la transacción, el motor calcula el resultado y el frontend muestra la
decisión y el *Risk X/100* que devolvió. Es decir, las transacciones de la captura que está en la presentación del parcial **las analizó el motor de
reglas**; no son filas escritas a mano en la interfaz.

### Lo que no coincide con lo que se venía diciendo

1. **"Sin lógica" no es exacto** (ver la corrección arriba): hay lógica real, sin ML.
2. **No usa los 3 datasets de la [decisión 0006](../03-decisiones/0006-tres-datasets-para-el-modelo.md).** El repo no incluye ni referencia ninguno de los tres.
   Solo menciona **PaySim** (`kaggle.com/datasets/ealaxi/paysim1`) como **inspiración** de unos campos opcionales.
3. **El notebook de Kaggle no está citado como corresponde.** El README del backend nombra *"el notebook de referencia de Carmen Castro González"* pero
   **sin título ni link al notebook**: el link de esa línea va al dataset PaySim.
4. **Ningún archivo menciona a Claude ni a Codex.** El README de la raíz tiene texto con formato de respuesta de una herramienta (*"Listo. Creé y levanté
   correctamente…"*, *"Edited 8 files…"*), pero no nombra cuál. **Que el backend lo hizo Claude y el frontend Codex lo dijo FGR; el repo no lo confirma**
   (todos los commits son de `fguerrero2`).
5. **Alcance contra la [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md).** El prototipo implementa **CU-02 y CU-07 como funciones vivas**
   (umbrales editables por un rol `admin`) y **tres roles** por API key, justo lo que la 0005 recortó para el MVP. Es un dato, no un error: el prototipo no es el MVP.
6. **Otras fuentes que cita el repo:** `Backend/evaluation/README.md` toma *"inspiración conceptual"* de **`YobieBen/FraudLens`** (el mismo repo que
   apareció en el chequeo del nombre, [P-23](../00-proyecto/preguntas-abiertas.md#p-23)) y `Frontend/VISUAL_IDENTITY.md` se basa en la identidad de
   **`facMolina/FraudLens`**, este repo. Hay que citarlas en el documento final.

### Detalles a revisar con FGR *(no se deduce nada)*

- **Contradicciones dentro del propio repo:** el README del backend dice **SQLite** y el schema usa **PostgreSQL** (hay una carpeta `migrations.sqlite-backup/`);
  dice que los `user_id` están "mockeados" en `App.jsx` y ya no lo están; dice que "ya existe un .env de desarrollo" y no hay ninguno.
- **`Frontend/node_modules` está commiteado** (4.484 archivos) aunque figura en `.gitignore`.
- **Claves de desarrollo en texto plano** en `.env.example`, `compose.yaml`, el README del backend y `Frontend/src/api.js`. Variables `VITE_*` van dentro del
  paquete del frontend: **si esos mismos valores se usaran en un despliegue real, quedarían a la vista de cualquiera**. Hay instrucciones de deploy (Supabase + Render).
- **Sin licencia** (no hay archivo `LICENSE`).
- El informe **no leyó completos** los `Dockerfile`, `nginx.conf`, `evaluation/metrics.ts` ni el resto de `seed.ts`.

## Actualización del 2026-10-18 — commits de FGR

> **Fuente y cómo leerlo.** Lo relevó **Claude Code** el 2026-10-20 sobre el clon local de FGR, en `main` al commit `af8c320`, que coincide con `origin/main`.
> Se leyeron el historial, los archivos de cada commit y algunos archivos puntuales. **No se ejecutó la aplicación ni los tests.**
> El trabajo de interfaz del 18/10 está en la
> [bitácora de ese día](../../bitacora/2026-10-18-prototipo-identidad-y-usabilidad.md). Lo cierra la tarjeta de Trello
> [Actualizar Prototipo de FraudLens…](https://trello.com/c/Yryt6P90).

### Commits nuevos

| Commit | Fecha | Qué trae |
|---|---|---|
| `e41d3c6` | 2026-10-18 | *"Tenant, idiomas, identidad visual, app movil"*: 125 archivos. Es el grueso del cambio y acumula trabajo que estaba sin commitear |
| `501121b` | 2026-10-18 | Ajuste menor del README de la raíz |
| `af8c320` | 2026-10-18 | *"Ajuste de botones y contraste"*: retoques de `styles.css`, de la pantalla de login y de la app móvil |

El historial pasa a **10 commits**, todos de `fguerrero2`, del 31/8 al 18/10.

### Qué cambió respecto del relevamiento del 2026-10-07

| Tema | Antes (2026-10-07) | Ahora (2026-10-18) |
|---|---|---|
| **Multi-tenant** | No había | Varias empresas (tenants) en la misma instalación: migración `20261007000000_multitenancy`, contexto e interceptor de tenant (`Backend/src/common/`), módulo `tenants` y tests de aislamiento (`Backend/test/rls.test.ts`) |
| **Autenticación** | **API key fija por rol** (`client`, `analyst`, `admin`) | Usuarios con contraseña y tokens (`Backend/src/auth/`). Se borró el viejo `api-key.guard.ts`. También hay **login por QR** desde la app móvil, con un desafío que vence a los 2 minutos |
| **Roles y permisos** | 3 roles fijos | Permisos por tenant con 5 roles predefinidos (`role-presets.ts`): `TENANT_ADMIN`, `FRAUD_ANALYST`, `OPERATOR`, `VIEWER` y `API_MANAGER`, más roles de plataforma (`SUPER_ADMIN`, `PLATFORM_SUPPORT`) |
| **Pantalla de login** | No había | `Frontend/src/Auth.jsx` |
| **Administración** | — | `Frontend/src/Administration.jsx`: usuarios, roles y grilla de permisos |
| **Idiomas** | Interfaz en inglés | i18n con traducción a español latinoamericano (`es-419.json`), compartida entre la web y la app móvil |
| **Identidad visual** | `VISUAL_IDENTITY.md` basado en este repo | `styles.css` reescrito con los tokens de [`paleta.md`](identidad/paleta.md), logos oficiales en modo claro y oscuro, y cambio de tema. Revisión con las heurísticas de Nielsen en `Frontend/UX_GUIDELINES.md` |
| **App móvil** | No había | `Frontend/mobile/`: app con Expo (hay `eas.json`), misma paleta y mismos textos que la web. **Solo se verificó que compila; no se probó en un dispositivo** |
| **Modelo de riesgo** | Motor de reglas; el modelo de anomalías solo corría en `evaluation/` | El motor de reglas sigue siendo el valor por defecto (`heuristic-v1`). Ahora el servidor puede **cargar un modelo estadístico de anomalías desde un archivo** (`Backend/src/risk/anomaly-model.ts`, con medias y escalas por variable), y cada tenant puede elegir el modelo activo (`Backend/src/ml/`). **Sigue sin haber un modelo de ML entrenado commiteado**: `Backend/models/` solo tiene `.gitkeep` |
| **Datasets** | Ninguno | Se suma `Datasets/` con **dos dominios separados**: tarjetas con [ULB Credit Card Fraud](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) y transferencias con [PaySim](https://www.kaggle.com/datasets/ealaxi/paysim1). Cada uno tiene una partición cronológica 60/20/20. **En el repo solo están el README y los manifiestos**: los `.jsonl` y los CSV crudos están en `.gitignore` |
| **Tests** | 12 en el backend, ninguno en el frontend | Según el conteo de `test(` en los archivos: 21 en el backend (`fraud`, `auth`, `rls`) y 3 en el frontend (`i18n`). **Sin ejecutar** |
| **Deploy** | Supabase + Render | Se suman `Frontend/vercel.json` y `_redirects`. Además hay un documento de arquitectura en la raíz (`fraudlens-arquitectura.md`) |

### Lo que esto implica para el proyecto *(para revisar en equipo, no son decisiones)*

1. **Los datasets no son los de la [decisión 0006](../03-decisiones/0006-tres-datasets-para-el-modelo.md).** La 0006 eligió tres datasets de Kaggle para
   entrenamiento, validación y test. El prototipo usa **otros dos**, ULB y PaySim, con un esquema distinto: un modelo por dominio y la partición dentro de cada uno.
   Hay que decidir cuál vale para el MVP ([P-11](../00-proyecto/preguntas-abiertas.md#p-11)).
2. **Multi-tenant, usuarios, 5 roles y administración van más allá del recorte de la [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md).**
   Hay que contrastarlos con la lista "NO MVP" de [`problema.md`](problema.md) y con el MoSCoW. Como en el relevamiento anterior, **es un dato, no un error**:
   el prototipo no es el MVP.
3. **Con el repo público, los puntos de seguridad de arriba ahora están a la vista de todos.** Sigue sin `LICENSE`, `Frontend/node_modules` sigue commiteado
   (4.484 archivos) y los `.env.example` siguen en el repo. Hay que revisar que no tengan claves reales.
4. **La cita del notebook de Kaggle y la declaración de uso de IA siguen faltando en el repo.** Ningún README nombra a Claude, a Codex ni el notebook.
   El README de la raíz todavía tiene texto con formato de respuesta de una herramienta y rutas absolutas de la máquina de FGR.

## Qué falta

- [x] **¿Dónde vive el código?** → repo de FGR, **público desde el 2026-10-20** (solo los colaboradores hacen cambios), ver arriba. Falta decidir dónde vive **el del MVP** → [P-05](../00-proyecto/preguntas-abiertas.md#p-05)
- [x] Link al repositorio del prototipo
- [x] Qué stack usa realmente → relevado arriba (NestJS + Prisma + PostgreSQL / React + Vite). Qué stack usa **el MVP** sigue abierto → [P-10](../00-proyecto/preguntas-abiertas.md#p-10)
- [x] Qué dataset usa → **ninguno** en el repo; no usa los 3 de la [decisión 0006](../03-decisiones/0006-tres-datasets-para-el-modelo.md) ([P-11](../00-proyecto/preguntas-abiertas.md#p-11))
- [x] Cómo se levanta → `docker compose up --build` desde `Backend/` (y `docker compose exec backend npm run seed` para datos de demo), según el README. **Sin ejecutar**
- [x] Qué casos de uso están implementados → los 7, según el código. **Sin ejecutar**
- [ ] **Ejecutar el prototipo y los 12 tests** para confirmar que lo que dice el código ocurre *(FM, 2026-10-07: "están MDV y FGR"; no es una asignación formal)*
- [ ] **Citar bien el notebook de Kaggle** (título y link) y **declarar el uso de IA** en el repo de FGR
- [ ] Decidir **qué se hace con este código en el MVP** (¿se parte de él o se arranca de cero?) → [P-05](../00-proyecto/preguntas-abiertas.md#p-05)
- [ ] Confirmar con FGR **qué partes generó cada herramienta de IA** (el repo no lo dice)
- [ ] **Probar la app móvil** en un dispositivo o en un emulador *(FGR)*
- [ ] Contrastar multi-tenant, autenticación y roles con la [decisión 0005](../03-decisiones/0005-recorte-alcance-mvp.md) y el MoSCoW
- [ ] Decidir si valen los datasets del prototipo (ULB + PaySim) o los de la [decisión 0006](../03-decisiones/0006-tres-datasets-para-el-modelo.md)
- [ ] Ahora que el repo es público: sacar `Frontend/node_modules`, revisar los `.env.example`, limpiar el README de la raíz y sumar una licencia

## ⚠️ Honestidad académica — hay que dejarlo escrito

El cronograma oficial de la cátedra advierte:

> *"Los actos de **deshonestidad académica** o cualquier situación de indisciplina serán sancionados
> según el régimen disciplinario correspondiente."*

**Nada de lo que se hizo acá es deshonesto** — partir de un notebook público y usar asistentes de IA
es práctica profesional normal. Pero **tiene que estar citado**, y tiene que estar citado **por
nosotros y por escrito**, no descubrirse en la defensa.

Concretamente, el documento final y el pitch tienen que poder responder:

| Pregunta | Dónde se responde |
|---|---|
| ¿De dónde salió la base del modelo? | Notebook de Kaggle, con link y autoría. **En el repo de FGR no está citado con título ni link**; además el repo **no tiene un modelo de ML**: lo que hay es un motor de reglas |
| ¿Qué partes generó una IA y cuáles escribió el equipo? | A documentar con FGR. **El repo no menciona ninguna herramienta de IA** |
| ¿Qué entiende el equipo de ese código? | **Cada integrante tiene que poder defender lo que se muestra en la demo** |
| ¿Qué aportamos nosotros por encima de la base? | Es la pregunta que decide la nota de *innovación tecnológica* |

> 💡 La última fila es la importante. El docente evalúa **"conocimiento y dedicación demostrado en
> el proyecto"** e **"innovación tecnológica"**. Un prototipo generado que nadie puede explicar es
> un riesgo en The Pitch; el mismo prototipo, entendido y documentado, es un activo.

## ⚠️ Y otra cosa: esto es la solución, no el problema

El prototipo se construyó a partir de los requerimientos, y los requerimientos se escribieron
**antes del User Research**.

La Clase 4 fue explícita:

> *"El 90% de las startups fallan **no por mal código, sino por crear algo que nadie necesita**."*
> *"Un prototipo te cuesta días. Un MVP programado te cuesta meses."*

Tener el prototipo andando **no es un problema** — es una ventaja para la demo. Lo que hay que
evitar es que el research termine ajustándose al prototipo en vez de al revés. Si el User Research
dice otra cosa, **gana el research** y el prototipo se corrige.

## Fuentes

- Notebook base: https://www.kaggle.com/code/carmencastrogonzlez/fraud-detection-full-project-in-spanish
- Especificación: [`requerimientos-funcionales-mvp.md`](requerimientos-funcionales-mvp.md)
- Relevamiento del repo (2026-10-07): otro chat de Claude con Claude in Chrome, solo lectura, commit `5f6528c`. Informe completo aportado por FM.
- Actualización (2026-10-20): Claude Code sobre el clon local de FGR, commit `af8c320`, sin ejecutar. El cambio de visibilidad a público lo informó FGR y se verificó con la API de GitHub.
