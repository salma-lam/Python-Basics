# Création d'un tuple
mon_tuple = (10, 20, 30, 40)

# 1. Accéder aux éléments d'un tuple (indexation)
premier_element = mon_tuple[0]  # Premier élément du tuple
dernier_element = mon_tuple[-1]  # Dernier élément du tuple
print("Premier élément:", premier_element)
print("Dernier élément:", dernier_element)

# 2. Longueur du tuple
# Utilisation de len() pour obtenir le nombre d'éléments dans le tuple
taille_tuple = len(mon_tuple)
print("Taille du tuple:", taille_tuple)

# 3. Indexation et slicing
# Comme avec les listes, on peut utiliser le slicing pour obtenir une partie du tuple
sous_tuple = mon_tuple[1:3]  # Éléments de l'index 1 à 2 (l'élément à l'index 3 est exclu)
print("Sous-tuple:", sous_tuple)

# 4. Tentative de modification (provoquera une erreur)
# mon_tuple[1] = 25  # Cela provoquera une erreur car les tuples sont immuables
