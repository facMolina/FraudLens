# Los 3 perfiles de usuario a investigar

| | |
|---|---|
| **Estado** | ✅ **Decidido** por el equipo (2026-09-02) |
| **Ticket** | [1. Decidir los 3 perfiles de usuario](https://trello.com/c/IYegyoM6) |
| **Método** | [Análisis de 6 Sombreros](analisis/6-sombreros-usuario-objetivo.md) |
| **Bloquea a** | Plan de research · User Persona ×3 · Mapa de Empatía ×3 · Problem Statement |

## La decisión

**Tres perfiles en tres niveles distintos del mismo problema**, con la accesibilidad como filtro
duro.

No son tres variantes del mismo usuario: son tres personas que viven el fraude desde lugares
estructuralmente diferentes. Uno lo **sufre**, otro lo **decide**, otro lo **paga**. Por eso los
tres Mapas de Empatía van a salir genuinamente distintos, que es lo que pide la consigna.

| | Perfil | Rol en el problema | Cómo se investiga | Acceso |
|---|---|---|---|---|
| **A** | **Analista de fraude** | El que **decide**: revisa la cola de casos y aprueba, rechaza o escala | Entrevistas en profundidad | ✅ **Confirmado por ML** |
| **B** | **Dueño de comercio / e-commerce chico** | El que **paga**: absorbe el fraude y los contracargos | Entrevistas | Accesible sin contactos especiales |
| **C** | **Consumidor** con fraude o rechazo indebido | El que lo **sufre**: le clonan la tarjeta, o le rechazan una compra legítima | Encuesta | Masivamente accesible |

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

### Perfil B — Dueño de comercio / e-commerce chico

**Es quien pone la plata.** No tiene equipo antifraude ni presupuesto para uno: come el contracargo
o pierde la venta.

- **Qué buscamos entender:** cuánto le cuesta el fraude en plata real, qué hace hoy al respecto
  (probablemente poco o nada), y cuál de los dos errores le duele más — dejar pasar un fraude o
  rechazar un cliente bueno.
- **Por qué está:** es el perfil que conecta el problema con el **modelo de negocio**. Sirve
  directo para la Clase 6 (BMC).

### Perfil C — Consumidor con fraude o rechazo indebido

**Es quien sufre el problema en el cuerpo**, y el único perfil al que podemos llegar en volumen.

- **Qué buscamos entender:** la experiencia del fraude vivido, y sobre todo **el falso positivo** —
  que te rechacen una compra legítima en el peor momento. Es el costo invisible que nadie mide.
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

Esto **no cierra** [P-07 (¿quién es el usuario objetivo?)](../00-proyecto/preguntas-abiertas.md#p-07).

Lo que se decidió acá es **a quién investigar**. Quién termina siendo *el* usuario objetivo del MVP
es una conclusión que sale **del research**, no de antes. La hipótesis de FM —que el usuario es el
equipo de fraude de una fintech— coincide con el perfil A, y el research la va a confirmar o a
tirar abajo.

## Estado del ticket

| Ítem | Estado |
|---|---|
| ML respondió sobre el acceso a expertos | ✅ Hay acceso |
| P-18 preguntada al docente | ✅ Son 3 perfiles distintos |
| Los 3 perfiles escritos | ✅ Este documento |
| El equipo validó el sombrero rojo | ⬜ **Pendiente** — ver [puntos a debatir](analisis/6-sombreros-usuario-objetivo.md#-pendiente-el-equipo-tiene-que-escribir-el-sombrero-rojo) |
