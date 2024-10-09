class FiniteAutomaton:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        """
        Initialise un automate fini.
        
        :param states: Ensemble des états de l'automate.
        :param alphabet: Alphabet de l'automate.
        :param transition_function: Fonction de transition (dictionnaire).
        :param start_state: État initial de l'automate.
        :param accept_states: Ensemble des états d'acceptation.
        """
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_string):
        """
        Vérifie si l'automate accepte une chaîne d'entrée.
        
        :param input_string: Chaîne d'entrée à tester.
        :return: True si la chaîne est acceptée, False sinon.
        """
        current_state = self.start_state  # État courant commence à l'état initial

        # Parcours de chaque symbole de la chaîne d'entrée
        for symbol in input_string:
            if symbol not in self.alphabet:
                raise ValueError(f"Le symbole '{symbol}' n'est pas dans l'alphabet.")
            # Transition vers l'état suivant
            current_state = self.transition_function[current_state][symbol]

        # Vérification si l'état final est un état d'acceptation
        return current_state in self.accept_states


# Définition des éléments de l'automate
states = {'q0', 'q1', 'q2'}  # Ensemble des états
alphabet = {'0', '1'}  # Alphabet
transition_function = {  # Fonction de transition
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q2', '1': 'q1'},
    'q2': {'0': 'q2', '1': 'q2'}
}
start_state = 'q0'  # État initial
accept_states = {'q1'}  # État d'acceptation

# Création de l'automate
afd = FiniteAutomaton(states, alphabet, transition_function, start_state, accept_states)

# Test de l'automate avec différentes chaînes d'entrée
test_strings = ['0', '1', '10', '11', '00', '010', '110']

# Vérification de chaque chaîne d'entrée
for test_string in test_strings:
    result = afd.accepts(test_string)
    print(f"La chaîne '{test_string}' est acceptée : {result}")
