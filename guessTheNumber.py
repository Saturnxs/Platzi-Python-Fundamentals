import random

def run():
    # Generating a random number between 1 and 100.
    numeroMaquina = random.randint(1,100);
    numeroElegido = int(input("Ingrese un numero del 1 al 100: "));

    
    # This is a while loop. It will execute the code inside of it while the condition is true. In this
    # case, the condition is `numeroElegido != numeroMaquina`. This means that the code inside of the
    # while loop will execute while the value of `numeroElegido` is not equal to the value of
    # `numeroMaquina`.
    while(numeroElegido != numeroMaquina):
        # This is a conditional statement that will print a message depending on the value of the
        # variable `numeroElegido`. If the value of `numeroElegido` is greater than the value of
        # `numeroMaquina`, then the message "Prueba con un numero menor" will be printed. If the value
        # of `numeroElegido` is less than the value of `numeroMaquina`, then the message "Prueba con
        # un numero mayor" will be printed.
        if(numeroElegido > numeroMaquina):
            print("Prueba con un numero menor")
        else:
            print("Prueba con un numero mayor")

        numeroElegido = int(input("Elije otro numero: "));
    print("Ganaste!")

if __name__ == '__main__':
    run()
    