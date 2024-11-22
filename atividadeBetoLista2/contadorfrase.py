from os import system

def wordPhrase():
    verification = 0
    while verification == 0:
        try:
            phrase = input('digite uma frase: ')
        except:
            system('cls')
            print('erro, digite uma palavra')
            continue
        else:
            words = phrase.lower().split()
            singleWords = set(words)
            singleCounted = len(singleWords)
            verification += 1
    return print(f'Sua frase tem {singleCounted} palavras, excluindo todas as que se repetem.', singleWords)

wordPhrase()