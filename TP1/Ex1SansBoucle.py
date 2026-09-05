def main():
    """Définition des variables :"""
    longueur : float
    largeur : float
    aire : float
    perimetre : float

    # Saisir la longueur :
    longueur = float(input("Saisissez longueur du rectangle : "))

    # Saisir la largeur :
    largeur = float(input("Saisissez largeur du rectangle : "))

    # Condition : s'assurer que longueur et largeur sont strictement supérieur à 0 :
    if longueur <= float(0) or largeur <= float(0):
        # Si inférieur ou égale à 0 on dit à l'utilisateur qu'il s'est trompé dans les mesures.
        print("Mesures pas bonne, calcul impossible.")
    # Si tout va bien dans les mesures les calculs sont fait :
    else:
        # Calcul du périmètre :
        perimetre = (largeur * float(2)) + (longueur * float(2)) 
        
        # Calcul de l'aire :
        aire = longueur * largeur

        # Affiche les résultats sous forme de phrase 
        print(f"Le perimetre du rectangle est {perimetre}um.(unité de mesure) , et l'aire est {aire} ua.(unité d'aire).")