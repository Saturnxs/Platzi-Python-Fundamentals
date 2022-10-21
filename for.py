# def run():
#     contador = 1
#     print(contador)
#     while contador < 1000:
#         contador += 1
#         print(contador)

def run():
    # Printing the numbers from 1 to 1000.
    for contador in range(1, 1001):
        print(contador)

    # Printing the multiples of 11 from 1 to 100.
    for i in range(1, 11):
        print(11*i)


if __name__ == '__main__':
    run()