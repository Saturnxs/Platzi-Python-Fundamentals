# def imprimir_mensaje():
#     print('Mensaje especial')
#     print('Estoy aprendiendo a usar funciones')

def opcionElegida(opcion):
    """
    It prints "Hola" and then prints "Elegiste la opcion" followed by the value of the parameter opcion
    
    :param opcion: The option that was selected
    """
    print('Hola')
    print('Elegiste la opcion ', opcion)

# Asking the user to input a number between 1 and 3 and then it is calling the function opcionElegida
# with the value of the input as the parameter.
opcion = int(input("Elige la opcion (1-3): "))
opcionElegida(opcion)
