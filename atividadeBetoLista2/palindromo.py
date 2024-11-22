from os import system

def word():
    validation = True
    while validation:   
        try:
            word = input("Digite uma palavra: ")
            if len(word) < 2:
                system('cls')
                print("uma palavra precisa de mais de uma letra")
                continue
        except:
            print('digite uma palavra')
            continue
        else:
            validation = False
    return word.lower()

def palindrome(palavra):
    return palavra == palavra[::-1]

if palindrome(word()) is True:
    print("A palavra e um palindromo")
else:
    print("A palavra nao e um palindromo")

word()