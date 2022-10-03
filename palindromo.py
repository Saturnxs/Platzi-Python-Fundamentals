def palindromo(palabra):
    palabra = palabra.replace(" ","").lower()
    if(palabra == palabra[::-1]):
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    if (palindromo(palabra)):
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()