from TP6 import ex1, ex1Q5, ex2
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 3
    numTP = 6

    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["Ex1 : Devine nombre première version", "Ex1Q5 : Devine nombre deuxième version", "Ex2 : Devine nombre troisième version (joueur IA ajouté)"])
        numExo = int(input("Saisissez l'exercice que vous voulez exécuter : "))
        if numExo == 1 :
            ex1.main()
        elif numExo == 2 :
            ex1Q5.main()
        elif numExo == 3 :
            ex2.main()
        elif numExo == 4 :
            conditionSorti = False
            print("Retour.")
            ALaLigne(4)
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")