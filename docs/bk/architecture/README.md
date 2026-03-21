# ARCHITECTURE

Esta carpeta queda reservada para documentación arquitectónica técnica.

El contexto canónico del proyecto fue movido a:

- docs/context/CONTEXT_REGISTRY.md

## Arquitectura de Validación

### Prompts

- docs/architecture/PROMPTS_DUAL_PIPELINE_STRATEGY.md

Define la estrategia dual de generación y ejecución de prompts.

### Layer2 (Capa 2 — Semántica IA)

- docs/architecture/LAYER2_ARCHITECTURE.md

Documentación modular de validación semántica. Incluye:

- Tabla de responsabilidades de módulos (layer2_*.py)
- Flujo de ejecución end-to-end
- Interfaz de cada módulo especializado
- Contrato de respuesta IA
- Configuración externa (plantilla, contexto, estrategia)
- Suite de testing

**Referencia rápida:**

| Módulo | Responsabilidad |
|--------|---|
| layer2_contract.py | Constantes compartidas, funciones de utilidad |
| layer2_prompt_builder.py | Construcción determinista de prompts con {{PLACEHOLDERS}} |
| layer2_governance_loader.py | Carga dinámico de contexto + reglas + estrategia |
| layer2_response_processor.py | Validación schema + reportes JSON/MD |
| validate_tree_layer2.py | CLI puro (orquestación) |

