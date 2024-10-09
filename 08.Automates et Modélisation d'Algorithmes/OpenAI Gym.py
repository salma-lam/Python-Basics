import gym

# 1. Créer l'environnement
env = gym.make('CartPole-v1')

# Nombre total d'épisodes
num_episodes = 5

# 3. Boucle à travers les épisodes
for episode in range(num_episodes):
    state = env.reset()  # Réinitialiser l'environnement à chaque épisode
    done = False  # Indicateur de fin d'épisode
    total_reward = 0  # Récompense totale de l'épisode
    
    while not done:
        # 4. Afficher l'environnement
        env.render()  # Visualiser l'environnement
        
        # 5. Choisir une action aléatoire
        action = env.action_space.sample()  # Sélectionner une action aléatoire
        
        # 6. Effectuer l'action et obtenir le nouvel état
        next_state, reward, done, truncated, info = env.step(action)
        
        # Mettre à jour l'état et la récompense totale
        state = next_state
        total_reward += reward
    
    print(f'Épisode {episode + 1}: Récompense totale = {total_reward}')

# 7. Fermer l'environnement
env.close()
