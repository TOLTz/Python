from os import system

def arithmeticMean():
    verification = 0
    while verification == 0:
        try:
            n1 = float(input('digite a primeira nota: '))
            n2 = float(input('digite a segunda nota: '))
            n3 = float(input('digite a terceira nota: '))
        except:
            system('cls')
            print('erro, digite um numero')
            continue
        else:
            result = round((n1+n2+n3)/3, 2)
            verification += 1
            if result >= 7:
                decision = 'passou'
            else:
                decision = 'reprovado'
    return print(f'A media e de {result} \n{decision}')

arithmeticMean()