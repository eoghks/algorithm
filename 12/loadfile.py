def load():
    infile=open("input.txt","r")
    L=[]
    for line in infile:
        line = line.rstrip()
        L.append(line)
    
    #total weight정리
    W=L[0].split("=")
    w=int(W[1])
    
    #item, weight, price정리, p,wegiht에 0-> index를 맞추기위해사용
    S=[]
    p=[0]
    weight=[0]
    for i in range(1,len(L)):
        linelist=L[i].split(" ")
        weight.append(int(linelist[5]))
        p.append(int(linelist[3]))
        S.append(int(linelist[1]))
    
    return w,S,p,weight
