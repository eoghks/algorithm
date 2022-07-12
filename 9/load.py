def load():
    infile = open("input.txt", "r")
    #load
    loaddata=[]
    for line in infile:
        line=line.rstrip()
        loaddata.append(line)
    #2차원 배열로 make
    graph=makelist(loaddata)
    return graph

def makelist(data):
    graph=[]
    for i in range(1, len(data)):
        row=data[i].split(" ")
        for j in range(len(row)):
            if(row[j]=="inf"):
                row[j]=99999
            else:
                row[j]=int(row[j])
        graph.append(row)
    
    return graph

    