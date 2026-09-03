# El problema

> Estado: 🟡 **Iniciado.** Lo que está acá viene de la planilla del docente y de la Clase 1.
> Falta todo el User Research, que es lo que le da sustento real.

## Cómo llegamos acá

| Clase | Qué pasó |
|---|---|
| **Clase 2** | El equipo expuso las ideas de problema que tenía. Todavía se evaluaban varios proyectos |
| **Clase 3** | Se decidió por este sistema. **El docente lo aprobó** |
| **Clase 4** | Se escribieron los [requerimientos funcionales del MVP](requerimientos-funcionales-mvp.md) y se definió el nombre **FraudLens** |

> ⚠️ El **User Research todavía no se hizo**. Las herramientas de la Clase 4 (User Persona, Mapa de
> Empatía, Escenario Actual) están pendientes, y son la consigna para la Clase 5.
> Ver [P-12](../00-proyecto/preguntas-abiertas.md#p-12).

## Enunciado (planilla del docente)

Los sistemas tradicionales de detección de fraude suelen apoyarse en **reglas predefinidas**, que
pueden resultar insuficientes para identificar comportamientos anómalos que no fueron contemplados
previamente.

Existe la oportunidad de **complementar** estas reglas mediante modelos de inteligencia artificial
capaces de analizar patrones históricos y características de cada transacción para detectar
operaciones potencialmente fraudulentas.

## Objetivo

Desarrollar un prototipo capaz de analizar transacciones **en tiempo real** y estimar su nivel de
riesgo de fraude mediante un modelo de IA entrenado con datos históricos, permitiendo identificar
comportamientos anómalos y **asistir en la decisión de aprobar, rechazar o revisar** una operación.

## Hipótesis de trabajo sobre el usuario

> 📌 **Aportada por FM el 2026-09-02. No está validada ni decidida en equipo.**

FraudLens sería un producto **B2B para empresas fintech** que manejan tráfico de transacciones:
integran nuestro sistema como **complemento** de su antifraude actual, sumando un filtro más
específico gracias a la IA, más un **dashboard de revisión** para su equipo.

Si se confirma: el **cliente** que paga es la fintech; los **usuarios** que lo usan todos los días
son los analistas de su equipo de fraude.

Queda registrada acá para que sea explícita y contrastable contra el research, no para darla por
cierta. Ver [P-07](../00-proyecto/preguntas-abiertas.md#p-07).

## Lo que todavía no sabemos

El enunciado describe una **oportunidad tecnológica**, no todavía un problema con dueño. Para que
sea un problema del TIF hace falta responder:

| Pregunta | Por qué importa |
|---|---|
| **¿A quién le duele?** ¿Un analista de fraude? ¿Un comercio chico? ¿Un banco? | Define el usuario, la interfaz y todo el User Research → [P-07](../00-proyecto/preguntas-abiertas.md#p-07) |
| **¿Cuánto duele?** ¿Cuánta plata o cuánto tiempo se pierde hoy? | Es la evidencia que justifica el proyecto |
| **¿Cómo lo resuelven hoy?** | Sin entender el sistema actual, no podemos decir que lo mejoramos |
| **¿Por qué no está resuelto?** | Si fuera fácil ya existiría. La respuesta es parte de la diferenciación |

Estas se responden con **User Research con datos reales** — exigencia explícita del docente.

## Reformular como "¿Cómo podríamos nosotros…?" *(Clase 4)*

El docente enseñó una fórmula para pasar de una descripción vaga a un problema específico:

| ❌ En lugar de | ✅ Definí |
|---|---|
| "Hacer una app de dietas" | "¿Cómo podríamos ayudar a **estudiantes universitarios sin tiempo** a planificar comidas saludables **con presupuesto limitado**?" |

Nuestro enunciado actual describe una **oportunidad tecnológica**, no un usuario con una restricción.

> ⚠️ **Por qué son 3 versiones y no una.** Esta fórmula normalmente se escribe **después** de
> Empatizar, como síntesis de entrevistas reales. Nosotros todavía tenemos **0 entrevistas hechas**,
> así que lo de abajo **no es un insight validado — es una hipótesis de trabajo**, construida sólo
> con lo que ya sabemos con certeza (la planilla del docente y la decisión de
> [los 3 perfiles](usuarios.md)), sin inventar dolores que todavía no confirmamos. Además,
> [P-07](../00-proyecto/preguntas-abiertas.md#p-07) —quién es *el* usuario objetivo del MVP— sigue
> abierta: elegir una sola reformulación hoy sería adelantar esa respuesta sin evidencia, que es
> justo el sesgo que nombró el
> [sombrero rojo](analisis/6-sombreros-usuario-objetivo.md#-sombrero-rojo--mente-emocional).
> Por eso hay una reformulación **por perfil**, igual que va a haber un User Persona por perfil.
>
> **Se corrige** en cuanto haya entrevistas reales — sobre todo la del perfil A, que depende de los
> contactos de ML.

### A — Analista de fraude *(el que decide)*

> **¿Cómo podríamos ayudar a analistas de fraude que deciden aprobar, rechazar o revisar
> transacciones a detectar los casos que las reglas predefinidas no contemplan?**

Fuente: planilla del docente (*"reglas predefinidas... insuficientes para identificar
comportamientos anómalos"*) + rol descripto en [usuarios.md](usuarios.md#perfil-a--analista-de-fraude).

### B — Dueño de comercio / e-commerce chico *(el que paga)*

> **¿Cómo podríamos ayudar a un dueño de comercio o e-commerce chico, sin equipo ni presupuesto
> para prevención de fraude, a reducir lo que pierde en contracargos y ventas fraudulentas?**

Fuente: [usuarios.md](usuarios.md#perfil-b--dueño-de-comercio--e-commerce-chico).

### C — Consumidor *(el que lo sufre)*

> **¿Cómo podríamos evitar que a un consumidor le rechacen una compra legítima o le aprueben una
> fraudulenta, sin que tenga forma de intervenir en esa decisión?**

Fuente: [usuarios.md](usuarios.md#perfil-c--consumidor-con-fraude-o-rechazo-indebido).

### Estado

✅ Reformuladas las 3 — pendiente de corregirse con entrevistas reales. No cierra P-07.

## El ángulo del proyecto

De la Clase 1, la **brecha de innovación** (la paradoja de la maleta con ruedas): la rueda existe
desde el 3500 A.C. y la maleta desde el 600 D.C., pero la maleta con ruedas recién apareció en 1970.

FraudLens está en la misma situación: los **motores de reglas** antifraude existen hace décadas y el
**machine learning** también. No inventamos ninguna pieza. El valor está en **integrarlas** de una
forma que hoy no está resuelta para nuestro usuario.

Es un buen argumento para el pitch, y sale del propio material del docente.

## El ángulo opuesto (pensamiento lateral)

También de la Clase 1: *para cada idea lógica, existe una idea opuesta que también puede ser válida*.

| Enfoque lógico | Enfoque opuesto |
|---|---|
| **Detectar fraude** — buscar el 0,1% malo | **Certificar operaciones legítimas** — acelerar el 99,9% bueno |
| Métrica: fraudes detectados | Métrica: fricción evitada a clientes legítimos |
| Usuario: el que investiga | Usuario: el que quiere vender sin frenar la operación |

Vale ponerlo sobre la mesa antes de cerrar la solución. Puede que lo descartemos, pero **haberlo
considerado y documentado por qué lo descartamos suma** en el documento entregable.

## Alcance del MVP

> Se completa cuando definamos el usuario. Por ahora, la hipótesis de trabajo:

**Sí es MVP:**
- Recibir una transacción y devolver un **score de riesgo**
- Mostrar las transacciones y su nivel de riesgo en una **pantalla**
- Un modelo entrenado con datos históricos

**No es MVP:**
- Reentrenamiento automático del modelo
- Múltiples clientes / multi-tenant
- Alertas por mail o notificaciones
- Panel de administración de usuarios y permisos
- Integraciones con procesadores de pago reales
- Explicabilidad avanzada del modelo

> Recordar el caso Uber de la Clase 1: el MVP no sólo recorta funciones, **recorta el alcance**.
> UberCab era una ciudad, una función.

## Chequeo contra "Problemas que NO"

El docente descartó explícitamente: reservas en general, estacionamiento, cómo viajar, filas y
turnos, pedidos y tiendas online, pagos de colegio o renta, calcular/dividir/medir gastos,
información de estudios médicos e historia clínica, gestores de biblioteca / taller mecánico /
edificio o cualquier ABM, mascotas perdidas y refugios, gimnasios, trackeo de camiones/perros/pedidos,
y qué cocinar con lo que hay en la heladera.

**FraudLens no cae en ninguna de esas categorías.** ✅
