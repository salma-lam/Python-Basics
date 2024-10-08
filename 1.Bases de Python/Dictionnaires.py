# Création d'un dictionnaire
mon_dictionnaire = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# 1. Accéder à une valeur via sa clé
nom = mon_dictionnaire["nom"]  # Accéder à la valeur associée à la clé "nom"
age = mon_dictionnaire.get("age")  # Une autre façon d'accéder à une valeur
print("Nom:", nom)
print("Âge:", age)

# 2. Ajouter ou modifier une paire clé-valeur
# Si la clé existe, la valeur est mise à jour, sinon elle est ajoutée
mon_dictionnaire["age"] = 26  # Met à jour l'âge
mon_dictionnaire["profession"] = "Ingénieur"  # Ajoute une nouvelle paire clé-valeur
print("Dictionnaire après modification:", mon_dictionnaire)

# 3. Supprimer une paire clé-valeur
del mon_dictionnaire["ville"]  # Supprime l'entrée pour la clé "ville"
print("Dictionnaire après suppression:", mon_dictionnaire)

# 4. Vérifier la présence d'une clé
presence_cle = "nom" in mon_dictionnaire  # Vérifie si "nom" est une clé dans le dictionnaire
print("Clé 'nom' présente:", presence_cle)

# 5. Boucler à travers un dictionnaire
# Boucle sur les clés
for cle in mon_dictionnaire:
    print("Clé:", cle, "-> Valeur:", mon_dictionnaire[cle])

# Boucle sur les paires clé-valeur
for cle, valeur in mon_dictionnaire.items():
    print(f"{cle} : {valeur}")

# 6. Obtenir seulement les clés ou les valeurs
cles = mon_dictionnaire.keys()  # Retourne les clés du dictionnaire
valeurs = mon_dictionnaire.values()  # Retourne les valeurs du dictionnaire
print("Clés:", cles)
print("Valeurs:", valeurs)
