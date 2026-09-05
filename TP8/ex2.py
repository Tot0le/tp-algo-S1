from random import randint
from outilsAffichage import pressEnterToContinue

class couleur:
    RED = "\x1b[91m"
    YELLOW = "\x1b[93m"
    BLUE = "\x1b[34m"
    RESET = "\033[0m"

def compare(nbDevine : int, nbRandom : int, msgWin : str, unIterateur : int, nbTourMax : int, etat : int) -> int :
    """
    Cette fonction compare si le nombre est tout petit ou trop grand ou égal ou out of range.
    entrée : nbDivine : nombre que l'IA ou le joueur a saisi pour savoir si c'est le bon nombre.
            nbRandom : nombre qu'on doit deviner
            msgWin : le message affiché lorsque cette personne gagne
            unIterateur : iterateur de votre boucle
            nbTourMax : nombre de tour maximal du jeu
    sortie : unIterateur : l'iterateur modifié
            etat : état, si le nombre est trop bas (-1), trop haut(1), égale(0), out(10)
    """
    if nbDevine < nbRandom:
        print("Oups, trop bas !")
        etat = -1
    elif nbDevine > nbRandom:
        print("Oups, trop haut !")
        etat = 1
    elif nbDevine == nbRandom:
        print(couleur.YELLOW + msgWin + couleur.RESET)
        unIterateur = nbTourMax + 1
        etat = 0
    elif nbDevine < 1 or nbDevine > 10:
        print(couleur.BLUE + "Valeur saisie en dehors de l'intervalle. Perdu d'avance !" + couleur.RESET)
        unIterateur = nbTourMax + 1
        etat = 10
    return unIterateur, etat

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

def aleatoireIA(nbMin : int, nbMax : int, monEtat : int, nombreDAvant) -> int :
    nombreDApres : int
    match monEtat :
        case -10: # Si le premier tour n'est pas encore passé
            nombreDApres = randint(nbMin, nbMax)
        case -1: # Si trop bas
            nombreDApres = randint(nombreDAvant+1, nbMax)
        case 1: # Si trop haut
            nombreDApres = randint(nbMin, nombreDAvant-1)
        case _:
            nombreDApres = randint(nbMin, nbMax)
    return nombreDApres

def main():
    """
    Programme principale
    """
    nombreDevine : int
    nbRandomise : int
    iterateur : int
    nombreDevineIA : int
    nombreDeTour : int
    valeurMaxRandom : int
    valeurMinRandom : int
    etat : int
    etatJ1 : int

    print("Jeu de devine nombre !")
    nombreDeTour = int(input("Saisissez le nombre de tour que vous voulez : "))
    valeurMaxRandom = int(input("Saisissez le nombre maximal qu'il faudra deviner (inclus) : "))
    nbRandomise = randint(1,valeurMaxRandom)
    valeurMinRandom = 1
    iterateur = 0
    nombreDevineIA = -10
    etat = 5
    etatJ1 = 5

    while iterateur <= nombreDeTour:
        
        nombreDevine, iterateur = devine(iterateur)
        iterateur, etatJ1 = compare(nombreDevine, nbRandomise, f"Bravo, vous avez gagné avant l'IA au tour {iterateur} !", iterateur, nombreDeTour, etatJ1)
        
        if iterateur <= nombreDeTour:
            nombreDevineIA = aleatoireIA(valeurMinRandom ,valeurMaxRandom, etat, nombreDevineIA)
            
            print(couleur.RED + f"L'IA a choisi le nombre : {nombreDevineIA}" + couleur.RESET)

            iterateur, etat = compare(nombreDevineIA, nbRandomise, f"Vous avez perdu, l'IA a deviné le nombre au tour {iterateur} !", iterateur, nombreDeTour, etat)
    pressEnterToContinue()