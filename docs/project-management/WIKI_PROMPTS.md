---

## Prompt de Arranque de Sesión (para copiar y pegar)

Usa este prompt al inicio de cada nueva conversación para asegurar que el agente siga el flujo operativo sin interrupciones ni sugerencias fuera del prompt:

```
Instrucción para la sesión:
- Sigue el prompt operativo seleccionado al pie de la letra, sin pedir confirmaciones ni sugerir pasos adicionales.
- No interrumpas el flujo salvo por errores fatales o ambigüedades no cubiertas.
- No expliques ni resumas a menos que el prompt lo indique.
- El usuario ya conoce el flujo y las reglas.
```

Pega este bloque antes de tu prompt operativo para maximizar la autonomía y evitar interrupciones.
## Prompts Finales para el Usuario

| Archivo                                             | Objetivo principal                                                      |
|-----------------------------------------------------|-------------------------------------------------------------------------|
| prompts/validate_master_layer2_prompt.txt           | Validación operativa del árbol con reglas/contexto más actualizados     |
| prompts/clasificador_generos_fase2_standalone.md    | Clasificación directa de géneros musicales (fase 2, uso standalone)     |
| prompts/generar_arbol_taxonomico_mvet_layer2_standalone.md | Generación de árbol taxonómico MVET Layer2 (uso standalone)     |

Utiliza solo estos prompts para validación, clasificación o generación directa. Los demás son de soporte o generación.
# Wiki de Prompts Operativos y de Sistema

Esta wiki te ayuda a identificar rápidamente qué prompt debes usar para cada tarea en el proyecto Music Taxonomy, evitando confusiones con prompts intermedios, generadores o desfasados.

## Tipos de Prompts

### 1. **Prompts Operativos (de usuario final)**
- **Propósito:** Son los prompts que debes usar directamente para validar, clasificar o analizar el árbol taxonómico.
- **Ubicación típica:** prompts/ o prompts/generadores/ (pero solo si están marcados como "standalone" o "operativo").
- **Ejemplo clave:**
  - `prompts/validate_master_layer2_prompt.txt` → **Este es el prompt principal para validar el árbol con las reglas actuales.**
  - `prompts/clasificador_generos_fase2_standalone.md` → Prompt para clasificación directa de géneros.

### 2. **Prompts Generadores o Intermedios**
- **Propósito:** Sirven para crear, actualizar o regenerar otros prompts operativos. No deben usarse para validar ni clasificar directamente.
- **Ubicación típica:** prompts/generadores/ o archivos con "generador" o "template" en el nombre.
- **Ejemplo:**
  - `prompts/prompt_bootstrap_generador_prompts.md` → Genera otros prompts, no usar directamente para validación.
  - `prompts/generadores/validate_master_layer2_prompt_template.md` → Plantilla para crear el prompt de validación, no usar directamente.

### 3. **Prompts de Contexto o Soporte**
- **Propósito:** Proveen contexto, reglas o corpus normativo que los prompts operativos cargan dinámicamente. No se usan solos.
- **Ubicación típica:** docs/context/, docs/governance/, etc.
- **Ejemplo:**
  - `docs/governance/MVET_LAYER2_RULES.md` → Corpus de reglas, no es prompt operativo.


## ¿Cómo asegurar que usas el prompt más reciente?

**Siempre que cambies reglas, contexto o taxonomía, sigue este flujo:**

1. Ejecuta el prompt generador correspondiente (por ejemplo, `prompts/prompt_bootstrap_generador_prompts.md` o el template en `prompts/generadores/`).
   - Esto regenerará el prompt operativo actualizado (ej: `prompts/validate_master_layer2_prompt.txt`).
2. Usa solo el prompt operativo recién generado para validar el árbol o clasificar.
3. Si tienes dudas, revisa la fecha de modificación del prompt operativo y del generador.

**Evita usar directamente:**
- Prompts operativos viejos si hubo cambios en reglas/contexto.
- Archivos de contexto o corpus de reglas.

## Reglas de oro
- Si el prompt dice "standalone" o "operativo" en el nombre, es seguro para uso directo, pero regenera antes si hubo cambios.
- Si el prompt menciona "template", "generador" o está en una subcarpeta de generadores, NO lo uses directamente para validar, solo para generar el operativo.
- Los prompts operativos deben regenerarse tras cada cambio relevante en reglas/contexto.

---

**Actualiza esta wiki si se agregan nuevos prompts o cambia la estructura.**

---

## Lista de Prompts Disponibles

| Archivo                                             | Objetivo principal                                                                 |
|-----------------------------------------------------|------------------------------------------------------------------------------------|
| prompts/validate_master_layer2_prompt.txt           | Validación operativa del árbol con reglas y contexto más actualizados              |
| prompts/clasificador_generos_fase2_standalone.md    | Clasificación directa de géneros musicales (fase 2, uso standalone)                |
| prompts/generar_arbol_taxonomico_mvet_layer2_standalone.md | Generación de árbol taxonómico MVET Layer2 (uso standalone)                |
| prompts/prompt_bootstrap_generador_prompts.md       | Generador de prompts operativos a partir de contexto y reglas                      |
| prompts/generadores/validate_master_layer2_prompt_template.md | Plantilla para generar el prompt de validación principal                |
| prompts/generadores/validate_master_layer2_agent_orchestrator.md | Orquestador para generación/validación avanzada de prompts           |
| prompts/generadores/validate_master_layer2_prompt_context.json | Contexto estructurado para generación de prompt de validación principal |

Revisa esta lista antes de usar o modificar un prompt. Si agregas uno nuevo, documenta aquí su objetivo.

🟢 Chat manejable
