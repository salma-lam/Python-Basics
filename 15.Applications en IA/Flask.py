from flask import Flask, request, jsonify
import numpy as np
import joblib

# Initialisation de l'application Flask
app = Flask(__name__)

# Chargement d'un modèle IA pré-entraîné (par exemple, un modèle de classification)
# Ici, on suppose que le modèle est sauvegardé dans un fichier .pkl
model = joblib.load("modele_classification.pkl")

# Point de terminaison pour faire des prédictions
@app.route('/predict', methods=['POST'])
def predict():
    # On attend que la requête envoie des données JSON contenant des features
    data = request.get_json(force=True)
    
    # Extraction des caractéristiques (features) à partir des données reçues
    features = np.array(data['features']).reshape(1, -1)
    
    # Prédiction avec le modèle chargé
    prediction = model.predict(features)
    
    # Retourne la prédiction sous forme de JSON
    return jsonify({
        'prediction': prediction[0]
    })

# Démarrage de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
