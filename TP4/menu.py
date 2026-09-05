from TP4 import Ex1TP4
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 1
    numTP = 4

    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["Programme de prix en fonction de l'age et si la personne est étudiante ou non"])
        numExo = int(input("Saisissez l'exercice que vous voulez exécuter : "))
        if numExo == 1 :
            Ex1TP4.main()
        elif (numExo == nombExo + 1) :
            conditionSorti = False
            print("Retour.")
            ALaLigne(4)
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")