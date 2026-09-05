import constante
from random import randint

#### SAISIE ####

def convertirType(type_voulu: str, valeur: str, monMessageTypeErreur : str) -> int | float | str | None:
    """
    Fonction qui convertit la 'valeur' (str) en le 'type_voulu' (str: "int", "float", "str")
    et gère les erreurs de conversion.

    Retourne la valeur convertie, ou None si la conversion a échoué.
    """
    
    match type_voulu:
        case "float":
            try:
                return float(valeur)
            except ValueError:
                # Si ça échoue (ex: "Saucisse"), on affiche une erreur et retourne None
                print(f"Erreur : Impossible de convertir la valeur '{valeur}' en float.")
                print(monMessageTypeErreur)
                return None
        
        case "int":
            try:
                return int(valeur)
            except ValueError:
                # Si ça échoue (ex: "10.5" ou "Saucisse"), on affiche une erreur
                print(f"Erreur : Impossible de convertir la valeur '{valeur}' en int.")
                print(monMessageTypeErreur)
                return None
        
        case "str":
            # C'est déjà un string, pas besoin de conversion, pas de risque d'erreur.
            print("Utiliser la fonction saisieStr est mieux.")
            return valeur
        
        case _:
            # Cas où le type_voulu n'est ni "float", "int", ou "str"
            print(f"Erreur : Le type '{type_voulu}' n'est pas géré. (Choix : float, int, str)")
            return None
    
def saisieFloat(message : str = "Veuillez saisir une valeur réel : ", msgErreur : str = "Erreur de saisie, veuillez saisir une valeur réel : ", 
                borneMin : float = constante.MINFLOAT, borneMax : float = constante.MAXFLOAT, MinInclus : bool = True, MaxInclus : bool = True) -> float:
    """
    Demande à l'utilisateur de saisir une valeur réel.

    Entrée : message : le message qui est affiché à la première saisie de l'utilisateur (sans erreur).
             msgErreur : le message qui est affiché lorsque l'utilisateur a saisie une valeur non conforme.
             borneMin : la borne minimale autorisée, float.
             borneMax : la borne maximale autorisée, float.
             MinInclus : booléen qui précise si la valeur borneMin est incluse ou non.
             MaxInclus : booléen qui précise si la valeur borneMax est incluse ou non.
    Sortie : Un nombre réel de type float.
    """
    valeur : float
    valeurStr : str

    valeurStr = str(input(message))
    valeur = convertirType("float", valeurStr, "Veuillez saisir un nombre réel, pas une chaine de caractère.")

    valeur = verifFloat(valeur, msgErreur, borneMin, borneMax, MinInclus, MaxInclus)

    return valeur

def verifFloat(valeur : float, msgErreur : str, borneMin : float, borneMax : float, MinInclus: bool, MaxInclus: bool) -> float:
    """
    Verifie si un reel est bien dans un intervalle donne.

    Entrée : valeur : float représentant une valeur réel.
             msgErreur : le message qui est affiché lorsque l'utilisateur a saisie une valeur non conforme.
             borneMin : la borne minimale autorisée, float.
             borneMax : la borne maximale autorisée, float.
             MinInclus : booléen qui précise si la valeur borneMin est incluse ou non.
             MaxInclus : booléen qui précise si la valeur borneMax est incluse ou non.
    Sortie : float représentant une valeur réel.
    """
    maValeurStr : str
    messageTypeErreur : str

    maValeurStr = str(valeur)

    messageTypeErreur = "Veuillez saisir un nombre réel, pas une chaine de caractère."
    # les if gere si les valeurs en bornes sont inclus ou non
    if MinInclus and MaxInclus:

        while valeur is None or float(maValeurStr) < borneMin or float(maValeurStr) > borneMax :

            maValeurStr = str(input(msgErreur))
            valeur = convertirType("float", maValeurStr, messageTypeErreur)

    elif not MinInclus and MaxInclus:

        while valeur is None or float(maValeurStr) <= borneMin or float(maValeurStr) > borneMax:

            maValeurStr = str(input(msgErreur))
            valeur = convertirType("float", maValeurStr, messageTypeErreur)

    elif MinInclus and not MaxInclus:

        while valeur is None or float(maValeurStr) < borneMin or float(maValeurStr) >= borneMax:

            maValeurStr = str(input(msgErreur))
            valeur = convertirType("float", maValeurStr, messageTypeErreur)
    
    else:
        while valeur is None or float(maValeurStr) <= borneMin or float(maValeurStr) >= borneMax:

            maValeurStr = str(input(msgErreur))
            valeur = convertirType("float", maValeurStr, messageTypeErreur)
    
    return valeur

def saisieEntier(message : str, msgErreur : str, borneMin : int = constante.MININT, borneMax : int = constante.MAXINT, MinInclus : bool = True, MaxInclus : bool = True) -> int:
    """
    Demande à l'utilisateur de saisir une valeur entière.

    Entrée : message : le message qui est affiché à la première saisie de l'utilisateur (sans erreur).
             msgErreur : le message qui est affiché lorsque l'utilisateur a saisie une valeur non conforme.
             borneMin : la borne minimale autorisée, int.
             borneMax : la borne maximale autorisée, int.
             MinInclus : booléen qui précise si la valeur borneMin est incluse ou non.
             MaxInclus : booléen qui précise si la valeur borneMax est incluse ou non.
    Sortie : Un nombre entier de type int. 
    """
    valeur : int
    valeurStr : str

    valeurStr = str(input(message))
    valeur = convertirType("int", valeurStr, "Veuillez saisir un nombre entier, pas une chaine de caractère ni un nombre réel.")

    valeur = verifEntier(valeur, msgErreur, borneMin, borneMax, MinInclus, MaxInclus)

    return valeur

def verifEntier(valeur : int, msgErreur : str, borneMin : int, borneMax : int, MinInclus: bool, MaxInclus: bool) -> int:
    """
    Verifie si un entiere est bien dans un intervalle donne.

    Entrée : valeur :   int représentant une valeur entière.
             msgErreur : le message qui est affiché lorsque l'utilisateur a saisie une valeur non conforme.
             borneMin : la borne minimale autorisée, float.
             borneMax : la borne maximale autorisée, float.
             MinInclus : booléen qui précise si la valeur borneMin est incluse ou non.
             MaxInclus : booléen qui précise si la valeur borneMax est incluse ou non.
    Sortie : int représentant une valeur entière.
    """
    maValeurStr : str
    msgErreurType : str

    maValeurStr = str(valeur)

    msgErreurType = "Veuillez saisir un nombre entier, pas une chaine de caractère ni un nombre réel."
    # les if gere si les valeurs en bornes sont inclus ou non
    if MinInclus and MaxInclus:

        while valeur is None or int(maValeurStr) < borneMin or int(maValeurStr) > borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = convertirType("int", maValeurStr, msgErreurType)

    elif not MinInclus and MaxInclus:

        while valeur is None or int(maValeurStr) <= borneMin or int(maValeurStr) > borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = convertirType("int", maValeurStr, msgErreurType)

    elif MinInclus and not MaxInclus:

        while valeur is None or int(maValeurStr) < borneMin or int(maValeurStr) >= borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = convertirType("int", maValeurStr, msgErreurType)
    
    else:

        while valeur is None or int(maValeurStr) <= borneMin or int(maValeurStr) >= borneMax:
            maValeurStr = str(input(msgErreur))
            valeur = convertirType("int", maValeurStr, msgErreurType)
    
    return valeur

def saisieStr(listValidChaine : list[str], message : str, msgErreur : str) -> str:
    """
    Procedure demandant à l'utilisateur de saisir une 
    chaine de caractere, puis qui la verifie avec la 
    procedure verifStrInL.

    Entrée : listValidChaine : liste de chaine de caractère qui représente les choix de saisie possible.
             message : le message qui est affiché à la première saisie de l'utilisateur (sans erreur).
             msgErreur : le message qui est affiché lorsque l'utilisateur a saisie une valeur non conforme.
    Sortie : chaine de caractère conforme (inclus dans listValidChaine)
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

    Entrée : chaine de caractère
             listValidChaine : liste de chaine de caractère qui représente les choix de saisie possible.
             msgErreur : le message qui est affiché lorsque l'utilisateur a saisie une valeur non conforme.
    Sortie : Sortie : chaine de caractère conforme (inclus dans listValidChaine)
    """
    while chaine not in listValidChaine:
        chaine = str(input(msgErreur))
    return chaine

def saisieYesOrNO(message : str) -> bool:
    """
    Fontion demandant oui ou non à l'utilisateur, renvoie True si il a tapé oui OU Oui OU OUI OU yes OU Yes OU y OU Y
    Entrée : message affiché à la demande du oui ou non
    Sortie : booléen enAccord
    """
    enAccord : bool
    aRepondu : bool
    reponse : str
    listReponseVrai : list[str]
    listReponseFaux : list[str]

    listReponseVrai = ["oui", "Oui", "OUI", "yes", "Yes", "y", "Y"]
    listReponseFaux = ["non", "Non", "NON", "no", "No", "n", "N"]
    aRepondu = False

    reponse = input(message)
    while not aRepondu :

        if reponse in listReponseVrai :
            enAccord = True
            aRepondu = True

        elif reponse in listReponseFaux :
            enAccord = False
            aRepondu = True

        else:
            print(f"Saisie incorrect, choix accepté : \n {listReponseVrai} \n {listReponseFaux}")
            reponse = input(message)
    
    return enAccord


#### LISTES ####

def genererListeValeurEntierAleatoire(nombre : int, borneMin : int, borneMax : int) -> list[int] : # could be in outils
    """
    Fonction qui genere une liste de valeur entier aléatoire d'un nombre donné entre 2 bornes donnés
    Entrée : nombre entier qui est le nombre de valeur aléatoire généré puis mis dans la liste.
             borneMin est la borne minimal du nombre random.
             borneMax est la borne maximal du nombre random.
    Sortie : Une liste de nombres générés aléatoirement de tailles de la variable nombre en entrée.
    """
    iterateur : int
    liste : list

    liste = []

    for iterateur in range(nombre):
        liste.append(randint(borneMin, borneMax))
    
    return liste

def nbElementUniqueDansListe(liste : list[int]) -> int : # faut mettre dans outils
    """
    Fonction qui renvoie le nombre d'élément unique dans une liste.
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

def estUnEnsemble(liste : list[int]) -> bool :
    """
    Renvoie True si la liste n'a pas de doublons.
    Entrée : liste d'entier.
    Sortie : booléen, renvoie Vrai si une liste est un ensemble (donc n'a pas de doublons), renvoie Faux sinon.
    """
    estUnEnsemble : bool
    estUnEnsemble = False

    if nbElementUniqueDansListe(liste) == 0 :
        estUnEnsemble = True

    return estUnEnsemble

def rajoutSiPasDedans(valeur : int, liste : list[int]) -> list[int] :
    """
    La fonction rajoute la valeur en entrée dans la liste si elle n'est pas déjà dedans.
    Entrée : valeur entière et liste de valeurs UNIQUES.
    Sortie : la liste en entrée avec la valeur rajoutée ou non.
    
    Lève une ValueError si la liste n'est pas un ensemble.

    Exemple pour traiter une ValueError : 

    pasUnEnsemble = [1, 2, 2]
    try:
        nouvelle_liste = rajoutSiPasDedans(3, pasUnEnsemble)
        print(f"Il y a {len(nouvelle_liste)} éléments.")
    except ValueError as e:
        print(f"Une erreur est survenue : {e}")
    """

    if not estUnEnsemble(liste) :
        # raise ValueError fait envoyer une erreur dans le terminal et cherche un except sinon ça crash 
        # (évite de continuer le programme alors que la fonction n'a pas fonctionné)
        raise ValueError("Erreur, la liste donnée n'est pas un ensemble")
    
    # Si on arrive ici, on sait que la liste est valide grace au raise
    if not valeur in liste : 
        liste.append(valeur)
    
    return liste