# Arquitectura de Validación Layer2 (Capa 2 — Semántica IA)

## Propósito

Validación semántica de la taxonomía de géneros musicales mediante evaluación IA.
Capa 2 complementa la validación determinista de Capa 1 con análisis contextual
y de coherencia mediante modelos de lenguaje.

## Organización Modular

La capa 2 se ha refactorizado en módulos especializados ubicados en `scripts/`:

### Tabla de Responsabilidades

| Módulo | Responsabilidad | Archivo |
|--------|---|---|
| **layer2_contract.py** | Constantes compartidas, funciones de utilidad | `scripts/layer2_contract.py` |
| **layer2_prompt_builder.py** | Construcción determinista de prompts con {{PLACEHOLDERS}} | `scripts/layer2_prompt_builder.py` |
| **layer2_governance_loader.py** | Carga dinámico de contexto + reglas + estrategia | `scripts/layer2_governance_loader.py` |
| **layer2_response_processor.py** | Validación schema + reportes JSON/MD | `scripts/layer2_response_processor.py` |
| **validate_tree_layer2.py** | CLI puro (orquestación) | `scripts/validate_tree_layer2.py` |

## Flujo de Ejecución

```
validate_tree_layer2.py (CLI)
    ↓
--print-prompt
    → layer2_governance_loader.load_prompt_template()
    → layer2_governance_loader.load_prompt_context()
    → layer2_governance_loader.load_governance_context()
    → layer2_prompt_builder.build_prompt()
    ✓ Output: prompts/validate_master_layer2_prompt.txt

--apply-response <JSON>
    → layer2_response_processor.load_response_json()
    → layer2_response_processor.validate_response_schema()
    → layer2_response_processor.process_layer2_response()
    ✓ Output: reports/validate_master_layer2_report.json
    ✓ Output: reports/validate_master_layer2_report.md

--apply-cycle <dir>
    → Itera --apply-response hasta cerrar ciclo
```

## Interfaz de Cada Módulo

### layer2_contract.py

Exporta constantes y utilidades compartidas:

```python
RESPONSE_LAYER = "MVET-LAYER2"
VALID_SEVERITIES = {"FATAL", "WARNING", "SUGGESTION"}
VALID_DECISIONS = {"PASS", "PASS_WITH_WARNINGS", "FAIL"}
VALID_RESULTS = {"PASS", "FAIL"}
LAYER2_RULE_REQUIRED_FIELDS = {"rule_id", "fb", "severity", "description", "check"}

def find_unresolved_placeholders(text: str) -> list[str]
def compute_decision(fatals: int, warnings: int, suggestions: int) -> str
```

### layer2_prompt_builder.py

Construye prompts determinísticos validando resolución completa:

```python
def build_prompt(
    taxonomy_text: str,
    governance_context: str,
    layer2_rules: list[dict[str, str]],
    prompt_template: str,
    prompt_context: dict[str, str],
) -> str
```

**Garantías:**
- Resuelve todos los {{PLACEHOLDERS}} o levanta `ValueError`
- Salida lista para enviar a LLM

### layer2_governance_loader.py

Carga configuración dinámicamente desde archivos:

```python
def load_prompt_template(prompt_template_path: Path) -> str
def load_prompt_context(prompt_context_path: Path) -> dict[str, str]
def load_governance_doc_groups(strategy_path: Path, repo_root: Path) -> dict[str, list[Path]]
def load_governance_context(strategy_path: Path, repo_root: Path, prompt_context: dict) -> str
def load_layer2_rules_from_governance(governance_dir: Path) -> list[dict[str, str]]
```

**Carga desde:**
- `prompts/generadores/validate_master_layer2_prompt_template.md` — Plantilla
- `prompts/generadores/validate_master_layer2_prompt_context.json` — Contexto
- `docs/governance/*.md` — Reglas (via `<!-- MVET:LAYER2_RULE_START -->` markers)
- `docs/operations/VALIDATE_MASTER_STRATEGY.md` — Estrategia (MANDATORY/CONDITIONAL)

### layer2_response_processor.py

Valida respuestas JSON de IA y genera reportes:

```python
@dataclass
class Layer2Finding:
    rule_id: str
    severity: str
    result: str
    node_path: str
    evidence: str
    recommendation: str
    confidence: float
    schema_valid: bool = True
    schema_error: str = ""

def validate_response_schema(data: dict, valid_rule_ids: set[str]) -> tuple[list[Layer2Finding], list[str]]
def validate_ai_summary(ai_summary: dict, fatal_count: int, warning_count: int, ...) -> list[str]
def process_layer2_response(response_data: dict, layer2_rules: list, valid_rule_ids: set, reports_dir: Path) -> tuple[...]
def write_layer2_reports(layer2_rules: list, findings: list, schema_errors: list, ...) -> None
```

**Validaciones:**
- Layer field = "MVET-LAYER2"
- Findings no contienen result="PASS"
- Summary counts son consistentes con hallazgos
- Todos los rule_ids son válidos
- Severities son FATAL|WARNING|SUGGESTION
- Confidence en rango [0.0, 1.0]

**Outputs:**
- `reports/validate_master_layer2_report.json` — Payload completo
- `reports/validate_master_layer2_report.md` — Reporte legible

### validate_tree_layer2.py

CLI puro que orquesta los módulos:

```bash
python scripts/validate_tree_layer2.py --print-prompt
python scripts/validate_tree_layer2.py --apply-response <archivo.json>
python scripts/validate_tree_layer2.py --apply-cycle <directorio>
```

## Contrato de Respuesta IA

Formato JSON esperado en respuesta:

```json
{
  "layer": "MVET-LAYER2",
  "findings": [
    {
      "rule_id": "MVET-L2-001",
      "severity": "WARNING",
      "result": "FAIL",
      "node_path": "Music > Pop > Electronic Pop",
      "evidence": "Descripción objetiva de lo observado",
      "recommendation": "Propuesta de mejora",
      "confidence": 0.85
    }
  ],
  "summary": {
    "total_fatal": 0,
    "total_warning": 3,
    "total_suggestion": 0,
    "decision_recommendation": "PASS_WITH_WARNINGS"
  }
}
```

## Testing

Suite de tests en `tests/test_validate_tree_layer2.py`:

| Test | Propósito |
|------|---|
| test_build_prompt_rejects_unresolved_placeholders | Valida que {{UNKNOWN}} sea detectado |
| test_process_layer2_response_reports_summary_mismatch_and_pass_items | Valida PASS filtering + summary consistency |
| test_load_governance_doc_groups_derives_strategy_matrix | Valida parsing de VALIDATE_MASTER_STRATEGY.md |
| test_response_processor_writes_both_report_formats | Valida generación de JSON + MD |

**Estado:** 4/4 tests ✅ (0.003s)

## Configuración Externa

### Plantilla de Prompt (`prompts/generadores/validate_master_layer2_prompt_template.md`)

Contiene placeholders reemplazables en temps de ejecución:
- `{{SYSTEM_CONTEXT}}` — Rol del sistema
- `{{CLONE_CONTEXT}}` — Contexto clone
- `{{GOVERNANCE_CONTEXT}}` — Reglas + documentos
- `{{RULES_BLOCK}}` — Reglas formateadas
- `{{TAXONOMY_TEXT}}` — Taxonomía master
- `{{OUTPUT_SCHEMA}}` — Estructura esperada JSON

### Contexto (`prompts/generadores/validate_master_layer2_prompt_context.json`)

```json
{
  "system_context": "Eres arquitecto de taxonomías...",
  "clone_context": "Tienes experiencia en...",
  "applicability_context": "Contexto de aplicabilidad..."
}
```

### Estrategia (`docs/operations/VALIDATE_MASTER_STRATEGY.md`)

Define qué documentos del governance cargar mediante secciones:
- `MANDATORY` — Siempre incluir
- `CONDITIONAL` — Incluir si existen
- `REFERENTIAL` — Solo referencia
- `EXCLUDED` — Excluir

## Mejoras Futuras

- [ ] Versionado de templates (metadata en YAML frontmatter)
- [ ] Config global en `scripts/config.py` para constantes de paths
- [ ] Integración automática de respuestas IA (actualmente manual)
- [ ] Soporte para múltiples LLMs
- [ ] Retry y fallback strategies
- [ ] Análisis agregado de hallazgos entre iteraciones

## Referencias Relacionadas

- [docs/operations/VALIDATE_MASTER_STRATEGY.md](../operations/VALIDATE_MASTER_STRATEGY.md) — Estrategia de validación
- [docs/governance/RULES_REGISTRY.md](../governance/RULES_REGISTRY.md) — Registro centralizado de reglas
- [docs/project-management/PROJECT_STATE.md](../project-management/PROJECT_STATE.md) — Estado general del proyecto
