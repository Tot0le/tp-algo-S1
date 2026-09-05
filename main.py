# IMPORTS
from outilsAffichage import clearConsole
from TP1 import menu as menuTP1
from TP2 import menu as menuTP2
from TP3 import menu as menuTP3
from TP4 import menu as menuTP4
from TP5 import menu as menuTP5
from TP6 import menu as menuTP6
from TP7 import menu as menuTP7
from TP8 import menu as menuTP8
from TP9 import menu as menuTP9
from TP10 import menu as menuTP10
from TP11 import menu as menuTP11
from TP12 import menu as menuTP12
from TP13 import menu as menuTP13
from TP14 import menu as menuTP14
from TP15 import menu as menuTP15
from TP16 import menu as menuTP16
from TP17 import menu as menuTP17
from TP18 import menu as menuTP18
from TP19 import menu as menuTP19
from TP20 import menu as menuTP20
from TP21 import menu as menuTP21

def saisi(nbMax: int, textUser : str) -> int:
    i : int
    num : str
    
    print("====== Menu Principal ======")
    for i in range(1, nbMax+1):
        print(f"{i} : TP{i}")
    print()
    print("0 : Quitter")

    num = str(input(textUser))
    return num

def afficheQuelTPchoisi(monNbTP : int) -> None:
    print(f"Vous avez choisi le TP{monNbTP}.")

if __name__=="__main__":
    choix : str
    nbTP : int
    numExo : int
    conditionSorti : bool

    clearConsole()

    conditionSorti = True
    nbTP = 21
    while conditionSorti :
        choix = saisi(nbTP, "Saisissez le numéro de TP de votre choix : ")
        print()
        if choix != "0" :
             afficheQuelTPchoisi(choix)
        match choix:
            case "0" :
                print("Fermeture.")
                conditionSorti = False
            case "1" : 
                menuTP1.menu()
            case "2" :
                menuTP2.menu()
            case "3" :
                menuTP3.menu()
            case "4" :
                menuTP4.menu()
            case "5" :
                menuTP5.menu()
            case "6" :
                menuTP6.menu()
            case "7" :
                menuTP7.menu()
            case "8" :
                menuTP8.menu()
            case "9" :
                menuTP9.menu()
            case "10" :
                menuTP10.menu()
            case "11" :
                menuTP11.menu()
            case "12" :
                menuTP12.menu()
            case "13" :
                menuTP13.menu()
            case "14" :
                menuTP14.menu()
            case "15" :
                menuTP15.menu()
            case "16" :
                menuTP16.menu()
            case "17" :
                menuTP17.menu()
            case "18" :
                menuTP18.menu()
            case "19" :
                menuTP19.menu()
            case "20" :
                menuTP20.menu()
            case "21" :
                menuTP21.menu()
            case _ :
                print("Choix invalide, veuillez resaisir.")
