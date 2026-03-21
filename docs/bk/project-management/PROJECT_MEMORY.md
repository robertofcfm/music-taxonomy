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
6. MEMORIA DE VALIDACIÓN MVET
--------------------------------------------------

Se formalizó un modelo híbrido de validación de taxonomía:

• Capa 1 (determinista): checks estructurales, trazables y repetibles
• Capa 2 (semántica): análisis musical con IA bajo contrato JSON estricto

La gobernanza se usa como fuente de conocimiento por archivo
(modelo FB), no como mapeo rígido SOURCE por regla.

Convención establecida:

• MVET-L1-* => Capa 1
• MVET-L2-* => Capa 2
• MVET-C-* => reglas condicionales

Decisión clave de profundidad:

• mínimo estructural (>= 3) se valida en Capa 1
• límite máximo por criterio atómico se evalúa en Capa 2

Regla de trazabilidad operativa:

El reporte debe incluir causantes explícitos cuando una regla falla.

--------------------------------------------------
7. MEMORIA DE OPERACIÓN WEB
--------------------------------------------------

Se implementó una interfaz web local para operar validación desde UI.

Componentes:

• scripts/web_app.py (servidor local)
• web/index.html (dashboard)

El botón principal ejecuta pipeline completo:

• Capa 1 siempre
• Capa 2 si existe reports/validate_master_layer2_response.json

La UI muestra resultados de Capa 1 en formato legible,
y estado de ejecución de pipeline incluyendo decisión de Capa 2.

--------------------------------------------------
FIN MEMORIA DEL PROYECTO

