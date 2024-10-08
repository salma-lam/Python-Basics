# Déclaration d'une chaîne de caractères
texte = "Hello, AI and Machine Learning!"

# 1. Accéder à des caractères individuels (indexation)
# Les chaînes sont comme des tableaux où chaque caractère a une position
premier_caractere = texte[0]  # Accède au premier caractère (index 0)
dernier_caractere = texte[-1]  # Accède au dernier caractère (index -1 pour accéder à partir de la fin)

print("Premier caractère:", premier_caractere)
print("Dernier caractère:", dernier_caractere)

# 2. Slicing (sous-chaînes)
# Obtenir une partie de la chaîne avec [début:fin] (fin non incluse)
sous_chaine = texte[7:9]  # Caractères de position 7 à 8 (le caractère à l'index 9 est exclu)
print("Sous-chaîne:", sous_chaine)

# 3. Longueur de la chaîne
longueur = len(texte)  # Utiliser la fonction len() pour connaître la longueur de la chaîne
print("Longueur de la chaîne:", longueur)

# 4. Conversion en majuscules et minuscules
majuscule = texte.upper()  # Convertir toute la chaîne en majuscules
minuscule = texte.lower()  # Convertir toute la chaîne en minuscules
print("Majuscules:", majuscule)
print("Minuscules:", minuscule)

# 5. Remplacement de sous-chaînes
# Remplacer une partie de la chaîne par une autre
remplacement = texte.replace("AI", "Artificial Intelligence")  # Remplace "AI" par "Artificial Intelligence"
print("Remplacement:", remplacement)

# 6. Vérifier la présence d'une sous-chaîne
# Utiliser l'opérateur "in" pour vérifier si une sous-chaîne est présente
presence = "Machine" in texte  # Retourne True si "Machine" est dans la chaîne
print("Présence de 'Machine' dans la chaîne:", presence)

# 7. Diviser une chaîne (split)
# Diviser une chaîne en une liste de sous-chaînes basées sur un délimiteur
mots = texte.split(" ")  # Divise la chaîne en mots (séparateur = espace)
print("Liste des mots:", mots)

# 8. Concaténation de chaînes
# Ajouter des chaînes ensemble
texte_concatene = texte + " Let's dive deeper!"
print("Chaîne concaténée:", texte_concatene)

# 9. Supprimer les espaces au début et à la fin (strip)
texte_avec_espaces = "    Hello, AI!    "
texte_sans_espaces = texte_avec_espaces.strip()  # Enlève les espaces en début et fin
print("Chaîne sans espaces:", texte_sans_espaces)
