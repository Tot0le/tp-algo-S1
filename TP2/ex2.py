def main():
    """
    Calcul le volume d'un prisme quelconque
    L'utilisateur saisie l'aire et la hauteur
    Le programme calcul le volume et l'affiche
    """
    aire : float
    hauteur : float
    volume : float

    # Saisis utilisateur :
    aire = float(input("Saisissez l'aire du prisme : "))
    hauteur = float(input("Saisissez la hauteur du prisme : "))

    # condition des saisis :
    if aire <= 0 or hauteur <= 0 :
        print("Réfléchis quand même une distance négative sérieux...")
        
    # sinon pas de problème :
    else:
        volume = aire * hauteur

        print(volume)