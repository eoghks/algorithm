def tree_bfs_brand_and_bound(root, best, count,w):
    #PQ=priority_queue
    PQ=[]
    PQ.append(root)
    
    while(len(PQ)>0):
        v=PQ.pop(0)
        count+=1
        if(v.profit>best and v.node_weight<=w):
            best=v.profit
        if(v.left!=None):
            if(v.left.bound>best):
                PQ=priority_append(PQ, v.left)
            if(v.right.bound>best):
                PQ=priority_append(PQ, v.right)
    return best,count

def priority_append(PQ, v):
    if(len(PQ)==0):
        PQ.append(v)
    else:
        a=len(PQ)+1
        for i in range(a):
            if(i==len(PQ)):
                PQ.append(v)
            elif(PQ[i].bound<v.bound):
                PQ.insert(i,v)
                break;
    return PQ
            
    