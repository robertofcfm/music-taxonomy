# REGLAS DE TAXONOMÍA
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Reglas estructurales de taxonomía usadas por
validación, clasificación y generación de playlists.

Responsable:

Propietario del proyecto

Última actualización:

2026-03-15

--------------------------------------------------
PROPÓSITO
--------------------------------------------------

Este documento define las reglas estructurales que
gobiernan la taxonomía de géneros.

La taxonomía representa la base de conocimiento
musical del sistema y es usada por el clasificador
y por el pipeline de generación de playlists.

--------------------------------------------------
1. PROPÓSITO DE LA TAXONOMÍA
--------------------------------------------------

La taxonomía define la estructura usada para
organizar géneros musicales.

La taxonomía debe mantenerse editable por humanos.

Su propósito es:

- representar relaciones entre géneros
- guiar la clasificación de canciones
- asegurar coherencia de playlists

La taxonomía debe priorizar la coherencia musical
por encima de la completitud.

Los géneros deben representar estilos musicalmente
significativos. Descriptores genéricos o vagos
no son nodos válidos de género.

--------------------------------------------------
2. ESTRUCTURA RAÍZ
--------------------------------------------------

La taxonomía debe tener un nodo raíz único.

Ejemplo:

Music

Todos los géneros deben descender de esta raíz.

--------------------------------------------------
3. DEFINICIÓN DE JERARQUÍA
--------------------------------------------------

La jerarquía se define por indentación.

Ejemplo:

Music
  Rock
    Alternative Rock
      Indie Rock
      Grunge

Cada nivel de indentación representa una
especialización más profunda.

--------------------------------------------------
4. REGLA DE NODO HOJA
--------------------------------------------------

Las canciones solo pueden clasificarse en nodos hoja.

Los nodos hoja son nodos que no tienen hijos.

Ejemplo:

Music
  Rock
    Alternative Rock
      Indie Rock
      Grunge

Solo:

- Indie Rock
- Grunge

son objetivos válidos de clasificación.

--------------------------------------------------
5. REGLA DE GÉNEROS HERMANOS
--------------------------------------------------

Los géneros que comparten el mismo padre deben
representar estilos musicalmente distinguibles.

Los géneros hermanos no deben ser tan similares
que produzcan playlists indistinguibles.

Si no pueden distinguirse con claridad,
deberían fusionarse.

--------------------------------------------------
6. REGLA DE COHESIÓN DE PLAYLIST
--------------------------------------------------

La taxonomía debe priorizar la coherencia de playlist.

Si un nodo genera playlists inconsistentes,
la taxonomía debe ajustarse.

Acciones posibles:

- fusionar géneros hermanos
- mover nodos a otro padre
- dividir géneros cuando sea necesario

--------------------------------------------------
7. POLÍTICA DE PROFUNDIDAD DE NODOS
--------------------------------------------------

La taxonomía debería mantener una profundidad moderada.

Profundidad típica:

3–5 niveles.

Deben evitarse jerarquías excesivamente profundas,
salvo cuando representen distinciones musicales
realmente significativas.

--------------------------------------------------
8. REGLA DE EXPANSIÓN
--------------------------------------------------

Un nodo puede expandirse cuando el número de canciones
asignadas supera el umbral de expansión.

Umbral de expansión:

45 canciones.

Cuando ocurre expansión, el nodo se convierte en padre
y sus canciones deben redistribuirse entre subgéneros.

--------------------------------------------------
9. POLÍTICA DE NODO GENERAL
--------------------------------------------------

Un nodo puede contener un subnodo General cuando
los subgéneros existentes no cubren completamente
el género padre.

Los nodos General actúan como fallback explícito
para canciones que no encajan en subgéneros conocidos
de ese padre.

Ejemplo:

Hard Rock
  Glam Metal
  Arena Rock
  Hard Rock (General)

Los nodos General deben:

- estar definidos explícitamente
- no crearse automáticamente por el sistema
- no reemplazar creación apropiada de géneros
- usarse solo cuando sea necesario

--------------------------------------------------
10. REGLA DE GÉNERO ATÓMICO
--------------------------------------------------

Algunos géneros no deberían subdividirse más.

Estos géneros se consideran atómicos.

Los géneros atómicos representan estilos donde
subdividir más crearía distinciones artificiales.

--------------------------------------------------
11. ESTRUCTURA DE RAMA LATIN
--------------------------------------------------

La música Latin existe en una rama dedicada.

Ejemplo:

Music
  Latin
    Latin Rock
    Latin Pop
    Regional Latin

Los géneros dentro de Latin representan estilos
propios de tradiciones musicales latinas.

Las canciones clasificadas como Latin deben usar
esta rama.

--------------------------------------------------
12. REGLA DE NOMBRADO DE GÉNEROS
--------------------------------------------------

Los nombres de género deben cumplir estas reglas:

- Title Case
- significado musical claro
- sin abreviaciones, salvo que estén ampliamente aceptadas

Evita etiquetas vagas o descriptivas.

Ejemplos de nombres inválidos:

- Latin Style
- Misc Genres
- Mixed Music

--------------------------------------------------
13. POLÍTICA DE MODIFICACIÓN DE TAXONOMÍA
--------------------------------------------------

Las modificaciones taxonómicas deben hacerse manualmente.

El sistema no puede modificar automáticamente la taxonomía.

El sistema solo puede:

- sugerir nuevos nodos
- reportar inconsistencias
- proponer mejoras estructurales

Todos los cambios deben ser aprobados por el usuario.

--------------------------------------------------
14. VALIDACIÓN DE TAXONOMÍA
--------------------------------------------------

Antes de un release, la taxonomía debe validarse.

La validación incluye:

- similitud entre géneros hermanos
- nodos redundantes
- jerarquías excesivamente profundas
- problemas de cohesión de playlists

--------------------------------------------------
15. REPRESENTACIÓN FUENTE Y OPERATIVA
--------------------------------------------------

La fuente editable autoritativa de la taxonomía es:

taxonomy/genre_tree_master.md

La taxonomía maestra debe mantenerse directamente
editable por usuarios.

La taxonomía operativa debe generarse a partir
de la plantilla maestra.

La representación operativa debe ser machine-readable
y debe incluir códigos numéricos de nodo.

El árbol de playlists debe generarse dinámicamente
desde canciones clasificadas usando esta taxonomía.

--------------------------------------------------
16. POLÍTICA DE GÉNEROS CLONE E HÍBRIDOS
--------------------------------------------------

La taxonomía soporta nodos clone.

Reglas de nodos clone:

- un clone debe referenciar un nodo canónico
- los nodos clone no deben tener hijos
- los nodos clone actúan como portales de navegación
- existen para evitar duplicación estructural
- los nodos canónicos pueden tener hijos

La taxonomía soporta géneros híbridos.

Reglas de géneros híbridos:

- un híbrido puede aparecer en múltiples ramas conceptuales
- cuando se representa en varias ramas, deberían usarse
  nodos clone para apuntar al nodo canónico

--------------------------------------------------
FIN REGLAS DE TAXONOMÍA

