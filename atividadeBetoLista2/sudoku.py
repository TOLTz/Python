# professor eu n consegui fazer essa sozinho, ent pedi ajuda para o Chat.


def is_valid_sudoku(board):
    # Verificar se cada linha é válida
    for row in board:
        seen = set()
        for num in row:
            if num != 0:
                if num in seen:
                    print('o sudoku n e valido!')
                seen.add(num)

    # Verificar se cada coluna é válida
    for col in range(9):
        seen = set()
        for row in range(9):
            num = board[row][col]
            if num != 0:
                if num in seen:
                    print('o sudoku n e valido!')
                seen.add(num)

    # Verificar se cada subgrade 3x3 é válida
    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            seen = set()
            for i in range(3):
                for j in range(3):
                    num = board[start_row + i][start_col + j]
                    if num != 0:
                        if num in seen:
                            return print('o sudoku n e valido!')
                        seen.add(num)

    return print('o sudoku e valido!')



board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

is_valid_sudoku(board)