from unittest import main


def run():
    mi_diccionario ={
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    };
    
    for llave, poblacion in mi_diccionario.items():
        print(llave + " es "+str(poblacion));
    

if __name__ == '__main__':
    run()
    