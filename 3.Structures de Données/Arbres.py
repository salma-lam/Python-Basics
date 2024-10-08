class Noeud:
    """Classe représentant un nœud d'un arbre binaire."""
    
    def __init__(self, valeur):
        """Initialise un nœud avec une valeur donnée et des fils gauche et droit à None."""
        self.valeur = valeur
        self.gauche = None
        self.droit = None


class ArbreBinaire:
    """Classe représentant un arbre binaire."""
    
    def __init__(self):
        """Initialise un arbre binaire vide."""
        self.racine = None

    def ajouter(self, valeur):
        """Ajoute une valeur à l'arbre binaire en maintenant l'ordre."""
        if self.racine is None:
            self.racine = Noeud(valeur)  # Si l'arbre est vide, la valeur devient la racine
        else:
            self._ajouter_recursif(self.racine, valeur)

    def _ajouter_recursif(self, nœud, valeur):
        """Ajoute récursivement une valeur à l'arbre."""
        if valeur < nœud.valeur:  # Si la valeur est inférieure, aller à gauche
            if nœud.gauche is None:
                nœud.gauche = Noeud(valeur)
            else:
                self._ajouter_recursif(nœud.gauche, valeur)
        elif valeur > nœud.valeur:  # Si la valeur est supérieure, aller à droite
            if nœud.droit is None:
                nœud.droit = Noeud(valeur)
            else:
                self._ajouter_recursif(nœud.droit, valeur)

    def parcours_inordre(self):
        """Effectue un parcours en ordre (in-order traversal) de l'arbre."""
        print("Parcours en ordre : ", end='')
        self._parcours_inordre_recursif(self.racine)
        print()  # Nouvelle ligne après le parcours

    def _parcours_inordre_recursif(self, nœud):
        """Parcours en ordre récursif."""
        if nœud is not None:
            self._parcours_inordre_recursif(nœud.gauche)  # Visiter le sous-arbre gauche
            print(nœud.valeur, end=' ')  # Visiter le nœud
            self._parcours_inordre_recursif(nœud.droit)  # Visiter le sous-arbre droit

    def parcours_preordre(self):
        """Effectue un parcours pré-ordre (pre-order traversal) de l'arbre."""
        print("Parcours pré-ordre : ", end='')
        self._parcours_preordre_recursif(self.racine)
        print()

    def _parcours_preordre_recursif(self, nœud):
        """Parcours pré-ordre récursif."""
        if nœud is not None:
            print(nœud.valeur, end=' ')  # Visiter le nœud
            self._parcours_preordre_recursif(nœud.gauche)  # Visiter le sous-arbre gauche
            self._parcours_preordre_recursif(nœud.droit)  # Visiter le sous-arbre droit

    def parcours_postordre(self):
        """Effectue un parcours post-ordre (post-order traversal) de l'arbre."""
        print("Parcours post-ordre : ", end='')
        self._parcours_postordre_recursif(self.racine)
        print()

    def _parcours_postordre_recursif(self, nœud):
        """Parcours post-ordre récursif."""
        if nœud is not None:
            self._parcours_postordre_recursif(nœud.gauche)  # Visiter le sous-arbre gauche
            self._parcours_postordre_recursif(nœud.droit)  # Visiter le sous-arbre droit
            print(nœud.valeur, end=' ')  # Visiter le nœud


# Test du code
print("Test de l'arbre binaire :")
arbre = ArbreBinaire()

# Ajouter des valeurs à l'arbre
valeurs = [7, 4, 9, 2, 5, 8, 10]
for val in valeurs:
    arbre.ajouter(val)

# Parcours de l'arbre
arbre.parcours_inordre()     # Affiche les valeurs dans l'ordre croissant
arbre.parcours_preordre()    # Affiche les valeurs dans l'ordre pré-ordre
arbre.parcours_postordre()    # Affiche les valeurs dans l'ordre post-ordre
