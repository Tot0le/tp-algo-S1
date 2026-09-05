from outilsMath import estPremier

def afficheNbPos(nombre : int):
    i : int
    ListNbPremierAvantLeNombreN : list

    ListNbPremierAvantLeNombreN = []
    for i in range(nombre):
        if estPremier(i):
            ListNbPremierAvantLeNombreN.append(i)

    return ListNbPremierAvantLeNombreN

def main():
    nb : int
    print("Programme nombre premier.")

    nb = int(input("Saisissez le nombre dont vous souhaitez savoir les nombres premiers entre 0 et lui : "))
    print(afficheNbPos(nb))
