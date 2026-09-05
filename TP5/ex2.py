def main():
    nb : int
    ListDivise : list
    nbBinaire : str
    nb = int(input("Saisir un nombre en base 10 à convertir : "))

    ListDivise=[]
    while nb > 0:
        ListDivise.insert(0,str(nb % 2))
        nb = nb//2
    nbBinaire = "".join(ListDivise)
    print(nbBinaire)