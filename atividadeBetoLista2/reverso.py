from os import system

def invert():
    verification = 0
    while verification == 0:
        try:
            word = input('digite uma palavra: ')
        except:
            system('cls')
            print('erro, digite uma palavra')
            continue
        else:
            inverted = word[::-1]
            verification += 1
    return print(inverted)

invert()