
import csv
import os

# Rutas absolutas basadas en la ubicación de este script
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
file_canciones_con_genero = os.path.join(BASE_DIR, 'catalog', 'cancionesConGenero.csv')
file_list_qobuz = os.path.join(BASE_DIR, 'catalog', 'list_qobuz.csv')
file_output = os.path.join(BASE_DIR, 'catalog', 'cancionesConGeneroDiff.csv')

# Leer ISRCs de list_qobuz.csv
isrcs_qobuz = set()
with open(file_list_qobuz, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        isrcs_qobuz.add(row['isrc'].strip())


# Filtrar canciones de cancionesConGenero.csv que no están en list_qobuz.csv, aplicando strip a todos los campos relevantes
rows_diff = []
with open(file_canciones_con_genero, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    for row in reader:
        # Limpiar espacios en todos los campos
        row_clean = {k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
        if row_clean['isrc'] not in isrcs_qobuz:
            rows_diff.append(row_clean)

# Escribir resultado
with open(file_output, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerows(rows_diff)

print(f"Canciones exportadas: {len(rows_diff)}")
