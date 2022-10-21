def es_primo(numero):
    """
    It returns True if the number is prime, and False if it isn't
    
    :param numero: The number to be checked
    :return: True or False
    """
    if numero == 1:
        return False
    else:
        contador = 0
    # Checking if the number is divisible by any number between 1 and the number itself.
    for i in range(1 , numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    # Checking if the number is prime or not.
    if contador == 0:
        return True
    else:
        return False


def run():
    """
    It takes a number and returns True if it's prime, False if it's not
    """
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print(str(numero) + " es primo")
    else:
        print(str(numero) +  " no es primo")


if __name__ == "__main__":
    run()