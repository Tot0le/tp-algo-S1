from TP19.ex1 import ListeChaineeEntier, MaillonStockeEntier, creerChaine, afficherListeChainee, creerTableauAleatoire
from time import time
from outils import saisieEntier

def rajoutEnTeteListeChainee(listeChainee : ListeChaineeEntier, element : int) -> ListeChaineeEntier:
    """
    Fonction qui renvoie la liste Chainée en entrée avec l'element en entrée au début de la liste chainée.
    """
    maillon : MaillonStockeEntier

    maillon = MaillonStockeEntier()
    maillon.valeur = element
    maillon.suivant = listeChainee.tete
    listeChainee.tete = maillon

    return listeChainee

def enleverEnTeteListeChainee(listeChainee : ListeChaineeEntier) -> ListeChaineeEntier:
    """
    Fonction qui enleve l'élement en tete de la liste chainée.
    """
    listeChainee.tete = listeChainee.tete.suivant
    return listeChainee

def rajoutFinListeChainee(listeChainee : ListeChaineeEntier, element : int) -> ListeChaineeEntier:
    """
    Fonction qui renvoie la liste Chainée en entrée avec l'element en entrée à la fin de la liste chainée.
    """
    maillon : MaillonStockeEntier
    now : MaillonStockeEntier

    maillon = MaillonStockeEntier()
    maillon.valeur = element
    maillon.suivant = None
    now = listeChainee.tete

    while now.suivant != None:
        now = now.suivant
    
    now.suivant = maillon

    return listeChainee

def enleverFinListeChainee(listeChainee : ListeChaineeEntier) -> ListeChaineeEntier:
    """
    Fonction qui enlever l'élement à la fin de la liste chainée.
    """
    now : MaillonStockeEntier

    now = listeChainee.tete

    while now.suivant.suivant != None:
        now = now.suivant
    
    now.suivant = None

    return listeChainee

def rajoutEnTeteListe(liste : list[int], element : int) -> list[int] :
    """
    Fonction qui renvoie la liste en entrée avec l'element en entrée au début de la liste.
    """
    liste.insert(0, element)
    return liste

def enleverEnTeteListe(liste : list) -> list :
    """
    Fonction qui enleve l'élement en tete de la liste.
    """
    liste.pop(0)
    return liste

def rajoutFinListe(liste : list, element : int) -> list :
    """
    Fonction qui renvoie la liste en entrée avec l'element en entrée à la fin de la liste.
    """
    liste.append(element)
    return liste

def enleverDernierElement(liste : list) -> list:
    """
    Fonction qui enlever l'élement à la fin de la liste.
    """
    liste.pop(len(liste) -1)
    return liste

def main():
    # Saisie de la liste
    taille = saisieEntier("Saisissez la taille de la liste : ", "Erreur, veuillez resaisir la taille de la liste : ", 1)
    liste = creerTableauAleatoire(taille, 100000)

    # Liste classique
    print()
    print()
    print("Liste classique : ")
    temps = time()
    rajoutEnTeteListe(liste, 5)
    temps = temps - time()

    print(f"rajoutEnTeteListe : {temps} secondes")

    temps = time()
    enleverEnTeteListe(liste)
    temps = temps - time()

    print(f"enleverEnTeteListe : {temps} secondes")

    temps = time()
    rajoutFinListe(liste, 5)
    temps = temps - time()

    print(f"rajoutFinListe : {temps} secondes")

    temps = time()
    enleverDernierElement(liste)
    temps = temps - time()

    print(f"enleverDernierElement : {temps} secondes")

    ##### LISTE CHAINEE #####
    # Création de la chaine
    print()
    print("Liste chainée : ")

    chaine = creerChaine(liste)

    temps = time()
    rajoutEnTeteListeChainee(chaine, 5)
    temps = temps - time()

    print(f"rajoutEnTeteListeChainee : {temps} secondes")

    temps = time()
    enleverEnTeteListeChainee(chaine)
    temps = temps - time()

    print(f"enleverEnTeteListeChainee : {temps} secondes")

    temps = time()
    rajoutFinListeChainee(chaine, 5)
    temps = temps - time()

    print(f"rajoutFinListeChainee : {temps} secondes")

    temps = time()
    enleverFinListeChainee(chaine)
    temps = temps - time()

    print(f"enleverFinListeChainee : {temps} secondes")
