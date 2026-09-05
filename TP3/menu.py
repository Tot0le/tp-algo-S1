from TP3 import Ex1TP3, ex2TP3, ex3TP3
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 3
    numTP = 3

    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["Programme division nombre pair", "Comparer deux variables", "Conversion base 16 en base 10 mais <= 15"])
        numExo = int(input("Saisissez l'exercice que vous voulez exécuter : "))
        if numExo == 1 :
            Ex1TP3.main()
        elif numExo == 2 :
            ex2TP3.main()
        elif numExo == 3 :
            ex3TP3.main()
        elif (numExo == nombExo + 1) :
            conditionSorti = False
            print("Retour.")
            ALaLigne(4)
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")