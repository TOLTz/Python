def whithOutTwins(nestedList):
    uniqueList = []
    for sublist in nestedList:
        uniqueSublist = []
        seen = set()
        for item in sublist:
            if item not in seen:
                uniqueSublist.append(item)
                seen.add(item) 
        uniqueList.append(uniqueSublist)  
    return print(uniqueList)

lista = [[2, 2, 2], [3, 7, 8], [5, 4, 4]]
whithOutTwins(lista)