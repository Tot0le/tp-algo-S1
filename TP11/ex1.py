import outils
def main():
    entier1 : int
    entier2 : int
    binEntier1 : list[int]
    binEntier2 : list[int]
    nbBinaireAdd : list[int]
    borneMini : int
    borneMaxi : int
    nombreAdd : int

    borneMini = 0
    borneMaxi = 100

    # LES SAISIES :
    entier1 = outils.saisieEntier("Saisissez le premier nombre entier : ", f"Erreur de saisie, veuillez saisir le premier nombre entier (entre {borneMini} et {borneMaxi}) : ", borneMini, borneMaxi, True, True)
    entier2 = outils.saisieEntier("Saisissez le deuxième nombre entier : ", f"Erreur de saisie, veuillez saisir le deuxième nombre entier (entre {borneMini} et {borneMaxi}) : ", borneMini, borneMaxi, True, True)

    # CONVERSIONS DECIMAL A BINAIRE
    binEntier1 = DecimalToBinaire(entier1)
    binEntier2 = DecimalToBinaire(entier2)

    # MISE A NIVEAU AU MEME NOMBRE D'ELEMENT DANS LA LISTE
    binEntier1, binEntier2 = egaliserTableauNbBinaire(binEntier1, binEntier2)

    # AFFICHAGE
    print(f"{entier1} = {binEntier1} en base 2.")
    print(f"{entier2} = {binEntier2} en base 2.")

    # ADDITION DES DEUX
    nbBinaireAdd = additionBinaire(binEntier1, binEntier2)

    # AFFICHER LE RESULTATS EN BINAIRE ET EN DECIMAL
    nombreAdd = binaireToDecimal(nbBinaireAdd)
    print(f"{binEntier1} + {binEntier2} = {nbBinaireAdd} ou {nombreAdd} en décimal.")

def DecimalToBinaire(nombreDeci : int) -> list[int] : # on peut mettre dans outils
    """
    Fonction renvoyant l'équivalent binaire d'un nombre décimal.
    Entrée : Nombre entier à convertir
    Sortie : Un tableau représentant un nombre binaire, contenant des entiers, résultant de la conversion du nombre en entrée.
    """
    binNumber : list
    quotient : int

    binNumber = []
    quotient = nombreDeci

    while quotient > 0 :
        binNumber.insert(0, quotient % 2)
        quotient = quotient // 2

    return binNumber


def binaireToDecimal(tab : list[int]) -> int:
    """
    Fonction renvoyant l'équivalent décimal d'un nombre binaire.
    Entrée : Un tableau représentant un nombre binaire, contenant des entiers.
    Sortie : nombre entier résultant de la conversion du nombre binaire.
    """
    resultat : int
    i : int
    compteurExposant : int

    resultat = 0
    compteurExposant = 0

    for i in range(len(tab) - 1, -1, -1) :
        resultat = resultat + tab[i] * (2**(compteurExposant))
        compteurExposant += 1

    return resultat

def additionBinaire(nb1 : list[int], nb2 : list[int]) -> list[int]:
    """
    Additionne 2 valeurs entre 0 et 100 en binaire dans deux tableaux de taille égale.
    Entrée : deux tableaux d'entier de tailles égales (nombre sous forme binaire) entre 0 et 100.
    Sortie : tableau d'entier représentant un nombre binaire qui est la somme des deux nombres en entrée.
    """
    retenu : int
    nbfin : int
    maxi : int

    nbfin = []
    retenu = 0
    maxi = 100
    if binaireToDecimal(nb1) > maxi or binaireToDecimal(nb2) < maxi :
        for i in range(len(nb1) - 1, -1, -1):
            if (nb1[i] + nb2[i] + retenu) == 2 :
                nbfin.insert(0, 0)
                retenu = 1
            elif (nb1[i] + nb2[i] + retenu) == 3 :
                nbfin.insert(0, 1)
                retenu = 1
            elif (nb1[i] + nb2[i] + retenu) == 1 :
                nbfin.insert(0, 1)
                retenu = 0
            elif (nb1[i] + nb2[i] + retenu) == 0 :
                nbfin.insert(0, 0)
                retenu = 0
        
        if retenu == 1 :
            nbfin.insert(0, 1)
    else:
        print(f"Erreur nombre binaire trop grand. (nombre > {maxi})")
    return nbfin


def egaliserTableauNbBinaire(monTab1 : list[int], monTab2 : list[int]) -> list[int]:
    """
    Procedure qui met 2 tableaux au même nombres d'élément en rajoutant des 0 en tête.
    Entrée : Deux tableaux représentant respectivement deux nombres binaires, tableaux contenant des entiers.
    Sortie : Deux tableaux de même taille représentant respectivement deux nombres binaires, tableaux contenant des entiers.
    """

    while len(monTab1) < len(monTab2) :
        monTab1.insert(0, 0)
    while len(monTab1) > len(monTab2) :
        monTab2.insert(0, 0)

    return monTab1, monTab2
