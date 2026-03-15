# CONTRATO DEL SISTEMA
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Reglas obligatorias del sistema, restricciones de validación
y requisitos de ejecución.

Propietario:

Propietario del proyecto

Última Actualización:

2026-03-15

--------------------------------------------------
PROPÓSITO
--------------------------------------------------

Este documento define las reglas obligatorias que gobiernan el sistema.

Estas reglas no pueden ser violadas por ningún componente del proyecto.

--------------------------------------------------
1. GOBERNANZA DE TAXONOMÍA
--------------------------------------------------

La taxonomía es controlada manualmente por el usuario.

El sistema nunca debe:

- agregar géneros
- mover géneros
- fusionar géneros
- renombrar géneros

El sistema solo puede:

- sugerir mejoras
- reportar inconsistencias

Todas las modificaciones estructurales deben ser aprobadas por el usuario.

--------------------------------------------------
2. ESTRUCTURA DE TAXONOMÍA
--------------------------------------------------

La taxonomía debe seguir estas reglas:

- Nodo raíz único
- Jerarquía definida por indentación
- Solo nodos hoja pueden recibir asignaciones de canciones

Los géneros deben representar estilos musicales reales.

Los géneros nunca deben ser categorías vagas como:

- "Latin rhythms"
- "Latin music"
- "World music"
- "Misc"

Los nodos hoja deben representar géneros musicales específicos.

--------------------------------------------------
3. TIPOS DE NODO
--------------------------------------------------

El sistema soporta cuatro tipos de nodo.

NODO NORMAL

Nodo taxonómico estándar.

NODO CLONE

Nodo portal que referencia un nodo canónico.

Los nodos Clone:

- no tienen hijos
- no contienen canciones
- actúan solo como portales de navegación

NODO GENERAL

Nodo de respaldo usado cuando las canciones encajan en el género
padre pero no en ningún subgénero existente.

Ejemplo:

Hard Rock
  Glam Metal
  Arena Rock
  Hard Rock (General)

Reglas para nodos General:

- deben estar definidos explícitamente en la taxonomía
- el clasificador debe intentar otros géneros antes de usarlos
- no deben abusarse como categoría por defecto

NODO ATOMIC

Género que no debe subdividirse más.

Los nodos Atomic representan géneros donde más subdivisión
crearía categorías artificiales o sin significado.

--------------------------------------------------
4. REGLA DE LA RAMA LATIN
--------------------------------------------------

La música latina existe dentro de una rama Latin dedicada.

Si una canción es Latin:

Los géneros deben seleccionarse solo dentro de la rama Latin.

Si una canción no es Latin:

Los géneros no deben seleccionarse dentro de la rama Latin.

Esta regla evita mezclar estilos Latin y no-Latin que comparten
nombre de género pero producen distinta coherencia de playlists.

--------------------------------------------------
5. REGLA DE ASIGNACIÓN DE GÉNERO
--------------------------------------------------

Un género puede asignarse solo cuando sus características
musicales definitorias están claramente presentes en la canción.

La influencia estilística menor no cuenta.

Ejemplo:

Una canción con una sección corta de rap no debe clasificarse como rap.

Las canciones pueden tener múltiples géneros si las características
definitorias de cada uno están claramente presentes.

No hay jerarquía ni prioridad entre géneros.

Si una canción pertenece claramente a múltiples géneros,
todos deben asignarse.

--------------------------------------------------
6. REGLA DE VALIDEZ DE GÉNERO
--------------------------------------------------

Los géneros deben representar estilos musicales reales.

El clasificador debe evitar etiquetas vagas como:

- latin rhythms
- latin style
- latin music
- fusion style

Los nodos hoja deben corresponder a géneros claramente reconocidos.

--------------------------------------------------
7. PIPELINE DE CLASIFICACIÓN
--------------------------------------------------

El clasificador debe cargar la taxonomía antes de clasificar canciones.

Existen dos modos de ejecución.

MODO TEST

Tamaño de lote: 5 canciones.

Propósito:

- depuración
- validación del clasificador
- verificación de reglas

Los logs deben ser altamente detallados.

MODO PRODUCCIÓN

Tamaño de lote: 100 canciones.

Los logs deben confirmar:

- que la taxonomía fue cargada
- que las reglas del sistema fueron cargadas
- versión del clasificador

El procesamiento por lotes es obligatorio.

Reglas de continuidad de lotes:

- la clasificación por lotes debe soportar resultados parciales
- las clasificaciones exitosas deben agregarse a la salida
- las canciones no clasificadas deben permanecer en cola
- la ejecución del lote debe detenerse al exceder el umbral de error

--------------------------------------------------
8. REGLA DE NODO FALTANTE
--------------------------------------------------

Si una canción requiere un género que no existe en la taxonomía,
el sistema debe detener la clasificación.

El sistema debe generar un reporte sugiriendo
un nuevo nodo de género.

Regla de lote:

Un lote puede generar un máximo de 5 reportes de nodo faltante.

Si aparecen más de 5, la ejecución debe detenerse.

--------------------------------------------------
9. MANEJO DE ERRORES
--------------------------------------------------

Los errores fatales detienen el procesamiento inmediatamente.

Ejemplos:

- género faltante en la taxonomía
- clasificación ambigua
- nodo taxonómico inválido
- estructura taxonómica inválida

Los reportes de error deben contener:

- título de la canción
- artista
- descripción del problema
- solución sugerida

El diagnóstico de errores debe ser suficientemente detallado
para soportar análisis de causa raíz y acción correctiva.

--------------------------------------------------
10. VALIDACIÓN DE TAXONOMÍA
--------------------------------------------------

Antes de cada release la taxonomía debe validarse.

La validación debe detectar:

- similitud entre géneros hermanos
- violaciones de cohesión de playlists
- nodos redundantes
- candidatos a nodos atomic
- posibles fusiones

Un release no puede avanzar hasta que los problemas
de validación estén resueltos.

--------------------------------------------------
11. CONTROL DE VERSIONES
--------------------------------------------------

Las versiones de taxonomía deben rastrearse.

Ejemplo:

taxonomy_version = 1.0

Las salidas de clasificación deben incluir:

- taxonomy_version
- classifier_version
- reglas_version

Esto permite reanudar clasificación o detectar
incompatibilidades.

--------------------------------------------------
12. REGLA DE COMPATIBILIDAD
--------------------------------------------------

Si la taxonomía cambia de forma que rompe compatibilidad,
las salidas de clasificación previas quedan obsoletas.

En ese caso:

Todas las canciones deben reclasificarse.

Si la taxonomía cambia sin romper compatibilidad:

- solo las canciones afectadas deberían reevaluarse
- las no afectadas no deben reclasificarse innecesariamente

--------------------------------------------------
FIN CONTRATO DEL SISTEMA

