import numpy as np

# Création d'un tableau NumPy unidimensionnel
array_1d = np.array([1, 2, 3, 4, 5])
print("Tableau 1D :")
print(array_1d)

# Création d'un tableau NumPy bidimensionnel (matrice)
matrix_2d = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
print("\nMatrice 2D :")
print(matrix_2d)

# Opérations de base sur les matrices
# Accès à un élément spécifique (ligne 1, colonne 2)
element = matrix_2d[1, 2]  # Accède à l'élément 6
print(f"\nÉlément à la ligne 1, colonne 2 : {element}")

# Slicing : récupérer une sous-matrice
sous_matrice = matrix_2d[0:2, 1:3]  # Récupère les 2 premières lignes et colonnes 1 et 2
print("\nSous-matrice :")
print(sous_matrice)

# Broadcasting : additionner un tableau à une matrice
array_to_add = np.array([10, 20, 30])  # Tableau 1D
result_broadcasting = matrix_2d + array_to_add  # Broadcasting de array_to_add sur matrix_2d
print("\nRésultat du broadcasting (ajout) :")
print(result_broadcasting)

# Opérations mathématiques sur les matrices
# Produit matriciel
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
produit_mat = np.dot(matrix_a, matrix_b)  # Produit matriciel
print("\nProduit matriciel de A et B :")
print(produit_mat)

# Inversion d'une matrice
# Pour inverser une matrice, elle doit être carrée et de rang complet
inversion_matrix = np.array([[1, 2], [3, 4]])
matrix_inverse = np.linalg.inv(inversion_matrix)  # Inversion de la matrice
print("\nMatrice inversée :")
print(matrix_inverse)

# Indexation avancée : récupérer des éléments spécifiques
indexation_avancee = matrix_2d[[0, 1, 2], [0, 1, 2]]  # Récupère les éléments diagonaux
print("\nIndexation avancée (éléments diagonaux) :")
print(indexation_avancee)
