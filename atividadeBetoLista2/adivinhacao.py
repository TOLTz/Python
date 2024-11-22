from os import system
from random import randint

def guessing():
    number_to_guess = randint(1, 100)
    print(number_to_guess)
    guesses = 0
    verification = 0
    while verification == 0:
        try:

            guess = int(input('Chute um numero entre 1 e 100: '))
        except:
            system('cls')
            print('Erro, insira um numero valido')
            continue
        else:
            if number_to_guess == guess:
                guesses += 1
                print('Parabens, voce acertou o numero!')
                print(f'voce tentou {guesses} vezes ')
                verification = 1
            elif number_to_guess > guess :
                print('Tente novamente, o numero que voce chutou e menor que a resposta')
                guesses += 1
                print(f'voce tentou {guesses} vezes')
            else:
                guesses += 1
                print('Tente novamente, o numero que voce chutou e maior que a resposta')
                
                
guessing()