# CONTEXTO DEL PROYECTO
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Última actualización:

2026-03-16

--------------------------------------------------
1. PROPÓSITO DEL PROYECTO
--------------------------------------------------

Este proyecto busca construir una taxonomía estructurada
de géneros musicales junto con un sistema de clasificación
capaz de asignar géneros precisos a las canciones.

La taxonomía está diseñada no solo para clasificación,
sino también para generar playlists coherentes basadas
en la jerarquía de géneros.

El objetivo final es permitir navegar por géneros de una
manera que produzca playlists musicalmente consistentes.

--------------------------------------------------
2. OBJETIVO CENTRAL
--------------------------------------------------

El sistema busca:

• clasificar canciones en géneros musicales significativos  
• mantener una taxonomía de géneros coherente  
• generar playlists basadas en géneros  
• evolucionar la taxonomía conforme crece el catálogo  

La taxonomía actúa como la base de conocimiento musical
del sistema.

--------------------------------------------------
3. ARQUITECTURA DEL SISTEMA
--------------------------------------------------

El sistema está compuesto por tres subsistemas principales.

FASE 1 — DISEÑO DE TAXONOMÍA

Define la jerarquía de géneros.

La taxonomía determina los géneros válidos que pueden
asignarse durante la clasificación.

FASE 2 — IDENTIFICACIÓN DE GÉNERO DE CANCIONES

Determina a qué géneros pertenece una canción.

Este proceso analiza las características musicales de
cada canción y asigna géneros apropiados.

FASE 3 — GENERACIÓN DE ÁRBOL GUIADA POR DATASET

Usa el catálogo clasificado para generar un árbol de escucha
que organiza canciones en nodos de género navegables.

--------------------------------------------------
4. CONCEPTO DE NAVEGACIÓN DE PLAYLISTS
--------------------------------------------------

La taxonomía está diseñada para soportar navegación
por estilos musicales.

Los usuarios deberían poder moverse por la jerarquía
para encontrar playlists que coincidan con un estado
de ánimo o estilo musical específico.

Cada nodo de la taxonomía puede corresponder a una
playlist con canciones de ese género.

--------------------------------------------------
5. EVOLUCIÓN DE LA TAXONOMÍA
--------------------------------------------------

Se espera que la taxonomía evolucione conforme crece
el catálogo.

Durante la clasificación pueden descubrirse géneros nuevos.

Cuando esto ocurra, la taxonomía podrá expandirse
tras una revisión manual.

--------------------------------------------------
6. GOBERNANZA DE TAXONOMÍA
--------------------------------------------------

La taxonomía se gobierna manualmente por el propietario del proyecto.

El sistema puede:

• analizar la taxonomía  
• validar la taxonomía  
• sugerir mejoras  

Pero los cambios estructurales siempre deben revisarse
antes de aplicarse.

--------------------------------------------------
FIN CONTEXTO DEL PROYECTO

