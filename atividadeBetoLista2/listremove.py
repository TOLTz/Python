def listremove():
    l1 = []
    for _ in range(1, 4):
        l1.append(input("digite um numero: "))
    unDuplicate = list(set(l1))
    unDuplicate.sort()
    l1.sort()
    print(l1)
    print(unDuplicate)
    
listremove()