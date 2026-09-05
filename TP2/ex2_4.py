import math
def main():
    """
    Calcul le volume d'un prisme rectangle et d'un cylindre
    """
    aire_prisme_base_rectangle : float
    aire_prisme_base_cercle : float# pi R²
    hauteur_prisme_base_rectangle : float
    volume_prisme_base_rectangle : float
    hauteur_prisme_base_cercle : float
    volume_prisme_base_cercle : float 
    rayon : float
    longueur : float
    largeur : float 

    # Saisis utilisateur :
    longueur = float(input("Saisissez la longueur rectangle de la base du prisme : "))
    largeur = float(input("Saisissez la largeur rectangle de la base du prisme : "))
    hauteur_prisme_base_rectangle = float(input("Saisissez la hauteur du prisme rectangle : "))

    rayon = float(input("Saisissez le rayon de la base du prisme : "))
    
    hauteur_prisme_base_cercle = float(input("Saisissez la hauteur du prisme cercle : "))

    # condition des saisis :
    if longueur <= 0 or largeur <= 0 or hauteur_prisme_base_rectangle <= 0 or rayon <= 0 or hauteur_prisme_base_cercle <= 0:
        print("Réfléchis quand même une distance négative sérieux...")
        
    # sinon pas de problème :
    else:
        aire_prisme_base_rectangle = longueur * largeur
        volume_prisme_base_rectangle = aire_prisme_base_rectangle * hauteur_prisme_base_rectangle

        print("Aire du prisme base rectangle : ",volume_prisme_base_rectangle)

        aire_prisme_base_cercle = rayon * math.pi * math.pi
        volume_prisme_base_cercle = aire_prisme_base_cercle * hauteur_prisme_base_cercle

        print("Aire du prisme base cercle : ",volume_prisme_base_cercle)