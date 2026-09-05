from random import randint
from outilsAffichage import pressEnterToContinue

class couleur:
    RED = "\x1b[91m"
    YELLOW = "\x1b[93m"
    BLUE = "\x1b[34m"
    RESET = "\033[0m"

def compare(nbDevine : int, nbRandom : int, msgWin : str, unIterateur : int, nbTourMax : int) -> int:
    """
    Cette fonction compare si le nombre est tout petit ou trop grand ou égal ou out of range.
    entrée : nbDivine : nombre que l'IA ou le joueur a saisi pour savoir si c'est le bon nombre.
            nbRandom : nombre qu'on doit deviner
            msgWin : le message affiché lorsque cette personne gagne
            unIterateur : iterateur de votre boucle
            nbTourMax : nombre de tour maximal du jeu
    sortie : unIterateur : l'iterateur modifié
    """
    if nbDevine < nbRandom:
        print("Oups, trop bas !")
    elif nbDevine > nbRandom:
        print("Oups, trop haut !")
    elif nbDevine == nbRandom:
        print(couleur.YELLOW + msgWin + couleur.RESET)
        unIterateur = nbTourMax + 1
    elif nbDevine < 1 or nbDevine > 10:
        print(couleur.BLUE + "Valeur saisie en dehors de l'intervalle. Perdu d'avance !" + couleur.RESET)
        unIterateur = nbTourMax + 1
    return unIterateur

def devine(unIterateur) -> int:
    """
    Cette procédure demande à l'utilisateur de deviner un nombre en le saisissant.
    entrée : unIterateur : iterateur de votre boucle
    sortie : nombreDevine : le nombre saisie par l'utilisateur
                unIterateur : votre iterateur modifié
    """
    nombreDevine = int(input(couleur.BLUE + "Devine le nombre entre 1 et 10 : " + couleur.RESET))
    unIterateur += 1
    return nombreDevine, unIterateur

def main():
    """
    Programme principale
    """
    nombreDevine : int
    nbRandomise : int
    iterateur : int
    nombreDevineIA : int
    nombreDeTour : int

    print("Jeu de devine nombre !")
    nbRandomise = randint(1,10)
    iterateur = 0
    nombreDeTour = int(input("Saisissez le nombre de tour que vous voulez : "))

    while iterateur <= nombreDeTour:

        nombreDevine, iterateur = devine(iterateur)
        iterateur = compare(nombreDevine, nbRandomise, f"Bravo, vous avez gagné avant l'IA au tour {iterateur} !", iterateur, nombreDeTour)
        
        if iterateur <= nombreDeTour:
            nombreDevineIA = randint(1,10)
            
            print(couleur.RED + f"L'IA a choisi le nombre : {nombreDevineIA}" + couleur.RESET)

            iterateur = compare(nombreDevineIA, nbRandomise, f"Vous avez perdu, l'IA a deviné le nombre au tour {iterateur} !", iterateur, nombreDeTour)
    pressEnterToContinue()