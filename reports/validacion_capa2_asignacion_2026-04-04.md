# Validacion Capa 2 - Asignacion manual de canciones nuevas

Fecha: 2026-04-04

Fuente ejecutada:
- scripts/filtrar_canciones_nuevas.py

Resultado del lote real:
- 15 canciones nuevas detectadas
- No se propone ningun nodo nuevo en esta iteracion

## Asignaciones realizadas

| Title | Artist | ISRC | Nodo asignado | Confianza | Razon breve |
| --- | --- | --- | --- | --- | --- |
| Free To Decide | The Cranberries | USIR29600118 | Music > Rock > Alternative Rock | Alta | Mantiene identidad alternativa de banda y no encaja mejor en un subnodo mas especifico existente. |
| Dying In The Sun | The Cranberries | USIR29900013 | Music > Rock > Soft Rock | Media | Predomina el caracter suave y melodico, cercano a precedentes del artista ya ubicados en Soft Rock. |
| Delilah | The Cranberries | USIR29900011 | Music > Rock > Alternative Rock | Alta | Pulso de banda y perfil alternativo mas marcado que una logica de soft rock. |
| Just My Imagination | The Cranberries | USIR29900005 | Music > Rock > Alternative Rock | Media | Es mas ligera, pero conserva identidad alternativa de banda mas que una lectura clara de soft rock. |
| You And Me | The Cranberries | USIR29900004 | Music > Rock > Soft Rock | Media | Arreglo mas suave y enfasis melodico-vocal, alineado con la rama Soft Rock ya usada en el catalogo. |
| Loud And Clear | The Cranberries | USIR29900002 | Music > Rock > Alternative Rock | Alta | La identidad sigue siendo de rock alternativo de banda, no de balada suave. |
| Si Me Quisiste Tanto | Los Vallenatos De La Cumbia | MXUM72000776 | Music > Roots > Folk > Latin Folk > Vallenato | Media-Baja | Se prioriza la maxima especificidad disponible; el bloque converge con repertorio romantico vallenato y no hay evidencia interna suficiente para abrir nodo nuevo. |
| Mentiras | Los Vallenatos De La Cumbia | MXUM70904329 | Music > Roots > Folk > Latin Folk > Vallenato | Media-Baja | Mismo criterio del bloque; asignacion provisional dentro de rama existente. |
| A Las Tres | Los Vallenatos De La Cumbia | USDS19700402 | Music > Roots > Folk > Latin Folk > Vallenato | Media-Baja | Mismo criterio del bloque; asignacion provisional dentro de rama existente. |
| Cariño Mío | Los Vallenatos De La Cumbia | USDS10711738 | Music > Roots > Folk > Latin Folk > Vallenato | Media-Baja | Mismo criterio del bloque; asignacion provisional dentro de rama existente. |
| Ese Amor | Los Vallenatos De La Cumbia | USDS19700408 | Music > Roots > Folk > Latin Folk > Vallenato | Media-Baja | Mismo criterio del bloque; asignacion provisional dentro de rama existente. |
| Sal Y Agua | Los Vallenatos De La Cumbia | USDS19700400 | Music > Roots > Folk > Latin Folk > Vallenato | Media-Baja | Mismo criterio del bloque; asignacion provisional dentro de rama existente. |
| Muchacha Encantadora | Los Vallenatos De La Cumbia | MXUM70904334 | Music > Roots > Folk > Latin Folk > Vallenato | Media | Coincide con un titulo ya clasificado en el catalogo dentro de Vallenato, aunque la version debe entenderse como decision provisional hasta escucha puntual. |
| Macondo | Celso Piña y su Ronda Bogotá | MXF169900216 | Music > Roots > Cumbia | Alta | Precedente fuerte del mismo artista en el catalogo autoritativo, todos en la rama Cumbia. |
| Juntos | Emilio Navaira | USEL19200164 | Music > Roots > Regional Mexicano > Texano | Alta | Precedente consistente del mismo artista en Texano y criterios del nodo alineados con la discografia ya catalogada. |

## Observaciones

- El caso mas inestable del lote es Los Vallenatos De La Cumbia: no justifica todavia abrir una rama nueva y se resolvio con el nodo existente mas especifico disponible.
- Macondo tenia una tension en archivos derivados, pero songs_with_genres.csv y el precedente del artista favorecen claramente Cumbia.

## Refinacion posterior de la rama Cumbia

- Se abrio el subnodo `Music > Roots > Cumbia > Cumbia Vallenata` como expansion controlada minima.
- Se movieron los cinco temas de Celso Piña y su Ronda Bogotá a ese nuevo subnodo.
- Se mantuvo `Music > Roots > Cumbia` como fallback para cumbia sin subvariante mas especifica.
- Se preservo `Music > Roots > Cumbia > Cumbia Pop` para Kumbia Kings y derivados donde la estructura pop domina.