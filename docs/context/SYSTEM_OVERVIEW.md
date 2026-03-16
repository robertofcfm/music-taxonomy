# VISIÓN GENERAL DEL SISTEMA
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento ofrece una visión de alto nivel del
Sistema de Taxonomía de Géneros Musicales.

Explica cómo interactúan los componentes principales
del proyecto y cómo operan juntos la taxonomía,
el clasificador y el pipeline de generación de playlists.

--------------------------------------------------
2. OBJETIVOS DEL SISTEMA
--------------------------------------------------

El sistema tiene tres objetivos principales:

• clasificar canciones en géneros musicales significativos  
• mantener una taxonomía de géneros coherente  
• generar playlists navegables basadas en géneros  

La taxonomía actúa como la estructura central de
conocimiento de todo el sistema.

--------------------------------------------------
3. COMPONENTES CENTRALES
--------------------------------------------------

El proyecto contiene tres subsistemas principales.

1. DISEÑO DE TAXONOMÍA

La taxonomía define la estructura jerárquica de
los géneros musicales.

Es mantenida manualmente por el usuario.

Archivos involucrados:

taxonomy/genre_tree_master.md  
taxonomy/genre_tree_operational.csv  

--------------------------------------------------

2. CLASIFICACIÓN DE CANCIONES

El clasificador asigna géneros a canciones usando
la taxonomía.

Entrada:

catalog/songs_raw.csv

Salida:

catalog/songs_with_genres.csv

La clasificación sigue reglas estrictas definidas en:

docs/governance/SYSTEM_CONTRACT.md

--------------------------------------------------

3. GENERACIÓN DE ÁRBOL

Después de clasificar canciones, puede generarse un
árbol dinámico de géneros basado en el dataset.

Este proceso organiza canciones en nodos que pueden
usarse para generar playlists.

--------------------------------------------------
4. FASES DEL PROYECTO
--------------------------------------------------

El proyecto evoluciona en tres fases.

FASE 1

Diseño de taxonomía y definición de reglas.

FASE 2

Clasificación de canciones usando la taxonomía.

FASE 3

Generación del árbol de géneros guiado por dataset.

--------------------------------------------------
5. PRINCIPIOS DEL SISTEMA
--------------------------------------------------

El sistema sigue varios principios centrales.

• diseño taxonomy-first  
• gobernanza taxonómica manual  
• coherencia de playlists  
• cumplimiento estricto de reglas  
• evolución taxonómica guiada por dataset  

--------------------------------------------------
6. DOCUMENTACIÓN DEL SISTEMA
--------------------------------------------------

Documentos clave que gobiernan el sistema:

docs/governance/SYSTEM_CONTRACT.md  
docs/governance/TAXONOMY_RULES.md  
docs/governance/TAXONOMY_CHANGE_POLICY.md  
docs/governance/TAXONOMY_DEPTH_POLICY.md  
docs/governance/TAXONOMY_NAMING_CONVENTION.md  

Estos documentos definen el comportamiento y la
estructura del sistema.

--------------------------------------------------
FIN VISIÓN GENERAL DEL SISTEMA

