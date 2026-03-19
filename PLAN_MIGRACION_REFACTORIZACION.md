# Plan de Migración y Refactorización

Este documento establece el plan de acción para migrar y reorganizar scripts y prompts, asegurando trazabilidad y control en cada paso.

## Objetivo
- Migrar todos los scripts y prompts a una estructura modular, separando los archivos ya refactorizados de los pendientes.
- Garantizar que cada archivo solo cargue el contexto y reglas estrictamente necesarios.
- Mantener trazabilidad de avance y decisiones.

## Pasos del plan

- [ ] 1. Crear carpetas `bk/` en `scripts/` y `prompts/` para archivos pendientes de migrar.
- [ ] 2. Listar todos los scripts y prompts actuales, identificando cuáles deben ir a `bk/`.
- [ ] 3. Definir y documentar el criterio de migración (qué va a `bk/` y qué queda activo).
- [ ] 4. Crear/actualizar un índice en `scripts/README.md` y `prompts/README.md` con el estado de cada archivo.
- [ ] 5. Migrar archivos a `bk/` según el criterio definido.
- [ ] 6. Refactorizar archivos uno por uno, moviéndolos de `bk/` a la ubicación principal y actualizando el índice.
- [ ] 7. Eliminar archivos de `bk/` solo cuando se confirme que ya no son necesarios.

## Condiciones y criterios
- No mover ni eliminar código sin antes documentar el cambio aquí.
- Cada archivo migrado debe cumplir con la carga mínima de contexto y reglas.
- El avance debe palomearse en este documento.

## Observaciones

## Estructura Detallada de Archivos y Funciones

### 1. scripts/
	- Contendrá solo scripts activos y refactorizados.
	- Cada script debe:
		- Cargar únicamente el contexto y reglas necesarios para su función.
		- Documentar en cabecera qué archivos de contexto/reglas utiliza y por qué.
		- Ser modular: una función por archivo o agrupados por dominio funcional.

### 2. scripts/bk/
	- Scripts pendientes de migrar/refactorizar.
	- No deben usarse en producción hasta ser revisados.

### 3. prompts/
	- Solo prompts activos y refactorizados.
	- Cada prompt debe:
		- Puede referenciar rutas internas del repositorio para reglas y contexto, aprovechando sincronización y actualización dinámica.
		- Documentar en cabecera el contexto/reglas que requiere.
		- Incluir la instrucción de reporte de estado (🟢/🟡/🔴).

### 4. prompts/bk/
	- Prompts pendientes de migrar/refactorizar.
	- No deben usarse hasta ser revisados.

### 5. governance/ y context/
	- Archivos de reglas y contexto deben estar divididos por dominio o tarea.
	- Ejemplo:
		- governance/reglas_validacion_arbol_script.md
		- governance/reglas_validacion_arbol_llm.md
		- context/contexto_validacion_arbol_script.md
		- context/contexto_validacion_arbol_llm.md
	- Si una regla/contexto es transversal, ubicarla en un archivo global temático y documentar alcance.

### 6. Índices y trazabilidad
	- scripts/README.md y prompts/README.md deben listar:
		- Archivos activos (refactorizados)
		- Archivos en bk/ (pendientes)
		- Estado de migración y fecha de último cambio

### 7. Orquestadores
	- Si una tarea es mixta (script + LLM), crear un orquestador que combine ambos flujos y documente el proceso.

### 8. Contexto para continuidad de sesión
	- Este plan debe actualizarse en cada iteración.
	- Documentar aquí cualquier decisión, cambio de criterio o ajuste de estructura.
	- Si se interrumpe la sesión, al reanudar se debe revisar este archivo antes de continuar.

🟢 Chat manejable
## Orden de migración de tareas

1. Validación del árbol (estructura, reglas y prompts asociados)
2. (En cola) Migrar y refactorizar el resto de tareas una por una, siguiendo el mismo proceso:
	- Clasificación de canciones
	- Generación de árbol
	- Otros procesos o validaciones
