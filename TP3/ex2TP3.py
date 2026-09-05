def main():
    var_a : float
    var_b : float

    var_a = float(input("Saisissez var_a : "))
    var_b = float(input("Saisissez var_b : "))

    if var_a == var_b :
        print(var_a, " = ", var_b)
    elif var_a < var_b :
        print(var_a, " < ", var_b)
    elif var_a > var_b :
        print(var_a, " > ", var_b)
