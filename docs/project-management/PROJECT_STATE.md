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
6. ARQUITECTURA DE VALIDACIÓN LAYER2 (CAPA 2)
--------------------------------------------------

Modularización de scripts/validate_tree_layer2.py (v2):

La validación semántica se ha refactorizado en módulos
especializados con responsabilidades claras:

| Módulo | Responsabilidad |
|--------|---|
| layer2_contract.py | Constantes compartidas, funciones de utilidad |
| layer2_prompt_builder.py | Construcción determinista de prompts con {{PLACEHOLDERS}} |
| layer2_governance_loader.py | Carga dinámico de contexto + reglas + estrategia |
| layer2_response_processor.py | Validación schema + reportes JSON/MD |
| validate_tree_layer2.py | CLI puro (orquestación) |

Estado:

• 5 módulos implementados y probados
• 4 unit tests con 100% pass rate
• separación de responsabilidades completada
• reducción de validate_tree_layer2.py de ~850 a ~250 líneas

--------------------------------------------------
7. SIGUIENTES PASOS
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

