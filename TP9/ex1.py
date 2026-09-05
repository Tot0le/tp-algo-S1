import constante
import outils
import outilsMath
import time

def main():
    """
    A la fin le programme compare la version fibo reccursive et fibonnacci
    Etapes :
    saisi et verif index
    boucle iterative
    boucle reccursive
    comparer les deux
    """
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
    indice : int

    indice = 0
    msg = "Saisissez l'indice de la valeur de fibonacci que vous voulez : "
    messageErreur = "Saisie incorrecte, saisissez l'indice de la valeur de fibonacci que vous voulez : "
    borneMin = 0
    borneMax = constante.MAXINT
    indice = outils.saisieEntier(msg, messageErreur, borneMin, borneMax, True, True)

    t1Itera = time.time()
    valeur = outilsMath.fibonacci_iterative(indice)
    t2Itera = time.time()
    tempsItera = t2Itera - t1Itera

    print("Valeur : ", valeur)
    print("Temps de fibo iteration : ", tempsItera)

    t1Rec = time.time()
    valeur = outilsMath.fibonacci_recursive(indice)
    t2Rec = time.time()
    tempsRec = t2Rec - t1Rec

    print("Temps de fibo reccursive : ", tempsRec)