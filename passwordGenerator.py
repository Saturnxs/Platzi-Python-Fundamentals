import random;

def generatePassword():
    """
    It creates a list of 15 random characters from a list of characters, and then joins the list into a
    string
    :return: A string of 15 characters.
    """
    mayus = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H');
    mins = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h');
    simbols = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0');
    
    # Creating a list of characters.
    chars = mayus+mins+simbols;
    
    password = []
    
    # Creating a list of 15 random characters.
    for i in range(15):
        ran_char = random.choice(chars)
        password.append(ran_char)
        
    # Joining the list of characters into a string.
    password = "".join(password)
    
    return password

def run():
    """
    It generates a random password of length 8, consisting of letters and digits
    """
    print("New password is: "+ generatePassword());
    
    while numero == 3:
        numero += numero
        print("xd")
    

if __name__ == '__main__':
    run();    