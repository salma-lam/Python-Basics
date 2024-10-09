import numpy as np

# 1. Création de matrices
# Création d'une matrice 2x2
A = np.array([[1, 2],
              [3, 4]])

# Création d'une matrice 2x2
B = np.array([[5, 6],
              [7, 8]])

# Affichage des matrices
print("Matrice A :")
print(A)
print("\nMatrice B :")
print(B)

# 2. Addition et soustraction de matrices
C = A + B  # Addition
D = A - B  # Soustraction

print("\nAddition de A et B (C) :")
print(C)
print("\nSoustraction de A et B (D) :")
print(D)

# 3. Produit matriciel
E = np.dot(A, B)  # Produit matriciel
print("\nProduit matriciel de A et B (E) :")
print(E)

# 4. Transposition de matrice
A_transpose = A.T
print("\nTransposée de A :")
print(A_transpose)

# 5. Inversion de matrice
# Pour inverser une matrice, elle doit être carrée et non singulière
try:
    A_inverse = np.linalg.inv(A)
    print("\nInverse de A :")
    print(A_inverse)
except np.linalg.LinAlgError:
    print("\nLa matrice A ne peut pas être inversée.")

# 6. Calcul des valeurs propres et vecteurs propres
valeurs_propres, vecteurs_propres = np.linalg.eig(A)
print("\nValeurs propres de A :")
print(valeurs_propres)
print("\nVecteurs propres de A :")
print(vecteurs_propres)

# 7. Résolution de systèmes d'équations linéaires
# Résoudre le système : Ax = b
b = np.array([1, 2])  # Vecteur de constantes
x = np.linalg.solve(A, b)  # Résoudre Ax = b

print("\nSolution du système Ax = b :")
print(x)

# 8. Calcul de la norme d'un vecteur
v = np.array([3, 4])
norme_v = np.linalg.norm(v)  # Calcul de la norme
print("\nNorme du vecteur v :")
print(norme_v)

# 9. Produit scalaire entre deux vecteurs
u = np.array([1, 2])
v = np.array([3, 4])
produit_scalaire = np.dot(u, v)  # Produit scalaire
print("\nProduit scalaire de u et v :")
print(produit_scalaire)
