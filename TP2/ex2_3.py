def main():
    """
    Calcul le volume d'un prisme rectangle
    L'utilisateur saisie la longueur, la largeur et la hauteur
    Le programme calcul l'aire puis le volume
    """
    aire : float
    hauteur : float
    volume : float
    longueur : float
    largeur : float

    # Saisis utilisateur :
    longueur = float(input("Saisissez la longueur rectangle de la base du prisme : "))
    largeur = float(input("Saisissez la largeur rectangle de la base du prisme : "))
    
    hauteur = float(input("Saisissez la hauteur du prisme : "))

    # condition des saisis :
    if longueur <= 0 or largeur <= 0 or hauteur <= 0 :
        print("Réfléchis quand même une distance négative sérieux...")
        
    # sinon pas de problème :
    else:
        aire = longueur * largeur
        volume = aire * hauteur

        print(volume)