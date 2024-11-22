from os import system

def areatriangle():
    verification = 0
    while verification == 0:
        try:
            base = float(input('qual a base do triangulo? '))
            height = float(input('qual a altura do triangulo? '))
        except:
            system('cls')
            print('erro, digite um numero')
            continue
        else:
            area = round((base*height)/2, 2)
            verification += 1
    return print(f'A area do triangulo e de: {area}')

areatriangle()