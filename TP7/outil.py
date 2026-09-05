import constante
def saisieFloat(message : str, msgErreur : str, borneMin : float, borneMax : float = constante.MAXFLOAT, MinInclus : bool = True, MaxInclus : bool = True):
    """
    Demande à l'utilisateur de saisir une valeur réel.
    """
    valeur : float

    valeur = float(input(message))

    verifFloat(valeur, msgErreur, borneMin, borneMax, MinInclus, MaxInclus)

    return valeur

def verifFloat(valeur : float, msgErreur : str, borneMin : float, borneMax : float, MinInclus: bool, MaxInclus: bool):
    """
    Verifie si un reel est bien dans un intervale donne.
    """
    # les if gere si les valeurs en bornes sont inclus ou non
    if MinInclus and MaxInclus:
        while valeur < borneMin or valeur > borneMax:
            valeur = float(input(msgErreur))

    elif not MinInclus and MaxInclus:
        while valeur <= borneMin or valeur > borneMax:
            valeur = float(input(msgErreur))

    elif MinInclus and not MaxInclus:
        while valeur < borneMin or valeur >= borneMax:
            valeur = float(input(msgErreur))
    
    else:
        while valeur <= borneMin or valeur >= borneMax:
            valeur = float(input(msgErreur))



def saisieStr(listValidChaine : list, message : str, msgErreur : str) -> str:
    """
    Procedure demandant à l'utilisateur de saisir une 
    chaine de caractere, puis qui la verifie avec la 
    procedure verifStrInL.
    """
    chaine : str

    chaine = str(input(message))
    chaine = verifStrInL(chaine, listValidChaine, msgErreur)
    return chaine

def verifStrInL(chaine : str, listValidChaine : list, msgErreur : str) -> str:
    """
    Procedure verifiant si la chaine de caractere saisi est dans 
    les choix possiblent, puis redemandent de saisir a l'infini 
    (tant que c'est mal saisi).
    """
    while chaine not in listValidChaine:
        chaine = str(input(msgErreur))
    return chaine
