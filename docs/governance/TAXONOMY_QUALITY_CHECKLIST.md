# CHECKLIST DE CALIDAD TAXONÓMICA
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Criterios de revisión de calidad para evaluar
la preparación de la taxonomía antes de cambios
o releases.

Responsable:

Propietario del proyecto

Última actualización:

2026-03-15

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento define el checklist usado para evaluar
la calidad de la taxonomía de géneros.

El checklist ayuda a detectar problemas estructurales
antes de crear un release.

El objetivo es mantener una taxonomía que sea:

• musicalmente coherente
• estructuralmente balanceada
• fácil de usar para clasificar
• adecuada para generación de playlists

--------------------------------------------------
2. CUÁNDO EJECUTAR EL CHECKLIST
--------------------------------------------------

El checklist de calidad taxonómica debe ejecutarse:

• antes de crear un release
• después de modificar la taxonomía
• después de agregar nuevos géneros
• después de fusionar o reubicar nodos

Un release no debe avanzar si quedan issues sin resolver.

--------------------------------------------------
3. CHECK DE ESTRUCTURA RAÍZ
--------------------------------------------------

Verifica que la taxonomía tenga exactamente un nodo raíz.

Ejemplo:

Music

Todos los géneros deben descender de esta raíz.

--------------------------------------------------
4. DISTINCIÓN ENTRE GÉNEROS HERMANOS
--------------------------------------------------

Verifica que los géneros hermanos representen
estilos musicales claramente distinguibles.

Preguntas guía:

• ¿Estos géneros producen playlists con sonido distinto?
• ¿Las canciones se pueden asignar claramente a uno u otro?
• ¿Representan categorías musicales reconocidas?

Si la respuesta no es clara, considera fusionarlos.

--------------------------------------------------
5. CHECK DE REDUNDANCIA DE GÉNEROS
--------------------------------------------------

Revisa si dos géneros representan el mismo estilo.

Puede haber redundancia cuando:

• diferentes nombres se refieren al mismo estilo
• los subgéneros se solapan fuertemente
• existen inconsistencias históricas de nombrado

En estos casos, puede recomendarse una fusión.

--------------------------------------------------
6. REVISIÓN DE EXPANSIÓN DE NODOS
--------------------------------------------------

Revisa si nodos grandes deberían expandirse.

Indicadores de expansión:

• gran número de canciones en un nodo
• existencia de subgéneros reconocibles
• playlists demasiado diversas

Umbral de referencia:

45 canciones.

--------------------------------------------------
7. REVISIÓN DE GÉNEROS ATÓMICOS
--------------------------------------------------

Revisa si ciertos nodos deberían marcarse como atómicos.

Un nodo debe considerarse atómico cuando:

• no existen subgéneros ampliamente reconocidos
• subdividir más daña la cohesión de playlists
• el género ya representa un estilo muy específico

Los nodos atómicos no deberían subdividirse.

--------------------------------------------------
8. USO DE NODO GENERAL
--------------------------------------------------

Verifica que los nodos General se usen correctamente.

Checklist:

• ¿El género padre justifica un nodo fallback?
• ¿Se están acumulando canciones incorrectamente en General?
• ¿Podrían definirse subgéneros nuevos en su lugar?

Los nodos General no deben convertirse en categoría por defecto.

--------------------------------------------------
9. CHECK DE BALANCE DE PROFUNDIDAD
--------------------------------------------------

Verifica que la profundidad de la taxonomía
se mantenga balanceada.

Problemas a detectar:

• ramas excesivamente profundas
• ramas extremadamente superficiales
• crecimiento jerárquico desigual

--------------------------------------------------
10. CHECK DE REUBICACIÓN DE NODOS
--------------------------------------------------

Verifica que los géneros estén bajo
el nodo padre más apropiado.

Si un género parece pertenecer de forma más natural
a otra rama, debe considerarse su reubicación.

--------------------------------------------------
11. CHECK DE SOBRE-FRAGMENTACIÓN
--------------------------------------------------

Detecta ramas que se hayan subdividido en exceso.

Indicadores:

• géneros hermanos demasiado pequeños
• géneros difíciles de distinguir
• especialización excesiva

En estos casos, la taxonomía puede requerir simplificación.

--------------------------------------------------
12. VALIDACIÓN DE RAMA LATIN
--------------------------------------------------

Verifica que los géneros Latin permanezcan
dentro de la rama Latin.

Las canciones clasificadas como Latin no deben
usar géneros fuera de esa rama.

--------------------------------------------------
13. CONSISTENCIA DE NOMBRADO
--------------------------------------------------

Verifica que los nombres de género respeten
las convenciones de nombrado.

Revisa:

• uso de Title Case
• patrones de nombrado consistentes
• ausencia de etiquetas ambiguas

--------------------------------------------------
14. VALIDACIÓN DE RELEASE
--------------------------------------------------

Antes de crear un release del proyecto, verifica que:

• todos los issues taxonómicos fueron revisados
• no quedan problemas estructurales sin resolver
• la estructura taxonómica es coherente
• se respetan las convenciones de nombrado

Un release no debe avanzar si el checklist falla.

--------------------------------------------------
FIN CHECKLIST DE CALIDAD TAXONÓMICA

