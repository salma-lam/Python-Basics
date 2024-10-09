# Implémentation d'une pile (Stack) avec une liste
class Pile:
    def __init__(self):
        """Initialise une nouvelle pile vide."""
        self.elements = []

    def empiler(self, element):
        """Ajoute un élément à la pile."""
        self.elements.append(element)
        print(f"Empilé : {element}")

    def depiler(self):
        """Supprime et retourne l'élément du sommet de la pile."""
        if self.est_vide():
            print("La pile est vide, impossible de dépiler.")
            return None
        return self.elements.pop()

    def est_vide(self):
        """Vérifie si la pile est vide."""
        return len(self.elements) == 0

    def afficher(self):
        """Affiche les éléments de la pile."""
        print("Éléments de la pile :", self.elements)


# Implémentation d'une file d'attente (Queue) avec collections.deque
from collections import deque

class File:
    def __init__(self):
        """Initialise une nouvelle file d'attente vide."""
        self.elements = deque()

    def ajouter(self, element):
        """Ajoute un élément à la fin de la file d'attente."""
        self.elements.append(element)
        print(f"Ajouté à la file : {element}")

    def retirer(self):
        """Supprime et retourne l'élément au début de la file d'attente."""
        if self.est_vide():
            print("La file d'attente est vide, impossible de retirer.")
            return None
        return self.elements.popleft()

    def est_vide(self):
        """Vérifie si la file d'attente est vide."""
        return len(self.elements) == 0

    def afficher(self):
        """Affiche les éléments de la file d'attente."""
        print("Éléments de la file d'attente :", list(self.elements))


# Test de la classe Pile
print("Test de la pile (Stack) :")
pile = Pile()
pile.empiler(1)
pile.empiler(2)
pile.empiler(3)
pile.afficher()  # Affiche les éléments de la pile

element_depile = pile.depiler()  # Dépile un élément
print(f"Élément dépilé : {element_depile}")
pile.afficher()  # Affiche les éléments restants de la pile

# Test de la classe File
print("\nTest de la file d'attente (Queue) :")
file = File()
file.ajouter('A')
file.ajouter('B')
file.ajouter('C')
file.afficher()  # Affiche les éléments de la file d'attente

element_retirer = file.retirer()  # Retire un élément
print(f"Élément retiré : {element_retirer}")
file.afficher()  # Affiche les éléments restants de la file d'attente
