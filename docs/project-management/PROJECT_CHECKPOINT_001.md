# Checkpoint del Proyecto 001
Instantánea de cierre de arquitectura

Este documento captura la primera reconstrucción estable del proyecto
tras consolidar conocimiento de la conversación de desarrollo.

Propósito:
Preservar arquitectura, reglas y estructura del proyecto para que pueda
retomarse más adelante sin pérdida de contexto.

---

# Objetivo del Proyecto

El proyecto construye un **sistema de taxonomía de géneros musicales** capaz de:

1. Definir una taxonomía estructurada de géneros.
2. Clasificar canciones en géneros usando esa taxonomía.
3. Generar un árbol dinámico de géneros según el catálogo real.

El sistema se divide en tres fases.

---

# Fase 1 — Diseño de Taxonomía

Estado: COMPLETADA

Objetivo:
Diseñar la taxonomía de géneros y todas las reglas estructurales antes de automatizar.

Salidas:

taxonomy/genre_tree_master.md
Plantilla editable de taxonomía.

taxonomy/genre_tree_operational.csv
Representación operativa usada por scripts.

taxonomy/taxonomy_version.md
Control de versión para compatibilidad taxonómica.

data/genre_alias.csv
Mapa de alias para normalización de géneros.

docs/governance/TAXONOMY_RULES.md
Reglas de taxonomía.

docs/governance/TAXONOMY_NAMING_CONVENTION.md
Reglas de nombrado de géneros.

docs/governance/TAXONOMY_CHANGE_POLICY.md
Reglas que gobiernan evolución taxonómica.

docs/governance/TAXONOMY_DEPTH_POLICY.md
Reglas para profundidad de ramas.

docs/governance/TAXONOMY_QUALITY_CHECKLIST.md
Criterios de validación de calidad taxonómica.

docs/operations/PHASE1_FINAL_CHECKLIST.md
Checklist de cierre de Fase 1.

---

# Fase 2 — Clasificación de Género en Canciones

Estado: DISEÑO COMPLETO / IMPLEMENTACIÓN PENDIENTE

Objetivo:
Asignar géneros a canciones usando la taxonomía.

Entrada:

catalog/songs_raw.csv

Salida:

catalog/songs_with_genres.csv

Reglas:

• Los géneros deben ser géneros musicales reales.
• Las canciones pueden pertenecer a múltiples géneros.
• Las influencias menores se ignoran.
• Los géneros deben corresponder a hojas de la taxonomía.

Si no existe un género adecuado:

Se genera error fatal y la taxonomía debe expandirse manualmente.

---

# Fase 3 — Generación Dinámica de Árbol de Géneros

Estado: DISEÑO COMPLETO / IMPLEMENTACIÓN PENDIENTE

Objetivo:
Generar un árbol de géneros basado en datos del catálogo.

Regla:

Un nodo se vuelve expandible cuando contiene más de:

45 canciones

En ese punto:

• El nodo se convierte en padre
• Las canciones se redistribuyen entre subgéneros

Este proceso construye el árbol de escucha final.

---

# Tipos de Nodo

NORMAL
Nodo taxonómico estándar.

CLONE
Nodo portal que apunta a otro nodo canónico.

GENERAL
Nodo fallback para canciones que pertenecen al género padre
pero no encajan en subgéneros definidos.

ATOMIC
Nodo terminal que no debe expandirse más.

---

# Estrategia de Géneros Latin

La música Latin se maneja como rama separada.

Si una canción es Latin:

Sus géneros deben seleccionarse del subárbol Latin.

Esto evita mezclar contextos Latin y no-Latin.

---

# Estrategia de Versionado

Cada resultado de clasificación almacena:

taxonomy_version

Si cambia la estructura de la taxonomía:

Clasificaciones previas pueden volverse incompatibles.

---

# Principio Clave del Proyecto

La plantilla taxonómica **nunca se modifica automáticamente**.

Solo el propietario del proyecto edita:

taxonomy/genre_tree_master.md

Las herramientas de automatización solo pueden:

• analizar
• validar
• sugerir cambios

---

# Estructura Actual del Repositorio

music-taxonomy/

data/
taxonomy/
catalog/
scripts/
reports/
docs/

---

# Propósito del Checkpoint

Este checkpoint garantiza que:

• la arquitectura del sistema se preserva
• las reglas de taxonomía están documentadas
• el proyecto puede retomarse meses después

sin perder contexto.