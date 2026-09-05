import constante
from TP7 import constanteUniteImperial
from outils import saisieFloat, saisieStr

def menu():
    """
    Menu de l'exercice pour choisir dans quel sens on veut la conversion ou quitter.
    """
    choix : int

    print("Menu :")
    print("Choix 1 : impérial -> métrique")
    print("Choix 2 : métrique -> impérial")
    print("Choix 3 : quitter")

    choix = int(input(("Donnez le numéro de votre choix : ")))

    match choix:
        case 1 : 
            choix1()
        case 2 :
            choix2()
        case 3 :
            print("Quitter")
        case _ :
            print("Choix invalide.")
            # quitter

def choix1():
    """
    Rassemble toutes les instructions du menu en choix 1.
    """
    msg : str
    msgError : str
    borneMini : float
    borneMaxi : float

    print("Unite de volume en entrée : ")
    uniteImperial = choixUniteMesureVolumeImperial()

    msg = "Saisissez la valeur du volume à convertir : "
    msgError = "Un volume ne peut pas être négatif, veuillez resaisir : "
    borneMini = 0
    borneMaxi = constante.MAXFLOAT
    MinInclus = True

    nombre = saisieFloat(msg, msgError, borneMini, borneMaxi, MinInclus)
    
    print("Unite de volume en sorti : ")
    uniteMetrique = choixUniteMesureVolumeMetrique()
    
    valeurUniteImp = UniteStrToValueImp(uniteImperial)
    convertirImpToMetr(nombre, uniteImperial, uniteMetrique, valeurUniteImp)

def choix2():
    """
    Rassemble toutes les instructions du menu en choix 2.
    """
    msg : str
    msgError : str
    borneMini : float
    borneMaxi : float

    print("Unite de volume en entrée : ")
    uniteMetrique = choixUniteMesureVolumeMetrique()
    

    msg = "Saisissez la valeur du volume à convertir : "
    msgError = "Un volume ne peut pas être négatif, veuillez resaisir : "
    borneMini = 0
    borneMaxi = constante.MAXFLOAT
    MinInclus = True

    nombre = saisieFloat(msg, msgError, borneMini, borneMaxi, MinInclus)
    
    print("Unite de volume en sorti : ")
    uniteImperial = choixUniteMesureVolumeImperial()
    
    valeurUniteImp = UniteStrToValueImp(uniteImperial)
    convertirMetrToImp(nombre, uniteImperial, uniteMetrique, valeurUniteImp)


def UniteStrToValueImp(uniteStr : str) -> float:
    """
    Fonction retournant la valeur de conversion de l'unité imperial pour 1mL
    entrée : uniteStr : nom de l'unite imperial en chaine de caractere
    sortie : valeur : valeur de conversion de l'unité imperial pour 1mL
    """
    valeur : float
    
    match uniteStr:
        case "once":
            valeur = constanteUniteImperial.ONCE
        case "once liquide":
            valeur = constanteUniteImperial.ONCE
        case "tasse":
            valeur = constanteUniteImperial.TASSE
        case "pinte":
            valeur = constanteUniteImperial.PINTE
        case "quart":
            valeur = constanteUniteImperial.QUART
        case "gallon":
            valeur = constanteUniteImperial.GALLON
        case _ :
            print("Cette unité impérial n'existe pas.")
            valeur = 0
    return valeur

def convertirImpToMetr(nombre : float, uniteImp : str, uniteMetr : str, valeurUniteImperial : float):
    """
    Converti une valeur impérial en valeur métrique.
    entrée : nombre : nombre à convertir
            uniteImp : nom de l'unité impérial choisi
            uniteMtr : nom de l'unité métrique choisi
            valeurUniteImperial : valeur de conversion de l'unité imperial pour 1mL
    """
    valeurEnML : float
    valeurEnL : float

    valeurEnML = nombre * valeurUniteImperial
    if uniteMetr == "ml" or uniteMetr == "mL":
        print(f"{nombre} {uniteImp} = {valeurEnML} {uniteMetr}")
    else:
        valeurEnL = valeurEnML / 1000
        print(f"{nombre} {uniteImp} = {valeurEnL} {uniteMetr}")

def convertirMetrToImp(nombre : float, uniteMetr : str, uniteImp : str, valeurUniteImperial : float):
    """
    Converti une valeur métrique en valeur impérial.
    entrée : nombre : nombre à convertir
            uniteMtr : nom de l'unité métrique choisi
            uniteImp : nom de l'unité impérial choisi
            valeurUniteImperial : valeur de conversion de l'unité imperial pour 1mL
    """
    valeurImp : float

    valeurImp = nombre / valeurUniteImperial
    print(f"{nombre} {uniteMetr} = {valeurImp} {uniteImp}")

def afficheTabCorrespondImperMetr():
    """
    Procedure affichant le tableau de correspondance 
    des unités de volumes impériales à métriques (en mL) 
    à l'utilisateur.
    """

    print("1 once liquide = 29.57 mL")
    print("1 tasse = 236.6 mL")
    print("1 pinte = 473.18 mL")
    print("1 quart = 946.35 mL")
    print("1 gallon = 3785.41 mL")

def choixUniteMesureVolumeImperial() -> str:
    """
    Procedure qui initialise le fait de demander la saisie du choix de l'utilisateur pour le volume Imperial.
    """
    listUniteMesuresImperial : list[str]
    msg : str
    messageErreur : str
    chaine : str

    print("Rappel :")
    afficheTabCorrespondImperMetr() # procedure d'affichage pour l'utilisateur

    listUniteMesuresImperial = ["once liquide", "once", "tasse", "pinte", "quart", "gallon"]
    msg = "Saisissez le nom de l'unité de mesure de volume impérial : "
    messageErreur = "Saisie incorrect, Veuillez saisir le nom de l'unité de mesure impérial désiré. \n (Soit : once, tasse, pinte, quart ou gallon) : "

    chaine = saisieStr(listUniteMesuresImperial, msg, messageErreur, )
    return chaine

def choixUniteMesureVolumeMetrique() -> str:
    """
    Procedure qui initialise le fait de demander la saisie du choix de l'utilisateur pour le volume Metrique.
    """
    listUniteMesuresMetric : list[str]
    msg : str
    messageErreur : str
    chaine : str

    print("Veuillez choisir votre unité de mesure métrique (L ou mL).")

    listUniteMesuresMetric = ["L", "l", "mL", "ml"]
    msg = "Saisissez le nom de l'unité de mesure de volume métrique (L ou mL): "
    messageErreur = "Saisie incorrect, Veuillez saisir le nom de l'unité de mesure métrique désiré entre mL ou L : "

    chaine = saisieStr(listUniteMesuresMetric, msg, messageErreur, )
    return chaine
