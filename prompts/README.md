# PROMPTS DEL PROYECTO

Esta carpeta centraliza los prompts operativos del repositorio.

Uso recomendado:
- Separar prompts en dos tipos: generador y final standalone.
- Guardar aqui prompts finales listos para ejecucion.
- Mantener nombres descriptivos por flujo o tarea.
- Componer prompts cargando solo archivos necesarios desde docs/context/ y docs/governance/.
- Declarar imports en grupos: MANDATORY, CONDITIONAL, REFERENTIAL y EXCLUDED.

Ejemplos de nombres:
- classify_songs_prompt_v1.txt
- validate_master_layer2_prompt_v2.txt

Prompt generador recomendado:
- prompt_bootstrap_generador_prompts.md

Nota:
- El diagnostico de imports se ejecuta en el prompt generador.
- El resultado final debe poder usarse en cualquier chat sin contexto del repositorio.

Validacion automatica recomendada:
- Ejecutar `python scripts/validate_prompt_bootstrap.py` antes de usar el bootstrap.
- Si falla, el script devuelve `NADA` y detalla faltantes/politicas incumplidas.

Automatizacion (recomendada):
- VS Code task disponible: `Validate Prompt Bootstrap`.
- Hook pre-commit disponible en `.githooks/pre-commit`.
- Para activarlo en el repo, ejecutar:
	`powershell -ExecutionPolicy Bypass -File scripts/setup_git_hooks.ps1`
- Desde ese momento, cada commit valida automaticamente el bootstrap y bloquea el commit si hay incumplimientos.
