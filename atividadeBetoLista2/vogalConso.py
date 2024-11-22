def count():
    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"
    frase = input("Digite uma frase: ")
    num_vogais = 0
    num_consoantes = 0
    
    for char in frase:
        if char in vogais:
            num_vogais += 1
        elif char in consoantes:
            num_consoantes += 1       
    return print(f'Numero de vogais: {num_vogais} \nNumero de consoantes: {num_consoantes}')

count()
