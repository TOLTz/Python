def countchar():
    phrase = input("Digite uma frase: ")
    count = {}
    for char in phrase:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return print(count)

countchar()