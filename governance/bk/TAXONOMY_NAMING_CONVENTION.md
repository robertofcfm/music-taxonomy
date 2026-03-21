# CONVENCIÓN DE NOMBRADO TAXONÓMICO
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Estándares de nombrado para nodos de la taxonomía,
nodos fallback y consistencia de nombres clone.

Responsable:

Propietario del proyecto

Última actualización:

2026-03-15

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento define las reglas usadas para nombrar
géneros dentro de la taxonomía.

Un nombrado consistente es crítico para:

• precisión de clasificación
• legibilidad de la taxonomía
• evitar ambigüedad
• mantener claridad estructural

--------------------------------------------------
2. NOMBRES DE GÉNERO ÚNICOS
--------------------------------------------------

Cada nombre de género debe ser único en toda la taxonomía.

Dos nodos nunca deben compartir el mismo nombre salvo que
uno sea un nodo clone que referencie el nodo canónico.

Esto garantiza que los objetivos de clasificación
permanezcan no ambiguos.

--------------------------------------------------
3. REGLA DE IDIOMA
--------------------------------------------------

en inglés.
4. EVITAR TÉRMINOS AMBIGUOS
--------------------------------------------------

Los nombres de género deben representar estilos
musicales claramente identificables.

No se permiten los siguientes tipos de nombres:

• descripciones estilísticas vagas
• etiquetas de marketing
• descriptores no musicales



--------------------------------------------------
5. TITLE CASE
--------------------------------------------------

Los nombres de género deben seguir formato Title Case.

Ejemplos:

Alternative Rock
Synth Pop
Progressive Rock

Esto mejora legibilidad y consistencia.

--------------------------------------------------
6. NOMBRADO DE NODO GENERAL
--------------------------------------------------

Los nodos fallback deben seguir una regla estricta
de nombrado.

El nombre debe ser:

Parent Genre + "(General)"

Ejemplo:

Hard Rock (General)
Latin Rock (General)

Esto garantiza que los nodos fallback sean
claramente identificables.

--------------------------------------------------
7. NOMBRADO DE NODO CLONE
--------------------------------------------------

Los nodos clone deben usar el mismo nombre de género
que su nodo canónico.

Sin embargo, internamente deben referenciar
al nodo canónico.

Los nodos clone existen solo para navegación y soporte
de clasificación.

No contienen asignaciones de canciones independientes.

--------------------------------------------------
8. EVITAR NOMBRES EXCESIVAMENTE LARGOS
--------------------------------------------------

Los nombres de género deberían mantenerse concisos.

Evita etiquetas innecesariamente largas que combinen
múltiples descriptores.

Ejemplo de mal nombrado:

Alternative Progressive Experimental Rock

En su lugar, prioriza nombres de género
claramente establecidos.

--------------------------------------------------
9. CONSISTENCIA CON EL DATASET
--------------------------------------------------

Los nombres de género usados durante la clasificación
deben coincidir exactamente con los definidos
en la taxonomía.

El clasificador no debe inventar variaciones ni
sinónimos de nombres de género.

Los alias pueden manejarse por separado mediante
el sistema de aliases de género.

--------------------------------------------------
FIN CONVENCIÓN DE NOMBRADO TAXONÓMICO

<!-- REGLAS MIGRADAS A governance/reglas_validacion_arbol_script.md y governance/reglas_validacion_arbol_llm.md: idioma, Title Case, nodo General, nodo clone, nombres largos, términos ambiguos, consistencia con dataset -->

