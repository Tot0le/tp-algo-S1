import outilsFichierBin
from outilsAffichage import ALaLigne, pressEnterToContinue
import pickle
from outils import saisieYesOrNO

class VilleDeFrance :
    nom :str
    surface : float
    codePostal : str
    departement : str
    nbHabitants : int
    nbEtudiants : int

def saisieUserVilleDeFrance():
    ville : VilleDeFrance
    ville = VilleDeFrance()
    print("Saisissez : ")
    ville.nom = input("Le nom de la ville : ")
    ville.surface = input("Sa surface : ")
    ville.codePostal = input("Son codepostal : ")
    ville.departement = input("Son département : ")
    ville.nbHabitants = input("Son nombre d'habitants : ")
    ville.nbEtudiants = input("Son nombre d'étudiant : ")
    return ville

def saisieVilleDeFrance(monNom : str, maSurface : float, monCodePostal : str, monDepartement : str, monNbHabitants : int, monNbEtudiants : int):
    ville : VilleDeFrance
    ville = VilleDeFrance()
    ville.nom = monNom
    ville.surface = maSurface
    ville.codePostal = monCodePostal
    ville.departement = monDepartement
    ville.nbHabitants = monNbHabitants
    ville.nbEtudiants = monNbEtudiants
    return ville

def concatenerClasseEnListe(monObjet) -> list:
    """
    Retourne une liste des valeurs de l'objet de la classe en entrée.
    """
    return list(monObjet.__dict__.values())

def convertirListeVersVille(listeDonnees: list) -> VilleDeFrance:
    """
    Fonction qui reçoit une liste ['Limoges', 77.45, ...] 
    et qui renvoie un objet VilleDeFrance rempli.
    """
    ville = VilleDeFrance()
    
    ville.nom = listeDonnees[0]
    ville.surface = listeDonnees[1]
    ville.codePostal = listeDonnees[2]
    ville.departement = listeDonnees[3]
    ville.nbHabitants = listeDonnees[4]
    ville.nbEtudiants = listeDonnees[5]
    
    return ville

def main():
    veuxSaisir : bool = True
    ville : VilleDeFrance
    Montpellier = saisieVilleDeFrance("Montpellier", 56.88, "34000", "Hérault", 307101, 25000)
    outilsFichierBin.rajouterElementFichierBin("villes.dat", Montpellier.nom, [Montpellier])
    Seissan = saisieVilleDeFrance("Seissan", 18.56, "32260", "Gers", 1098, 2)
    outilsFichierBin.rajouterElementFichierBin("villes.dat", Seissan.nom, [Seissan])

    while veuxSaisir:
        ville = saisieUserVilleDeFrance()
        outilsFichierBin.rajouterElementFichierBin("villes.dat", ville.nom, [ville])

        veuxSaisir = saisieYesOrNO("Voulez vous saisir d'autres villes : ")

    outilsFichierBin.afficherFichierBin(VilleDeFrance(), "villes.dat")
    # ville = saisieVilleDeFrance("Limoges", 77.45, "87000", "Haute-Vienne", 129754, 17000)
    # saisieVilleDeFrance("Seissan", 18.56, "32260", "Gers", 1098, 2)
    # saisieVilleDeFrance("Toulouse", 118.3, "31000", "Haute-Garonne", 511684, 50000)
    # saisieVilleDeFrance("Auch", 72.48, "32000", "Gers", 22825, 3000)
    # saisieVilleDeFrance("Pau", 32.52, "64000", "Pyrénées-Atlantiques", 78620, 5000)
    