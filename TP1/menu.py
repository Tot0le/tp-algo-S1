from TP1 import Ex1Boucle, Ex1SansBoucle, Ex2, Ex3
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 4
    numTP = 1

    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["Ex1 boucle : Calcul aire et périmetre d'un rectangle", "Ex1 sans boucle : Calcul aire et périmetre d'un rectangle", "Ex2 : Information à propos de 2 variables entières", "Ex3 : Division Euclidienne"])
        numExo = int(input("Saisissez l'exercice que vous voulez exécuter : "))
        if numExo == 1 :
            Ex1Boucle.main()
        elif numExo == 2 :
            Ex1SansBoucle.main()
        elif numExo == 3 :
            Ex2.main()
        elif numExo == 4 :
            Ex3.main()
        elif (numExo == nombExo + 1) :
            conditionSorti = False
            print("Retour.")
            ALaLigne(4)
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")