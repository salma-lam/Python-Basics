import threading
import multiprocessing
import time

# Fonction à exécuter avec threading
def task_with_threading(task_name, duration):
    print(f"Début de la tâche {task_name} avec Threading...")
    time.sleep(duration)
    print(f"Fin de la tâche {task_name} avec Threading après {duration} secondes.")

# Fonction à exécuter avec multiprocessing
def task_with_multiprocessing(task_name, duration):
    print(f"Début de la tâche {task_name} avec Multiprocessing...")
    time.sleep(duration)
    print(f"Fin de la tâche {task_name} avec Multiprocessing après {duration} secondes.")

if __name__ == "__main__":
    # Exécution parallèle avec Threading
    thread1 = threading.Thread(target=task_with_threading, args=("Thread 1", 2))
    thread2 = threading.Thread(target=task_with_threading, args=("Thread 2", 4))
    
    # Exécution parallèle avec Multiprocessing
    process1 = multiprocessing.Process(target=task_with_multiprocessing, args=("Processus 1", 3))
    process2 = multiprocessing.Process(target=task_with_multiprocessing, args=("Processus 2", 5))
    
    # Démarrage des threads
    thread1.start()
    thread2.start()

    # Démarrage des processus
    process1.start()
    process2.start()

    # Attendre la fin des threads et processus
    thread1.join()
    thread2.join()
    
    process1.join()
    process2.join()

    print("Toutes les tâches sont terminées.")
