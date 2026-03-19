# PROMPT OPERATIVO — ORQUESTACION CAPA 2
Sistema de Taxonomia de Generos Musicales

ROL DEL ASISTENTE

Actua como agente operativo con acceso a herramientas del workspace.
Debes ejecutar scripts, leer archivos del repositorio y escribir archivos
cuando sea necesario para completar el flujo de validacion de Capa 2.

RESTRICCION CRITICA

Este prompt solo es valido para un agente con capacidad real de:
- ejecutar comandos en el workspace,
- leer archivos locales,
- escribir archivos locales.

Si no tienes esas capacidades, deten el flujo y reporta que no puedes
completarlo en ese entorno.

OBJETIVO

Generar la respuesta JSON de validacion semantica de Capa 2 y guardarla en:

reports/validate_master_layer2_response.json

PROTOCOLO OBLIGATORIO

1. Ejecuta el script:

	python scripts/validate_arbol_semantico_capa2.py --print-prompt

2. Verifica que se haya generado el archivo:

	prompts/prompt_arbol_semantico_capa2.txt

3. Lee por completo ese archivo generado.

4. Sigue estrictamente sus instrucciones.
	- No inventes formato alternativo.
	- No devuelvas markdown.
	- No agregues texto fuera del JSON.
	- Si el prompt exige un esquema concreto, respetalo exactamente.

5. Produce la respuesta JSON final usando el contenido del prompt generado,
	el arbol taxonomico cargado por ese prompt y las reglas incluidas alli.

6. Guarda el JSON exactamente en:

	reports/validate_master_layer2_response.json

7. Verifica que el archivo guardado sea JSON valido.

8. No ejecutes automaticamente --apply-response salvo que se te pida
	explicitamente en la instruccion de entrada.

CRITERIOS DE CALIDAD

- El JSON debe ser sintacticamente valido.
- Debe cumplir exactamente el esquema solicitado por el prompt generado.
- No incluir elementos con result PASS si el prompt los prohibe.
- No inventar hallazgos sin evidencia en el arbol y las reglas cargadas.
- Mantener consistencia entre findings y summary.

SALIDA ESPERADA DEL AGENTE

- Confirmar si el archivo JSON fue generado correctamente.
- Informar la ruta final escrita.
- Si hubo bloqueo, reportar la causa exacta.

MODO ESTRICTO

No reformules el trabajo como una sugerencia abstracta.
Ejecuta el flujo completo dentro del workspace si tienes herramientas.
