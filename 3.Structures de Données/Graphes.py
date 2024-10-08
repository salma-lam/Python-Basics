class Graphe:
    def __init__(self):
        """Initialise un graphe vide sous forme de dictionnaire."""
        self.adjacences = {}

    def ajouter_sommet(self, sommet):
        """Ajoute un sommet au graphe."""
        if sommet not in self.adjacences:
            self.adjacences[sommet] = []
            print(f"Sommet ajouté : {sommet}")

    def ajouter_arete(self, sommet1, sommet2):
        """Ajoute une arête (connexion) entre deux sommets."""
        if sommet1 in self.adjacences and sommet2 in self.adjacences:
            self.adjacences[sommet1].append(sommet2)
            self.adjacences[sommet2].append(sommet1)  # Pour un graphe non orienté
            print(f"Arête ajoutée : {sommet1} <-> {sommet2}")

    def parcours_en_largeur(self, start):
        """Parcours en largeur (BFS) à partir d'un sommet donné."""
        visite = set()  # Ensemble pour suivre les sommets visités
        file = [start]  # File pour le BFS

        while file:
            sommet = file.pop(0)  # Retire le premier élément de la file
            if sommet not in visite:
                visite.add(sommet)  # Marque le sommet comme visité
                print(sommet, end=' ')  # Affiche le sommet
                # Ajoute les sommets adjacents non visités à la file
                for voisin in self.adjacences[sommet]:
                    if voisin not in visite:
                        file.append(voisin)

    def parcours_en_profondeur(self, start):
        """Parcours en profondeur (DFS) à partir d'un sommet donné."""
        visite = set()  # Ensemble pour suivre les sommets visités
        self._dfs_recursive(start, visite)

    def _dfs_recursive(self, sommet, visite):
        """Fonction récursive pour le DFS."""
        visite.add(sommet)  # Marque le sommet comme visité
        print(sommet, end=' ')  # Affiche le sommet
        # Explore les voisins non visités
        for voisin in self.adjacences[sommet]:
            if voisin not in visite:
                self._dfs_recursive(voisin, visite)


# Test du code
print("Test du graphe :")
graphe = Graphe()

# Ajouter des sommets
graphe.ajouter_sommet(1)
graphe.ajouter_sommet(2)
graphe.ajouter_sommet(3)
graphe.ajouter_sommet(4)
graphe.ajouter_sommet(5)

# Ajouter des arêtes
graphe.ajouter_arete(1, 2)
graphe.ajouter_arete(1, 3)
graphe.ajouter_arete(2, 4)
graphe.ajouter_arete(3, 5)

# Parcours en largeur (BFS)
print("\n\nParcours en largeur (BFS) à partir du sommet 1 :")
graphe.parcours_en_largeur(1)

# Parcours en profondeur (DFS)
print("\n\nParcours en profondeur (DFS) à partir du sommet 1 :")
graphe.parcours_en_profondeur(1)
