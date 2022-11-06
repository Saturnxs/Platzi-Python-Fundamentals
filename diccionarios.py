def run():
    # Creating a dictionary.
    mi_diccionario ={
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    };
    
    # Iterating over the dictionary and printing the key and value.
    for llave, poblacion in mi_diccionario.items():
        print(llave + " es "+str(poblacion));
    

if __name__ == '__main__':
    run()
    