def compterNombreVoyelle(voyelle : str, monMot : str):
    """
    Fonction qui compte le nombre de fois que la voyelle est dans le mot.
    """
    compteur : int = 0
    caractere : str

    for caractere in monMot:
        if caractere == voyelle:
            compteur += 1
    
    return compteur

def estPalindrome(monMot : str) -> bool:
    """
    Fonction qui retourne vrai si le mot en entrée est un palindrome.
    """
    resultat : bool

    resultat = True

    for indice in range(1, len(monMot) + 1) :
        if monMot[indice - 1] != monMot[-(indice)]:
            resultat = False
    
    return resultat

def main():
    mot : str
    caractere : str
    listeVoyelles : list[str] = []
    listeValeur : list[int] = []
    i : int
    resultat : str
    voyelles : list[str]
    palindrome : bool
    
    voyelles = ["aeiouyAEIOUY"]

    mot = input("Saisissez votre mot : ")

    resultat = ""

    for caractere in mot:
        if caractere not in listeVoyelles:
            if caractere in voyelles[0]:
                listeVoyelles.append(caractere)
                listeValeur.append(compterNombreVoyelle(caractere, mot))

    for i in range(len(listeValeur)):
        resultat = resultat + (f"«{listeVoyelles[i]}»:{listeValeur[i]};")

    if len(resultat) <= 0 :
        print("Ce mot n'a pas de voyelle")
    else:
        if resultat[-1] == ";":
            resultat = resultat[:-1]
        
    print(resultat)

    palindrome = estPalindrome(mot)

    if palindrome :
        print(f"Le mot {mot} est un palindrome.")
    else:
        print(f"Le mot {mot} n'est pas un palindrome.")
    input("Press enter to continue : ")
