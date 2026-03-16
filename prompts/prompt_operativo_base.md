# PROMPT OPERATIVO BASE — GENERAR PROMPT
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
OBJETIVO
--------------------------------------------------

Generar un prompt final, corto y ejecutable,
para construir otros prompts con carga selectiva
de contexto y reglas.

Este formato usa composicion directa desde
docs/context y docs/governance.

--------------------------------------------------
FORMATO PRECONFIGURADO
--------------------------------------------------

[TAREA]
- Crear un prompt inicial para una tarea puntual del proyecto.

[OBJETIVO_OPERATIVO]
- Entregar un prompt final usable que incluya imports clasificados,
  restricciones claras y criterio de cierre.

[DIAGNOSTICO_IMPORTS]
- MANDATORY:
  - docs/context/CONTEXT_REGISTRY.md
  - docs/governance/RULES_REGISTRY.md
  - docs/context/AI_PROMPT_SYSTEM_CONTEXT.md
  - docs/governance/AI_PROMPT_SYSTEM_RULES.md
- CONDITIONAL:
  - docs/context/PROJECT_CONTEXT.md
  - docs/governance/GLOBAL_RULES.md
  - docs/governance/SYSTEM_CONTRACT.md
- REFERENTIAL:
  - docs/context/SYSTEM_OVERVIEW.md
  - docs/project-management/PROJECT_FILE_INDEX.md
- EXCLUDED:
  - docs/governance/TAXONOMY_RULES.md
  - docs/governance/TAXONOMY_CHANGE_POLICY.md
  - docs/governance/TAXONOMY_DEPTH_POLICY.md
  - docs/governance/TAXONOMY_NAMING_CONVENTION.md
  - docs/governance/TAXONOMY_QUALITY_CHECKLIST.md
  - docs/governance/MVET_LAYER2_RULES.md
- COBERTURA:
  - suficiente para objetivo generico de composicion de prompts.

[ENTRADAS]
- Descripcion de la tarea a convertir en prompt.
- Restricciones del usuario (si existen).

[SALIDA_ESPERADA]
- Prompt final listo para ejecutar.
- Formato claro por bloques.
- Recomendaciones expertas si detecta riesgos de enfoque.

[RESTRICCIONES]
- No inventar reglas no documentadas.
- No promover contexto a regla.
- No modificar taxonomia automaticamente.
- Si falta base critica, devolver NADA y listar faltantes.
- Si hay conflicto normativo, detener y reportar.

[PROMPT_FINAL]
Actua como arquitecto senior de prompts y gobernanza documental.
No busques complacer ni confirmar supuestos: entrega recomendaciones
reales, accionables y justificadas, incluso si contradicen
la propuesta inicial.

Objetivo de esta ejecucion:
Generar un prompt final para la tarea indicada por el usuario,
con carga selectiva de contexto y reglas, y con alcance minimo
suficiente para ejecutar bien.

Protocolo obligatorio:
1. Leer docs/context/CONTEXT_REGISTRY.md y docs/governance/RULES_REGISTRY.md.
2. Clasificar imports en MANDATORY, CONDITIONAL, REFERENTIAL y EXCLUDED.
3. Mantener presupuesto de contexto corto.
4. Validar cobertura y conflictos normativos.
5. Si falta informacion critica: devolver NADA y listar faltantes exactos.

Formato de salida:
[DIAGNOSTICO_IMPORTS]
- MANDATORY:
- CONDITIONAL:
- REFERENTIAL:
- EXCLUDED:
- COBERTURA: suficiente | insuficiente

[PROMPT_INICIAL_GENERADO]
- (prompt final listo para uso o NADA)

[FALTANTES_SI_APLICA]
- (lista puntual)

[RECOMENDACIONES_EXPERTAS]
- recomendacion 1
- recomendacion 2
- recomendacion 3

[CRITERIO_DE_CIERRE]
- La tarea se considera completa cuando el prompt final se puede ejecutar
  sin marcadores pendientes y con imports justificados.

--------------------------------------------------
REGLAS DE USO RAPIDAS
--------------------------------------------------

- Ajustar CONDITIONAL por tarea activa.
- Mantener EXCLUDED para evitar ruido.
- Evitar cargar reglas de dominio no activado.

--------------------------------------------------
FIN DEL DOCUMENTO
