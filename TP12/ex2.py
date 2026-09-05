# IMPORTS
from random import randint
from outilsAffichage import ALaLigne
import outils
import outilsMath

def main():
    conditionSorti : bool
    choix : int

    conditionSorti = True
    
    while conditionSorti :
        ALaLigne(5)
        print("--- Exercice 2 ---")
        print("Deux choix possible : ")
        print("1. Programme question 6 : Générer x fois des listes uniques pour calculer la probabilité d'avoir une liste avec des doublons.")
        print("2. Programme question 7 : Génère deux listes de 50 élements uniques et calculer l'union, l'intesection, la différence et afficher leurs cardinalités.")
        print("3. Quitter")
        choix = outils.saisieEntier("Saisissez votre choix : ", "Erreur de saisie, veuillez choisir votre choix entre 1 et 3 : ", 1, 3, True, True)
        match choix:
            case 1 :
                Q6()
            case 2 :
                Q7()
            case 3 :
                print("Sorti exo 2.")
                conditionSorti = False
                ALaLigne(5)

def Q6():
    listeEssaies : list[int]
    nbFoisGenere : int

    nbFoisGenere = outils.saisieEntier("Saisissez le nombre de fois que vous voulez générée des listes uniques : ", "Erreur de saisie, veuillez saisir le nombre de fois que vous voulez générée des listes uniques : ", 1, 100000, True, True)
    listeEssaies = boucleEssaies(nbFoisGenere, 50, -100, 100)
    print(f"Les {nbFoisGenere} listes générées en {listeEssaies} tentatives.")

    print("La probabilité de tomber sur une liste avec doublons est : ")
    print(calculProba(listeEssaies))

def Q7():
    listeRandom1 : list[int]
    listeRandom2 : list[int]
    unionListes : list[int]
    intersecListes : list[int]
    list1PriveDeList2 : list[int]
    list2PriveDeList1 : list[int]

    ALaLigne(3)
    # GENERATION DE DEUX LISTES ALEATOIRES UNIQUES
    listeRandom1 = genereListeValeurEntierAleatoireUnique(50, -100, 100)
    listeRandom2 = genereListeValeurEntierAleatoireUnique(50, -100, 100)
    
    # AFFICHAGE DES DEUX LISTES
    print(f"La première liste générée est : {listeRandom1} de cardinal : {len(listeRandom1)}")
    print(f"La deuxième liste générée est : {listeRandom2} de cardinal : {len(listeRandom2)}")
    ALaLigne(3)

    # CALCUL DE L'UNION
    unionListes = outilsMath.union(listeRandom1, listeRandom2)
    print(f"L'union des deux listes est : {unionListes} de cardinal : {len(unionListes)}")
    ALaLigne(3)

    # CALCUL DE L'INTERSECTION
    intersecListes = outilsMath.intersection(listeRandom1, listeRandom2)
    print(f"L'intersection des deux listes est : {intersecListes} de cardinal : {len(intersecListes)}")
    ALaLigne(3)

    # CALCUL DES DIFFERENCES
    list1PriveDeList2, list2PriveDeList1 = outilsMath.difference(listeRandom1, listeRandom2)
    print(f"Les différences des deux listes sont : \n Liste1\Liste2 = {list1PriveDeList2} de cardinal : {len(list1PriveDeList2)} et Liste2\Liste1 = {list2PriveDeList1} de cardinal : {len(list2PriveDeList1)}")
    ALaLigne(3)
    
def isIn(valeur : int, liste : list[int]) -> bool : # fonction inutile mais demandé
    """
    Fonction qui renvoie True si une valeur est présent dans la liste
    Entrée : valeur entière et liste d'entier
    Sortie : un booléen True si la valeur est présente False sinon
    """
    estDedans : bool

    estDedans = False
    if valeur in liste :
        estDedans = True
    return estDedans

def genererListeValeurEntierAleatoire(nombre : int, borneMin : int, borneMax : int) -> list[int] : # could be in outils
    """
    Fonction qui genere une liste de valeur entier aléatoire d'un nombre donné entre 2 bornes donnés
    Entrée : nombre entier qui est le nombre de valeur aléatoire généré puis mis dans la liste.
             borneMin est la borne minimal du nombre random.
             borneMax est la borne maximal du nombre random.
    Sortie : Une liste de nombres générés aléatoirement de tailles de la variable nombre en entrée.
    """
    iterateur : int
    liste : list

    liste = []

    for iterateur in range(nombre):
        liste.append(randint(borneMin, borneMax))
    
    return liste

def genereListeValeurEntierAleatoireUnique(nombre : int, borneMin : int, borneMax : int) -> list[int] : # could be in outils
    """
    C'est la meme fonction que genereListeEntierAleatoireUnique mais qui ne renvoie pas le nombre de tentative.
    Entrée : Nombre entier qui est le nombre de valeur aléatoire généré puis mis dans la liste.
             BorneMin est la borne minimal du nombre random.
             BorneMax est la borne maximal du nombre random.
    Sortie : Une liste unique.
    """
    listeAleatoire = [0,0]
    while not outils.estUnEnsemble(listeAleatoire) : # tant que la liste n'est pas un ensemble
        listeAleatoire = genererListeValeurEntierAleatoire(nombre, borneMin, borneMax)

    return listeAleatoire

def genereListeEntierAleatoireUnique(nombre : int, borneMin : int, borneMax : int) -> tuple[list[int], int]:
    """
    Entrée : Nombre entier qui est le nombre de valeur aléatoire généré puis mis dans la liste.
             BorneMin est la borne minimal du nombre random.
             BorneMax est la borne maximal du nombre random.
    Sortie : Une liste unique.
             Un entier représentant le nombre de tentative de génération de liste de 50 nombres aléatoires entre -100 et 100 
             dans une liste avant qu'elle soit unique
    """
    compteurEssaies : int

    compteurEssaies = 0

    while compteurEssaies == 0 or not outils.estUnEnsemble(listeAleatoire) : # tant que la liste n'est pas un ensemble
        listeAleatoire = genererListeValeurEntierAleatoire(nombre, borneMin, borneMax)
        compteurEssaies += 1

    return listeAleatoire, compteurEssaies

def calculProba(liste : list[int]) -> float :
    """
    Entrée : Une liste de valeurs entières représentant des compteurs d'essaies avant d'avoir une liste unique.
    Sortie : Probabilité d'avoir des élements en doublons entre les listes.
    """
    valeur : int
    somme : float
    moyenneEssaies : float
    probaListeUnique : float
    probaDoublons : float

    somme = 0.0
    for valeur in liste :
        somme = somme + float(valeur)
    
    moyenneEssaies = somme / len(liste)

    probaListeUnique = 1.0 / moyenneEssaies

    probaDoublons = 1.0 - probaListeUnique

    return probaDoublons

def boucleEssaies(nbIteration : int, nombre : int, borneMin : int, borneMax : int) -> list[int] :
    """
    Fonction qui boucle nbIteration fois sur la fonction cbEssaies.
    Entrée : Nombre d'itération voulu.
             Nombre entier qui est le nombre de valeur aléatoire généré puis mis dans la liste.
             BorneMin est la borne minimal du nombre random.
             BorneMax est la borne maximal du nombre random.
    Sortie : Une liste de valeur de compteur d'essaies (entier).
    """
    listeCompteurEssaies : list[int]
    iterateur : int
    compteur : int
    liste : int

    listeCompteurEssaies = []

    for iterateur in range(nbIteration) :
        liste, compteur = genereListeEntierAleatoireUnique(nombre, borneMin, borneMax)
        listeCompteurEssaies.append(compteur)
    
    return listeCompteurEssaies
