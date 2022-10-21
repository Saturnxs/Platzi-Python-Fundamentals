def run():
    LIMITE = 1000
    contador = 0
    potencia_2 = 2**contador
    # A while loop that prints the value of 2 to the power of the value of contador.
    while potencia_2 < LIMITE:
        print("2 elevado a "+ str(contador) + " es igual a: " + str(potencia_2))
        contador = contador +1
        potencia_2 = 2**contador


if __name__ == "__main__":
    run()