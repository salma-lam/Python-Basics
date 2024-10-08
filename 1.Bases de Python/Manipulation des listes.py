# Création d'une liste
ma_liste = [10, 20, 30, 40, 50]

# 1. Accéder aux éléments d'une liste (indexation)
# Comme les chaînes de caractères, les listes commencent à l'index 0
premier_element = ma_liste[0]  # Premier élément
dernier_element = ma_liste[-1]  # Dernier élément
print("Premier élément:", premier_element)
print("Dernier élément:", dernier_element)

# 2. Modifier un élément dans une liste
# On peut directement remplacer un élément en spécifiant l'index
ma_liste[1] = 25  # Remplacer le deuxième élément (index 1) par 25
print("Liste après modification:", ma_liste)

# 3. Ajouter des éléments à une liste
# Utilisation de append() pour ajouter un élément à la fin
ma_liste.append(60)
print("Liste après ajout:", ma_liste)

# 4. Insérer un élément à une position spécifique
# Utilisation de insert() pour ajouter à une position spécifique (ici à l'index 2)
ma_liste.insert(2, 35)
print("Liste après insertion:", ma_liste)

# 5. Supprimer un élément d'une liste
# Utilisation de remove() pour supprimer la première occurrence d'une valeur
ma_liste.remove(25)  # Supprime le nombre 25 de la liste
print("Liste après suppression:", ma_liste)

# 6. Longueur de la liste
# Utilisation de len() pour obtenir le nombre total d'éléments dans la liste
taille = len(ma_liste)
print("Taille de la liste:", taille)

# 7. Trier une liste
ma_liste.sort()  # Trie la liste par ordre croissant
print("Liste triée:", ma_liste)

# 8. Liste inversée
ma_liste.reverse()  # Inverse l'ordre des éléments
print("Liste inversée:", ma_liste)

# 9. Boucle à travers une liste
# Utilisation d'une boucle for pour parcourir et afficher chaque élément de la liste
for element in ma_liste:
    print("Élément:", element)
