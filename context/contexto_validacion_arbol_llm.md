# Contexto para Validación de Árbol (LLM)

Contexto mínimo necesario para validaciones que requieren LLM.

## Contexto adicional para validaciones LLM
- La redundancia puede surgir por alias, solapamiento o inconsistencias históricas de nombrado.
- Nodos con muchas canciones o playlists diversas pueden requerir subdivisión si existen subgéneros reconocibles (umbral sugerido: 45 canciones).
- Un nodo atómico no debe subdividirse si representa un estilo muy específico y la cohesión de playlists se vería afectada.
- El balance de profundidad busca evitar ramas excesivamente profundas o superficiales y crecimiento jerárquico desigual.
- Los géneros deben estar bajo el nodo padre más apropiado según afinidad musical.
- La sobre-fragmentación ocurre cuando hay hermanos pequeños, difícil de distinguir o especialización excesiva.
- Nombres ambiguos, vagos, de marketing o no musicales deben evitarse; priorizar nombres musicales reconocidos.
- Los nombres de género deben ser concisos y no combinar múltiples descriptores innecesarios.

(Agregar detalles conforme se identifiquen en la migración)
