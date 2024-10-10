import gradio as gr
import joblib
import numpy as np

# Chargement du modèle pré-entraîné (par exemple, un modèle de classification)
# On suppose que le modèle est déjà entraîné et sauvegardé dans un fichier .pkl
model = joblib.load("modele_classification.pkl")

# Fonction pour faire des prédictions
def predict_class(features):
    features = np.array(features).reshape(1, -1)  # Reshape pour correspondre au modèle
    prediction = model.predict(features)  # Prédiction avec le modèle
    return prediction[0]

# Création de l'interface Gradio
# Interface à 4 entrées correspondant aux features du modèle
interface = gr.Interface(
    fn=predict_class,  # La fonction de prédiction
    inputs=[gr.inputs.Number(label="Feature 1"), 
            gr.inputs.Number(label="Feature 2"),
            gr.inputs.Number(label="Feature 3"),
            gr.inputs.Number(label="Feature 4")],
    outputs="text",  # Retourne la classe prédite sous forme de texte
    title="Prédiction de classe avec Gradio",
    description="Entrez les caractéristiques pour prédire la classe.",
)

# Lancement de l'interface
if __name__ == "__main__":
    interface.launch()
