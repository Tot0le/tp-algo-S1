from TP11 import ex0, ex1
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 2
    numTP = 11

    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["Pyramide d'étoiles.", "Conversion binaire et addition."])
        numExo = int(input("Saisissez l'exercice que vous voulez exécuter : "))
        if numExo == 1 :
            ex0.main()
        elif numExo == 2 :
            ex1.main()
        elif numExo == 3 :
            conditionSorti = False
            print("Retour.")
            ALaLigne(4)
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")