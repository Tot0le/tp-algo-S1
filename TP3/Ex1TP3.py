def main():
    a : int

    a = int(input("Saisissez a : "))

    if a % 2 == 0 :
        print(a, "/ 2 =", a//2)

    else:
        print(a,"est un nombre impair !")
