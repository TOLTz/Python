def countFrequent(text):
    words = text.lower().split()
    wordCount = {}
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
            
    sortedWord = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)

    print("AS 5 palvras mais frequentes sao:")
    for i in range(min(5, len(sortedWord))):
        print(f"{sortedWord[i][0]}: {sortedWord[i][1]}")


user_text = input("Digite um texto longot: ")
countFrequent(user_text)