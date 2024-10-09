# Création d'une liste multidimensionnelle (tableau 2D)
tableau_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Fonction pour afficher le tableau 2D
def afficher_tableau(tableau):
    """
    Affiche les éléments d'un tableau 2D.
    """
    for ligne in tableau:
        print(ligne)

# Appel de la fonction pour afficher le tableau
print("Affichage du tableau 2D :")
afficher_tableau(tableau_2d)

# Accès aux éléments d'une liste multidimensionnelle
element = tableau_2d[1][2]  # Accéder à l'élément à la ligne 1, colonne 2 (6)
print(f"\nL'élément à la ligne 1 et colonne 2 est : {element}")

# Modification d'un élément dans le tableau
tableau_2d[0][0] = 10  # Change l'élément en haut à gauche de 1 à 10
print("\nTableau après modification :")
afficher_tableau(tableau_2d)

# Calcul de la somme de tous les éléments du tableau
def somme_tableau(tableau):
    """
    Calcule la somme de tous les éléments d'un tableau 2D.
    """
    total = 0
    for ligne in tableau:
        total += sum(ligne)  # Ajoute la somme de chaque ligne
    return total

# Appel de la fonction pour calculer la somme
total_somme = somme_tableau(tableau_2d)
print(f"\nLa somme de tous les éléments du tableau est : {total_somme}")

# Transposition du tableau 2D (inverser lignes et colonnes)
def transposer_tableau(tableau):
    """
    Transpose un tableau 2D (inverse les lignes et les colonnes).
    """
    return [list(ligne) for ligne in zip(*tableau)]  # Utilisation de zip pour transposer

# Appel de la fonction pour transposer le tableau
tableau_transpose = transposer_tableau(tableau_2d)
print("\nTableau transposé :")
afficher_tableau(tableau_transpose)
