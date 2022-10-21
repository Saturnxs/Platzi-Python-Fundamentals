def conversor(tipo_pesos, valor_dolar):
    """
    It takes two arguments, a string and a float, and then asks the user for a number, converts it to a
    float, divides it by the float argument, rounds it to two decimal places, converts it to a string,
    and then prints a string with the result
    
    :param tipo_pesos: This is the type of currency you want to convert
    :param valor_dolar: The value of the currency in dollars
    """
    # Taking the input from the user, converting it to a float, dividing it by the value of the
    # currency in dollars, rounding it to two decimal places, and then converting it to a string.
    dolares = str(round(float(input("Cuantos pesos "+ tipo_pesos +" tienes?: "))/valor_dolar,2))
    print("Tienes $"+ dolares + " dolares")

# A string that is being assigned to the variable `menu`.
menu = """ 
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """
opcion = int(input(menu))

# Asking the user for an input, and then depending on the input, it will call the function `conversor`
# with different arguments.
if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingrese una opcion correcta, por favor")

