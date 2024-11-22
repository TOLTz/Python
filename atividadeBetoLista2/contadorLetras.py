from os import system
def counterletter():  
    verification = 0
    while verification == 0:
        try:
            a = input('digite uma palavra: ')
        except:
            system('cls')
            print('erro, digite uma palavra')
            continue
        else:
            counted = len(a)
            verification += 1
    return print(f'sua palavra tem {counted} letra(s)')
counterletter()