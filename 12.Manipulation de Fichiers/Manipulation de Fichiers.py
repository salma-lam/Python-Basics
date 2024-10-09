import pandas as pd
import json
import re

# 1. Manipulation de fichiers CSV
# Création d'un DataFrame et sauvegarde en CSV
data = {
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Âge': [25, 30, 35],
    'Ville': ['Paris', 'Londres', 'Berlin']
}
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)  # Écriture du DataFrame dans un fichier CSV

# Lecture du fichier CSV
df_loaded = pd.read_csv('data.csv')
print("Contenu du fichier CSV :")
print(df_loaded)

# 2. Manipulation de fichiers JSON
# Création d'un dictionnaire et sauvegarde en JSON
data_json = {
    'Nom': 'Alice',
    'Âge': 25,
    'Ville': 'Paris'
}
with open('data.json', 'w') as json_file:
    json.dump(data_json, json_file)  # Écriture du dictionnaire dans un fichier JSON

# Lecture du fichier JSON
with open('data.json', 'r') as json_file:
    json_loaded = json.load(json_file)
print("\nContenu du fichier JSON :")
print(json_loaded)

# 3. Manipulation de fichiers Excel
# Écriture du DataFrame dans un fichier Excel
df.to_excel('data.xlsx', index=False)  # Écriture du DataFrame dans un fichier Excel

# Lecture du fichier Excel
df_excel_loaded = pd.read_excel('data.xlsx')
print("\nContenu du fichier Excel :")
print(df_excel_loaded)

# 4. Utilisation des expressions régulières
# Création d'un fichier texte pour la démonstration
with open('sample.txt', 'w') as text_file:
    text_file.write("Alice 25\nBob 30\nCharlie 35\n")

# Lecture et traitement du fichier texte
with open('sample.txt', 'r') as text_file:
    content = text_file.read()
    print("\nContenu du fichier texte :")
    print(content)

# Utilisation des expressions régulières pour extraire les noms et âges
pattern = r'(\w+)\s(\d+)'  # Regex pour extraire le nom et l'âge
matches = re.findall(pattern, content)

print("\nNoms et âges extraits :")
for match in matches:
    print(f"Nom : {match[0]}, Âge : {match[1]}")
