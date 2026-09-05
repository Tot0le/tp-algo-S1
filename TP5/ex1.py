def dmdNbPair():
    nb : int
    nb = int(input("Saisissez un nombre pair : "))

    while nb % 2 == 1:
        nb = int(input("Votre nombre est impair. Saisissez un nombre pair : "))

    print(f"Le nombre {nb} est pair.")

def main():
    dmdNbPair()