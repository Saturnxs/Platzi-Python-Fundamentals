def conversor(tipo_pesos, valor_dolar):
    dolares = str(round(float(input("Cuantos pesos "+ tipo_pesos +" tienes?: "))/valor_dolar,2))
    print("Tienes $"+ dolares + " dolares")

menu = """ 
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """
opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingrese una opcion correcta, por favor")

