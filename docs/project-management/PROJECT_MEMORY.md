# MEMORIA DEL PROYECTO
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento registra las decisiones clave de diseño del proyecto.

Existe para preservar el razonamiento detrás de la arquitectura
del sistema, la estructura de la taxonomía y la metodología de
clasificación.

El objetivo es asegurar que el trabajo futuro en el proyecto se
mantenga consistente con la filosofía de diseño original.

--------------------------------------------------
2. VISIÓN DEL PROYECTO
--------------------------------------------------

El sistema está diseñado para clasificar canciones en géneros
musicales significativos y organizarlos en una taxonomía estructurada.

La taxonomía no solo se utiliza para clasificación, sino también para
navegación de playlists.

Los usuarios deberían poder navegar la jerarquía de géneros para
seleccionar playlists que coincidan con un estado de ánimo musical deseado.

--------------------------------------------------
3. ENFOQUE TAXONOMY-FIRST
--------------------------------------------------

El proyecto sigue un diseño taxonomy-first.

Esto significa:

• la taxonomía se diseña antes de la clasificación  
• la clasificación debe seguir la taxonomía  
• la taxonomía define los objetivos de género válidos  

El clasificador nunca debe inventar géneros.

--------------------------------------------------
4. PRINCIPIO DE DISEÑO: NAVEGACIÓN DE PLAYLISTS
--------------------------------------------------

La taxonomía está pensada no solo como un sistema de clasificación,
sino también como una estructura de navegación para escucha musical.

Los usuarios deberían poder subir o bajar por el árbol taxonómico
para encontrar playlists que coincidan con un estado de ánimo deseado.

--------------------------------------------------
5. PRINCIPIO DE DISEÑO: EVOLUCIÓN GUIADA POR DATASET
--------------------------------------------------

La taxonomía puede evolucionar conforme crece el dataset.

A medida que el catálogo se expande, ciertos géneros pueden acumular
suficientes canciones para justificar una subdivisión adicional.

El diseño de taxonomía debe mantenerse lo suficientemente flexible para
acomodar esta evolución preservando la coherencia musical.

--------------------------------------------------
FIN MEMORIA DEL PROYECTO