import numpy as np
import scipy.integrate as spi
import scipy.optimize as opt
import scipy.linalg as la
import matplotlib.pyplot as plt

# 1. Résolution d'équations différentielles
# Définir une équation différentielle (dy/dt = -2y)
def equation_differentielle(y, t):
    return -2 * y

# Conditions initiales
y0 = 1  # valeur initiale de y
t = np.linspace(0, 5, 100)  # intervalle de temps

# Résoudre l'équation différentielle
solution = spi.odeint(equation_differentielle, y0, t)

# Affichage de la solution de l'équation différentielle
plt.figure(figsize=(10, 6))
plt.plot(t, solution, label='Solution de dy/dt = -2y', color='blue')
plt.title("Résolution d'équation différentielle")
plt.xlabel('Temps')
plt.ylabel('y(t)')
plt.legend()
plt.grid()
plt.show()

# 2. Optimisation
# Définir une fonction à minimiser
def fonction_a_minimiser(x):
    return (x - 2)**2 + 3  # Exemple : fonction quadratique

# Trouver le minimum de la fonction
resultat_optimisation = opt.minimize(fonction_a_minimiser, x0=0)  # point de départ
print(f"Minimum trouvé à x = {resultat_optimisation.x[0]:.4f}, valeur de la fonction au minimum : {resultat_optimisation.fun:.4f}")

# 3. Calcul d'intégrales
# Définir une fonction pour l'intégration
def fonction_a_integrer(x):
    return np.sin(x)  # Exemple : fonction sinus

# Calculer l'intégrale de sin(x) de 0 à π
integrale, erreur = spi.quad(fonction_a_integrer, 0, np.pi)
print(f"Intégrale de sin(x) de 0 à π : {integrale:.4f}, avec une erreur estimée : {erreur:.4e}")

# 4. Résolution de systèmes d'équations linéaires
# Définir une matrice et un vecteur
A = np.array([[3, 2], [1, 2]])  # Matrice des coefficients
b = np.array([5, 5])  # Vecteur des constantes

# Résoudre le système d'équations Ax = b
solution_systeme = la.solve(A, b)
print(f"Solution du système d'équations : x = {solution_systeme}")

# 5. Calcul de valeurs propres
# Définir une matrice
B = np.array([[4, -2], [1, 1]])

# Calculer les valeurs propres et les vecteurs propres
valeurs_propres, vecteurs_propres = la.eig(B)
print(f"Valeurs propres : {valeurs_propres}")
print(f"Vecteurs propres : \n{vecteurs_propres}")
