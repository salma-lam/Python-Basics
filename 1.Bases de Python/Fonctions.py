# Fonction qui salue un utilisateur avec un argument ayant une valeur par défaut
def saluer_utilisateur(nom="utilisateur"):
    """
    Cette fonction salue l'utilisateur.
    Si aucun nom n'est fourni, elle utilise 'utilisateur' par défaut.
    """
    print(f"Bonjour, {nom} !")

# Appel de la fonction avec et sans argument
saluer_utilisateur()         # Utilise la valeur par défaut "utilisateur"
saluer_utilisateur("Alice")  # Utilise "Alice" comme argument

# Fonction avec plusieurs arguments, retour de plusieurs valeurs
def calculer_operations(a, b):
    """
    Cette fonction prend deux nombres et retourne leur somme et leur produit.
    """
    somme = a + b
    produit = a * b
    return somme, produit  # Retourne un tuple contenant la somme et le produit

# Appel de la fonction et récupération des valeurs retournées
somme, produit = calculer_operations(5, 3)
print("Somme:", somme)      # Affiche la somme des deux nombres
print("Produit:", produit)  # Affiche le produit des deux nombres
