# ESTRATEGIA DUAL DE PROMPTS
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
OBJETIVO
--------------------------------------------------

Formalizar un flujo de dos artefactos para prompts:

1) Prompt generador
2) Prompt final standalone

La meta es separar la fase de gobernanza documental de la fase
operativa de uso del prompt.

--------------------------------------------------
1. ARQUITECTURA DE DOS FASES
--------------------------------------------------

FASE A — GENERADOR DE PROMPTS

Entrada:
- tarea solicitada
- restricciones del usuario

Responsabilidad:
- leer registros canonicos
- diagnosticar imports (MANDATORY, CONDITIONAL, REFERENTIAL, EXCLUDED)
- validar cobertura y conflictos normativos
- decidir si hay base suficiente

Salida:
- prompt final standalone listo para ejecutar, o
- mensaje NADA con faltantes exactos

FASE B — PROMPT FINAL STANDALONE

Entrada:
- prompt generado en Fase A

Responsabilidad:
- ejecutar la tarea en cualquier chat
- no depender de rutas del repositorio
- no requerir contexto documental previo

Salida:
- respuesta final de la tarea

--------------------------------------------------
2. PRINCIPIOS DE DISEÑO
--------------------------------------------------

- El diagnostico de imports solo vive en Fase A.
- El prompt final no incluye rutas docs/* ni reglas internas del repositorio.
- Si falta base critica en Fase A, se bloquea la generación.
- El prompt final debe quedar sin placeholders ni marcadores pendientes.

--------------------------------------------------
3. CRITERIOS DE CALIDAD
--------------------------------------------------

Calidad de Fase A (generador):
- imports clasificados con justificación
- cobertura suficiente declarada
- conflictos reportados antes de continuar

Calidad de Fase B (standalone):
- ejecutable en un chat externo sin contexto adicional
- objetivo, formato y cierre definidos
- faltantes solicitados de forma puntual cuando aplique

--------------------------------------------------
4. ESPECIFICACIÓN DE LA PÁGINA DE PROCESAMIENTO
--------------------------------------------------

Nombre funcional:
- Generador de prompts

Ubicación en la app web:
- página: web/utilerias.html
- ruta: /utilerias
- API de carga: GET /api/utilerias/requests
- API de proceso: POST /api/utilerias/process

Propósito:
- mostrar lista de prompts a generar
- procesar cada solicitud y devolver resultado usable o mensaje de corrección

Flujo de usuario:
1. Ver lista de solicitudes de prompt.
2. Seleccionar una o varias solicitudes.
3. Presionar Procesar.
4. Recibir para cada solicitud uno de dos resultados:
   - PROMPT_OK: prompt final standalone listo para usar.
   - REQUIERE_CORRECCION: mensaje con faltantes o conflicto a resolver.

Campos mínimos por solicitud en la lista:
- id
- nombre
- tarea
- restricciones
- estado (pendiente, procesando, ok, requiere_correccion)
- mensaje de validación
- prompt generado (si estado ok)

Reglas de resultado:
- Si cobertura es insuficiente, devolver REQUIERE_CORRECCION.
- Si hay conflicto normativo, devolver REQUIERE_CORRECCION.
- Solo devolver PROMPT_OK cuando el prompt final no tenga placeholders.

--------------------------------------------------
5. CONTRATO DE RESPUESTA RECOMENDADO
--------------------------------------------------

Formato por item procesado:

- id
- status: PROMPT_OK | REQUIERE_CORRECCION
- prompt_final: string (vacio si requiere correccion)
- errores: lista de strings
- recomendaciones: lista de strings

Esto permite que la página renderice una tabla clara y accionable.

--------------------------------------------------
6. UBICACIÓN DE ARTEFACTOS
--------------------------------------------------

Prompts activos:
- prompts/prompt_bootstrap_generador_prompts_v1.md
- prompts/prompt_operativo_base.md

Documentación de soporte:
- docs/context/AI_PROMPT_SYSTEM_CONTEXT.md
- docs/governance/AI_PROMPT_SYSTEM_RULES.md
- docs/context/CONTEXT_REGISTRY.md
- docs/governance/RULES_REGISTRY.md

--------------------------------------------------
FIN DEL DOCUMENTO
