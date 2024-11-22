from os import system

def sub(n1, n2):
    return(n1 - n2)

def mul(n1, n2):
    return(n1 * n2)

def div(n1, n2):
    if n2 == 0:
        return("Erro! N tem como dividir por zero!")
    return (n1 / n2)

def add(n1, n2):
    return(n1 + n2)

def choice():
    verification = True
    while verification:
        operator = input('escolha uma opcao abaixo \n +, -, *, / \n')
        try:
            n1 = float(input('digite o primeiro valor: \n'))
            n2 = float(input('digite o segundo valor: \n'))
        except:
            system('cls')
            print('erro! valor invalido')
            continue
        else:
            if operator == '+':
                verification = False
                return print(f'{n1} + {n2} = {add(n1, n2)}')
            elif operator == '-':
                verification = False
                return print(f'{n1} - {n2} = {sub(n1, n2)}')
            elif operator == '*':
                verification = False
                return print(f'{n1} * {n2} = {mul(n1, n2)}')
            elif operator == '/':
                verification = False
                return print(f'{n1}/{n2} = {div(n1, n2)}')
            else:
                system('cls')
                print('erro! operador invalido')
                continue
                
choice()