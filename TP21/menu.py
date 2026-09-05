from TP21 import TPChainage, TPDoubleChainage
from outilsAffichage import affichageMenuTP, ALaLigne, clearConsole

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 2
    numTP = 20
    clearConsole()
    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["TPChainage", "TPDoubleChainage"])
        numExo = input("Saisissez l'exercice que vous voulez exécuter : ")
        if numExo == "1" :
            TPChainage.main()
        elif numExo == "2" :
            TPDoubleChainage.main()
        elif numExo == "3" :
            conditionSorti = False
            print("Retour.")
            clearConsole()
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")
