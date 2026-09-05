from random import randint

def tropBasOuHaut(nbDevine : int, nbRandom : int):
    """
    Cette fonction test si le nombre que l'utilisateur devine est trop grand que celui qu'il doit deviné ou trop petit.
    """
    if nbDevine < nbRandom:
        print("Oups, trop bas !")
    elif nbDevine > nbRandom:
        print("Oups, trop haut !")

def main():
    nombreDevine : int
    nbRandomise : int
    iterateur : int

    print("Jeu de devine nombre !")
    nbRandomise = randint(1,10)
    iterateur = 0
    while iterateur <= 10:
        nombreDevine = int(input("Devine le nombre entre 1 et 10 : "))
        iterateur += 1
        tropBasOuHaut(nombreDevine, nbRandomise)
        if nombreDevine == nbRandomise:
            iterateur = 11
            print("Bravo, gagné en un coup !")
        elif nombreDevine < 1 or nombreDevine > 10:
            print("Valeur saisie en dehors de l'intervalle. Perdu d'avance !")
            iterateur = 11