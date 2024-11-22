import os
def soma():
    verification = 0
    while verification == 0:
        try:
            a = int(input('digite um numero: '))
            b = int(input('digite outro numero: '))
        except:
            os.system('cls')
            print('erro, digite um valor numerico')
            continue
        else:
            verification += 1
    return print(f'sua soma: {a} + {b} = {a + b}')

soma()