from TP19.ex1 import ListeChaineeEntier, MaillonStockeEntier, creerChaine, afficherListeChainee, creerTableauAleatoire
from time import time
from outils import saisieEntier

def enleverIndiceDeListe(liste : list[int], index : int) -> list[int]:
    """
    Fonction renvoie la liste sans l'element de l'index donné en entrée.
    """
    if 0 <= index < len(liste) :
        liste.pop(index)
    return liste

def enleverIndiceDeListeChaine(listeChainee : ListeChaineeEntier, index : int) -> ListeChaineeEntier:
    """
    Fonction renvoie la liste chainée sans l'element de l'index donné en entrée.
    """
    now : MaillonStockeEntier

    now = listeChainee.tete
    for i in range(index - 1):
        now = now.suivant
    now.suivant = now.suivant.suivant
    return listeChainee


def main():
    liste : list[int]
    listeModif : list[int]
    taille : int
    indice : int
    chaine : ListeChaineeEntier
    temps : float

    print("Vous allez saisir une taille de liste qui va créer une liste aléatoire puis qui va ensuite être converti en liste chainée, " \
    "puis on va comparer le temps que ça prend d'enlever un element à une liste chainée et à une liste simple pour les comparer.")

    # Saisie de la liste
    taille = saisieEntier("Saisissez la taille de la liste : ", "Erreur, veuillez saisir la taille de la liste", 0)
    liste = creerTableauAleatoire(taille, 100000)

    # saisie de l'indice à enlever
    indice = int(input("Saisissez un indice qu'on va enlever à la liste : "))

    # Affichage de la liste de base
    # print(f"La liste saisie : {liste}")

    # Enlever l'element dans la liste + calcul du temps
    temps = time()
    listeModif = enleverIndiceDeListe(liste, indice)
    temps = temps - time()

    # Affichage liste modifié et temps
    # print(f"La liste sans l'indice {indice} : {listeModif}")
    print(f"Ça a pris {temps} d'enlever l'indice dans la liste Classique")

    # Création de la chaine
    chaine = creerChaine(liste)
    
    # afficher la liste chainée
    # afficherListeChainee(chaine)

    # enlever un indice de la liste chainée : 
    temps = time()
    chaine = enleverIndiceDeListeChaine(chaine, indice)
    temps = temps - time()

    # Affichage de la liste chainée et du temps : 
    # afficherListeChainee(chaine)
    print(f"Ça a pris {temps} d'enlever l'indice dans la liste Chainée")
