def outputScore(name1, name2, score1, score2, nfile, sfile):
    with open(nfile, 'a') as f:
        if score1 > score2:
            f.write("\n"+name1)
        else:
            f.write("\n"+name2)
    with open(sfile, 'a') as f:
        if score1 > score2:
            f.write("\n"+str(score1))
        else:
            f.write("\n"+str(score2))

def getHighestScore(nfile, sfile):
    x = 0
    name = ""
    n = []
    s = []
    data = []
    highest = 0

    with open(nfile, 'r') as f:
        for x in f:
            n.append(x.strip("\n"))
    with open(sfile, 'r') as f:
        for x in f:
            s.append(x.strip("\n"))
      
    for y in s:
        try:
            if int(y) > int(highest):
                highest = int(y)
        except Exception as err:
            highest = 0
        
            
    if highest == 0: data = "There is not a highest score yet!"

    else:
        data = [n[s.index(str(highest))], highest]

    return data

