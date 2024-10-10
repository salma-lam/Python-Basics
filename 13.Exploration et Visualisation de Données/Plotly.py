import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# 1. Chargement des données
# Utilisation du jeu de données "iris"
iris = px.data.iris()

# 2. Graphique en nuage de points interactif
# Visualisation de la relation entre la longueur et la largeur des pétales, colorée par espèce
fig = px.scatter(iris, 
                 x='petal_length', 
                 y='petal_width', 
                 color='species', 
                 title="Relation entre la longueur et la largeur des pétales",
                 labels={'petal_length': 'Longueur des pétales (cm)', 'petal_width': 'Largeur des pétales (cm)'})

fig.show()

# 3. Graphique en ligne interactif
# Affichage de la longueur des sépales pour chaque espèce
fig_line = px.line(iris, 
                   x='species', 
                   y='sepal_length', 
                   title="Longueur moyenne des sépales par espèce",
                   labels={'species': 'Espèces', 'sepal_length': 'Longueur des sépales (cm)'},
                   markers=True)

fig_line.show()

# 4. Graphique à barres interactif
# Visualisation de la longueur moyenne des sépales par espèce
sepal_mean = iris.groupby('species')['sepal_length'].mean().reset_index()

fig_bar = px.bar(sepal_mean, 
                 x='species', 
                 y='sepal_length', 
                 title="Longueur moyenne des sépales par espèce",
                 labels={'species': 'Espèces', 'sepal_length': 'Longueur des sépales (cm)'},
                 color='species')

fig_bar.show()

# 5. Graphique interactif avec annotations et traces multiples
# Tracer des courbes multiples (longueur des sépales et pétales)
fig_multitrace = go.Figure()

# Ajout de la courbe pour les sépales
fig_multitrace.add_trace(go.Scatter(x=iris['species'], y=iris['sepal_length'],
                                    mode='lines+markers',
                                    name='Longueur des sépales'))

# Ajout de la courbe pour les pétales
fig_multitrace.add_trace(go.Scatter(x=iris['species'], y=iris['petal_length'],
                                    mode='lines+markers',
                                    name='Longueur des pétales'))

fig_multitrace.update_layout(
    title="Longueur des sépales et des pétales par espèce",
    xaxis_title="Espèces",
    yaxis_title="Longueur (cm)"
)

fig_multitrace.show()
