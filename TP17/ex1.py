from typing import TextIO
from outilsAffichage import ALaLigne, pressEnterToContinue

def afficherMot(monfic : TextIO, nombre : int) -> None:
    mot : str
    car : str
    
    mot = ""
    car = monfic.read(1)
    
    while car != "" and car != "/":
        mot = mot + car       
        car = monfic.read(1)  

    for i in range(nombre):
        print(mot, end="")

def main():
    f : TextIO
    monfic : str
    car : str
    nb : int
    fin : bool
    boucle : bool = True
    monfic = input("Saisissez le nom du fichier : ")
    while boucle:
        
        try :
            f = open(monfic, "r")
            boucle = False
        except FileNotFoundError:
            monfic = input("Erreur, saisissez le nom du fichier : ")

    car = f.read(1)
    fin = 0
    while car != "": # si pas EOF
        if car == "/":
            nb = f.read(1)
            if nb != "" and car != "": # si pas EOF
                car = f.read(1)
                if car != "": # si pas EOF
                    match car:
                        case '/' :
                            afficherMot(f,int(nb))
                        case 'n' :
                            ALaLigne(int(nb))
                        case _:
                            fin = 1
                else:
                    fin = 1
            else:
                fin = 1
        else:
            print(car, end="")
        if fin == 1:
            print("Erreur sur le fichier.")
        else:
            car = f.read(1)
    
    f.close()
    print()
    pressEnterToContinue()