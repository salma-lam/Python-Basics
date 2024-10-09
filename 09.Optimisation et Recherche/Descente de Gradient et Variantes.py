import numpy as np
import matplotlib.pyplot as plt

class GradientDescentOptimizer:
    def __init__(self, learning_rate=0.01, tolerance=1e-6, max_iterations=1000):
        """
        Initialise l'optimiseur de descente de gradient.
        
        :param learning_rate: Taux d'apprentissage pour la mise à jour des paramètres.
        :param tolerance: Critère d'arrêt basé sur la variation de la perte.
        :param max_iterations: Nombre maximal d'itérations.
        """
        self.learning_rate = learning_rate
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def optimize(self, loss_function, gradient_function, initial_params):
        """
        Applique l'algorithme de descente de gradient pour optimiser la fonction de perte.
        
        :param loss_function: Fonction de perte à minimiser.
        :param gradient_function: Fonction qui calcule le gradient de la fonction de perte.
        :param initial_params: Valeurs initiales des paramètres à optimiser.
        :return: Paramètres optimisés et l'historique des pertes.
        """
        params = np.array(initial_params, dtype=float)  # Convertir en float
        losses = []

        for iteration in range(self.max_iterations):
            loss = loss_function(params)
            losses.append(loss)

            # Calcul du gradient
            gradients = gradient_function(params)

            # Mise à jour des paramètres
            params -= self.learning_rate * gradients

            # Vérification de la convergence
            if iteration > 0 and abs(losses[-1] - losses[-2]) < self.tolerance:
                break

        return params, losses


# Exemple de fonction de perte : fonction quadratique
def loss_function(params):
    return np.sum((params - 3) ** 2)  # Vise à minimiser la distance à 3


# Exemple de fonction de gradient
def gradient_function(params):
    return 2 * (params - 3)  # Dérivée de la fonction quadratique


# Utilisation de la descente de gradient
initial_params = [0.0]  # Point de départ, converti en float
optimizer = GradientDescentOptimizer(learning_rate=0.1)

# Optimisation
optimized_params, loss_history = optimizer.optimize(loss_function, gradient_function, initial_params)

# Affichage des résultats
print(f"Paramètres optimisés : {optimized_params}")
print(f"Valeur de la fonction de perte finale : {loss_history[-1]}")

# Visualisation de l'historique de la perte
plt.plot(loss_history)
plt.title('Historique de la fonction de perte')
plt.xlabel('Itération')
plt.ylabel('Perte')
plt.yscale('log')  # Échelle logarithmique pour mieux visualiser la convergence
plt.show()
