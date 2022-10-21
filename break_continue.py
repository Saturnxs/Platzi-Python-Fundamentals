def run():
    # for i in range(1000):
    #     if ((i % 2) != 0):
    #             continue
    #     print(i)
    
    
    # for i in range(10000):
    #     print(i)
    #     if (i == 5878):
    #         break
    
    
    # Asking for a text and printing it until it finds an "o"
    texto = input("Escribe un texto: ").lower()
    for i in texto:
        if (i == "o"):
                break
        print(i)
        

if __name__ == '__main__':
    run()
    