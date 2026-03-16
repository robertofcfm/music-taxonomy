# PROMPT OPERATIVO BASE (V2)
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
OBJETIVO
--------------------------------------------------

Construir un prompt final corto, claro y ejecutable,
con carga selectiva de contexto y reglas.

--------------------------------------------------
FORMATO BASE
--------------------------------------------------

[TAREA]
- [describir en una linea]

[OBJETIVO_OPERATIVO]
- [resultado esperado]

[DIAGNOSTICO_IMPORTS]
- MANDATORY:
  - docs/governance/GLOBAL_RULES.md
  - docs/governance/SYSTEM_CONTRACT.md
  - docs/context/PROJECT_CONTEXT.md
- CONDITIONAL:
  - [agregar solo si aplica]
- REFERENTIAL:
  - [agregar solo si aporta claridad]
- EXCLUDED:
  - [listar lo descartado para evitar ruido]
- COBERTURA:
  - suficiente | insuficiente

[ENTRADAS]
- [archivo principal]
- [archivo secundario opcional]

[SALIDA_ESPERADA]
- [tipo de salida]
- [formato]
- [criterio de calidad]

[RESTRICCIONES]
- No inventar reglas no documentadas.
- No modificar taxonomia automaticamente.
- Reportar conflictos normativos antes de ejecutar.

[PROMPT_FINAL]
- [redactar aqui el prompt final listo para uso]

[FALTANTES_SI_APLICA]
- [vaciar si no aplica]

[CRITERIO_DE_CIERRE]
- [condicion de tarea completada]

--------------------------------------------------
REGLAS DE USO RAPIDAS
--------------------------------------------------

- Mantener el presupuesto de contexto corto.
- Si falta informacion critica, devolver NADA y listar faltantes.
- No promover un documento referencial a regla obligatoria.
- Si hay conflicto normativo, detener y reportar.

--------------------------------------------------
FIN DEL DOCUMENTO
