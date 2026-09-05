# =================================================================
#
# Code support du TP chaine d'entiers
# 
# Non redistibuable en dehors du Département Informatique de l'IUT
#
# =================================================================

from typing import Optional

# structure de maillon
class Maillon:
    data: int
    suivant: Optional["Maillon"]

# structure de liste
class ListeChainee:
    tete: Optional[Maillon]


def longueur(liste: ListeChainee) -> int:
    """
    Renvoie le nombre de chaine d'une liste chainée
    
    
    
    Parameters:
        liste (ListeChainee): liste chainée
    
    Returns:
        taille: la taille de la liste chainée (le nombre de chaine)
    """
    now : Maillon
    compteur : int = 0

    if liste.tete is not None:
        now = liste.tete

        while now.suivant is not None:
            compteur += 1
            now = now.suivant
    
    return compteur +1
   

def afficherListeChainee(liste: ListeChainee) -> None:
    """Fonction qui affiche les éléments de la liste

    Dans cette version, chaque élément est affiché sur une ligne

    Args:
        li (ListeChainee): la liste que l'on veut afficher
    """
    courant : Maillon | None

    courant = liste.tete
    while(courant):
        print(courant.data)
        courant = courant.suivant


def ajouterEnQueue(liste: ListeChainee, valeur: int) -> ListeChainee:
    """
    Fonction qui renvoie la liste Chainée en entrée avec l'element en entrée à la fin de la liste chainée.
    """
    maillon : Maillon
    now : Maillon

    maillon = Maillon()
    maillon.data = valeur
    maillon.suivant = None
    if liste.tete is not None:
        now = liste.tete

        while now.suivant != None:
            now = now.suivant
        
        now.suivant = maillon
    else:
        liste.tete = maillon

    return liste



def ajouterEnTete(liste: ListeChainee, valeur: int) -> ListeChainee:
    """
    Fonction qui renvoie la liste Chainée en entrée avec l'element en entrée au début de la liste chainée.
    """
    maillon : Maillon

    maillon = Maillon()
    maillon.data = valeur
    maillon.suivant = liste.tete
    liste.tete = maillon

    return liste



def ajouterEnPos(liste: ListeChainee, indice : int, valeur: int) -> ListeChainee:
    """
    Fonction ajoutant la valeur à la position de l'indice en entrée.
    
    
    
    Parameters:
        liste (ListeChainee): liste chainée
        indice (int): un indice entre 0 et la taille de la listeChainée
        valeur (int): valeur à insérer en tant que data
    
    Returns:
        ListeChainee: la liste chainée d'origine avec la un maillon et une valeur à l'indice
    """
    now : Maillon | None
    maillonAJoute : Maillon
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
            
            maillonAJoute = Maillon()
            maillonAJoute.data = valeur
            maillonAJoute.suivant = now.suivant  # type: ignore
            now.suivant = maillonAJoute  # type: ignore
    else:
        print("Impossible. Indice out of range.")
    
    return liste


def suppTete(liste : ListeChainee):
    """
    Fonction qui enleve l'élement en tete de la liste chainée.
    """
    if liste.tete is not None:
        liste.tete = liste.tete.suivant
        
    return liste


def suppQueue(liste : ListeChainee):
    """
    Fonction qui enlever l'élement à la fin de la liste chainée.
    """
    now : Maillon | None

    if liste.tete is not None:

        if liste.tete.suivant is not None:
            now = liste.tete

            while now.suivant is not None and now.suivant.suivant is not None:
                now = now.suivant
            now.suivant = None
        else:
            liste.tete = None

    return liste



def suppEnPos(liste: ListeChainee, indice : int) -> ListeChainee:
    """
    Fonction supprimant la chaine à la position de l'indice en entrée.
    
    
    
    Parameters:
        liste (ListeChainee): liste chainée
        indice (int): un indice entre 0 et la taille de la listeChainée
    
    Returns:
        ListeChainee: la liste chainée d'origine avec la un maillon et une valeur à l'indice
    """
    now : Maillon | None
    maillonAJoute : Maillon
    compteur : int = 0

    if 0 <= indice <= (longueur(liste)):
        if liste.tete is not None:
            now = liste.tete

            while compteur < indice:
                compteur += 1
                now = now.suivant # type: ignore
        
            now.suivant = now.suivant.suivant
    else:
        print("Impossible. Indice out of range.") # type: ignore
    
    return liste


def rechercher(liste: ListeChainee, valeur : int) -> int :
    """
    Fonction renvoyant l'indice de la valeur qu'on cherche dans une listeChaine si elle existe, -1 sinon
    """
    maillon : Maillon
    now : Maillon
    compteurIndice : int = 0
    resultat : int = -1

    maillon = Maillon()
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


def main():
    boucle : bool = True
    choix : str
    liste : ListeChainee

    liste = ListeChainee()
    liste.tete = None
    while boucle :
        print("Création et Manipulation de Liste Chainée")
        print("1 : créé une nouvelle liste chainée (reset)")
        print("2 : ajouterEnQueue")
        print("3 : ajouterEnTete")
        print("4 : ajouterEnPos")
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
                liste = ListeChainee()
                liste.tete = None
            case "2":
                print()
                valeur = int(input("Saisissez la valeur à ajouter : "))
                ajouterEnQueue(liste, valeur)
                print()
                print("Votre liste chainée : ")
                afficherListeChainee(liste)
            case "3":
                print()
                valeur = int(input("Saisissez la valeur à ajouter : "))
                ajouterEnTete(liste, valeur)
                print()
                print("Votre liste chainée : ")
                afficherListeChainee(liste)
            case "4":
                print()
                valeur = int(input("Saisissez la valeur à ajouter : "))
                pos = int(input("Saisissez la position à ajouter : "))
                ajouterEnPos(liste, pos, valeur)
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


    # ecrire tous les tests / jeux d'essai
    # permettant de mettre en évidence le fonctionnement de la liste
    # ainsi que les cas particuliers (impossible de supprimer un élément 
    # d'une liste vide par exemple)

#     maLC = ajouterEnQueue(maLC, 5)
#     maLC = ajouterEnQueue(maLC, 8)
#     maLC = ajouterEnQueue(maLC, 57)
#     # maLC = ajouterEnTete(maLC, 5)
#     print()
#     afficherListeChainee(maLC)
#     print()
#
#     maLC = (ajouterEnPos(maLC, 2, 3))
#     afficherListeChainee(maLC)
#     print()
#     maLC = ajouterEnPos(maLC, 0, 9)
#     afficherListeChainee(maLC)
#     print()
#
#     maLC = ajouterEnPos(maLC, 2, 7)
#     afficherListeChainee(maLC)
#     print()
#
#     maLC = ajouterEnPos(maLC, 2, 6)
#     afficherListeChainee(maLC)
#     print("Supp tete :")
#     maLC = suppTete(maLC)
#     afficherListeChainee(maLC)
#     print()
#     maLC = suppQueue(maLC)
#     afficherListeChainee(maLC)
#     print()
#
#
#
#
