from random import randint
from outils import genererListeValeurEntierAleatoire

def main():
    listeRandom : list[int]
    nbElementUnique : int

    listeRandom = genererListeValeurEntierAleatoire(100, 0, 100)

    nbElementUnique = elementUniqueDansListe(listeRandom)
    print(f"Il y a {nbElementUnique} valeurs distinctes dans cette liste.")

def elementUniqueDansListe(liste : list) -> int :
    """
    Fonction renvoyant le nombre de valeur distincte dans la liste en entrée.
    Entrée : liste quelconque
    Sortie : un entier qui représente le nombre de valeur distincte dans la liste
    """
    elementUnique : list
    indiceElement : int
    indiceIteraElement : int
    compteurElementUnique : int

    elementUnique = []
    compteurElementUnique = 0

    for indiceElement in range(len(liste) + 1) : 
        for indiceIteraElement in range(indiceElement + 1, len(liste)) :
            if liste[indiceElement] == liste[indiceIteraElement] and liste[indiceElement] not in elementUnique and liste[indiceIteraElement] not in elementUnique:
                elementUnique.append(liste[indiceElement])
                compteurElementUnique += 1
    
    return compteurElementUnique


# 2. Si on utilise des ensembles on aurait juste à comparer pour trouver