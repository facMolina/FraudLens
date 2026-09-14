# 6 Sombreros — ¿A qué tipo de cliente apunta FraudLens? (Perfil B)

| | |
|---|---|
| **Decisión** | Redefinir el Perfil B: de "dueño de comercio chico" a "responsable de riesgo/producto en una fintech o banco tradicional" |
| **Fecha** | 2026-09-14 |
| **Participantes** | Decisión charlada en equipo (según FM) · análisis armado por FM con asistencia de Claude Code |
| **Decisión relacionada** | [0004 — Enfoque de cliente: fintechs y bancos tradicionales](../../03-decisiones/0004-enfoque-cliente-fintech-bancos.md) |
| **Pregunta relacionada** | [P-07](../../00-proyecto/preguntas-abiertas.md#p-07) |
| **Estado** | 🟡 En análisis — el 🔴 sombrero rojo lo tiene que escribir el equipo |

> ⚠️ **El 🔴 sombrero rojo es un borrador escrito desde afuera.** Corríjanlo con lo que sienten de
> verdad — ver el criterio de la [decisión 0003](../../03-decisiones/0003-metodo-seis-sombreros.md).

## El problema, en una frase

**El Perfil B decidido el 2/9 ("dueño de comercio chico") ya no representa a quién el equipo quiere
vender FraudLens. El foco real es empresas fintech y bancos tradicionales — ¿cómo se redefine el
perfil sin perder la estructura de los tres niveles del dolor (decide / paga / sufre)?**

---

## ⚪ Sombrero Blanco — Analista racional

| Hecho | Fuente |
|---|---|
| Perfil B fue decidido el 2/9 como "dueño de comercio / e-commerce chico" | [`usuarios.md`](../usuarios.md), marcado ✅ Decidido |
| La identidad visual ya se construyó sobre la hipótesis de que FraudLens es **B2B para fintechs** | [P-07](../../00-proyecto/preguntas-abiertas.md#p-07), aportada por FM el 2026-09-02 |
| El equipo decidió (2026-09-14) que el enfoque real es **fintechs y bancos tradicionales** | FM, en esta sesión |
| El BCRA emitió las **Comunicaciones "A" 8471 (27/08/2026) y "A" 8473 (03/09/2026)**, que obligan a entidades financieras y Proveedores de Servicios de Pago a tener una función de gestión de riesgo de fraude, autoevaluaciones y reportes periódicos | Búsqueda web, 2026-09-14 — [Bruchou & Funes de Rioja](https://bruchoufunes.com/nueva-regulacion-del-bcra-sobre-gestion-del-riesgo-de-fraude-com-a-8471/), [Tavarone Rovelli Salim Miani](https://tavarone.com/comunicaciones-bcra-a-8471-y-a-8473-gestion-y-prevencion-del-riesgo-de-fraude/) |
| El benchmarking ya hecho usó "comercio chico + LatAm" como ángulo, parcialmente cubierto por ClearSale/Tiendanube | [`benchmarking.md`](../benchmarking.md) |
| Hay contenido ya escrito específicamente sobre "dueño de comercio chico" en `ideacion.md`, la narrativa de `problema.md`, y la guía de entrevista de `user-research.md` | Sesión del 2026-09-10 |
| Para el Perfil A (analista), **ML confirmó acceso real** a entrevistados | [`usuarios.md`](../usuarios.md) |
| Para el nuevo Perfil B, **no hay ningún acceso confirmado todavía** | Esta sesión |

### Lo que NO sabemos

- **Si alguien del equipo tiene un contacto real** en una fintech, billetera virtual, pasarela de pago o banco tradicional para entrevistar. No se preguntó todavía.
- **Si "fintech" y "banco tradicional" tienen el mismo proceso de decisión de compra.** Un banco grande y una billetera chica pueden tener ciclos y presupuestos muy distintos — no lo sabemos, no se investigó.
- **Si el nuevo Perfil B es un único rol** (responsable de riesgo/producto) o si en la práctica varía según el tamaño de la empresa.

---

## 🔴 Sombrero Rojo — Mente emocional

> Sin justificar. **Borrador escrito desde afuera — ⬜ el equipo todavía tiene que reescribirlo.**

- **Alivio de coherencia:** el nuevo enfoque encaja con lo que ya se venía construyendo (identidad, hipótesis de FM) — se siente menos como un parche y más como un ajuste que faltaba.
- **Incomodidad de rehacer:** hay documentos enteros (ideación, narrativa, guía de entrevista) escritos sobre "comercio chico" que hay que reescribir. Puede sentirse como trabajo perdido.
- **Preocupación de acceso:** a diferencia del Perfil A, nadie confirmó todavía tener un contacto real en una fintech o banco para el nuevo Perfil B. Puede repetirse el mismo cuello de botella que tuvo el Perfil A antes de que ML confirmara acceso.

### ⬜ PENDIENTE: el equipo tiene que escribir el sombrero rojo

1. ¿Alguien sintió que "comercio chico" nunca terminaba de cerrar, desde el principio?
2. ¿Quién tiene o puede conseguir un contacto real en una fintech, billetera o banco para entrevistar al nuevo Perfil B?
3. ¿Da tranquilidad o presión que la normativa BCRA le dé urgencia real al problema?

**Validado por:** ⬜ *(pendiente)* · **Fecha:** ⬜

---

## ⚫ Sombrero Negro — Crítico estratégico

| Riesgo | Cómo se ve el fracaso |
|---|---|
| **Cero acceso confirmado al nuevo Perfil B** | Mismo problema que tuvo el Perfil A antes del 2/9, pero ahora con menos tiempo antes del parcial (16/9) |
| **"Fintech" y "banco tradicional" pueden ser demasiado distintos como para ser un solo perfil** | El Mapa de Empatía sale genérico o inconsistente si mezcla una billetera chica con un banco grande |
| **Reescribir documentos ya entregados** (ideación, narrativa, benchmarking) sin actualizar todos consistentemente | Quedan contradicciones internas en el documento final — un lector nota que un documento habla de comercio chico y otro de fintechs |
| **Decidir el perfil sin research nuevo, otra vez** | Es el mismo patrón de riesgo que ya señaló el sombrero negro del análisis anterior: elegir antes de tener evidencia |

---

## 🟡 Sombrero Amarillo — Optimista estratégico

- **Coherencia total con lo ya construido.** La identidad visual, la hipótesis de FM y ahora el Perfil B apuntan al mismo lugar — menos re-trabajo estratégico del que parece a primera vista.
- **La normativa BCRA es un gancho de venta real y verificable.** No es una necesidad hipotética: hay una obligación legal concreta (Com. "A" 8471/8473) que las fintechs y bancos tienen que cumplir **ahora**, con etapas hasta 2027.
- **Simplifica el pitch.** Un solo tipo de cliente (empresas reguladas por el BCRA) en vez de mezclar comercios sin regulación con entidades financieras reguladas.

---

## 🟢 Sombrero Verde — Pensamiento creativo

> Sin filtrar ni evaluar.

1. Buscar contactos de Perfil B por LinkedIn, en áreas de riesgo/producto de fintechs y bancos locales.
2. Usar la normativa BCRA como gancho de entrevista: *"¿cómo están encarando la Comunicación 'A' 8471?"*
3. Tratar "fintech chica/billetera virtual" y "banco tradicional grande" como dos variantes dentro del mismo Perfil B, en vez de forzarlos a ser idénticos.
4. Entrevistar a alguien de compliance/legal en vez de riesgo/producto, si resulta más accesible.
5. Preguntarle a ML si sus contactos del rubro (que ya sirven para el Perfil A) conocen a alguien del lado comprador/de riesgo.

---

## 🔵 Sombrero Azul — Director estratégico

### Puntos clave de cada sombrero

| Sombrero | Lo que aportó |
|---|---|
| ⚪ Blanco | El nuevo enfoque es coherente con lo ya construido, y hay normativa BCRA real y reciente que lo sostiene. Pero no hay acceso confirmado al nuevo Perfil B |
| ⚫ Negro | El riesgo central es repetir el cuello de botella de acceso que tuvo el Perfil A, ahora con menos tiempo |
| 🟡 Amarillo | La normativa BCRA da un argumento de venta concreto y verificable, no hipotético |
| 🟢 Verde | Hay varias vías para buscar acceso (LinkedIn, ML, compliance en vez de riesgo) que todavía no se probaron |

### Decisión final

> Se confirma la redefinición del **Perfil B**: pasa de "dueño de comercio / e-commerce chico" a
> **"responsable de riesgo o producto en una fintech, billetera virtual, pasarela de pago o banco
> tradicional"** — sigue siendo "el que paga/decide integrar" la solución, ahora en un rol
> corporativo. El **Perfil C** pasa a ser específicamente **"usuario final de una fintech, billetera
> virtual o pasarela de pago"** (ej. Mercado Pago, Ualá, Modo), en vez de "consumidor" genérico.
>
> Se registra en [decisión 0004](../../03-decisiones/0004-enfoque-cliente-fintech-bancos.md).

### Qué la sostiene

- Es coherente con la identidad visual, con la hipótesis de FM (P-07) y con la normativa BCRA real.
- Mantiene la estructura de tres niveles del dolor (decide / paga / sufre).

### Qué la haría cambiar

- Que el equipo no consiga **ningún** contacto de acceso al nuevo Perfil B en las próximas semanas — ahí habría que evaluar un perfil proxy, igual que se previó para el Perfil A.
- Que el research con el Perfil A revele que el comprador real no es "riesgo/producto" sino otro rol.

### Lo primero que hay que hacer

1. **Preguntar en el equipo si alguien tiene contacto real** en una fintech, billetera, pasarela o banco tradicional, del lado de riesgo/producto/compliance.
2. Actualizar la guía de entrevista del Perfil B en `user-research.md` para el nuevo rol.
3. Si no aparece contacto en un plazo corto, documentar el plan B (perfil proxy) como se hizo con el Perfil A.

---

## Verificación final

- [x] El problema se analizó desde múltiples perspectivas reales
- [x] El blanco **no inventó** ningún dato: lo que falta está listado como falta
- [x] El azul integra las visiones anteriores, sin agregar contenido nuevo
- [ ] ⬜ **El equipo validó el sombrero rojo** *(pendiente)*
- [ ] ⬜ **Alguien confirmó o descartó acceso al nuevo Perfil B** *(pendiente — es la misma bisagra que tuvo el Perfil A)*
