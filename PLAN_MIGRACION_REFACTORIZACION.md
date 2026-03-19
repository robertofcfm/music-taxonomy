# Plan de Migración y Refactorización

Este documento establece el plan de acción para migrar y reorganizar scripts y prompts, asegurando trazabilidad y control en cada paso.

## Objetivo
- Migrar todos los scripts y prompts a una estructura modular, separando los archivos ya refactorizados de los pendientes.
- Garantizar que cada archivo solo cargue el contexto y reglas estrictamente necesarios.
- Mantener trazabilidad de avance y decisiones.

## Pasos del plan

- [x] 1. Crear carpetas `bk/` en `scripts/` y `prompts/` para archivos pendientes de migrar.
- [x] 2. Listar todos los scripts y prompts actuales, identificando cuáles deben ir a `bk/`.
- [x] 3. Definir y documentar el criterio de migración (qué va a `bk/` y qué queda activo).
- [x] 4. Crear/actualizar un índice en `scripts/README.md` y `prompts/README.md` con el estado de cada archivo.
- [x] 5. Migrar archivos a `bk/` según el criterio definido.
- [x] 6. Refactorizar archivos uno por uno, moviéndolos de `bk/` a la ubicación principal y actualizando el índice.
- [x] 7. Eliminar archivos de `bk/` solo cuando se confirme que ya no son necesarios.

### [2026-03-18] Cierre de migración de validación de árbol (Capa 2)
- Script principal: scripts/validate_tree_layer2.py (modular, documentado, carga contexto y reglas externas)
- Prompt operativo: prompts/validate_master_layer2_prompt.txt (generado y editable como plantilla en generadores/)
- Orquestador: prompts/generadores/validate_master_layer2_agent_orchestrator.md (define el flujo operativo, criterios y restricciones)
- Contexto y reglas: prompts/generadores/validate_master_layer2_prompt_context.json, governance/reglas_validacion_arbol_llm.md, context/contexto_validacion_arbol_llm.md
- Todos los componentes están sincronizados, modularizados y documentados.
- Fase de validación de árbol completamente migrada y lista para producción.

### [2026-03-18] Fase de validación de árbol completada. Todos los scripts, prompts, reglas y contexto migrados y documentados. Índices y plan actualizados. Listo para siguiente tarea.
