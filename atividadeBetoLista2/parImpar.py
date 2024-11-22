from os import system
def evenOrOdd():
    verification = 0
    while verification == 0:
        try:
            a = int(input('digite um numero: '))
        except:
            system('cls')
            print('erro, digite um valor numerico')
            continue
        else:
            if a % 2 == 0:
                print(f'{a} é par')
            else:
                print(f'{a} é impar')
            verification += 1
            
evenOrOdd()