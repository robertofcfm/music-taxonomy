
import csv
import os
import unicodedata

# Rutas de los archivos
file1 = os.path.join("catalog", "favorites_qobuz.csv")




def normalize_text(text):
    import re
    text = str(text)
    text = text.strip().lower()
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    # Elimina cualquier tipo de comillas (simples, dobles, dobles dobles, escapadas) y barras invertidas
    text = re.sub(r'["\'\u201c\u201d\u2018\u2019\\]', '', text)
    # Reemplaza múltiples espacios internos por uno solo
    text = re.sub(r'\s+', ' ', text)
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
