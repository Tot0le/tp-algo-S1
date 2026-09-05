from TP5 import ex1, ex2, ex2entiersigne
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 3
    numTP = 5

    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["Demande si le nombre est pair ou non", "Conversion base 10 en binaire", "Conversion base 2 signé en base 10"])
        numExo = int(input("Saisissez l'exercice que vous voulez exécuter : "))
        if numExo == 1 :
            ex1.main()
        elif numExo == 2 :
            ex2.main()
        elif numExo == 3 :
            ex2entiersigne.main()
        elif (numExo == nombExo + 1) :
            conditionSorti = False
            print("Retour.")
            ALaLigne(4)
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")