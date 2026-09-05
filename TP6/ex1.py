from random import randint

def devine(nbDevine : int, nbRandom : int):
    if nbDevine <= 0 or nbDevine > 10 :
        print("Valeur saisie en dehors de l'intervalle. Perdu d'avance !")
    elif nbDevine == nbRandom:
        print("Bravo, gagné en un coup !")
    elif nbDevine < nbRandom:
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
        devine(nombreDevine, nbRandomise)
        if nombreDevine == nbRandomise:
            iterateur = 11