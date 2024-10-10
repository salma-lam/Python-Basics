import numba
import numpy as np
import time

# Définition d'une fonction lente sans JIT
def slow_function(arr):
    result = 0
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            result += arr[i, j] ** 2
    return result

# Définition d'une fonction accélérée avec JIT via Numba
@numba.jit(nopython=True)  # Le mode "nopython" permet une meilleure optimisation
def fast_function(arr):
    result = 0
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            result += arr[i, j] ** 2
    return result

# Création d'un tableau aléatoire de grande taille
arr = np.random.rand(1000, 1000)

# Mesure du temps d'exécution de la fonction lente
start_time = time.time()
slow_result = slow_function(arr)
print(f"Résultat avec fonction lente: {slow_result}")
print(f"Temps d'exécution (sans JIT) : {time.time() - start_time} secondes")

# Mesure du temps d'exécution de la fonction rapide (JIT)
start_time = time.time()
fast_result = fast_function(arr)
print(f"Résultat avec fonction rapide: {fast_result}")
print(f"Temps d'exécution (avec JIT) : {time.time() - start_time} secondes")
