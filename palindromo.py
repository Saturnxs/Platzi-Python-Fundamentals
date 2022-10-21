def palindromo(palabra):
    """
    It takes a string, removes all spaces and makes it lowercase, then checks if the string is the same
    as the string reversed
    
    :param palabra: The word you want to check
    :return: True or False
    """
    # Removing all spaces and making the word lowercase.
    palabra = palabra.replace(" ","").lower()
    # Checking if the word is the same as the word reversed.
    if(palabra == palabra[::-1]):
        return True
    else:
        return False


def run():
    """
    It takes a string as input, and returns True if the string is a palindrome, and False otherwise
    """
    palabra = input("Escribe una palabra: ")
    if (palindromo(palabra)):
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()