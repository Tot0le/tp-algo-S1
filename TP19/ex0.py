import outils
from random import randint

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

