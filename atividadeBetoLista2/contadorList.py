from os import system
from random import randint


def counterList():
    l1 = []
    for num in range(randint(0, 50)):
        l1.append(randint(0, 50))
        
    
    counted = len(l1)
    arrumado = sorted(l1)
    return print(f'A lista tem {counted} itens \n{arrumado}')

counterList()