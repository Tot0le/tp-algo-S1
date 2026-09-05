def main():
    menu()


def menu():
    choix : int

    print("--- Menu ---")
    print("1) une commande type petite quantité")
    print("2) une commande grande quantité")
    print("3) quitter")
    
    choix = int(input("Votre choix : "))

    match choix :
        case 1 :
            option1()
        case 2 :
            pass
        case 3 :
            print("Quitter")
        case _:
            print("Erreur")

def option1():
    grosCarton : int
    moyenCarton : int
    petitCarton : int

    quantitePair = int(input("Saisissez un entier pair "))

    if quantitePair % 2 == 0 and quantitePair <= 20 :
        print(quantitePair)
        print(glouton(quantitePair, [200, 50, 10, 2]))


def glouton(valeur : int, liste : list[int]):
    """
    Précondition : Liste trié du plus gros au plus petit
    """
    valeurIntermediaire : int
    listeResutat : list[int] = []
    valeurIntermediaire = valeur
    for indElement in range(len(liste)):
        while valeurIntermediaire >= liste[indElement]:
            valeurIntermediaire -= liste[indElement]
            listeResutat.append(liste[indElement])
    return listeResutat
