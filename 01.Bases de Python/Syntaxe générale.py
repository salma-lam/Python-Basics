# Variables de différents types
x = 10       # Type entier (int)
y = 3.14     # Type flottant (float)
z = "Python" # Type chaîne de caractères (str)

# Condition if, elif, else
if x > 5:
    print("x est supérieur à 5")
elif x == 5:
    print("x est égal à 5")
else:
    print("x est inférieur à 5")

# Boucle for (pour répéter une action un nombre de fois fixe)
for i in range(5):  # La boucle va de 0 à 4
    print(f"Valeur de i: {i}")  # Affiche la valeur de i à chaque itération

# Boucle while (répétition tant qu'une condition est vraie)
count = 0
while count < 3:
    print(f"Compte actuel: {count}")
    count += 1  # Incrémentation de count (on ajoute 1 à chaque itération)
