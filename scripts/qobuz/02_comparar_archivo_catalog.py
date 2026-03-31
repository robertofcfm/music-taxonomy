
import csv
import os
import unicodedata

# Rutas de los archivos
file1 = os.path.join("catalog", "favorites_qobuz.csv")
file2 = os.path.join("catalog", "songs_raw.csv")



def normalize_text(text):
    text = text.strip().lower()
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    # Normalizar comillas dobles y escapadas
    text = text.replace('\\"', '"')  # \" -> "
    text = text.replace('""', '"')   # "" -> "
    text = text.replace('“', '"').replace('”', '"')
    # Quitar comillas dobles al inicio y final
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    # Quitar comillas dobles sueltas al final de la cadena
    text = text.rstrip('"')
    # Quitar comillas dobles sueltas antes de paréntesis de cierre
    import re
    text = re.sub(r'\)"$', ')', text)
    # Quitar espacios extra dentro de paréntesis
    import re
    text = re.sub(r'\(\s+', '(', text)
    text = re.sub(r'\s+\)', ')', text)
    # Quitar comillas dobles sueltas dentro de paréntesis
    text = re.sub(r'\((.*?)\)', lambda m: '(' + m.group(1).replace('"', '') + ')', text)
    # Quitar comillas dobles sueltas al final de palabras
    text = re.sub(r'"([\s\)])', r'\1', text)
    text = text.replace('\\', '')  # Quitar barras invertidas sobrantes
    return text

def load_title_artist_set(filepath):
    result = set()
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = normalize_text(row.get("title", ""))
            artist = normalize_text(row.get("artist", ""))
            if title and artist:
                result.add((title, artist))
    return result

def main():

    set1 = load_title_artist_set(file1)
    set2 = load_title_artist_set(file2)

    # Comparación adicional con songs_with_genres.csv
    file4 = os.path.join("catalog", "songs_with_genres.csv")
    set4 = load_title_artist_set(file4)

    only_in_1_4 = set1 - set4
    only_in_4_1 = set4 - set1

    print("\nComparando favorites_qobuz.csv vs songs_with_genres.csv:")
    if not only_in_1_4 and not only_in_4_1:
        print("Los archivos están correctamente sincronizados.")
    else:
        if only_in_1_4:
            print("En favorites_qobuz.csv pero NO en songs_with_genres.csv:")
            for t, a in sorted(only_in_1_4):
                print(f"  - {t} | {a}")
        if only_in_4_1:
            print("En songs_with_genres.csv pero NO en favorites_qobuz.csv:")
            for t, a in sorted(only_in_4_1):
                print(f"  - {t} | {a}")

    only_in_1 = set1 - set2
    only_in_2 = set2 - set1

    print("\nComparando favorites_qobuz.csv vs songs_raw.csv:")
    if not only_in_1 and not only_in_2:
        print("Los archivos están correctamente sincronizados.")
    else:
        if only_in_1:
            print("En favorites_qobuz.csv pero NO en songs_raw.csv:")
            for t, a in sorted(only_in_1):
                print(f"  - {t} | {a}")
        if only_in_2:
            print("En songs_raw.csv pero NO en favorites_qobuz.csv:")
            for t, a in sorted(only_in_2):
                print(f"  - {t} | {a}")

    # Comparación adicional con cancionesConGenero.csv
    file3 = os.path.join("catalog", "cancionesConGenero.csv")
    set3 = load_title_artist_set(file3)

    only_in_1_3 = set1 - set3
    only_in_3_1 = set3 - set1

    print("\nComparando favorites_qobuz.csv vs cancionesConGenero.csv:")
    if not only_in_1_3 and not only_in_3_1:
        print("Los archivos están correctamente sincronizados.")
    else:
        if only_in_1_3:
            print("En favorites_qobuz.csv pero NO en cancionesConGenero.csv:")
            for t, a in sorted(only_in_1_3):
                print(f"  - {t} | {a}")
        if only_in_3_1:
            print("En cancionesConGenero.csv pero NO en favorites_qobuz.csv:")
            for t, a in sorted(only_in_3_1):
                print(f"  - {t} | {a}")

if __name__ == "__main__":
    main()
