import numpy as np
import scipy.optimize as opt
import scipy.interpolate as interp
import matplotlib.pyplot as plt

# 1. Résolution d'équations
# Définir une fonction pour laquelle nous voulons trouver la racine
def f(x):
    return x**3 - 6*x**2 + 11*x - 6  # Exemple : f(x) = x^3 - 6x^2 + 11x - 6

# Trouver une racine de la fonction f
racine = opt.root_scalar(f, bracket=[0, 3])  # Cherche une racine entre 0 et 3
print(f"Racine trouvée : {racine.root:.4f}")

# 2. Optimisation
# Définir une fonction à minimiser
def g(x):
    return (x - 3)**2 + 1  # Exemple : g(x) = (x - 3)^2 + 1

# Trouver le minimum de la fonction g
resultat_optimisation = opt.minimize(g, x0=0)  # x0 est le point de départ
print(f"Minimum trouvé : {resultat_optimisation.x[0]:.4f}, valeur de g au minimum : {resultat_optimisation.fun:.4f}")

# 3. Interpolation
# Création de données d'exemple pour l'interpolation
x_donnees = np.array([0, 1, 2, 3, 4, 5])
y_donnees = np.array([1, 2, 0, 2, 3, 1])

# Créer une fonction d'interpolation
fonction_interpolante = interp.interp1d(x_donnees, y_donnees, kind='cubic')

# Générer des points pour l'interpolation
x_interpolation = np.linspace(0, 5, 100)
y_interpolation = fonction_interpolante(x_interpolation)

# Affichage des résultats d'interpolation
plt.figure(figsize=(10, 6))
plt.scatter(x_donnees, y_donnees, color='red', label='Données d\'exemple')
plt.plot(x_interpolation, y_interpolation, label='Interpolation cubique', color='blue')
plt.title('Interpolation des données')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
