import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Création d'un DataFrame fictif
np.random.seed(42)  # Pour la reproductibilité
data = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Âge': np.random.randint(20, 40, size=8),
    'Salaire': np.random.randint(40000, 80000, size=8),
    'Score': np.random.rand(8) * 100  # Score entre 0 et 100
}

df = pd.DataFrame(data)

# Afficher le DataFrame
print("DataFrame :")
print(df)

# 1. Statistiques descriptives
print("\nStatistiques descriptives :")
print(df.describe())

# 2. Corrélations
correlation = df.corr()
print("\nCorrélations :")
print(correlation)

# Visualisation de la matrice de corrélation
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Matrice de Corrélation')
plt.show()

# 3. Regroupement par département et calcul de la moyenne des salaires
# Pour cet exemple, ajoutons une colonne de département
df['Département'] = ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'HR']

average_salary_by_department = df.groupby('Département')['Salaire'].mean().reset_index()
print("\nMoyenne des salaires par département :")
print(average_salary_by_department)

# Visualisation de la moyenne des salaires par département
plt.figure(figsize=(8, 5))
sns.barplot(x='Département', y='Salaire', data=average_salary_by_department, palette='viridis')
plt.title('Moyenne des Salaires par Département')
plt.xlabel('Département')
plt.ylabel('Salaire Moyen')
plt.show()

# 4. Analyse de la distribution des salaires
plt.figure(figsize=(10, 5))
sns.histplot(df['Salaire'], bins=5, kde=True, color='blue', edgecolor='black')
plt.title('Distribution des Salaires')
plt.xlabel('Salaire')
plt.ylabel('Fréquence')
plt.grid(axis='y', alpha=0.75)
plt.show()

# 5. Box plot pour visualiser la distribution des âges
plt.figure(figsize=(10, 5))
sns.boxplot(x='Âge', data=df, color='lightgreen')
plt.title('Box Plot des Âges')
plt.xlabel('Âge')
plt.grid(axis='y', alpha=0.75)
plt.show()
