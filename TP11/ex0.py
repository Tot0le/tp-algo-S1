import outils
import constante

def main():
    hauteur : int
    indexLigne : int
    affichageFinal : str

    hauteur = outils.saisieEntier("Saisissez la hauteur de la pyramide : ", "Saisie incorrecte, veuillez saisir la hauteur de la pyramide : ", 1, constante.MAXINT, True, True)
    affichageFinal = ""
    
    for indexLigne in range(1, hauteur + 1) :
        affichageFinal = affichageFinal + "\n" + mkLignePyramide(indexLigne, hauteur)

    print(affichageFinal)

def mkLignePyramide(indexRang : int, hauteur : int) -> str :
    ligne : str
    nbEtoiles : int
    nbEspaces : int
    i : int

    nbEtoiles = indexRang * 2 - 1
    nbEspaces = (hauteur - indexRang) * 2
    ligne = ""

    for i in range(nbEspaces):
        ligne = " " + ligne
    
    for i in range(nbEtoiles):
        ligne = ligne + "*" + " "
    
    return ligne