from TP7 import ex1, ex2
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    numTP : int
    nombExo : int

    numTP = 7
    nombExo = 2
    
    conditionSorti = True
    while conditionSorti :
        affichageMenuTP(numTP, nombExo, ["Programme afficher tout les nombres premiers de 0 à n", "Conversion unité de volumes impérials/métriques"])
        numExo = int(input("Saisissez l'exercice que vous voulez exécuter : "))
        if numExo == 1 :
            ex1.main()
        elif numExo == 2 :
            ex2.menu()
        elif numExo == 3 :
            print("Retour.")
            ALaLigne(4)
            conditionSorti = False
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")