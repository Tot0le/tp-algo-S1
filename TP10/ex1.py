from outilsMath import factorielle
import outils
import time
import constante

def main():
    valeur : int
    msg : str
    messageErreur : str
    borneMin : str
    borneMax : str
    valeur : str
    t1Itera : str
    t2Itera : str
    tempsItera : str
    t1Rec : str
    t2Rec : str
    tempsRec : str
    n : int
    k : int

    n = 0
    k = 0
    msg = "Saisissez le nombre n : "
    messageErreur = "Saisie incorrecte, saisissez le nombre n : "
    borneMin = 0
    borneMax = constante.MAXINT
    n = outils.saisieEntier(msg, messageErreur, borneMin, borneMax, True, True)

    msg = "Saisissez le nombre k : "
    messageErreur = "Saisie incorrecte, saisissez le nombre k : "
    k = outils.saisieEntier(msg, messageErreur, borneMin, borneMax, True, True)

    t1Itera = time.time()
    valeur = combiDirecte(n, k)
    t2Itera = time.time()
    tempsItera = t2Itera - t1Itera

    print()
    print("Valeur : ", valeur)
    print("Temps de COMBI directe : ", tempsItera)

    t1Rec = time.time()
    valeur = combiRecursive(n, k)
    t2Rec = time.time()
    tempsRec = t2Rec - t1Rec

    print("Valeur : ", valeur)
    print("Temps de COMBI reccursive : ", tempsRec)

def combiDirecte(n : int, k : int) -> int :
    valeur : int

    valeur = factorielle(n) // (factorielle(k) * factorielle(n - k))
    return valeur

def combiRecursive(n : int, k : int) -> int :
    if (k == 0 or n == k) :
        return 1
    else:
        return combiRecursive(n-1, k) + combiRecursive(n-1, k-1)
    
