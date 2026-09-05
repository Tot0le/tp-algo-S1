# =================================================================
#
# Code support du TP chaine d'entiers
# 
# Non redistibuable en dehors du Département Informatique de l'IUT
#
# =================================================================

from typing import Optional

# structure de maillon
class MaillonDoubleDouble:
    data: int
    suivant: Optional["MaillonDoubleDouble"]
    precedent : Optional["MaillonDoubleDouble"]

# structure de liste
class ListeDoubleChainee:
    tete: Optional[MaillonDoubleDouble]


def longueur(liste: ListeDoubleChainee) -> int:
    """
    Renvoie le nombre de chaine d'une liste chainée



    Parameters:
        liste (ListeChainee): liste chainée

    Returns:
        taille: la taille de la liste chainée (le nombre de chaine)
    """
    now : MaillonDoubleDouble
    compteur : int = 0

    if liste.tete is not None:
        now = liste.tete

        while now.suivant is not None:
            compteur += 1
            now = now.suivant

    return compteur +1
   

def afficheLC(liste: ListeDoubleChainee):
    """Fonction qui affiche les éléments de la liste

    Dans cette version, chaque élément est affiché sur une ligne

    Args:
        li (ListeChainee): la liste que l'on veut afficher
    """
    courant = liste.tete
    while(courant):
        print(courant.data)
        courant = courant.suivant


def ajoutQueue(liste: ListeDoubleChainee, valeur: int):
    """
    Fonction qui renvoie la liste Chainée double en entrée avec l'element en entrée à la fin de la liste chainée.
    """
    maillon : MaillonDouble
    now : MaillonDouble

    maillon = MaillonDouble()
    maillon.data = valeur
    maillon.suivant = None
    if liste.tete is not None:
        now = liste.tete

        while now.suivant != None:
            now = now.suivant

        now.suivant = maillon
        now.suivant.precedent = now
    else:
        liste.tete = maillon

    return liste


def ajoutTete(liste: ListeDoubleChainee, valeur: int):
    """
    Fonction qui renvoie la liste Chainée double en entrée avec l'element en entrée au début de la liste chainée double.
    """
    newMaillonDouble : MaillonDouble

    newMaillonDouble = MaillonDouble()
    newMaillonDouble.data = valeur
    newMaillonDouble.suivant = liste.tete
    liste.tete = newMaillonDouble
    liste.tete.precedent = None
    liste.tete.suivant.precedent = newMaillonDouble

    return liste


def ajoutEnPos(liste: ListeDoubleChainee, indice : int, valeur: int):
    """
    Fonction ajoutant la valeur à la position de l'indice en entrée.



    Parameters:
        liste (ListeChainee): liste chainée
        indice (int): un indice entre 0 et la taille de la listeChainée
        valeur (int): valeur à insérer en tant que data

    Returns:
        ListeChainee: la liste chainée d'origine avec la un maillon et une valeur à l'indice
    """
    now : MaillonDouble | None
    maillonAJoute : MaillonDouble
    compteur : int = 0

    if 0 <= indice <= longueur(liste):

        if indice == 0:
            ajouterEnTete(liste, valeur)
        else:
            if liste.tete is not None:
                now = liste.tete

                while compteur < indice - 1:
                    compteur += 1
                    now = now.suivant # type: ignore

            maillonAJoute = MaillonDouble()
            maillonAJoute.data = valeur
            maillonAJoute.suivant = now.suivant  # type: ignore
            now.suivant = maillonAJoute  # type: ignore
            now.suivant.precedent = now
    else:
        print("Impossible. Indice out of range.")

    return liste


def suppTete(liste : ListeDoubleChainee):
    """
    Fonction qui enleve l'élement en tete de la liste chainée double.
    """
    if liste.tete is not None:
        liste.tete = liste.tete.suivant
        liste.tete.precedent = None

    return liste


def suppQueue(liste : ListeDoubleChainee):
    """
    Fonction qui enlever l'élement à la fin de la liste chainée double.
    """
    now : MaillonDouble | None

    if liste.tete is not None:

        if liste.tete.suivant is not None:
            now = liste.tete

            while now.suivant is not None and now.suivant.suivant is not None:
                now = now.suivant
            now.suivant.suivant.precedent = None
            now.suivant = None
        else:
            liste.tete = None

    return liste


def suppEnPos(liste: ListeDoubleChainee, indice : int):
    """
    Fonction supprimant la chaine à la position de l'indice en entrée.



    Parameters:
        liste (ListeChainee): liste chainée
        indice (int): un indice entre 0 et la taille de la listeChainée

    Returns:
        ListeChainee: la liste chainée d'origine avec la un maillon et une valeur à l'indice
    """
    now : MaillonDouble | None
    maillonAJoute : MaillonDouble
    compteur : int = 0

    if 0 <= indice <= (longueur(liste)):
        if liste.tete is not None:
            now = liste.tete

            while compteur < indice:
                compteur += 1
                now = now.suivant # type: ignore

            now.suivant = now.suivant.suivant
            now.suivant.precedent = now
    else:
        print("Impossible. Indice out of range.") # type: ignore

    return liste


def recherche(liste: ListeDoubleChainee, valeur : int) -> int :
    """
    Fonction renvoyant l'indice de la valeur qu'on cherche dans une listeChaine double si elle existe, -1 sinon
    """
    maillon : MaillonDouble
    now : MaillonDouble
    compteurIndice : int = 0
    resultat : int = -1

    maillon = MaillonDouble()
    maillon.data = valeur
    maillon.suivant = None
    if liste.tete is not None:
        now = liste.tete

        while now.suivant != None and now.data != valeur:
            compteurIndice += 1
            now = now.suivant
            if now.data == valeur:
                resultat = compteurIndice


    else:
        liste.tete = maillon

    return resultat


if __name__=="__main__" :
    maLDC = ListeDoubleChainee()
    maLDC.tete = None
    # ecrire tous les tests / jeux d'essai
    # permettant de mettre en évidence le fonctionnement de la liste
    # ainsi que les cas particuliers (impossible de supprimer un élément 
    # d'une liste vide par exemple)
    boucle : bool = True
    choix : str
    liste : ListeDoubleChainee

    liste = ListeDoubleChainee()
    liste.tete = None
    while boucle :
        print("Création et Manipulation de Liste Chainée")
        print("1 : créé une nouvelle liste chainée double (reset)")
        print("2 : ajoutQueue")
        print("3 : ajoutTete")
        print("4 : ajoutEnPos")
        print("5 : suppQueue")
        print("6 : suppTete")
        print("7 : suppEnPos")
        print("8 : afficher liste actuelle")
        print("9 : rechercher")
        print("10 : retour")

        print()
        choix = input("Votre choix :")

        match choix:
            case "1":
                liste = ListeDoubleChainee()
                liste.tete = None
            case "2":
                print()
                valeur = int(input("Saisissez la valeur à ajouter : "))
                ajoutQueue(liste, valeur)
                print()
                print("Votre liste chainée : ")
                afficherListeChainee(liste)
            case "3":
                print()
                valeur = int(input("Saisissez la valeur à ajouter : "))
                ajoutTete(liste, valeur)
                print()
                print("Votre liste chainée : ")
                afficherListeChainee(liste)
            case "4":
                print()
                valeur = int(input("Saisissez la valeur à ajouter : "))
                pos = int(input("Saisissez la position à ajouter : "))
                ajoutEnPos(liste, pos, valeur)
                print()
                print("Votre liste chainée : ")
                afficherListeChainee(liste)
            case "5":
                print()
                suppQueue(liste)
                print()
                print("Votre liste chainée : ")
                afficherListeChainee(liste)
            case "6":
                print()
                suppTete(liste)
                print()
                print("Votre liste chainée : ")
                afficherListeChainee(liste)
            case "7":
                print()
                pos = int(input("Saisissez la position à supprimer : "))
                suppEnPos(liste, pos)
                print()
                print("Votre liste chainée : ")
                afficherListeChainee(liste)
            case "8":
                print()
                print("Votre liste chainée : ")
                afficherListeChainee(liste)
            case "9":
                print()
                valeur = int(input("Quel valeur voulez vous rechercher ?"))
                indice = rechercher(liste, valeur)
                if indice != -1:
                    print(f"Valeur {valeur} trouvé à l'indice {indice}.")
            case "10":
                print("retour")
                boucle = False
            case _:
                print("Entrez une valeur entre 1 et 10.")

