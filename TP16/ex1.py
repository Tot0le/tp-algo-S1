class VilleDeFrance:
    nom:str
    surface:float
    codePostal:str
    departement:str
    nbHabitants:int
    nbEtudiants:int

class RegionDeFrance:
    nom:str
    nbVE:int
    lstVE:list

def creation_obj_ville(nom, sur, cp, dep, nbH, nbE):
    ville: VilleDeFrance
    ville = VilleDeFrance()
    ville.nom = nom
    ville.surface = sur
    ville.codePostal = cp
    ville.departement = dep
    ville.nbHabitants = nbH
    ville.nbEtudiants = nbE
    return ville

def creation_obj_region(nom, nbVE, lstVE):
    if nom != "" and nbVE >= 0:
        region: RegionDeFrance
        region = RegionDeFrance()
        region.nom = nom
        region.nbVE = nbVE
        region.lstVE = lstVE
        return region
    else:
        print("Impossible de creer l'objet.")
        return

def affichage_ville(ville):
    print(f"[{ville.nom}, {ville.surface}, {ville.codePostal}, {ville.departement}, {ville.nbHabitants}, {ville.nbEtudiants}]")

def affichage_ville(region):
    print(f"[{region.nom}, {region.nbVE}, {region.lstVE}]")

def ville_plus_etudiant(region):
    max_hab = 0
    max_ville = ""
    for ville in region.lstVE:
        if ville.nbEtudiants > max_hab:
            max_hab = ville.nbEtudiants
            max_ville = ville.nom
    return max_ville

def region_avec_ville_plus_etudiant(region_array):
    max_hab = 0
    max_region = ""
    for region in region_array:
        if ville_plus_etudiant(region) > max_hab:
            max_region = region.nom
            max_hab = region.ville.nbEtudiants
    return max_region

# Il manque l'exo 1 question 7 et l'exo 2

def main():
    villeLimoges: VilleDeFrance
    villeLimoges = creation_obj_ville("Limoges", 77.45, "87000", "Haute-Vienne", 129754, 17000)
    villeSeissan = creation_obj_ville("Seissan", 18.56, "32260", "Gers", 1098, 2)
    villeToulouse = creation_obj_ville("Toulouse", 118.3, "31000", "Haute-Garonne", 511684, 50000)
    villeAuch = creation_obj_ville("Auch", 72.48, "32000", "Gers", 22825, 3000)
    villePau = creation_obj_ville("Pau", 32.52, "64000", "Pyrénées-Atlantiques", 78620, 5000)
    villeMontpellier = creation_obj_ville("Montpellier", 56.88, "34000", "Hérault", 307101, 25000)
    regionOccitanie = creation_obj_region("Occitanie", 2, [villeToulouse, villeAuch, villePau, villeMontpellier])
    print(f"La ville avec le plus d'étudiant en région occitanie est : {ville_plus_etudiant(regionOccitanie)}.")