from TP17 import ex0, ex1
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 2
    numTP = 17

    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["Ex0 : mot voyelle & palindrome", "Ex1 : Lecture de fichier spécial"])
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