import outils
from random import randint
from typing import Optional

class MaillonStockeEntier:
    valeur : int
    suivant : Optional["MaillonStockeEntier"]

class ListeChaineeEntier:
    tete : MaillonStockeEntier

def creerChaineAleatoire(taille : int, monMaxi : int) -> ListeChaineeEntier:
    maListeChainee : ListeChaineeEntier = ListeChaineeEntier()
    chaine1 : MaillonStockeEntier = MaillonStockeEntier()
    chaine2 : MaillonStockeEntier
    valeurPrecedente : int
    iterateur : int

    # Pour la première valeur
    valeurPrecedente = randint(-monMaxi, monMaxi)
    chaine1.valeur = valeurPrecedente
    chaine2 = MaillonStockeEntier()
    chaine1.suivant = chaine2
    maListeChainee.tete = chaine1
    chaine1 = chaine2

    # Pour les autres valeurs : 
    for iterateur in range(taille-2):
        valeurPrecedente = randint(valeurPrecedente, monMaxi)
        chaine1.valeur = valeurPrecedente
        chaine2 = MaillonStockeEntier()
        chaine1.suivant = chaine2
        chaine1 = chaine2

    # Pour la dernière valeur
    valeurPrecedente = randint(valeurPrecedente, monMaxi)
    chaine1.valeur = valeurPrecedente
    chaine1.suivant = None


    return maListeChainee

def creerChaine(listeValeur : list[int]) -> ListeChaineeEntier:
    """
    Crée une liste chainée avec les valeurs qui sans dans la liste en entrée.
    """
    maListeChainee : ListeChaineeEntier = ListeChaineeEntier()
    chaine1 : MaillonStockeEntier = MaillonStockeEntier()
    chaine2 : MaillonStockeEntier
    iterateur : int

    # Pour la première valeur
    chaine1.valeur = listeValeur[0]
    chaine2 = MaillonStockeEntier()
    chaine1.suivant = chaine2
    maListeChainee.tete = chaine1
    chaine1 = chaine2

    # Pour les autres valeurs : 
    for iterateur in range(1, len(listeValeur)-1):

        chaine1.valeur = listeValeur[iterateur]
        chaine2 = MaillonStockeEntier()
        chaine1.suivant = chaine2
        chaine1 = chaine2

    # Pour la dernière valeur
    valeurPrecedente = listeValeur[len(listeValeur)-1]
    chaine1.valeur = valeurPrecedente
    chaine1.suivant = None


    return maListeChainee

def afficherListeChainee(liste : ListeChaineeEntier) -> None:
    elementTemporaire : MaillonStockeEntier

    elementTemporaire = liste.tete
    print("Liste chainée : ")
    while elementTemporaire.suivant != None:
        print(elementTemporaire.valeur, end=", ")
        elementTemporaire = elementTemporaire.suivant
    print(elementTemporaire.valeur)

def creerTableauAleatoire(taille : int, monMaxi : int) -> list[int]:
    listeAleatoire : list[int] = []
    iterateur : int
    valeur : int

    valeur = randint(-monMaxi, monMaxi)
    for iterateur in range(taille):
        
        listeAleatoire.append(valeur)
        valeur = randint(valeur, monMaxi)

    return listeAleatoire


def main():
    message : str
    nombre : int
    maxi : int

    message = "Saisissez une valeur entière supérieur ou égale à 10 : "

    nombre = outils.saisieEntier(message, "Erreur." + message, 10)

    message = "Saisissez une valeur entière supérieur ou égale à 1000 : "
    maxi = outils.saisieEntier(message, "Erreur" + message, 1000)


    print(creerTableauAleatoire(nombre, maxi))
    afficherListeChainee(creerChaineAleatoire(nombre, maxi))
    