from random import randint
from outilsAffichage import pressEnterToContinue

class couleur:
    RED = "\x1b[91m"
    YELLOW = "\x1b[93m"
    BLUE = "\x1b[34m"
    RESET = "\033[0m"

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
    nbDevineIA : int

    print("Jeu de devine nombre !")
    nbRandomise = randint(1,10)
    iterateur = 0
    while iterateur <= 5:
        nombreDevine = int(input(f"{couleur.BLUE}Devine le nombre entre 1 et 10 : {couleur.RESET}"))
        iterateur += 1
        tropBasOuHaut(nombreDevine, nbRandomise)
        if nombreDevine == nbRandomise:
            print(f"{couleur.YELLOW}Bravo, vous avez gagné avant l'IA au tour {iterateur} !{couleur.RESET}")
            iterateur = 11
            
        elif nombreDevine < 1 or nombreDevine > 10:
            print(f"{couleur.BLUE}Valeur saisie en dehors de l'intervalle. Perdu d'avance !{couleur.RESET}")
            iterateur = 11
        else:

            nombreDevineIA = randint(1,10)
            
            print(f"{couleur.RED}L'IA a choisi le nombre : {nombreDevineIA}{couleur.RESET}")
            tropBasOuHaut(nombreDevineIA, nbRandomise)
            if nombreDevineIA == nbRandomise:
                print(f"{couleur.RED}Vous avez perdu, l'IA a deviné le nombre au tour {iterateur} !{couleur.RESET}")
                iterateur = 11
    pressEnterToContinue()