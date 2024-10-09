import pandas as pd
import numpy as np

# Chargement d'un jeu de données depuis un fichier CSV
# Pour cet exemple, nous allons créer un DataFrame fictif
data = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Âge': [25, 30, 35, np.nan, 28],
    'Salaire': [50000, 60000, np.nan, 70000, 45000],
    'Département': ['IT', 'HR', 'IT', 'Finance', 'HR']
}

df = pd.DataFrame(data)

# Afficher le DataFrame initial
print("DataFrame initial :")
print(df)

# Traitement des données manquantes
# Remplacer les valeurs manquantes dans la colonne 'Âge' par la moyenne des âges
df['Âge'].fillna(df['Âge'].mean(), inplace=True)

# Remplacer les valeurs manquantes dans la colonne 'Salaire' par la médiane des salaires
df['Salaire'].fillna(df['Salaire'].median(), inplace=True)

# Afficher le DataFrame après traitement des données manquantes
print("\nDataFrame après traitement des données manquantes :")
print(df)

# Filtrage des données : sélectionner les employés ayant un salaire supérieur à 50000
high_salary_df = df[df['Salaire'] > 50000]
print("\nEmployés avec un salaire supérieur à 50000 :")
print(high_salary_df)

# Tri des données : trier par 'Âge' de manière ascendante
sorted_df = df.sort_values(by='Âge', ascending=True)
print("\nDataFrame trié par Âge :")
print(sorted_df)

# Agrégation des données : calculer la moyenne des salaires par département
average_salary_by_department = df.groupby('Département')['Salaire'].mean().reset_index()
print("\nMoyenne des salaires par département :")
print(average_salary_by_department)

# Fusion de DataFrames : créer un nouveau DataFrame pour la fusion
new_data = {
    'Département': ['IT', 'HR', 'Finance'],
    'Localisation': ['New York', 'Los Angeles', 'Chicago']
}
new_df = pd.DataFrame(new_data)

# Fusionner les deux DataFrames sur la colonne 'Département'
merged_df = pd.merge(df, new_df, on='Département', how='inner')
print("\nDataFrame fusionné avec localisation :")
print(merged_df)
