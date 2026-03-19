# Plan de Migración y Refactorización

Este documento establece el plan de acción para migrar y reorganizar scripts y prompts, asegurando trazabilidad y control en cada paso.

## Objetivo
- Migrar todos los scripts y prompts a una estructura modular, separando los archivos ya refactorizados de los pendientes.
- Garantizar que cada archivo solo cargue el contexto y reglas estrictamente necesarios.
- Mantener trazabilidad de avance y decisiones.

## Pasos del plan

- [ ] 1. Crear carpetas `bk/` en `scripts/` y `prompts/` para archivos pendientes de migrar.
- [ ] 2. Listar todos los scripts y prompts actuales, identificando cuáles deben ir a `bk/`.
- [ ] 3. Definir y documentar el criterio de migración (qué va a `bk/` y qué queda activo).
- [ ] 4. Crear/actualizar un índice en `scripts/README.md` y `prompts/README.md` con el estado de cada archivo.
- [ ] 5. Migrar archivos a `bk/` según el criterio definido.
- [ ] 6. Refactorizar archivos uno por uno, moviéndolos de `bk/` a la ubicación principal y actualizando el índice.
- [ ] 7. Eliminar archivos de `bk/` solo cuando se confirme que ya no son necesarios.

## Condiciones y criterios
- No mover ni eliminar código sin antes documentar el cambio aquí.
- Cada archivo migrado debe cumplir con la carga mínima de contexto y reglas.
- El avance debe palomearse en este documento.

## Observaciones
- El prompt `prompt_bootstrap_generador_prompts.md` queda siempre fuera de `bk/`.
- Este plan debe actualizarse en cada iteración.

🟢 Chat manejable
