# IMPORTS
from math import sqrt
import outils

def estPremier(nombre : int) -> bool:
    """
    Fonction qui renvoie vrai si le nombre donné est premier, faux sinon
    entrée : nombre : entier
    sorti : estPremier : booleen
    """
    i : int
    estPremier : bool
    
    if nombre <= 1:
        estPremier = False
    else:
        estPremier = True
        i = 2
        while i <= sqrt(nombre) and estPremier:
            if nombre % i == 0 : # si le nombre est divisible par i alors il n'est pas premier
                estPremier = False
            i += 1

    return estPremier

def fibonacci_iterative(k : int) -> int:
    """
    Fonction iterative qui calcule le k-ième élement de fibonacci.
    entrée : k : entier : l'indice de la suite de fibonacci
    sorti : valeur : entier : valeur de l'élement k de la suite de fibonacci
    """
    valeur : int = 1
    Un : int
    Un1 : int
    Un2 : int
    i : int

    Un = 0
    Un1 = 1

    if k == 1:
        valeur = Un1
    else:
        for i in range(2, k + 1) :
            Un2 = Un + Un1
            valeur = Un + Un1
            Un = Un1
            Un1 = Un2
    
    return valeur

def fibonacci_recursive(k : int) -> int:
    """
    Fonction recursive qui calcule le k-ième élement de fibonacci.
    entrée : k : entier : l'indice de la suite de fibonacci
    sorti : valeur : entier : valeur de l'élement k de la suite de fibonacci
    """
    if k == 1 :
        return 1
    elif k == 0 :
        return 0
    else :
        return fibonacci_recursive(k-1) + fibonacci_recursive(k-2)
    
def factorielle(nombre : int) -> int :
    """
    Fonction retounant la valeur factorielle du nombre en entrée
    entrée : nombre : entier
    sorti : nombre! : entier
    """
    if (nombre <= 1) :
        return 1
    else:
        return nombre * factorielle(nombre-1)




################ ENSEMBLES ################

def union(liste1 : list[int], liste2 : list[int]) -> list[int] :
    """
    Fonction qui renvoie l'union des deux listes en entrée.
    Entrée : Deux listes uniques.
    Sortie : Une liste unique avec les élements des deux listes en entrée.
    """
    listeUnion : list[int]
    element : int

    listeUnion = liste1

    for element in liste2 :
        listeUnion = outils.rajoutSiPasDedans(element, listeUnion)
    
    return listeUnion

def intersection(liste1 : list[int], liste2 : list[int]) -> list[int] :
    """
    Fonction qui renvoie l'intersection des deux listes en entrée.
    Entrée : Deux listes uniques.
    Sortie : Une liste unique avec les élements en commun aux deux listes en entrée.
    """
    listeIntersection : list[int]
    element : int

    listeIntersection = []
    for element in liste1 :
        if element in liste2 :
            listeIntersection.append(element)
    
    return listeIntersection

def difference(liste1 : list[int], liste2 : list[int]) -> tuple[list[int], list[int]] :
    """
    Fonction qui renvoie les deux differences (dans les deux sens) des deux listes en entrée.
    Entrée : Deux listes uniques.
    Sortie : Deux listes uniques représentant :
             1 : liste1 privé de liste2
             2 : liste2 privé de liste1
    """
    listeIntersection1_2 : list[int]
    listeIntersection2_1 : list[int]
    element : int

    # Pour liste1\liste2
    listeIntersection1_2 = liste1.copy()
    for element in liste2 :
        if (element in listeIntersection1_2):
            listeIntersection1_2.remove(element)

    # Pour liste2\liste1
    listeIntersection2_1 = liste2.copy()
    for element in liste1 :
        if (element in listeIntersection2_1):
            listeIntersection2_1.remove(element)

    return listeIntersection1_2, listeIntersection2_1

def disjointes(liste1 : list[int], liste2 : list[int]) -> bool :
    """
    Fonction renvoyant un booléen de si les deux listes en entrée sont dijointes (pas d'élement en commun).
    Entrée : Deux listes uniques.
    Sortie : booléen représentant si les deux listes sont disjointes ou non.
    """
    sontDisjointes : bool
    indElement : int # Indice de l'élement de la liste

    sontDisjointes = True
    indElement = 0

    while sontDisjointes and indElement < len(liste1):
        if liste1[indElement] in liste2:
            sontDisjointes = False
        indElement += 1

    return sontDisjointes
