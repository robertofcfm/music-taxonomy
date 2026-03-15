# REGLAS GLOBALES
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Reglas transversales que gobiernan más de un
componente del repositorio.

Propietario:

Propietario del proyecto

Última Actualización:

2026-03-15

--------------------------------------------------
PROPÓSITO
--------------------------------------------------

Este documento define reglas que aplican a
múltiples subsistemas del proyecto.

Estas reglas afectan componentes del sistema como:

• taxonomía
• clasificador
• mapeo de alias
• validación del sistema
• generación de playlists

Las reglas que aplican a más de un componente
deben colocarse aquí.

--------------------------------------------------
REGLAS GLOBALES
--------------------------------------------------

G001 — AUTORIDAD DE LA TAXONOMÍA

La taxonomía define los únicos géneros válidos
para el sistema de clasificación.

Todos los géneros asignados a canciones deben existir
en la taxonomía.

--------------------------------------------------

G002 — NO INVENTAR GÉNEROS

El clasificador nunca debe inventar géneros.

Todos los géneros asignados deben corresponder a
nodos existentes en la taxonomía.

--------------------------------------------------

G003 — FALLO POR GÉNERO FALTANTE

Si falta un género requerido en la taxonomía,
el sistema debe producir un error fatal.

--------------------------------------------------

G004 — POLÍTICA DE ERROR FATAL

Los errores fatales deben detener la ejecución y
reportar la causa del fallo.

--------------------------------------------------

G005 — CLASIFICACIÓN MULTI-GÉNERO

Una canción puede pertenecer a múltiples géneros
cuando esté musicalmente justificado.

--------------------------------------------------

G006 — NORMALIZACIÓN DE GÉNERO

Los nombres de género deben normalizarse antes de
la clasificación.

--------------------------------------------------

G007 — RESOLUCIÓN DE ALIAS

Los alias de género deben resolverse a géneros
canónicos de la taxonomía.

--------------------------------------------------

G008 — INMUTABILIDAD DE LA TAXONOMÍA

El sistema nunca debe modificar la taxonomía automáticamente.

--------------------------------------------------

G009 — AUTORIDAD DE EDICIÓN DE TAXONOMÍA

Solo el propietario del proyecto puede editar la plantilla taxonómica.

--------------------------------------------------

G010 — CONSISTENCIA DE VERSIÓN DE TAXONOMÍA

Las versiones de plantilla y taxonomía operativa siempre deben coincidir.
Si las versiones difieren, la taxonomía operativa debe regenerarse.

--------------------------------------------------

G011 — CONSISTENCIA DE PLAYLISTS

La taxonomía, la clasificación y la estructura de playlists deben
mantener coherencia musical.
La estructura de playlists debe seguir la jerarquía taxonómica.

--------------------------------------------------

G012 — SEPARACIÓN DEL DOMINIO LATIN

Los dominios de clasificación Latin y no-Latin son independientes.
Las canciones Latin deben usar solo géneros de la rama Latin.
Las canciones no-Latin no deben usar géneros de la rama Latin.

--------------------------------------------------

G013 — POLÍTICA DE ASIGNACIÓN CANÓNICA

Las canciones deben asignarse a nodos canónicos de la taxonomía,
no a nodos clone.

--------------------------------------------------

G014 — NO AUTOMATIZAR PROPUESTAS

El clasificador puede sugerir géneros pero no debe agregarlos automáticamente.

--------------------------------------------------

G015 — SEPARACIÓN ENTRE ESTRUCTURA Y ASIGNACIÓN

Las asignaciones de género deben almacenarse por separado de la
estructura taxonómica.

--------------------------------------------------

G016 — RESTRICCIONES DEL ÁRBOL GENERADO

El árbol generado debe seguir la estructura taxonómica y no debe
alterar datos de la taxonomía.

--------------------------------------------------

G017 — SEPARACIÓN DATASET/TAXONOMÍA

El estado del dataset no debe modificar la taxonomía automáticamente.

--------------------------------------------------

G018 — TRAZABILIDAD VERSIONADA DE CLASIFICACIÓN

El sistema debe versionar taxonomía/reglas, y los resultados de
clasificación deben registrar la versión de taxonomía utilizada.

--------------------------------------------------

G019 — RECLASIFICACIÓN ANTE CAMBIO

Los cambios en la taxonomía pueden requerir reclasificación de
resultados afectados.

--------------------------------------------------

G020 — CONSISTENCIA REPOSITORIO/DOCUMENTACIÓN

El contenido del repositorio debe mantenerse consistente con la
documentación y los principios de diseño.

--------------------------------------------------

---
REGLA 019

La influencia estilística menor no debe activar
la asignación de género.

---

FIN DEL ARCHIVO

