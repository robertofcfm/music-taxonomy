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

## Reglas estructurales validadas por script
  descripcion: "La taxonomía debe tener un nodo raíz único."
  severidad: FATAL
  logica: "Verificar que solo existe un nodo sin padre."
  descripcion: "Cada nombre de género debe ser único en toda la taxonomía."
  severidad: FATAL
  logica: "Verificar que no hay nombres duplicados salvo clones explícitos."
  descripcion: "Checklist de calidad estructural debe cumplirse antes de release."
  severidad: WARNING
  logica: "Ejecutar checklist de coherencia, balance y facilidad de uso."
- id: ARBOL-S-003
  descripcion: "Fuera de la rama Latin, los nombres de género deben estar en inglés; dentro de Latin, se permite español o inglés reconocido."
  severidad: WARNING
  logica: "Verificar idioma de los nombres según la rama."
- id: ARBOL-S-004
  descripcion: "Todos los nombres de género deben estar en Title Case."
  severidad: WARNING
  logica: "Verificar que cada nombre de género sigue el formato Title Case."
- id: ARBOL-S-006
  descripcion: "Los nodos General deben nombrarse como 'Parent Genre (General)'."
  severidad: WARNING
  logica: "Verificar que los nodos General sigan la convención de nombrado."
- id: ARBOL-S-007
  descripcion: "Los nodos clone deben usar el mismo nombre que su nodo canónico y no deben tener canciones propias."
  severidad: WARNING
  logica: "Verificar que los nodos clone cumplen las reglas de nombrado y asignación."
- id: ARBOL-S-008
  descripcion: "Los nombres de género usados en clasificación deben coincidir exactamente con los definidos en la taxonomía."
  severidad: FATAL
  logica: "Verificar coincidencia exacta entre nombres usados y los definidos; alias solo por sistema de alias."
