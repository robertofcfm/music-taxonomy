# IMPORTANTE: El match de género lo realizas tu como el agente LLM (modelo de lenguaje), siguiendo el protocolo standalone y evaluando cada canción según los criterios de pertenencia, exclusión y coherencia musical definidos en la taxonomía.
# El usuario no debe realizar el match manualmente. No se permite automatizar el match mediante lógica de script, heurísticas ni inferencias automáticas fuera del razonamiento del LLM.
# Cada asignación debe justificarse explícitamente y cumplir la regla de convivencia homogénea dentro del nodo hoja.
# Script para clasificación de canciones según protocolo standalone
# Regla de sugerencia de género faltante:
# Si una canción no puede ser clasificada en un nodo hoja existente, se sugiere un género faltante SOLO si:
#   - El nodo sugerido permitiría que la canción conviva exclusivamente con otras de características musicales, instrumentales y de contexto muy similares.
#   - Se evita toda heterogeneidad o disonancia estilística dentro del nodo.
#   - No se permite sugerir nodos padres amplios ni géneros que agrupen canciones diversas.
#   - La justificación debe incluir por qué el nodo propuesto garantiza coherencia musical.

# Ejemplo de sugerencias para los 5 casos GENRE_MISSING:
# 1. "I'm Not In Love" – 10cc
#    Género sugerido: Soft Rock (nodo hoja propuesto)
#    Justificación: Soft Rock agrupa canciones de producción sofisticada, tempo medio, énfasis en melodía y armonía vocal, evitando mezclar con balada pop, hard rock o géneros alternativos. Todas las canciones en este nodo comparten rasgos musicales y de contexto homogéneos, garantizando coherencia musical.
#
# 2. "Dancing Queen" – ABBA
#    Género sugerido: Disco (nodo hoja propuesto)
#    Justificación: Disco agrupa canciones con ritmo bailable, arreglos orquestales, base rítmica constante y producción pulida, evitando mezclar con pop, rock o electrónica pura. El nodo mantiene homogeneidad estilística.
#
# 3. "The Winner Takes It All" – ABBA
#    Género sugerido: Pop Balada (nodo hoja propuesto)
#    Justificación: Pop Balada agrupa canciones de estructura pop con enfoque en melodía, armonía vocal y temática sentimental, evitando mezclar con rock, disco o géneros alternativos. Nodo homogéneo en estilo y contexto.
#
# 4. "Back In Black" – AC/DC
#    Género sugerido: Hard Rock (nodo hoja propuesto)
#    Justificación: Hard Rock agrupa canciones con guitarras eléctricas prominentes, riffs potentes, ritmo enérgico y actitud rockera, evitando mezclar con grunge, art rock o rock alternativo. Nodo estilísticamente coherente.
#
# 5. "Llegaste Tú" – Adriana Lucia
#    Género sugerido: Pop Latino (nodo hoja propuesto)
#    Justificación: Pop Latino agrupa canciones de producción contemporánea, melodía accesible y raíces latinas, evitando mezclar con cumbia, norteño o balada anglo. Nodo homogéneo en contexto y estilo.