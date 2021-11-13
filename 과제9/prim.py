def prim(graph):
    F=[]
    n=len(graph)
    nearest=[]
    distance=[]
    #초기화
    for i in range(n):
        nearest.append(1)
        distance.append(-1)
    
    for i in range(1,n):
        nearest[i]=0
        distance[i]=graph[0][i]
    #n-1번 반복
    for k in range(n-1):
        vnear=-1
        min=99999
        for i in range(1,n):
            if(0<=distance[i] and distance[i] < min):
                min=distance[i]
                vnear=i
        #edge 추가, vertex 존재한다고 표시
        e=[vnear+1, nearest[vnear]+1]
        F.append(e)
        distance[vnear]=-1
        #nearest, distance update
        for i in range(1,n):
            if(graph[i][vnear] < distance[i]):
                distance[i]=graph[i][vnear]
                nearest[i]=vnear
    return F
