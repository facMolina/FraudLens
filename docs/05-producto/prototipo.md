# Prototipo de FraudLens

> **Estado:** 🟡 existe, pero **no está documentado ni versionado** en este repositorio.
> **Autor:** Francisco Daniel Guerrero Rojas (FGR)
> **Registrado acá:** 2026-09-02 por FM, a partir de lo que FGR compartió por WhatsApp.

## Qué hay

Francisco armó un prototipo funcional de FraudLens:

| Parte | Cómo se hizo |
|---|---|
| **Backend** | Generado con **Claude** |
| **Frontend** | Generado con **Codex** y después ajustado al backend ya desarrollado |
| **Base técnica** | Notebook de Kaggle: [*Fraud Detection Full Project in Spanish*](https://www.kaggle.com/code/carmencastrogonzlez/fraud-detection-full-project-in-spanish), de `carmencastrogonzlez` |
| **Especificación** | Se le pasó el documento [*FraudLens — Requerimientos funcionales del MVP*](requerimientos-funcionales-mvp.md) (escrito por ML) y de ahí salió todo |

## Qué falta

- [ ] **¿Dónde vive el código?** ¿Repo de GitHub, carpeta local, otra cosa? → [P-05](../00-proyecto/preguntas-abiertas.md#p-05)
- [ ] Link al repositorio del prototipo
- [ ] Qué stack usa realmente (lenguaje, framework, librerías) → [P-10](../00-proyecto/preguntas-abiertas.md#p-10)
- [ ] Qué dataset usa y si es el mismo "dataset de casos de prueba" del que habló el equipo → [P-11](../00-proyecto/preguntas-abiertas.md#p-11)
- [ ] Cómo se levanta y se prueba
- [ ] Qué casos de uso del documento de ML están implementados y cuáles no

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
| ¿De dónde salió la base del modelo? | Notebook de Kaggle, con link y autoría |
| ¿Qué partes generó una IA y cuáles escribió el equipo? | A documentar |
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
