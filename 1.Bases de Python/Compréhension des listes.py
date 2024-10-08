# Exemple 1: Créer une liste des carrés des nombres de 0 à 9
carres = [x**2 for x in range(10)]
print("Liste des carrés:", carres)

# Exemple 2: Filtrer une liste pour ne conserver que les nombres pairs
nombres_pairs = [x for x in range(10) if x % 2 == 0]
print("Liste des nombres pairs:", nombres_pairs)

# Exemple 3: Transformer les éléments d'une liste de chaînes de caractères en majuscules
mots = ["machine", "learning", "python", "intelligence"]
mots_majuscule = [mot.upper() for mot in mots]
print("Liste des mots en majuscule:", mots_majuscule)

# Exemple 4: Créer une liste à partir de deux listes en combinant les éléments
liste1 = [1, 2, 3]
liste2 = [10, 20, 30]
combinaison = [(x, y) for x in liste1 for y in liste2]
print("Liste des combinaisons:", combinaison)
