import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Chargement des données
# Pour cet exemple, nous utilisons le jeu de données "iris" disponible dans Seaborn
iris = sns.load_dataset("iris")

# Aperçu des données
print("Aperçu des données Iris :")
print(iris.head())

# 2. Histogramme
# Histogramme pour visualiser la répartition de la longueur des sépales
plt.figure(figsize=(8, 6))
plt.hist(iris['sepal_length'], bins=20, color='blue', edgecolor='black')
plt.title('Répartition de la longueur des sépales', fontsize=16)
plt.xlabel('Longueur des sépales (cm)', fontsize=12)
plt.ylabel('Fréquence', fontsize=12)
plt.grid(True)
plt.show()

# 3. Graphique en nuage de points
# Scatter plot (nuage de points) entre la longueur et la largeur des sépales, coloré par espèce
plt.figure(figsize=(8, 6))
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette='Set1')
plt.title('Relation entre la longueur et la largeur des sépales', fontsize=16)
plt.xlabel('Longueur des sépales (cm)', fontsize=12)
plt.ylabel('Largeur des sépales (cm)', fontsize=12)
plt.legend(title='Espèces')
plt.show()

# 4. Carte thermique (Heatmap)
# Création d'une matrice de corrélation
correlation_matrix = iris.corr()

# Affichage de la carte thermique des corrélations
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matrice de corrélation des attributs de l\'iris', fontsize=16)
plt.show()
