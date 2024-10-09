# Importation de la bibliothèque PuLP
from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value

# Création du problème d'optimisation
problem = LpProblem("Maximisation_de_Profit", LpMaximize)

# Définition des variables de décision
x1 = LpVariable("x1", lowBound=0)  # Variable x1, doit être >= 0
x2 = LpVariable("x2", lowBound=0)  # Variable x2, doit être >= 0

# Définition de la fonction objective (maximiser le profit)
# Par exemple, maximiser 3*x1 + 2*x2
problem += 3 * x1 + 2 * x2, "Profit"

# Définition des contraintes
# Contrainte 1 : x1 + 2*x2 <= 6
problem += x1 + 2 * x2 <= 6, "Contrainte_1"

# Contrainte 2 : 4*x1 + 2*x2 <= 12
problem += 4 * x1 + 2 * x2 <= 12, "Contrainte_2"

# Contrainte 3 : x1 + x2 <= 4
problem += x1 + x2 <= 4, "Contrainte_3"

# Résolution du problème
problem.solve()

# Affichage des résultats
print("Statut de la solution :", LpStatus[problem.status])
print(f"Valeur optimale de x1 : {value(x1)}")
print(f"Valeur optimale de x2 : {value(x2)}")
print(f"Valeur maximale du profit : {value(problem.objective)}")
