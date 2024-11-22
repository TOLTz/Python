def diagonal():
    main = 0
    secundary = 0
    matrix = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    
    # Define os numeros
    for l in range(0, 3):
        for c in range(0, 3):
            matrix[l][c] = int(input(f'Digite um numero: '))
    # Exibi os numeros setados acima
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{matrix[l][c]}]', end='')
        print()
    # Aqui exibi os resultados com as variaveis main  e  secundary
    for i in range(len(matrix)):
        main += matrix[i][i] 
        secundary += matrix[i][len(matrix) - 1 - i] 
    return print(f'Soma da diagonal primaria: {main}\nsoma da sua diagonal secundaria: {secundary}')
diagonal()

