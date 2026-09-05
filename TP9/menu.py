from TP9 import ex1
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    numTP : int
    nombExo : int

    numTP = 9
    nombExo = 1
    
    conditionSorti = True

    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["Compare fibonacci iteratif et reccursif"])
        numExo = int(input("Saisissez l'exercice que vous voulez exécuter : "))

        if numExo == 1 :
            ex1.main()
        elif numExo == 2 :
            conditionSorti = False
            print("Retour.")
            ALaLigne(4)
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")