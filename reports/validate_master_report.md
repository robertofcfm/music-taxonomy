# Reporte de Validación MVET (Capa 1)

- Fecha: 2026-03-16T01:20:27+00:00
- Archivo: taxonomy/genre_tree_master.md
- SHA256: a657efe1f7a615e73e615084a431d926f85e230938e383d27a90ea932b853dbe
- Decisión: PASS
- FATAL: 0
- WARNING: 0

## Hallazgos

### MVET-L1-001 [FB-01] - FATAL - PASS
- Descripción: Debe existir un nodo raíz único.
- Evidencia: Raíces detectadas: 1
- Causantes: N/A
- Fuentes: docs/governance/SYSTEM_CONTRACT.md, docs/governance/TAXONOMY_RULES.md

### MVET-L1-002 [FB-01] - FATAL - PASS
- Descripción: Jerarquía válida por indentación.
- Evidencia: Sin errores de parser
- Causantes: N/A
- Fuentes: docs/governance/SYSTEM_CONTRACT.md, docs/governance/TAXONOMY_RULES.md

### MVET-L1-003 [FB-02] - FATAL - PASS
- Descripción: Nombres de género únicos (excepto clone permitido).
- Evidencia: Sin duplicados inválidos
- Causantes: N/A
- Fuentes: docs/governance/TAXONOMY_NAMING_CONVENTION.md

### MVET-L1-004 [FB-02] - FATAL - PASS
- Descripción: Formato de nombrado válido (Title Case y patrón General).
- Evidencia: Formato válido
- Causantes: N/A
- Fuentes: docs/governance/TAXONOMY_NAMING_CONVENTION.md

### MVET-L1-005 [FB-01] - FATAL - PASS
- Descripción: Nodos General explícitos y bajo su padre correspondiente.
- Evidencia: Nodos General válidos
- Causantes: N/A
- Fuentes: docs/governance/SYSTEM_CONTRACT.md, docs/governance/TAXONOMY_RULES.md

### MVET-L1-006 [FB-01] - FATAL - PASS
- Descripción: Restricciones de nodo clone (sin hijos).
- Evidencia: Sin clones con hijos
- Causantes: N/A
- Fuentes: docs/governance/SYSTEM_CONTRACT.md, docs/governance/TAXONOMY_RULES.md

### MVET-L1-007 [FB-03] - WARNING - PASS
- Descripción: Profundidad mínima estructural >= 3.
- Evidencia: Max leaf depth: 5. La evaluación de profundidad máxima por criterio atómico corresponde a Capa 2.
- Causantes: N/A
- Fuentes: docs/governance/TAXONOMY_DEPTH_POLICY.md, docs/governance/TAXONOMY_RULES.md

### MVET-L1-008 [FB-04] - FATAL - PASS
- Descripción: Inmutabilidad del archivo maestro.
- Evidencia: Hash estable durante la ejecución
- Causantes: N/A
- Fuentes: docs/governance/GLOBAL_RULES.md, docs/governance/SYSTEM_CONTRACT.md

### MVET-L1-009 [FB-02] - FATAL - PASS
- Descripción: Términos ambiguos prohibidos.
- Evidencia: Sin términos ambiguos
- Causantes: N/A
- Fuentes: docs/governance/TAXONOMY_NAMING_CONVENTION.md

### MVET-L1-010 [FB-04] - FATAL - PASS
- Descripción: Separación de dominio Latin en estructura base.
- Evidencia: Rama Latin válida bajo Music
- Causantes: N/A
- Fuentes: docs/governance/GLOBAL_RULES.md, docs/governance/SYSTEM_CONTRACT.md
