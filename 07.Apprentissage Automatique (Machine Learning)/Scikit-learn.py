# Importation des bibliothèques nécessaires
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, make_regression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix
from sklearn.cluster import KMeans

# 1. Chargement des jeux de données
# Exemple de classification avec le jeu de données Iris
iris = load_iris()
X_classification = iris.data  # Caractéristiques
y_classification = iris.target  # Labels

# Exemple de régression avec des données générées
X_regression, y_regression = make_regression(n_samples=100, n_features=1, noise=10)

# 2. Séparation des données
# Pour la classification
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(
    X_classification, y_classification, test_size=0.2, random_state=42)

# Pour la régression
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_regression, y_regression, test_size=0.2, random_state=42)

# 3. Modélisation

# a. Régression linéaire
linear_model = LinearRegression()
linear_model.fit(X_train_reg, y_train_reg)

# Prédictions et évaluation
y_pred_reg = linear_model.predict(X_test_reg)
mse = mean_squared_error(y_test_reg, y_pred_reg)
print("MSE de la régression linéaire :", mse)

# b. Classification avec régression logistique
logistic_model = LogisticRegression(max_iter=200)
logistic_model.fit(X_train_class, y_train_class)

# Prédictions et évaluation
y_pred_class = logistic_model.predict(X_test_class)
accuracy = accuracy_score(y_test_class, y_pred_class)
conf_matrix = confusion_matrix(y_test_class, y_pred_class)

print("Précision de la classification :", accuracy)
print("Matrice de confusion :\n", conf_matrix)

# 4. Validation croisée
cv_scores = cross_val_score(logistic_model, X_classification, y_classification, cv=5)
print("Scores de validation croisée :", cv_scores)

# 5. Clustering avec K-Means
kmeans = KMeans(n_clusters=3)
kmeans.fit(X_classification)
labels = kmeans.labels_

# Visualisation des clusters
plt.figure(figsize=(10, 6))
plt.scatter(X_classification[:, 0], X_classification[:, 1], c=labels, cmap='viridis')
plt.title("Clusters K-Means sur les données Iris")
plt.xlabel("Longueur du sépale")
plt.ylabel("Largeur du sépale")
plt.show()
