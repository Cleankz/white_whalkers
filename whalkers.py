def white_walkers(village):
    index = []
    result= []
    r = []
    for i in range(len(village)):
        if village[i] == "0" or  village[i] == "1" or village[i] == "2" or village[i] == "3" or village[i] == "4" or village[i] == "5" or village[i] == "6" or village[i] == "7" or village[i] == "8" or village[i] == "9":
            index.append(i)
    if len(index) <= 1:
        return False
    for j in range(len(index)):
        for x in range(j,len(index)):
            if j == x:
                continue
            if village.count("=",index[j],index[x]) % 3 == 0 and len(index) == 2:
                r.append(False)
            elif int(village[index[j]]) + int(village[index[x]]) == 10 and village.count("=",index[j],index[x]) == 3 or village.count("=",index[j],index[x]) % 3 == 0:
                r.append( True)
            elif int(village[index[j]]) + int(village[index[x]]) == 10 and (village.count("=",index[j],index[x])) != 3:
                r.append(False)
    if False in r:
        return False
    return True