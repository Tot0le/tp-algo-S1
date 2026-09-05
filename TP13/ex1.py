# IMPORTS
from outils import saisieEntier
from math import sqrt

def main():
    entier1 : int
    entier2 : int

    print("Saisissez a, b et c de : ax² + bx + c = 0.")
    entier1 = saisieEntier("Veuillez saisir a : ", "Erreur de saisie, veuillez saisir a : ")
    entier2 = saisieEntier("Veuillez saisir b : ", "Erreur de saisie, veuillez saisir b : ")
    entier3 = saisieEntier("Veuillez saisir c : ", "Erreur de saisie, veuillez saisir c : ")

    calculEqSecondDegres(entier1, entier2, entier3)
    
def calculEqSecondDegres(a : int, b : int, c : int) -> list[float] | None:

    delta : int
    listResult : list[float]
    
    listResult = []

    if a == b == 0:
        if c == 0:
            print("0 = 0 donc x a pour solution l'ensemble des Réels.")
        else:
            print("Erreur. Equation impossible.")
        return None
    else:
        delta = b**2 - 4 * a * c
        if a == 0 :
                print("C'est aussi une équation de degrès simple.")
                listResult.append(calculEqPremierDegres(b, c))
        else:
            match delta :
                case 0 :
                    listResult.append(calculEqPremierDegres(-b / (2 * a)))
                case _ :
                    if delta > 0 :
                        print(f"x1 = (- {b} - √{delta}) / ({2 * a})")
                        listResult.append((-b - sqrt(delta)) / (2 * a))
                        print(f"x2 = (- {b} + √{delta}) / ({2 * a})")
                        listResult.append((-b + sqrt(delta)) / (2 * a))
                    else:
                        print( "Pas de solution réel pour cette équation.")
    
        return listResult

def calculEqPremierDegres(a : int, b : int) -> int :
    print(f"-{b} / {a}")
    return -b / a

