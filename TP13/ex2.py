from random import randint
from outils import genererListeValeurEntierAleatoire
from outilsAffichage import pressEnterToContinue

def trieSpecial(tableauCent : list[int]) -> list[int] :
    tab_final : list[int]
    tab_pair : list[int]
    tab_impair : list[int]
    compteur_zeros : int
    i : int

    tab_pair = []
    tab_impair = []
    tab_final = []
    compteur_zeros = 0
    for i in range(0,len(tableauCent)):
        if tableauCent[i] % 2 == 0:
            if tableauCent[i] == 0:
                compteur_zeros += 1
            else:
                tab_pair.append(tableauCent[i])
        else :
            tab_impair.append(tableauCent[i])
    
    # TRIE DES TABLEAUX
    tab_pair.sort()
    reversed(tab_pair)
    tab_impair.sort()
    print(tab_pair)
    # ITERATION POUR RAJOUT DANS LE TABLEAU FINAL
    for i in range(0, len(tab_pair)):
        tab_final.append(tab_pair[i])
    for i in range(compteur_zeros):
        tab_final.append(0)
    for i in range(len(tab_impair)):
        tab_final.append(tab_impair[i])
    return tab_final

def main():
    listeAleatoire : list[int]

    listeAleatoire = genererListeValeurEntierAleatoire(500,-10,10)
    print(trieSpecial(listeAleatoire))
    pressEnterToContinue()