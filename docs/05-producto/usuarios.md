# Los 3 perfiles de usuario a investigar

| | |
|---|---|
| **Estado** | ✅ **Decidido** por el equipo (2026-09-02) · Perfil B y C **redefinidos** el 2026-09-14 |
| **Ticket** | [1. Decidir los 3 perfiles de usuario](https://trello.com/c/IYegyoM6) |
| **Método** | [Análisis de 6 Sombreros (2/9)](analisis/6-sombreros-usuario-objetivo.md) · [Análisis de 6 Sombreros — enfoque fintech (14/9)](analisis/6-sombreros-enfoque-fintech.md) |
| **Bloquea a** | Plan de research · User Persona ×3 · Mapa de Empatía ×3 · Problem Statement |

> 🔄 **2026-09-14 — Perfil B y C redefinidos.** El equipo decidió que el enfoque del proyecto es
> llegar a **empresas fintech y bancos tradicionales**, no comercio chico. Ver
> [decisión 0004](../../03-decisiones/0004-enfoque-cliente-fintech-bancos.md). Lo que sigue abajo
> ya refleja esa redefinición; la versión original del 2/9 (comercio chico) queda documentada en el
> [análisis de 6 sombreros del 2/9](analisis/6-sombreros-usuario-objetivo.md) como parte del
> historial de la decisión.

## La decisión

**Tres perfiles en tres niveles distintos del mismo problema**, con la accesibilidad como filtro
duro.

No son tres variantes del mismo usuario: son tres personas que viven el fraude desde lugares
estructuralmente diferentes. Uno lo **sufre**, otro lo **decide**, otro lo **paga**. Por eso los
tres Mapas de Empatía van a salir genuinamente distintos, que es lo que pide la consigna.

| | Perfil | Rol en el problema | Cómo se investiga | Acceso |
|---|---|---|---|---|
| **A** | **Analista de fraude** (dentro de la fintech/banco cliente) | El que **decide**: revisa la cola de casos y aprueba, rechaza o escala | Entrevistas en profundidad | ✅ **Nicolás entrevistado** |
| **B** | **Analista de producto en una fintech, billetera virtual, pasarela de pago o banco tradicional** | El que **paga/decide integrar** FraudLens | Entrevistas | ✅ **Agustín identificado** |
| **C** | **Usuario final de una fintech, billetera virtual o pasarela de pago** (ej. Mercado Pago, Ualá, Modo) con fraude o rechazo indebido | El que lo **sufre**: le clonan la tarjeta, o le rechazan una compra legítima | Encuesta | ✅ **Tobías identificado** |

### Perfil A — Analista de fraude

**Es el usuario directo del producto.** Es quien va a tener el dashboard abierto varias horas por
día y quien toma la decisión que FraudLens asiste.

- **Qué buscamos entender:** cómo es hoy su cola de trabajo, con qué herramientas decide, cuánto
  tarda por caso, qué información le falta en el momento de decidir, y qué pasa cuando se equivoca
  en cada dirección.
- **Acceso:** ✅ **ML confirmó que consigue entrevistas** en las próximas dos semanas. Es el activo
  más valioso del research y hay que usarlo bien: son pocas entrevistas y no se repiten.
- **Por qué importa que sea entrevista y no encuesta:** lo que necesitamos de él es el *proceso* y
  las *excepciones*, y eso no entra en un formulario.

### Perfil B — Analista de producto en una fintech o banco tradicional

**Es quien pone la plata.** Trabaja en una fintech, billetera virtual, pasarela de pago o banco
tradicional, y es quien evalúa e integra una solución antifraude como FraudLens.

> 🔄 **Redefinido el 2026-09-14** — antes era "dueño de comercio/e-commerce chico". Ver
> [decisión 0004](../../03-decisiones/0004-enfoque-cliente-fintech-bancos.md) y el
> [análisis de 6 sombreros](analisis/6-sombreros-enfoque-fintech.md).

- **Qué buscamos entender:** cómo gestiona hoy el riesgo de fraude, qué le exige la normativa (las
  Comunicaciones "A" 8471 y "A" 8473 del BCRA obligan a tener una función de gestión de riesgo de
  fraude), y cuál de los dos errores le duele más — dejar pasar un fraude o rechazar un cliente
  bueno.
- **Por qué está:** es el perfil que conecta el problema con el **modelo de negocio**. Sirve
  directo para la Clase 6 (BMC).
- ✅ **Agustín entrevistado.**

### Perfil C — Usuario final de una fintech, billetera virtual o pasarela de pago

**Es quien sufre el problema en el cuerpo**, y el único perfil al que podemos llegar en volumen.

> 🔄 **Redefinido el 2026-09-14** — antes era "consumidor" genérico. Ahora es específicamente
> alguien que usa una fintech/billetera/pasarela (ej. Mercado Pago, Ualá, Modo). Ver
> [decisión 0004](../../03-decisiones/0004-enfoque-cliente-fintech-bancos.md).

- **Qué buscamos entender:** la experiencia del fraude vivido, y sobre todo **el falso positivo** —
  que te rechacen una compra o transferencia legítima en el peor momento. Es el costo invisible que
  nadie mide.
- **Por qué está:** hace que el research tenga **datos reales en cantidad**, que es lo que el
  docente exige, sin depender de conseguir entrevistas.

## Qué se descartó y por qué

| Descartado | Motivo |
|---|---|
| **Administrador del sistema** | Es un **rol de configuración**, no una persona con un dolor propio. Su User Persona y su Mapa de Empatía saldrían vacíos: no sufre el problema, sólo opera la herramienta. Sigue existiendo como actor del software, pero no es sujeto de research. |
| **Sistema cliente** (la API que consume) | No es una persona. No se le puede hacer un mapa de empatía. |
| **Tres analistas de fraude** (3 personas del mismo perfil) | El docente confirmó que pide **3 perfiles distintos**, no 3 personas del mismo. Ver [P-18](../00-proyecto/preguntas-abiertas.md#p-18). |

## ⚠️ El sesgo que hay que vigilar

Del sombrero rojo del análisis, y queda escrito acá para que no actúe en silencio:

> **Hay tentación de elegir el usuario que le queda cómodo al prototipo que ya existe**, en vez del
> que le conviene al proyecto.

El equipo escribió los requerimientos y armó un prototipo **antes** de saber para quién — que es
exactamente lo que la Clase 4 advierte que hace fallar al 90% de las startups. Este research existe
para corregir eso, no para justificarlo.

**Regla que se desprende:** si el research contradice los
[requerimientos](requerimientos-funcionales-mvp.md) o la
[identidad visual](identidad/propuesta-canva.md), se corrigen **esos documentos**, no el research.

## Relación con P-07

El **tipo de cliente** (empresas fintech y bancos tradicionales, no comercio chico) quedó decidido
por el equipo el 2026-09-14 — ver [decisión 0004](../../03-decisiones/0004-enfoque-cliente-fintech-bancos.md).

Pero esto **no cierra del todo** [P-07](../00-proyecto/preguntas-abiertas.md#p-07): falta confirmar
si *el* usuario objetivo del MVP (a quién se le diseña la interfaz, el dashboard, el pitch) es el
Perfil A (analista) o el Perfil B (quien decide integrarlo) — eso sigue siendo una conclusión que
sale **del research**, no de antes.

## Estado del ticket

| Ítem | Estado |
|---|---|
| ML respondió sobre el acceso a expertos | ✅ Hay acceso |
| P-18 preguntada al docente | ✅ Son 3 perfiles distintos |
| Los 3 perfiles escritos | ✅ Este documento |
| El equipo validó el sombrero rojo | ⬜ **Pendiente** — ver [puntos a debatir](analisis/6-sombreros-usuario-objetivo.md#-pendiente-el-equipo-tiene-que-escribir-el-sombrero-rojo) |
