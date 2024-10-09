# Importation de spaCy
import spacy

# Télécharger le modèle de langue anglais de spaCy si ce n'est pas déjà fait
# !python -m spacy download en_core_web_sm

# Charger le modèle de langue anglais
nlp = spacy.load('en_core_web_sm')

# Texte d'exemple à analyser
texte = "Natural Language Processing is fascinating! Let's explore tokenization and stemming."

# Appliquer le pipeline NLP de spaCy pour le traitement
doc = nlp(texte)

# Tokenization avec spaCy
tokens = [token.text for token in doc]
print("Tokens (spaCy):", tokens)

# Lemmatisation (réduction des mots à leur forme de base)
lemmas = [token.lemma_ for token in doc]
print("Lemmas (spaCy):", lemmas)

# Stemming n'est pas directement disponible dans spaCy, mais on utilise ici la lemmatisation qui est plus avancée
# Affichage de quelques autres informations utiles
pos_tags = [token.pos_ for token in doc]  # Tags des parties du discours (verbe, nom, etc.)
print("Part of Speech Tags (spaCy):", pos_tags)

# Dépendances syntaxiques (relation entre les mots dans une phrase)
dependencies = [token.dep_ for token in doc]
print("Dépendances syntaxiques (spaCy):", dependencies)

# Visualisation de l'analyse syntaxique (si vous voulez visualiser dans un environnement graphique)
# from spacy import displacy
# displacy.serve(doc, style="dep")
