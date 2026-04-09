# Validacion Capa 2: lote club/pop 2026-04-08

## Fuentes usadas

- governance/01_auditar_arbol
- taxonomy/genre_tree_master.md
- taxonomy/genre_tree_node_criteria.json
- catalog/songs_with_genres.csv
- reports/canciones_nuevas_detalle.csv
- Metadatos reales de Qobuz consultados por API para casos dudosos

## Resultado

| Cancion | Artista | Nodo propuesto | Tipo | Puntuacion | Regla 15 | Observacion |
| --- | --- | --- | --- | ---: | --- | --- |
| Gypsy Woman (La Da Dee) | Crystal Waters | Music > Electronic > House | Existente | 96 | Encaje perfecto | House vocal clasico con pulso 4/4 dominante. |
| Confusion | New Order | Music > Electronic > House | Existente | 68 | Borderline (requiere revision) | La version Pump Panel Reconstruction Mix empuja hacia club 4/4 duro; el encaje ideal seria una rama Techno, pero por estabilidad se absorbe en House. |
| Get Get Down | Paul Johnson | Music > Electronic > House | Existente | 97 | Encaje perfecto | Caso canonico de house. |
| Sandstorm | Darude | Music > Electronic > House | Existente | 71 | Encaje fuerte (valido) | La identidad historica roza Trance, pero dentro del arbol actual el mejor ajuste operativo sigue siendo House por pulso 4/4 continuo y enfoque club no pop. |
| The Launch | DJ Jean | Music > Electronic > House | Existente | 84 | Encaje fuerte (valido) | Club track 4/4 de identidad house/hard house suficiente para el arbol actual. |
| Country Grammar (Hot Shit) | Nelly | Music > Hip Hop > Pop Rap | Existente | 86 | Encaje fuerte (valido) | Mantiene continuidad con otros Nelly ya clasificados en Pop Rap. |
| It Wasn't Me | Shaggy | Music > Hip Hop > Pop Rap | Existente | 72 | Encaje fuerte (valido) | El groove tensiona hacia reggae fusion, pero la estructura pop con entrega hablada-ritmica y hook prominente permite absorberlo operativamente en Pop Rap. |
| Magic Orgasm | Scorsi | Music > Electronic > House | Existente | 73 | Encaje fuerte (valido) | Sin genero explicito en Qobuz, pero el contexto del artista y sus remixes apunta mas a House que a otros nodos actuales. |

## Observaciones

- Este lote revela una posible futura necesidad de separar `Techno` y `Trance` dentro de `Music > Electronic` si siguen entrando mas casos de club 4/4 no-house.
- Por ahora no se abre nodo nuevo para evitar expansion prematura con evidencia todavia escasa.
