from os import system

def multiplicationTable():
    verification = 0
    while verification == 0:
        try:
            a = int(input('digite um numero: '))
        except:         
            system('cls')
            print('erro, digite uma numero valido')
            continue
        else:
            for num in range(11):
                print(f'{a} x {num} = {a * num}')
                verification += 1
                
multiplicationTable()