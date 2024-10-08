# Importation des bibliothèques nécessaires
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Chargement et prétraitement du jeu de données MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape((60000, 28, 28, 1)).astype("float32") / 255  # Normalisation
x_test = x_test.reshape((10000, 28, 28, 1)).astype("float32") / 255  # Normalisation
y_train = tf.keras.utils.to_categorical(y_train, 10)  # Encodage one-hot
y_test = tf.keras.utils.to_categorical(y_test, 10)  # Encodage one-hot

# Création du modèle
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))  # Couche convolutive
model.add(layers.MaxPooling2D((2, 2)))  # Couche de max pooling
model.add(layers.Conv2D(64, (3, 3), activation='relu'))  # Couche convolutive
model.add(layers.MaxPooling2D((2, 2)))  # Couche de max pooling
model.add(layers.Flatten())  # Aplatissement
model.add(layers.Dense(64, activation='relu'))  # Couche dense
model.add(layers.Dense(10, activation='softmax'))  # Couche de sortie

# Compilation du modèle
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Entraînement du modèle
history = model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))

# Évaluation du modèle
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print("\nTest accuracy:", test_acc)

# Visualisation de l'historique d'entraînement
plt.plot(history.history['accuracy'], label='précision (entraînement)')
plt.plot(history.history['val_accuracy'], label='précision (validation)')
plt.title('Précision du modèle')
plt.xlabel('Époques')
plt.ylabel('Précision')
plt.legend()
plt.show()
