def main():
    """Définition des variables :"""
    longueur : float
    largeur : float
    aire : float
    perimetre : float

    # Initialisons les deux variables à un nombre négatif pour qu'ils rentrent dans les boucles "tant que"
    longueur = -1
    largeur = -1

    # Boucle pour s'assurer qu'une bonne valeur est données pour longueur :
    while longueur < 0:
        longueur = float(input("Saisissez longueur du rectangle : "))

    # Boucle pour s'assurer qu'une bonne valeur est données pour largeur
    while largeur < 0 :
        largeur = float(input("Saisissez largeur du rectangle : "))
    
    # Calcul :
    perimetre = (largeur * float(2)) + (longueur * float(2))
    aire = longueur * largeur

    # Affichage :
    print(f"Le perimetre du rectangle est {perimetre}um. , et l'aire est {aire} ua. .")