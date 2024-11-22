from os import system
def conversionC():
    verification = 0
    while verification == 0:
        try:
            c = int(input('digite a temperatura em celcius: '))
        except:
            system('cls')
            print('erro, digite um valor numerico')
            continue
        else:
            F = c * 1.8 + 32
            verification += 1
    return print(f'A sua temperatura sera de {F}°F ')

conversionC()