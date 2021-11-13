def kruskal(graph):
    sortedge=sorting(graph)
    F=[]
    vertex=[]
    for i in range(len(graph)):
        vertex.append(i)

    while(len(F)<len(graph)-1):
        e=sortedge.pop(0)
        i=e[0]
        j=e[1]
        p=vertex[i]
        q=vertex[j]
        if(p!=q):
            vertex[p]=vertex[q]
            F.append(e)
    for i in range(len(F)):
        for j in range(len(F[i])):
            F[i][j]+=1
    return F
    
def sorting(graph):
    sortedge=[]
    for i in range(len(graph)):
        for j in range(i+1,len(graph)):
            if(graph[i][j]==99999):
                continue
            sortedge.append([graph[i][j],i,j])
    sortedge.sort()
    for i in range(len(sortedge)):
        del sortedge[i][0]
    return sortedge
