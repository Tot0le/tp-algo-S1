def main():
    """
    Conversion base 10 en binaire <0 et > 15
    """
    b0 : int
    b1 : int
    b2 : int
    b3 : int
    N : int

    # saisie de l'utilisateur
    N = int(input("Saisir votre nombre N : "))

    if N < 0 or N > 15 : # vérification du nombre saisie
        print("Nombre trop grand ou trop petit, veuillez saisir un nombre entre 0 et 15.")
    else:

        # traite le bit de rang 3
        if N >= 8 :
            b3 = 1
            N = N - 8
        else:
            b3 = 0

        # traite le bit de rang 2
        if N >= 4 :
            b2 = 1
            N = N - 4
        else:
            b2 = 0
        
        # traite le bit de rang 1
        if N >= 2 :
            b1 = 1
            N = N - 2
        else:
            b1 = 0

        # traite le bit de rang 0
        if N >= 1 :
            b0 = 1
            N = N - 1
        else:
            b0 = 0

        # affiche le nombre en binaire :
        print(str(b3) + str(b2) + str(b1) + str(b0))