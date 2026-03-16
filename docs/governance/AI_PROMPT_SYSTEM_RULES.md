# REGLAS DEL SISTEMA DE COMPOSICION DE PROMPTS
Sistema de Taxonomía de Géneros Musicales

--------------------------------------------------
METADATOS DEL DOCUMENTO
--------------------------------------------------

Alcance:

Reglas que gobiernan la composicion de prompts para IA
en este proyecto.

Propietario:

Propietario del proyecto

Última actualización:

2026-03-16

--------------------------------------------------
1. PRINCIPIOS DE COMPOSICIÓN
--------------------------------------------------

P1 — NÚCLEO PEQUEÑO Y ESTABLE

Toda sesión debe cargar un conjunto mínimo de documentos
canónicos que evite respuestas erráticas.

P2 — CARGA SELECTIVA POR TAREA

Cada prompt debe sumar solo reglas y contexto que tengan
injerencia directa en el trabajo actual.

P3 — CONTEXTO NO ES REGLA

Los documentos contextuales ayudan a orientar decisiones,
pero no deben convertirse en fuente de obligaciones si no
son documentos normativos.

P4 — CONSISTENCIA NORMATIVA

No debe existir conflicto entre documentos normativos.

Si se detecta un conflicto durante la generación o uso
de una instancia, debe reportarse y corregirse en el
documento fuente antes de continuar.

Un sistema bien gobernado no resuelve conflictos por
precedencia en tiempo de ejecución; los elimina en el origen.

P5 — TAMAÑO CONTROLADO

Si el prompt crece demasiado, baja la calidad operativa.
Debe existir un presupuesto de contexto por sesión.

La instancia concreta debe incluir un campo de estado
de capacidad que la IA monitoree y reporte durante
la conversación.

Ver: PROTOCOLO DE CIERRE DE CONVERSACIÓN (sección 3
de este documento).

--------------------------------------------------
2. REGLA DE SELECCIÓN
--------------------------------------------------

Para cada prompt debe aplicarse esta matriz.

MANDATORY

Documentos sin los cuales la tarea quedaría mal gobernada.

CONDITIONAL

Documentos que aplican solo si el escenario los activa.

REFERENTIAL

Documentos que ayudan a entender pero no deben imponer reglas.

EXCLUDED

Documentos que no deben cargarse porque no afectan la tarea
o introducirían ruido.

Esta clasificación es consistente con el enfoque usado en:

docs/operations/VALIDATE_MASTER_STRATEGY.md

No se está introduciendo un modelo nuevo sino formalizando
uno ya presente en el proyecto.

--------------------------------------------------
3. PROTOCOLO DE CIERRE DE CONVERSACIÓN
--------------------------------------------------

Una conversación activa puede terminar por límite de contexto,
decisión activa del usuario o completud de la tarea.

En todos los casos, el conocimiento generado no debe perderse.

INDICADOR DE ESTADO DE CAPACIDAD

El asistente debe reportar el estado de la conversación
al final de cada respuesta relevante con uno de estos
indicadores:

🟢 Chat manejable
🟡 Chat extenso, considera cerrar pronto
🔴 Chat crítico, cerrar antes de perder contexto

PROTOCOLO DE RESPALDO ANTES DE CERRAR

Cuando el indicador sea 🟡 o 🔴, ejecutar los siguientes
pasos antes de cerrar:

PASO 1 — RESUMEN DE DECISIONES

Solicitar al asistente el resumen de la sesión
usando el mensaje tipo definido abajo.

PASO 2 — ARCHIVOS MODIFICADOS

Confirmar que todos los archivos editados están guardados.

PASO 3 — ESTADO PENDIENTE

Identificar tareas incompletas y registrarlas en:

docs/project-management/PROJECT_STATE.md

PASO 4 — PUNTO DE REANUDACIÓN

El resumen generado en el PASO 1 se carga al iniciar
la siguiente sesión como contexto inicial junto con
el prompt operativo base.

MENSAJE TIPO PARA SOLICITAR RESPALDO

Copiar y enviar al asistente cuando se quiera cerrar
la conversación de forma controlada:

---
Vamos a cerrar esta conversación.
Resume en formato copiable:

1. Decisiones tomadas en esta sesión.
2. Archivos modificados y cambios clave.
3. Tareas pendientes.
4. Punto de reanudación recomendado para la siguiente sesión.
---

--------------------------------------------------
FIN DEL DOCUMENTO
