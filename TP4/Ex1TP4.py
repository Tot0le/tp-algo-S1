def main():        
    age : int
    etudiantStr : str
    etudiant : bool

    # Saisir age
    age = int(input("Saisir votre age : "))

    # Boucle vérification d'age
    while age < 0 or age > 150 :
        age = int(input("Saisir votre véritable age : "))

    # Saisir si la personne est étudiante ou non
    etudiantStr = str(input("Êtes vous étudiant ? (y/n) "))

    # Boucle vérification pour étudiant
    while etudiantStr != "y" and etudiantStr != "n" :
        etudiantStr = str(input("Êtes vous étudiant ? (Écrivez 'y' pour oui ou 'n' pour non) :"))

    # Conversion oui ou non à True et False
    if etudiantStr == "y" :
        etudiant = True
    else :
        etudiant = False

    # Toutes les conditions de prix :
    if age <= 3:
        print("Gratuit")

    elif age <= 6 :
        print("2 euros")

    elif age <= 12 :
        print("5 euros")

    elif etudiant :
        print("8 euros")

    elif age <= 18 :
        print("8 euros")

    elif age <= 65 :
        print("12 euros")

    else: 
        print("8 euros")
