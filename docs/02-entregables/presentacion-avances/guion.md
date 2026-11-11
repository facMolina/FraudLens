# Guion de la presentación de avances (2° Parcial, 11/11)

> Speech por slide, el mismo que está en las notas del orador del [deck](https://claude.ai/artifact/9YuGw3Cw2HDJkb5ncYuWPd).
> Escrito por Claude Code a pedido de MDV; **revisalo y ajustalo con tus palabras**. Lo que va en «Si preguntan» no se dice: es respaldo.
> Tiempo total ≈ 12 min 50 s (supuesto: no hay un tiempo oficial confirmado).
> Mapa, flujos, backlog y MoSCoW se presentan como **propuesta del equipo**, no como decisión cerrada (pedido de FM).

## Reparto

| Presenta | Slides | Tema | Tiempo |
|---|---|---|---|
| ML · Mateo Lewinzon | 1–5 | Portada, avance, problema, usuarios y research | 3:30 |
| FM · Facundo Molina | 6–8 | Hallazgos, alcance y del mapa al backlog | 2:50 |
| FGR · Francisco Guerrero Rojas | 9–12 | Mercado, Océano Azul, UX/UI y arquitectura | 3:20 |
| MDV · Mateo Diaz Valdez | 13–15 | Demo en vivo, proceso y pendientes | 3:10 |
| Todos | 16 | Preguntas | — |

Reparto según el historial de aportes: cada bloque lo presenta quien hizo más de ese contenido. En las preguntas responde quien hizo cada parte: benchmarking, Océano Azul y BMC (FM); arquitectura (ML y MDV); prototipo y datasets (FGR).

## 1. Portada · ML · Mateo Lewinzon (20 s)

Buenas. Somos FraudLens: Mateo Diaz Valdez, Francisco Guerrero Rojas, Mateo Lewinzon y Facundo Molina. Les vamos a mostrar todo lo que avanzamos desde el primer parcial: el problema, lo que aprendimos de los usuarios, el MVP funcionando y lo que nos falta para la entrega final.

## 2. Del 1° Parcial a hoy · ML · Mateo Lewinzon (30 s)

Antes de entrar, qué cambió desde el primer parcial. El 16 de septiembre teníamos solo el prototipo de Francisco; hoy hay un MVP desplegado que decide con IA. La encuesta estaba difundida y sin respuestas; hoy tiene 28 y nos corrigió una hipótesis. Y sumamos la planificación ágil y el diseño de la interfaz. Lo que ya teníamos, las entrevistas, el benchmarking y el modelo de negocio, sigue en pie.

> **Si preguntan:** el estado del 16/9 está en la guía del 1° Parcial, en el repo.

## 3. El problema · ML · Mateo Lewinzon (60 s)

El punto de partida: los sistemas tradicionales de detección de fraude se apoyan en reglas predefinidas, y esas reglas no detectan lo que nadie previó. Lo trabajamos con el Árbol de Problemas y los 5 Por Qué: la causa es que las reglas dependen de una persona que las reconfigura cada vez que aparece algo nuevo. Por eso FraudLens no reemplaza las reglas: asiste al analista, marcándole lo que se les escapa. Y el problema golpea distinto a cada actor: el analista decide sin poder explicar el riesgo, la fintech o el banco queda expuesto ante el BCRA y pierde plata, y el usuario final sufre rechazos o cargos que no reconoce. Con eso escribimos una pregunta ¿Cómo podríamos…? por perfil.

> **Si preguntan:** los 5 Por Qué cerraron en 4 niveles. La narrativa sigue en borrador y le falta un número de respaldo.

## 4. Usuarios · ML · Mateo Lewinzon (50 s)

Segmentamos por rol, en tres perfiles. El A es el analista de fraude: decide, es el usuario directo. El B es la fintech o el banco: paga, es nuestro cliente. El C es el usuario final: sufre el problema. Al principio el perfil B era un comercio chico; el 14 de septiembre cambiamos el foco a fintechs y bancos, en la decisión 0004, con el respaldo de dos comunicaciones del BCRA de este año, la A 8471 y la A 8473.

> **Si preguntan:** el perfil B es una hipótesis; no registramos presupuesto ni disposición a pagar.

## 5. User research · ML · Mateo Lewinzon (50 s)

Para validar aplicamos Design Thinking. Hicimos dos entrevistas en profundidad, una con un analista de fraude y otra con un analista de producto, y una encuesta a usuarios finales que juntó 28 respuestas. Los dos analistas pidieron lo mismo: menos falsos positivos, que cada alerta traiga las señales que la explican, y la información centralizada. Con eso armamos las User Persona y los Mapas de Empatía. Y somos honestos con el límite: el plan pedía dos o tres entrevistas por perfil y hicimos una, y los mapas tienen huecos marcados donde no hay evidencia.

> **Si preguntan:** un falso positivo es una operación legítima marcada como fraude. El cuadrante ¿Qué oye? quedó vacío en los 3 mapas. La encuesta apuntaba a 80-100 respuestas.

## 6. Hallazgos de la encuesta · FM · Facundo Molina (70 s)

Esta es la slide que más nos importa, porque la evidencia contradijo nuestra hipótesis. Creíamos que al usuario lo que más le molesta es que le rechacen una compra legítima. Pero cuando preguntamos qué es peor, 19 de 28 eligieron que les aprueben una operación que no hicieron, y solo uno eligió el rechazo. El segundo dato: 21 de 28 recibieron una explicación poco clara o ninguna, y nadie marcó una explicación clara. Lo contamos con storytelling con datos porque este dato cambia la historia: la explicación de cada decisión pasa a ser el centro del producto. Los límites: la muestra es autoseleccionada y joven, 22 de 28 tienen entre 18 y 34 años, y el análisis todavía no lo validó todo el equipo.

## 7. Solución y alcance · FM · Facundo Molina (50 s)

Para definir el alcance usamos User Story Mapping sobre el día del analista, en cinco pasos: ver la cola, encontrar los casos que importan, abrir un caso, entender por qué y actuar. Lo cortamos en tres releases. La primera es el MVP: nueve tareas, un solo rol, el analista, y configuración fija, como decidimos en la 0005. Alertas, explicabilidad avanzada, umbrales en vivo y reentrenamiento quedan para la segunda, y el resto para la tercera. Es una propuesta del equipo: falta validarla entre los cuatro.

> **Si preguntan:** el Story Map es un borrador mío; falta que lo validemos entre los cuatro.

## 8. Del mapa al backlog · FM · Facundo Molina (50 s)

Del mapa bajamos al backlog, también como propuesta del equipo. Hicimos cinco User Flows, uno por cada paso del recorrido, con sus caminos alternativos, por ejemplo qué ve el analista si no hay transacciones. Escribimos un Product Backlog de 14 historias de usuario con criterios Dado, Cuando, Entonces, todavía sin estimar. Y con MoSCoW unificamos en una sola lista los 16 ítems que quedan fuera del MVP. Para cerrarlo falta que el equipo valide el mapa y los flujos, clasificar las tareas con MoSCoW, resolver qué hacemos con las historias que no tienen al analista como actor y elegir dónde registramos el backlog.

> **Si preguntan:** (1) Historias sin el analista: yo cuento 5, HU-07 a HU-10 y HU-14; el backlog dice que de HU-07 a HU-14 tienen otro actor (el sistema cliente) o ninguno claro. Es la pregunta abierta P-32. (2) Herramienta: la opción en análisis es Trello, en la lista Backlog con una etiqueta HU; falta el sombrero rojo de los cuatro y la decisión. (3) Sin estimar: no usamos Story Points todavía.

## 9. Mercado y negocio · FGR · Francisco Guerrero Rojas (50 s)

En el benchmarking relevamos seis competidores: Sift, Feedzai, Forter, Signifyd, Riskified y ClearSale. Ninguno se posiciona como complemento de un antifraude que el cliente ya tiene: compiten para ser el sistema. Ese es nuestro lugar. En el Business Model Canvas, el modelo de monetización es una suscripción SaaS B2B: paga la fintech o el banco y la usa el analista. Como referencia, el mercado cobra entre 99 y 500 dólares por mes, o entre 2.000 y 10.000, según la categoría. Son precios de otros, no una cotización nuestra, y el modelo sigue siendo una hipótesis.

> **Si preguntan por el P&L:** no está hecho, es pendiente para el 18/11.

## 10. Océano Azul · FGR · Francisco Guerrero Rojas (50 s)

Con la estrategia del Océano Azul armamos la curva de valor: los factores en los que compite la industria, competidor por competidor. Y la curva nos corrigió. En la ideación pensábamos que la explicabilidad era nuestro espacio libre, pero resultó ser tendencia de toda la industria en 2026: no es un hueco. Lo que sí queda libre es ser complemento: ninguno de los seis lo ofrece. Con las cuatro acciones lo bajamos a producto: eliminar la configuración manual de reglas, reducir los falsos positivos y los casos a revisión, incrementar la explicación para el analista y crear ese rol de complemento.

> **Si preguntan:** los signos de pregunta son celdas sin evidencia, no ceros. La columna FraudLens y las 4 acciones son hipótesis de ideación, todavía en borrador.

## 11. Diseño UX/UI · FGR · Francisco Guerrero Rojas (50 s)

En diseño UX/UI fuimos de la identidad a la interfaz. Primero la identidad visual: logo y paleta violeta, decididos el 9 de septiembre, con una regla de accesibilidad: el color nunca va solo, cada nivel de riesgo lleva color, forma y texto. Después, wireframes de baja fidelidad en Figma: dos pantallas de concepto. El prototipo clickeable que armé lo revisamos con las heurísticas de Nielsen. Y esa interfaz se migró al MVP, con modo claro y oscuro.

> **Si preguntan:** los wireframes quedaron en 2 de 9 porque la interfaz real del prototipo los reemplazó.

## 12. Cómo está construido · FGR · Francisco Guerrero Rojas (50 s)

Así está construido el MVP. La interfaz manda la transacción a la API; la API busca en MongoDB hasta 50 transacciones aprobadas del mismo usuario como contexto y le pide la decisión al modelo a través de un contrato propio, DecisionModel. Hoy ese contrato usa Groq, un modelo de lenguaje. Vuelve aprobada o rechazada, con motivos, señales y un puntaje, y queda en el historial. Todo en Next.js con TypeScript, en un solo deploy en Vercel. El contrato nos deja cambiar de proveedor sin tocar la API.

> **Si preguntan:** (1) el modelo entrenado de la decisión 0006 no está; decidir LLM, modelo entrenado o los dos es la decisión abierta. (2) MongoDB: es el stack definido del MVP; la 0007, con PostgreSQL, era para el prototipo. (3) El CI está en rojo por un bloqueo de facturación de GitHub, no por el código.

## 13. Demo en vivo · MDV · Mateo Diaz Valdez (90 s)

Vamos a verlo en vivo. [Pasar al navegador: fraudlens-two.vercel.app] Cargo una transacción de ejemplo: usuario, comercio, monto y un país distinto al de la tarjeta. Guardo, y la IA responde: aprobada o rechazada, con los motivos en lenguaje natural y las señales, por ejemplo país distinto al de la tarjeta o falta de historial. Queda guardada en el historial. Fíjense que es lo que pedían los usuarios en la encuesta: que cada decisión venga explicada.

> **Plan B:** si falla la red o la IA, mostrar esta captura, que es una evaluación real ya guardada. Si la IA falla, la API devuelve 503 y no guarda nada.

## 14. Cómo trabajamos · MDV · Mateo Diaz Valdez (50 s)

Cómo trabajamos. Todo vive en un repositorio que funciona como centro de cómputos: siete decisiones numeradas y siete análisis con los 6 Sombreros que pidió el docente, 32 entradas de bitácora, 81 aportes registrados con quién hizo qué y nueve clases documentadas con su aplicación al proyecto. El tablero es un Kanban en Trello, con límite de tarjetas en curso por persona. Definimos roles de equipo en lugar de Product Owner y Scrum Master, y tenemos una plantilla de retrospectiva. El código vive aparte, con siete pull requests integrados, y la declaración de uso de IA está al día.

> **Si preguntan:** los análisis de 6 Sombreros están en borrador; el sombrero rojo lo escribe el equipo.

## 15. Lo que falta para el 18/11 · MDV · Mateo Diaz Valdez (50 s)

Para la entrega del 18 nos falta: decidir qué modelo de IA usamos, el modelo de lenguaje, el entrenado de la decisión 0006 o los dos, registrar las retrospectivas y las Sprint Reviews, que no documentamos, y validar entre los cuatro el mapa, los flujos y el backlog: la clasificación MoSCoW, las historias que no son del analista y la herramienta. En la documentación, el Problem Statement, los OKR y KPI, y el P&L. El modelo de negocio ya está: lo que falta es ponerle números, los costos en horas-hombre y los ingresos. Y en el MVP, los tests de integración real y el CI en verde. Preferimos mostrar los huecos antes que inventar datos. ¿Preguntas?

## 16. Preguntas · Todos

Respuestas preparadas:

1. ¿Por qué un LLM y no el modelo entrenado? Es lo que se pudo construir y probar a tiempo; el contrato DecisionModel permite sumar el modelo entrenado sin tocar la API. La decisión es del equipo y está abierta.
2. ¿Por qué MongoDB? Es el stack definido del MVP (Next.js, MongoDB Atlas y Vercel); la decisión 0007, con PostgreSQL, era para el prototipo.
3. ¿Cuántos usuarios validaron? Dos entrevistas (una por perfil A y B) y 28 encuestas; menos de lo planeado, y lo decimos.
4. ¿Qué los diferencia? El posicionamiento como complemento del antifraude existente; la explicabilidad sola es tendencia de la industria. Sigue siendo hipótesis.
5. ¿La interfaz es propia? Viene del prototipo de FGR, generado con Codex, y se migró al MVP; está declarado en la declaración de uso de IA.
6. ¿Por qué el CI está en rojo? Bloqueo de facturación de la cuenta de GitHub, no un error del código.
7. ¿Qué cambió desde el 1° Parcial? Enfoque fintech y bancos, encuesta con 28 respuestas, recorte del MVP y un MVP desplegado que decide con IA.
