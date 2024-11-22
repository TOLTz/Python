def filterPair(pairs):
    lista1 = []
    for pair in pairs:
        if pair % 2 == 0:
            lista1.append(pair)
    return print(f'Os numeros pares sao {lista1}')        
        
lista = [1,2,3,4,5,6]
filterPair(lista)