# Reporte de Validación MVET (Capa 1)

- Fecha: 2026-03-15T22:47:26+00:00
- Archivo: taxonomy/genre_tree_master.md
- SHA256: 85e0abf22fb194319a16b32e3aabf0448915c184380737561491606ec3147e8c
- Decisión: PASS_WITH_WARNINGS
- FATAL: 0
- WARNING: 1

## Hallazgos

### MVET-L1-001 [FB-01] - FATAL - PASS
- Descripción: Debe existir un nodo raíz único.
- Evidencia: Raíces detectadas: 1
- Fuentes: docs/governance/SYSTEM_CONTRACT.md, docs/governance/TAXONOMY_RULES.md

### MVET-L1-002 [FB-01] - FATAL - PASS
- Descripción: Jerarquía válida por indentación.
- Evidencia: Sin errores de parser
- Fuentes: docs/governance/SYSTEM_CONTRACT.md, docs/governance/TAXONOMY_RULES.md

### MVET-L1-003 [FB-02] - FATAL - PASS
- Descripción: Nombres de género únicos (excepto clone permitido).
- Evidencia: Sin duplicados inválidos
- Fuentes: docs/governance/TAXONOMY_NAMING_CONVENTION.md

### MVET-L1-004 [FB-02] - FATAL - PASS
- Descripción: Formato de nombrado válido (Title Case y patrón General).
- Evidencia: Formato válido
- Fuentes: docs/governance/TAXONOMY_NAMING_CONVENTION.md

### MVET-L1-005 [FB-01] - FATAL - PASS
- Descripción: Nodos General explícitos y bajo su padre correspondiente.
- Evidencia: Nodos General válidos
- Fuentes: docs/governance/SYSTEM_CONTRACT.md, docs/governance/TAXONOMY_RULES.md

### MVET-L1-006 [FB-01] - FATAL - PASS
- Descripción: Restricciones de nodo clone (sin hijos).
- Evidencia: Sin clones con hijos
- Fuentes: docs/governance/SYSTEM_CONTRACT.md, docs/governance/TAXONOMY_RULES.md

### MVET-L1-007 [FB-03] - WARNING - FAIL
- Descripción: Profundidad recomendada 3-5 niveles.
- Evidencia: Min depth: 1, Max depth: 6
- Fuentes: docs/governance/TAXONOMY_DEPTH_POLICY.md, docs/governance/TAXONOMY_RULES.md

### MVET-L1-008 [FB-04] - FATAL - PASS
- Descripción: Inmutabilidad del archivo maestro.
- Evidencia: Hash estable durante la ejecución
- Fuentes: docs/governance/GLOBAL_RULES.md, docs/governance/SYSTEM_CONTRACT.md

### MVET-L1-009 [FB-02] - FATAL - PASS
- Descripción: Términos ambiguos prohibidos.
- Evidencia: Sin términos ambiguos
- Fuentes: docs/governance/TAXONOMY_NAMING_CONVENTION.md

### MVET-L1-010 [FB-04] - FATAL - PASS
- Descripción: Separación de dominio Latin en estructura base.
- Evidencia: Rama Latin válida bajo Music
- Fuentes: docs/governance/GLOBAL_RULES.md, docs/governance/SYSTEM_CONTRACT.md
