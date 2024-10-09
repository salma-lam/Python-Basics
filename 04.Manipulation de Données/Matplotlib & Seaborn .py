import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# 1. Histogramme des âges
plt.figure(figsize=(10, 5))
plt.hist(df['Âge'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogramme des âges')
plt.xlabel('Âge')
plt.ylabel('Fréquence')
plt.grid(axis='y', alpha=0.75)
plt.show()

# 2. Graphique en nuage de points (scatter plot)
plt.figure(figsize=(10, 5))
plt.scatter(df['Âge'], df['Salaire'], color='green', s=100, alpha=0.7)
plt.title('Nuage de points : Âge vs Salaire')
plt.xlabel('Âge')
plt.ylabel('Salaire')
plt.grid()
plt.show()

# 3. Carte thermique (heatmap) de corrélation
correlation = df.corr()  # Calcul des corrélations
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Carte thermique de corrélation')
plt.show()

# 4. Box plot pour visualiser la distribution des salaires
plt.figure(figsize=(10, 5))
sns.boxplot(x='Salaire', data=df, color='lightblue')
plt.title('Box Plot des Salaires')
plt.xlabel('Salaire')
plt.grid(axis='y', alpha=0.75)
plt.show()
