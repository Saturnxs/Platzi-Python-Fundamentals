import random

def run():
    numeroMaquina = random.randint(1,100);
    numeroElegido = int(input("Ingrese un numero del 1 al 100: "));

    while(numeroElegido != numeroMaquina):
        if(numeroElegido > numeroMaquina):
            print("Prueba con un numero menor")
        else:
            print("Prueba con un numero mayor")

        numeroElegido = int(input("Elije otro numero: "));
    print("Ganaste!")

if __name__ == '__main__':
    run()
    