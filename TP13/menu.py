from TP13 import ex0, ex1, ex2
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 3
    numTP = 13

    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["0. Calcul PGCD.","1. Equation du second degrès.", "2. Trie bizarre."])
        numExo = int(input("Saisissez l'exercice que vous voulez exécuter : "))
        if numExo == 1 :
            ex0.main()
        elif numExo == 2 :
            ex1.main()
        elif numExo == 3 :
            ex2.main()
        elif numExo == 4 :
            conditionSorti = False
            print("Retour.")
            ALaLigne(4)
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")