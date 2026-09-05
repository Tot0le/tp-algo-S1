import pickle
import os
from typing import TypeVar
from outils import saisieYesOrNO

genericClasse = TypeVar('genericClasse')
# genericCLasse est maintenant un type afin de typé une classe quand on ne sait pas qu'elle classe est en entrée ou sortie

def chargerFichierBin(cheminFichier : str) -> list:
    """
    Fonction générique qui lit n'importe quel fichier binaire et retourne son contenu (une liste).
    
    Entrée : cheminFichier : le chemin ou nom du fichier à lire (str).
    Sortie : Une liste (list) contenant les objets stockés.
             Renvoie une liste vide [] si le fichier n'existe pas ou est corrompu.
    """
    contenu : list

    if not os.path.exists(cheminFichier):
        return []
    
    try:
        with open(cheminFichier, "rb") as f:
            contenu = pickle.load(f)
            return contenu
    except (EOFError, pickle.UnpicklingError):
        return []

def sauvegarderFichierBin(cheminFichier : str, donnees : list) -> None:
    """
    Fonction générique qui sauvegarde n'importe quelle liste dans un fichier binaire.
    
    Entrée : cheminFichier : le chemin ou nom du fichier où écrire (str).
             donnees : la liste des objets à sauvegarder (list).
    Sortie : Aucune (None).
    """
    with open(cheminFichier, "wb") as f:
        pickle.dump(donnees, f)

def rajouterElementFichierBin(cheminFichier : str, elementComparatif : str, listeDonnees : list, modifierSiDedans : bool | None = None) -> None:
    """
    Rajoute une ligne dans un fichier binaire si l'élement comparatif n'est pas dedans

    Entrée : cheminFichier doit reférencer un fichier qui a des lignes que d'un seul type de données.
             elementComparatif : l'élement d'une classe avec laquelle on va comparer si l'élement est dans la liste globale en premier élement
             listeDonnes : liste d'objet à rajouter
             modifierSiDedans booléen ou None, booléen oui pour qu'on modifie les valeurs si c'est dedans ou si on fait rien, 
                              si None demande à l'utilisateur de choisir
    Sortie : le fichier binaire est modifié (ou non)
    """
    objet : object | None
    iterateur : int
    listeAttributs : list[str]
    # listeDonnees arrive sous la forme [Objet]

    listeGlobale = chargerFichierBin(cheminFichier)

    objet = trouverElementFichierBin(listeGlobale, elementComparatif)

    # Si l'elementComparatif est déjà présent dans le fichier
    if objet is not None:
        ##### modif la ligne avec les donnees qu'on veut rajouter #####

        # si le modifierSiDedans est None alors on demande sinon on demande pas à l'utilisateur car c'est le développeur qui a choisi en amont
        if modifierSiDedans is None:
            modifierSiDedans = saisieYesOrNO("L'élement est déjà présent dans le fichier, voulez vous le modifier avec vos valeurs saisies ? " \
            "\n(si non : ne rien faire) : ")

        if modifierSiDedans:
            listeAttributs = list(objet.__dict__.keys())
            
            # On récupère l'objet qui est dans la liste [Objet]
            nouveau_objet = listeDonnees[0]
            # On transforme cet objet en liste de valeurs
            valeursAMettre = list(nouveau_objet.__dict__.values())

            for iterateur in range(len(listeAttributs)):
                
                # set l'attribut "listeAttributs[iterateur]" d'"objet" à "listeDonnees[iterateur]"
                setattr(objet, listeAttributs[iterateur], valeursAMettre[iterateur])
    else:
        # rajouter la ligne de données
        listeGlobale = listeGlobale + listeDonnees

    sauvegarderFichierBin(cheminFichier, listeGlobale)


def trouverElementFichierBin(listeDeType: list[genericClasse], monElementComparatif: str) -> None | genericClasse:
    """
    Parcourt la liste pour trouver l'objet de nom monElementComparatif correspondant au premier attribut.
    
    Entrée : listeDeType : une liste de type de fichier
             monElementComparatif : le nom (str) que l'on cherche.
    Sortie : L'objet si trouvé, sinon None.
    """
    objet : genericClasse

    for objet in listeDeType:
        listeAttributs = list(objet.__dict__.keys())
        if getattr(objet, listeAttributs[0]) == monElementComparatif:
            return objet
    return None


def concatenerClasseEnListe(monObjet : object) -> list:
    """
    Retourne une liste des valeurs de l'objet de la classe en entrée.
    """
    return list(monObjet.__dict__.values())


# def trouverNomInListe(maListeDAttributs : list) -> int:
#     emplacement : int
#     iterateur : int

#     for iterateur in range(len(maListeDAttributs)):
#         if maListeDAttributs[iterateur] == "nom":
#             emplacement = iterateur
#     return emplacement


def afficherFichierBin(maClasse : object, cheminDuFichier : str) -> None:
    """
    Entrée : maClasse : une structure, celle qui est à l'intérieur du fichier
             cheminDuFichier précondition : référence un fichier binaire avec qu'un seule type de structure à l'intérieur (celle de maClasse)
    """
    listeAttributs = list(maClasse.__dict__.keys())
    listeGeneral = chargerFichierBin(cheminDuFichier)

    for classe in listeGeneral:
        print(concatenerClasseEnListe(classe))


def nombreLigneFichier(nomFichier : str) -> int:
    """
    Compte le nombre de ligne dans un fichier et le retourne.
    
    
    Parameters:
        nomFichier (str): Le nom du fichier dont vous voulez savoir le nombre de ligne.
    
    Returns:
        entier: le nombre de ligne du fichier dont on dit le nom en entrée.
    """
    f = open(nomFichier, 'r')
    nombreLigne = 0
    for line in f:
            nombreLigne += 1
    f.close()
    return nombreLigne