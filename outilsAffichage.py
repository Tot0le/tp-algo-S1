import os
def affichageMenuTP(monNumTP : int, monNbEx : int, maListeDAffichage : list) -> None:
    print()
    print(f"--- Menu TP{monNumTP} ---")

    match monNbEx:
        case 1:
            print("Un exercice disponible : ")
            print("    1: " + maListeDAffichage[0])
            print()
            print("    2: Retour au menu principal")
            print()
        case monNbEx if monNbEx > 1:
            print(f"{monNbEx} exercices disponibles : ")

            for i in range(len(maListeDAffichage)):
                print(f"    {i+1}: " + maListeDAffichage[i])
            
            print(f"    {len(maListeDAffichage) + 1}: Retour au menu principal")
            print()
        case _ :
            print("Erreur de saisie, le nombre d'exercices saisie est certainement négatif.")

def ALaLigne(monNombreDeFois : int) -> None:
    i : int

    for i in range(monNombreDeFois):
        print()

def pressEnterToContinue(langue : str = "en") -> None:
    """
    Fonction qui fait qu'on doit appuyer sur entrée pour continuer
    """
    langue.lower()
    match langue:
        case "fr":
            input("Appuyez sur Entrée pour continuer...")
        case _:
            input("Press Enter to continue.")

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')