import numpy as np
import matplotlib.pyplot as plt

# 1. Définir la règle de l'automate cellulaire
def rule30(left, center, right):
    """Fonction qui applique la règle 30 pour un triplet de cellules."""
    return left ^ (center or right)  # XOR entre left et (OR de center et right)

# 2. Initialiser l'état de l'automate
def initialize_automaton(size):
    """Initialise l'automate avec une cellule centrale active."""
    automaton = np.zeros(size, dtype=int)
    automaton[size // 2] = 1  # Mettre une cellule active au centre
    return automaton

# 3. Simuler l'automate sur plusieurs générations
def simulate_automaton(generations):
    """Simule l'automate cellulaire sur un nombre donné de générations."""
    size = 2 * generations + 1  # Taille pour contenir toutes les générations
    grid = np.zeros((generations, size), dtype=int)
    
    # Initialiser la première génération
    current_state = initialize_automaton(size)
    grid[0] = current_state
    
    # Évoluer à travers les générations
    for i in range(1, generations):
        next_state = np.zeros(size, dtype=int)
        for j in range(1, size - 1):
            next_state[j] = rule30(current_state[j - 1], current_state[j], current_state[j + 1])
        grid[i] = next_state
        current_state = next_state  # Mettre à jour l'état actuel
    
    return grid

# 4. Visualiser l'automate cellulaire
def plot_automaton(grid):
    """Affiche le résultat de la simulation de l'automate cellulaire."""
    plt.imshow(grid, cmap='binary', interpolation='nearest')
    plt.title("Simulation d'un Automate Cellulaire (Règle 30)")
    plt.xlabel("Cellules")
    plt.ylabel("Générations")
    plt.show()

# 5. Paramètres de simulation
generations = 61  # Nombre de générations à simuler

# Exécuter la simulation
grid = simulate_automaton(generations)

# Afficher le résultat
plot_automaton(grid)
