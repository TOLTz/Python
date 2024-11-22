from os import system

def mean():
    verification = 0
    estudant = []
    meanTeam = []
    while verification != 1:
        try:
            alunos = int(input('quantos alunos tem na sala? '))
        except:
            print("Erro, coloque um numero valido")
            continue
        else:
            if alunos <= 0:
                print('a quantidade de alunos tem que ser maior do que 0')
                continue
            else:
                for a in range(alunos):
                    try:
                        nota = float(input(f'qual a nota do aluno {a+1}? '))
                    except:
                        print('insira uma nota valida!')
                        continue
                    else:
                        estudant.append(nota)
                        meanTotal = sum(estudant)/alunos
                        estudant.sort()
                        for num in estudant:
                            if num > meanTotal:
                                meanTeam.append(num)
                    verification += 1
    return print(f'Essas sao as notas maiores que a media({meanTotal}): \n {meanTeam}')

mean()