def main():
    """Définition des variables :"""
    dividende : float
    diviseur : float
    quotient : int
    reste : int

    # Input utilisateurs de dividende et diviseur :
    dividende = float(input("Saisissez le dividende : "))
    diviseur = float(input("Saisissez le diviseur : "))

    if diviseur != 0:
        # Calcul :
        quotient = dividende // diviseur
        reste = dividende % diviseur
        
        # Afficher :
        print(f"{dividende} = {quotient} * {diviseur} + {reste}")
    else:
        print ("Division par 0 impossible")