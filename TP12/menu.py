from TP12 import ex1, ex2
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 2
    numTP = 12

    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["Simulation de nombre de valeurs distinctes dans une liste aléatoire à 100 nombre.", "Générer des listes uniques et les analyser."])
        numExo = int(input("Saisissez l'exercice que vous voulez exécuter : "))
        if numExo == 1 :
            ex1.main()
        elif numExo == 2 :
            ex2.main()
        elif numExo == 3 :
            conditionSorti = False
            print("Retour.")
            ALaLigne(4)
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")