def load():
    infile = open("example.txt", "r")
    #index 1부터 데이터 저장 
    data=[0]
    probability=[0]
    for line in infile:
        line=line.rstrip()
        lineList=line.split(", ")
        data.append(lineList[0])
        probability.append(float(lineList[1]))
    
    return data, probability
    
