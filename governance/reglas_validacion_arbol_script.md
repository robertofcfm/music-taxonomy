# Reglas de Validación de Árbol (Script)

Aquí se colocarán únicamente las reglas que pueden ser validadas de forma determinista mediante scripts.

## Formato sugerido
- Cada regla debe tener: id, descripción, severidad, lógica de validación.
- Ejemplo:

---
- id: ARBOL-S-001
  descripcion: "Todos los nodos deben tener un padre salvo la raíz."
  severidad: FATAL
  logica: "Recorrer el árbol y verificar que solo la raíz no tenga padre."
---

(Agregar reglas conforme se identifiquen en la migración)
