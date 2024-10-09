# Importation des bibliothèques nécessaires
import cv2
import numpy as np

# Chargement de l'image en couleur
image = cv2.imread('C:/Users/HP/Desktop/Basics Python/11.Traitement des Images et du Texte/image.jpeg')

# Affichage de l'image originale
cv2.imshow('Image Originale', image)

# Conversion de l'image en niveaux de gris
image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Affichage de l'image en niveaux de gris
cv2.imshow('Image en Niveaux de Gris', image_gris)

# Détection des contours avec Canny
contours = cv2.Canny(image_gris, threshold1=100, threshold2=200)

# Affichage des contours détectés
cv2.imshow('Contours', contours)

# Attente d'une touche pour fermer les fenêtres
cv2.waitKey(0)
cv2.destroyAllWindows()
