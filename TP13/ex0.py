# IMPORTS
from outils import saisieEntier

def PGCD_Rec(a : int, b : int) -> int:
    """
    Fonction recursive retournant le PGCD entre les deux nombres en entrée a et b POSITIFS. 0 exclus.
    """
    if a == b :
        return a
    elif a > b :
        return PGCD_Rec(a-b, b)
    else:
        return PGCD_Rec(a, b-a)

def PGCD(a : int, b : int) -> int:
    """
    Fonction iterative retournant le PGCD entre les deux nombres en entrée a et b POSITIFS. 0 exclus.
    """
    while a != b :
        if a > b :
            a = a - b
        else:
            b = b - a
    return a

def main():
    entier1 : int
    entier2 : int
    pgcd : int

    print("Vous allez saisir deux entiers positifs pour calculer le PGCD entre ces deux nombres.")
    entier1 = saisieEntier("Veuillez saisir le premier nombre : ", "Erreur de saisie, veuillez saisir le premier nombre POSITIF : ", 1)
    entier2 = saisieEntier("Veuillez saisir le deuxième nombre : ", "Erreur de saisie, veuillez saisir le deuxième nombre POSITIF : ", 1)

    pgcd = PGCD(entier1, entier2)
    print(f"Le PGCD de {entier1} et {entier2} est {pgcd}.")