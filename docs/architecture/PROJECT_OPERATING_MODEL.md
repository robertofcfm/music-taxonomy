# MODELO OPERATIVO DEL PROYECTO
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
1. PROPÓSITO
--------------------------------------------------

Este documento define el modelo operativo del
Sistema de Taxonomía de Géneros Musicales.

El proyecto opera mediante tres actividades distintas.

Cada actividad manipula un tipo de dato diferente
y debe seguir reglas específicas.

Entender esta separación es crítico para mantener
la integridad del sistema.

--------------------------------------------------
2. PRINCIPIO CENTRAL
--------------------------------------------------

El sistema separa tres frentes:

1. Definición de taxonomía
2. Identificación de género en canciones
3. Generación de árbol de géneros guiada por dataset

Cada actividad interactúa con archivos distintos y
no debe modificar datos que pertenezcan a otra actividad.

--------------------------------------------------
3. ACTIVIDAD 1 — GESTIÓN DE PLANTILLA TAXONÓMICA
--------------------------------------------------

Propósito:

Definir y mantener la taxonomía maestra de géneros.

La taxonomía actúa como la definición autoritativa
de géneros usada por todo el sistema.

Características clave:

• mantenimiento manual
• define hojas de género válidas
• define relaciones jerárquicas entre géneros
• no contiene datos de canciones

Archivo principal:

taxonomy/genre_tree_master.md

Este archivo contiene la estructura taxonómica editable
por humanos usando indentación.

--------------------------------------------------

Representación operativa:

taxonomy/genre_tree_operational.csv

Este archivo se genera a partir de la taxonomía maestra
y es usado por scripts y herramientas de clasificación.

--------------------------------------------------

Regla importante:

La plantilla taxonómica nunca se modifica automáticamente.

Las herramientas de automatización solo pueden:

• validar
• analizar
• sugerir mejoras

Solo el project owner modifica la taxonomía maestra.

--------------------------------------------------
4. ACTIVIDAD 2 — IDENTIFICACIÓN DE GÉNERO EN CANCIONES
--------------------------------------------------

Propósito:

Determinar a qué géneros pertenece una canción.

Este proceso analiza canciones y asigna géneros
basados en la taxonomía.

Archivo de entrada:

catalog/songs_raw.csv

Este archivo contiene la lista de canciones a clasificar.

Archivo de salida:

catalog/songs_with_genres.csv

Este archivo almacena los resultados de clasificación.

--------------------------------------------------

Reglas de clasificación:

• Los géneros deben existir en la taxonomía
• Los géneros deben corresponder a hojas taxonómicas
• Las canciones pueden pertenecer a múltiples géneros
• No deben considerarse influencias estilísticas menores

Ejemplo:

Una canción con una sección breve de rap no debería
clasificarse como Rap, a menos que el rap sea una
parte estructural de la canción.

--------------------------------------------------

Manejo de género faltante:

Si no se encuentra un género adecuado en la taxonomía,
el proceso de clasificación debe detenerse y reportar
un error fatal.

Luego, la taxonomía debe expandirse manualmente.

--------------------------------------------------
5. ACTIVIDAD 3 — GENERACIÓN DINÁMICA DE ÁRBOL DE GÉNEROS
--------------------------------------------------

Propósito:

Generar un árbol de escucha basado en el catálogo
musical real.

Este árbol se deriva de la taxonomía y del dataset
de canciones clasificadas.

La estructura resultante puede usarse para generar
playlists basadas en géneros.

--------------------------------------------------

Regla de expansión:

Un nodo se vuelve expandible cuando el número de canciones
asignadas a ese nodo supera:

45 canciones

Cuando esto ocurre:

• el nodo se convierte en padre
• las canciones se redistribuyen en subgéneros

Esto permite que el árbol crezca de manera orgánica
de acuerdo con el catálogo real.

Los nodos sin canciones asignadas permanecen inactivos y
representan ramas taxonómicas actualmente sin uso.

--------------------------------------------------
6. ESTRATEGIA DE GÉNEROS LATINOS
--------------------------------------------------

La música latina se trata como una rama separada.

Si una canción se identifica como música latina,
sus géneros deben seleccionarse del subárbol Latin.

Esto evita mezclar contextos de géneros latinos y no latinos
que con frecuencia representan tradiciones musicales distintas.

--------------------------------------------------
7. TIPOS ESPECIALES DE NODOS
--------------------------------------------------

La taxonomía soporta varios tipos especiales de nodos.

NORMAL

Nodo de género estándar.

CLONE

Nodo que referencia otro nodo canónico.
Los nodos Clone actúan como portales de navegación y
no duplican el subárbol.

GENERAL

Nodo de respaldo usado cuando una canción pertenece a un
género padre pero no coincide con ningún subgénero definido.

Ejemplo:

Hard Rock
  Glam Metal
  Arena Rock
  Hard Rock (General)

ATOMIC

Género terminal que no debe subdividirse más,
porque ya representa un estilo específico.

--------------------------------------------------
8. VERSIONADO
--------------------------------------------------

La versión de taxonomía se almacena en:

taxonomy/taxonomy_version.md

Los resultados de clasificación guardan la versión de
taxonomía usada durante la clasificación.

Si la estructura taxonómica cambia,
clasificaciones previas pueden volverse incompatibles.

--------------------------------------------------
9. MODELO DE NAVEGACIÓN DEL PROYECTO
--------------------------------------------------

La taxonomía también funciona como estructura de
navegación de playlists.

Los usuarios deberían poder subir o bajar por la
jerarquía de géneros para encontrar playlists que
coincidan con un estado de ánimo musical deseado.

Cada nodo puede corresponder a una playlist.

--------------------------------------------------
FIN DOCUMENTO