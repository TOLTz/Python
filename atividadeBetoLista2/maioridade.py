from os import system

def adulthood():
    verification = 0
    while verification == 0:
        try:
            age = int(input('digite sua idade: '))
        except:
            system('cls')
            print('erro, digite uma idade valida')
            continue
        else:
            if age >= 18:
               print('usuario de maior')
            else:
                print('usuario de menor')
            verification += 1
            
adulthood()