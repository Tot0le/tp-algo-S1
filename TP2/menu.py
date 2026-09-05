from TP2 import ex1, ex2_3, ex2_4, ex2
from outilsAffichage import affichageMenuTP, ALaLigne

def menu():
    numExo : int
    conditionSorti : bool
    nombExo : int
    
    conditionSorti = True
    nombExo = 4
    numTP = 2

    while conditionSorti :

        affichageMenuTP(numTP, nombExo, ["Ex1 : Conversion base 10 en binaire <0 et > 15", "Ex2 : Calcul le volume d'un prisme quelconque", "Ex2_3 : Calcul le volume d'un prisme rectangle en donnant les mesures de largeur et longueur", "Calcul le volume d'un prisme rectangle et d'un cylindre"])
        numExo = int(input("Saisissez l'exercice que vous voulez exécuter : "))
        if numExo == 1 :
            ex1.main()
        elif numExo == 2 :
            ex2.main()
        elif numExo == 3 :
            ex2_3.main()
        elif numExo == 4 :
            ex2_4.main()
        elif (numExo == nombExo + 1) :
            conditionSorti = False
            print("Retour.")
            ALaLigne(4)
        else:
            print("Le numéro de cette exercice de ce TP n'existe pas.")