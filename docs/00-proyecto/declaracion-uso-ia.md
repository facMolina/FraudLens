# Declaración de Uso de Inteligencia Artificial — FraudLens

| | |
|---|---|
| **Proyecto** | FraudLens — Sistema inteligente de detección de fraude en transacciones en tiempo real |
| **Materia** | Seminario de Gestión Tecnológica — TIF, 2C 2026 |
| **Equipo** | Diaz Valdez, Mateo (1192969) · Guerrero Rojas, Francisco Daniel (1042529) · Lewinzon, Mateo (1151641) · Molina, Facundo Roman (1115862) |
| **Fecha** | 2026-09-15 *(documento vivo — se actualiza cada vez que cambia el uso de IA)* |
| **Marco normativo** | [Lineamientos de Uso de Inteligencia Artificial — UADE](https://dre.uade.edu.ar/PDFs/lineamientosiaalumnos1.pdf), sección *"Uso de IA en Trabajos Integradores Finales, Trabajos Finales de Investigación, Proyectos Finales de Ingeniería"* |

> Esta declaración se presenta porque el lineamiento de la UADE la exige de forma **obligatoria**
> para TIF: *"Los alumnos deberán presentar una declaración informando si se utilizaron
> herramientas de IA."* La omisión, o presentar información falsa o engañosa, se considera falta a
> la integridad académica — la declaración en sí **no penaliza**.

## Herramientas utilizadas

| Herramienta | Quién la usó | Para qué |
|---|---|---|
| **Claude** (chat web) | Los 4 integrantes del equipo | Consultas de estudio, redacción y comprensión de conceptos de la materia — uso instrumental |
| **Claude Code** | Facundo Molina (FM), con validación del equipo en cada sesión | Construcción y mantenimiento de este repositorio: documentación de clases, decisiones, diseño del research, identidad visual, benchmarking, ideación, revisión de requerimientos |
| **Claude** | Francisco Guerrero Rojas (FGR) | Generación del **backend** del prototipo de FraudLens |
| **Codex** | Francisco Guerrero Rojas (FGR) | Generación del **frontend** del prototipo, ajustado al backend ya generado |

## Alcance del uso, por etapa

| Etapa / entregable | Herramienta | Qué se generó con IA | Qué hizo el equipo |
|---|---|---|---|
| Documentación de clases (`docs/01-clases/`) | Claude Code | Redacción de notas trabajadas a partir del material crudo cargado por el equipo | El equipo aportó el material fuente y la bajada a FraudLens se basa en decisiones y hechos que el equipo confirmó en sesión |
| Identidad visual (logo, paleta, tipografía) | Claude Code | Exploración de símbolos, medición de contraste WCAG, presentación en Canva, reconstrucción de los assets finales del logo | El equipo votó entre las 3 propuestas finales y aprobó la decisión final |
| Plan de research, benchmarking, ideación, Árbol de Problemas/5 Por Qué | Claude Code | Redacción de los documentos, búsqueda web para benchmarking y normativa citada | FM corrigió cada punto en vivo (ver `bitacora/2026-09-14-*.md`); ninguna afirmación fáctica quedó sin fuente marcada |
| Revisión de requerimientos funcionales del MVP | Claude Code | Análisis de los puntos a discutir, propuesta de recorte de alcance | El equipo definió las respuestas de fondo (roles, alcance, qué es MVP); Claude Code documentó y estructuró |
| Documentación del dataset del MVP (`datos.md`) | Claude Code | Investigación web para identificar qué dataset usa cada notebook candidato y sus características (registros, columnas, licencia), marcando qué quedó confirmado con fuente y qué no | **FGR decidió** usar 3 datasets y el rol de cada uno (entrenamiento / validación y explicabilidad / test final) — no fue una sugerencia del asistente |
| Prototipo — backend | Claude | Código del backend a partir del documento de requerimientos y un notebook de Kaggle citado | FGR es responsable de entender, ejecutar y poder defender el código |
| Prototipo — frontend | Codex | Código del frontend, ajustado al backend | FGR es responsable de entender, ejecutar y poder defender el código |
| Documento de requerimientos funcionales del MVP | — | Escrito por Mateo Lewinzon (ML) | Sin asistencia de IA declarada por el autor a la fecha de este documento |

## Procesos de validación

Este repositorio tiene reglas propias, escritas desde el inicio del proyecto (`CLAUDE.md`), que
funcionan como control de validación sobre el uso de IA:

- **"No deducir nada."** Ninguna afirmación fáctica se completa sin fuente. Lo que no se sabe se
  marca explícitamente como falta (⬜), nunca se rellena "porque tendría sentido".
- **El sombrero rojo (emociones) del método de 6 Sombreros lo escribe siempre el equipo**, nunca
  la IA — está documentado así en cada análisis (`docs/05-producto/analisis/`).
- **Cada documento generado se revisó y corrigió en vivo** antes de darlo por cerrado. Ejemplos con
  fecha: la cadena de 5 Por Qué del 14/9 fue corregida punto por punto por FM; el benchmarking del
  10/9 corrigió la propia hipótesis del equipo cuando la evidencia no la sostenía; la identidad
  visual se sometió a votación del equipo antes de cerrarse.
- **Las decisiones quedan registradas, numeradas y no se editan retroactivamente**
  (`docs/03-decisiones/`) — para cambiar una, se escribe una nueva que la supersede.
- **Todos los commits de git quedan firmados** con la autoría real de quien los hizo y, cuando hubo
  asistencia de Claude Code, con un trailer `Co-Authored-By` — el historial de git es evidencia
  auditable de cuándo y en qué se usó.

### ⬜ Pendiente de completar

- Documentar con más detalle **qué partes del código del prototipo entiende y puede defender cada
  integrante** — señalado como falta en [`prototipo.md`](../05-producto/prototipo.md) desde el
  2/9 y todavía sin resolver.
- Confirmar con ML si usó alguna herramienta de IA para el documento de requerimientos, para
  completar la fila correspondiente de esta tabla.

## Responsabilidad sobre el contenido

El equipo de FraudLens declara que:

- Asume la **responsabilidad académica plena** sobre todo el contenido presentado, generado con o
  sin asistencia de IA.
- El uso de IA fue de **apoyo instrumental y de producción asistida con supervisión humana** en
  todos los casos — no reemplazó las decisiones de fondo, que fueron tomadas y validadas por el
  equipo.
- Cada integrante puede explicar y defender lo que su parte del proyecto muestra.
