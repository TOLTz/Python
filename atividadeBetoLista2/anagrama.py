def checkAnagram():
    word1 = input("Digite a primeira palavra: ")
    word2 = input("Digite a segunda palavra: ")

    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    if len(word1) != len(word2):
        print("As palavras não são anagramas.")
        return

    if sorted(word1) == sorted(word2):
        print("As palavras são anagramas.")
    else:
        print("As palavras não são anagramas.")

checkAnagram()