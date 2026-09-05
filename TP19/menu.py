from TP19 import ex0, ex1, ex2
from outilsAffichage import affichageMenuTP, ALaLigne, clearConsole

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 3
    numTP = 19
    clearConsole()
    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["Ex0. Tableau de taille n aléatoire trié", "Ex1. Liste Chainee de taille n aléatoire trié", "Ex2. Analyse de mémoires liste chainée et liste"])
        numExo = input("Saisissez l'exercice que vous voulez exécuter : ")
        if numExo == "1" :
            ex0.main()
        elif numExo == "2" :
            ex1.main()
        elif numExo == "3" :
            ex2.main()
        elif numExo == "4" :
            conditionSorti = False
            print("Retour.")
            clearConsole()
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")