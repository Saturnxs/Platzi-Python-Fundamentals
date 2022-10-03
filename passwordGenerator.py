import random;

def generatePassword():
    mayus = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H');
    mins = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h');
    simbols = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0');
    
    chars = mayus+mins+simbols;
    
    password = []
    
    for i in range(15):
        ran_char = random.choice(chars)
        password.append(ran_char)
        
    password = "".join(password)
    
    return password

def run():
    print("New password is: "+ generatePassword());
    
    while numero == 3:
        numero += numero
        print("xd")
    

if __name__ == '__main__':
    run();    