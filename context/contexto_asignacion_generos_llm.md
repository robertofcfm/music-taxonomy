# CONTEXTO PARA ASIGNACIÓN DE GÉNEROS CON LLM
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
OBJETIVO DE ESTE CONTEXTO
--------------------------------------------------

Este archivo define el contexto mínimo y relevante para la tarea de asignar géneros musicales a canciones usando un modelo LLM, siguiendo la estrategia de prompts tipo capa2.

--------------------------------------------------
1. PROPÓSITO DEL PROYECTO
--------------------------------------------------

Construir una taxonomía estructurada de géneros musicales y un sistema de clasificación capaz de asignar géneros precisos a canciones.

La taxonomía es la base de conocimiento y permite generar playlists coherentes basadas en la jerarquía de géneros.

--------------------------------------------------
2. OBJETIVO DE LA TAREA
--------------------------------------------------

Clasificar canciones en géneros musicales significativos usando LLM, manteniendo la coherencia con la taxonomía y asegurando que las asignaciones sean precisas y justificadas.

--------------------------------------------------
3. PRINCIPIOS OPERATIVOS
--------------------------------------------------

- Usar solo el contexto mínimo necesario para la tarea.
- No duplicar reglas ni contexto en otros archivos.
- Separar claramente la lógica de procesamiento LLM de la lógica de procesamiento por script.
- Mantener la integridad de la taxonomía: solo asignar géneros válidos definidos en la estructura maestra.
- Una canción solo puede ser asignada a uno o más géneros si estos representan de manera predominante su carácter musical. No se deben asignar géneros cuya influencia sea secundaria o marginal en la obra.

--------------------------------------------------
4. MODELO DE COMPOSICIÓN DE PROMPTS
--------------------------------------------------

- El prompt debe construirse con un núcleo pequeño y módulos seleccionados por tarea.
- Declarar imports por grupos y justificar cobertura.
- No usar herencia formal de plantillas, solo composición explícita.

--------------------------------------------------
5. ARQUITECTURA RELEVANTE
--------------------------------------------------

- FASE 1: Diseño de taxonomía (estructura de géneros)
- FASE 2: Identificación de género de canciones (asignación por LLM)

--------------------------------------------------
6. RESTRICCIONES
--------------------------------------------------

- No modificar la taxonomía desde el proceso de asignación.
- No usar información fuera de la taxonomía y contexto definidos aquí.
- Si falta información crítica, detener y reportar faltantes.

--------------------------------------------------
7. CRITERIO DE CIERRE
--------------------------------------------------

La tarea se considera completa cuando cada canción ha sido asignada a uno o más géneros válidos, siguiendo la taxonomía y sin violar las restricciones anteriores.
