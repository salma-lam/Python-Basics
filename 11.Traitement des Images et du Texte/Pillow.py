from PIL import Image

# Charger l'image
image = Image.open('C:/Users/HP/Desktop/Basics Python/11.Traitement des Images et du Texte/image.jpeg')

# Afficher les dimensions de l'image originale
print("Taille originale :", image.size)

# Redimensionner l'image
new_size = (300, 300)
image_resized = image.resize(new_size)
print("Nouvelle taille :", image_resized.size)

# Faire une rotation de l'image de 45 degrés
image_rotated = image.rotate(45)

# Convertir l'image en niveaux de gris
image_gray = image.convert("L")

# Sauvegarder les images résultantes
image_resized.save("image_resized.jpg")
image_rotated.save("image_rotated.jpg")
image_gray.save("image_gray.jpg")

# Afficher les images manipulées
image_resized.show()
image_rotated.show()
image_gray.show()
