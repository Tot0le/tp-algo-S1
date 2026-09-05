def main():
    nombre : str
    result : str

    nombre = str(input("Saisissez votre nombre entre 0 et 15 : "))


    while int(nombre) < 0 or int(nombre) > 15 :
        nombre = str(input("Veuillez saisir un nombre entre 0 et 15 : "))

    if int(nombre) < 10 :
        result = nombre
    elif int(nombre) == 10 :
        result = "A"
    elif int(nombre) == 11 :
        result = "B"
    elif int(nombre) == 12 :
        result = "C"
    elif int(nombre) == 13 :
        result = "D"
    elif int(nombre) == 14 :
        result = "E"
    elif int(nombre) == 15 :
        result = "F"
    else:
        print("Nombre out of range")

    print(result)