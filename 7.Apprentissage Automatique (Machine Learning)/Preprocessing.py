# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# 1. Création d'un DataFrame exemple
data = {
    'age': [25, 30, np.nan, 22, 28, 35, np.nan],
    'income': [50000, 60000, 70000, 80000, np.nan, 120000, 110000],
    'gender': ['male', 'female', 'female', np.nan, 'male', 'female', 'male'],
    'city': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', np.nan, 'Chicago']
}

df = pd.DataFrame(data)

print("Données originales :")
print(df)

# 2. Gestion des valeurs manquantes
# Remplacement des valeurs manquantes
imputer_age = SimpleImputer(strategy='mean')  # Imputer pour l'âge
imputer_income = SimpleImputer(strategy='mean')  # Imputer pour le revenu
imputer_gender = SimpleImputer(strategy='most_frequent')  # Imputer pour le genre
imputer_city = SimpleImputer(strategy='most_frequent')  # Imputer pour la ville

# Application de l'imputation
df['age'] = imputer_age.fit_transform(df[['age']])
df['income'] = imputer_income.fit_transform(df[['income']])
df['gender'] = imputer_gender.fit_transform(df[['gender']]).ravel()  # Flatten the array
df['city'] = imputer_city.fit_transform(df[['city']]).ravel()  # Flatten the array

print("\nDonnées après gestion des valeurs manquantes :")
print(df)

# 3. Normalisation des données
# Normalisation des colonnes numériques
scaler = StandardScaler()
df[['age', 'income']] = scaler.fit_transform(df[['age', 'income']])

print("\nDonnées après normalisation :")
print(df)

# 4. Encodage des catégories
# Encodage des colonnes catégorielles
encoder_gender = OneHotEncoder(sparse_output=False)  # Use sparse_output instead of sparse
encoded_gender = encoder_gender.fit_transform(df[['gender']])
df_encoded_gender = pd.DataFrame(encoded_gender, columns=encoder_gender.get_feature_names_out())

encoder_city = OneHotEncoder(sparse_output=False)  # Create a new encoder for city
encoded_city = encoder_city.fit_transform(df[['city']])
df_encoded_city = pd.DataFrame(encoded_city, columns=encoder_city.get_feature_names_out())

# Concaténation des DataFrames
df_final = pd.concat([df, df_encoded_gender, df_encoded_city], axis=1)
df_final = df_final.drop(['gender', 'city'], axis=1)  # Suppression des colonnes originales

print("\nDonnées finales après encodage :")
print(df_final)
