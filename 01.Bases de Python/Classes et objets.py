# Définition d'une classe de base
class Animal:
    """
    Classe de base pour représenter un animal.
    """
    
    def __init__(self, nom, age):
        self.nom = nom  # Attribut de l'instance
        self.age = age  # Attribut de l'instance
    
    def decrire(self):
        """
        Affiche les informations sur l'animal.
        """
        print(f"Cet animal s'appelle {self.nom} et il a {self.age} ans.")
    
    def emettre_son(self):
        """
        Méthode par défaut pour émettre un son.
        """
        print(f"{self.nom} fait un bruit d'animal.")

# Classe dérivée qui hérite de la classe Animal
class Chien(Animal):
    """
    Classe qui représente un chien, héritant d'Animal.
    """
    
    def __init__(self, nom, age, race):
        super().__init__(nom, age)  # Appelle le constructeur de la classe parente
        self.race = race  # Attribut propre à la classe Chien
    
    def emettre_son(self):
        """
        Redéfinition de la méthode emettre_son pour un chien.
        """
        print(f"{self.nom} aboie.")

# Classe dérivée qui hérite de la classe Animal
class Chat(Animal):
    """
    Classe qui représente un chat, héritant d'Animal.
    """
    
    def emettre_son(self):
        """
        Redéfinition de la méthode emettre_son pour un chat.
        """
        print(f"{self.nom} miaule.")

# Création d'objets à partir des classes
chien1 = Chien("Bobby", 5, "Labrador")
chat1 = Chat("Mimi", 3)

# Appel des méthodes des objets
chien1.decrire()      # "Cet animal s'appelle Bobby et il a 5 ans."
chien1.emettre_son()  # "Bobby aboie."

chat1.decrire()      # "Cet animal s'appelle Mimi et il a 3 ans."
chat1.emettre_son()  # "Mimi miaule."
