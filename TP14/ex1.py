def main():
    valeur : int
    liste : list[int]

    print("j'ai pas trop avancé sur ce TP donc y'a pas grand chose")
    valeur = int(input("Saisissez 1 pour tri bulles, 2 pour insertion et 3 selection"))
    liste = list(input("Saisissez votre liste"))
    match valeur:
        case 1:
            print(tri_bulle(liste))
        case 2:
            print(tri_insertion(liste))
        case 3:
            print(tri_selection(liste))
        case _ :
            print("pas bon")


def tri_bulle(tableau):
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        for en_cours in range(0, len(tableau) - passage):
            if tableau[en_cours] > tableau[en_cours + 1]:
                permutation = True
                # On echange les deux elements
                tableau[en_cours], tableau[en_cours + 1] = \
                tableau[en_cours + 1],tableau[en_cours]
    return tableau  


def tri_insertion(tableau):
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        #décalage des éléments du tableau }
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
        #on insère l'élément à sa place
        tableau[j]=en_cours

def tri_selection(tableau):
    nb = len(tableau)
    for en_cours in range(0,nb):    
        plus_petit = en_cours
        for j in range(en_cours+1,nb) :
            if tableau[j] < tableau[plus_petit] :
                plus_petit = j
        if min is not en_cours :
            temp = tableau[en_cours]
            tableau[en_cours] = tableau[plus_petit]
            tableau[plus_petit] = temp

