import sympy as sp

# 1. Définir des symboles
x = sp.symbols('x')  # Définir une variable symbolique x

# 2. Algèbre
# Définir une expression algébrique
expression = 2*x**2 + 3*x + 1
print("Expression algébrique :", expression)

# Simplifier l'expression
expression_simplifiee = sp.simplify(expression)
print("Expression simplifiée :", expression_simplifiee)

# Factoriser l'expression
expression_factoree = sp.factor(expression)
print("Expression factorisée :", expression_factoree)

# Développer l'expression
expression_developpee = sp.expand(expression_factoree)
print("Expression développée :", expression_developpee)

# 3. Dérivées
# Calculer la dérivée de l'expression par rapport à x
derivative = sp.diff(expression, x)
print("Dérivée de l'expression par rapport à x :", derivative)

# 4. Intégrales
# Calculer l'intégrale de l'expression par rapport à x
integrale = sp.integrate(expression, x)
print("Intégrale de l'expression par rapport à x :", integrale)

# 5. Résolution d'équations
# Résoudre une équation
equation = sp.Eq(expression, 0)  # Équation : 2x^2 + 3x + 1 = 0
solutions = sp.solve(equation, x)
print("Solutions de l'équation :", solutions)

# 6. Limites
# Calculer la limite de l'expression lorsque x approche 0
limite = sp.limit(expression, x, 0)
print("Limite de l'expression lorsque x approche 0 :", limite)

# 7. Séries de Taylor
# Calculer la série de Taylor de l'expression autour de x=0
serie_taylor = sp.series(expression, x, 0, 3)  # Expansion jusqu'à l'ordre 3
print("Série de Taylor de l'expression autour de x=0 :", serie_taylor)
