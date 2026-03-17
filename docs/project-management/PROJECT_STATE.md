# ESTADO DEL PROYECTO
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento almacena el estado operativo
actual del proyecto.

Permite reanudar el proyecto después de períodos
largos sin depender del historial de conversación.

--------------------------------------------------
2. FASE ACTUAL
--------------------------------------------------

Fase Activa: Fase 1 — Validación Operativa de Taxonomía

Descripción de la fase:

La taxonomía maestra ya cuenta con pipeline de validación
operativo en dos capas:

• Capa 1 determinista implementada en scripts/validate_tree.py
• Capa 2 semántica implementada como stub operativo en
	scripts/validate_tree_layer2.py

Además existe una interfaz web local para ejecutar el pipeline
y visualizar resultados en formato legible.

--------------------------------------------------
3. ESTADO DE LA TAXONOMÍA
--------------------------------------------------

Archivo maestro de taxonomía:

taxonomy/genre_tree_master.md

Taxonomía operativa:

taxonomy/genre_tree_operational.csv

Estado actual de la taxonomía:

• estructura validable automáticamente (Capa 1)
• estrategia MVET consolidada hasta versión v0.6
• validación semántica disponible por respuesta JSON de IA (Capa 2)

--------------------------------------------------
4. ESTADO DEL SISTEMA DE CLASIFICACIÓN
--------------------------------------------------

Estado de implementación del clasificador:

• no finalizado
• reglas base validadas con pipeline MVET
• clasificación de canciones aún pendiente de ejecución por lotes

Estado del sistema de validación:

• scripts/validate_tree.py: implementado y probado
• scripts/validate_tree_layer2.py: implementado y probado
• scripts/web_app.py + web/index.html: dashboard local implementado

--------------------------------------------------
5. ESTADO DEL DATASET
--------------------------------------------------

Archivo de catálogo de canciones:

catalog/songs_raw.csv

Archivo de salida de clasificación:

catalog/songs_with_genres.csv

Estado de procesamiento del dataset:

• pipeline de clasificación aún no ejecutado

--------------------------------------------------
6. SIGUIENTES PASOS
--------------------------------------------------

Prioridades inmediatas:

1. definir y estandarizar flujo de respuesta IA para Capa 2
2. consolidar decisiones taxonómicas derivadas de warnings L2
3. integrar validación MVET en rutina previa a clasificación
4. preparar ejecución de clasificación por lotes (Fase 2)

Artefactos clave actualmente activos:

• reports/validate_master_report.json (resultado Capa 1)
• reports/validate_master_layer2_report.json (resultado Capa 2)
• prompts/validate_master_layer2_prompt.txt (prompt determinista L2)

--------------------------------------------------
FIN ESTADO DEL PROYECTO

