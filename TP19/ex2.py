import outils
from random import randint
from typing import Optional
import tracemalloc

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

    # Variables pour la moyenne
    cumulMemoire = 0
    nbMesures = 0

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

        # Mémoire : 
        current, _ = tracemalloc.get_traced_memory()
        cumulMemoire += current
        nbMesures += 1

    # Pour la dernière valeur
    valeurPrecedente = randint(valeurPrecedente, monMaxi)
    chaine1.valeur = valeurPrecedente
    chaine1.suivant = None

    # Affichage de la moyenne calculée
    if nbMesures > 0:
        moyenne = cumulMemoire / nbMesures
        print(f"[Liste Chainée] Mémoire Moyenne estimée : {moyenne} Ko")

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

    # Variables pour la moyenne
    cumulMemoire = 0

    valeur = randint(-monMaxi, monMaxi)
    for iterateur in range(taille):
        
        listeAleatoire.append(valeur)
        valeur = randint(valeur, monMaxi)

        # Mémoire : 
        current, _ = tracemalloc.get_traced_memory()
        cumulMemoire += current
    
    # Affichage de la moyenne calculée
    if taille > 0:
        moyenne = cumulMemoire / taille
        print(f"[Tableau Simple] Mémoire Moyenne estimée : {moyenne} Ko")

    return listeAleatoire


def main():
    message : str
    nombre : int
    maxi : int

    message = "Saisissez une valeur entière supérieur ou égale à 10 : "

    nombre = outils.saisieEntier(message, "Erreur." + message, 10)

    message = "Saisissez une valeur entière supérieur ou égale à 1000 : "
    maxi = outils.saisieEntier(message, "Erreur" + message, 1000)
    print()
    tracemalloc.start()
    creerTableauAleatoire(nombre, maxi)
    _, maxA = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print()
    tracemalloc.start()
    creerChaineAleatoire(nombre, maxi)
    _, maxB = tracemalloc.get_traced_memory()
    
    tracemalloc.stop()
    print()
    print(f"[Tableau Simple] PIC (Max) : {maxA} Ko")
    print()
    print(f"[Liste Chainée]  PIC (Max) : {maxB} Ko")