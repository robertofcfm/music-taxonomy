gobiernan la taxonomía de géneros.
y por el pipeline de generación de playlists.
Este archivo ha sido migrado. Las reglas de asignación de géneros con LLM se encuentran ahora en governance/reglas_asignacion_generos_llm.md
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

(Esta regla fue migrada a reglas_validacion_arbol_llm.md)

--------------------------------------------------
6. REGLA DE COHESIÓN DE PLAYLIST
--------------------------------------------------

(Esta regla fue migrada a reglas_validacion_arbol_llm.md)

--------------------------------------------------
7. POLÍTICA DE PROFUNDIDAD DE NODOS
--------------------------------------------------

(Esta regla fue migrada a reglas_validacion_arbol_script.md)

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

