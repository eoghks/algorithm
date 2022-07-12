def checknode(v,best,count,w):
    count+=1
    if (promsing(v,best,w)):
        if(v.profit>best):
            best=v.profit
        if(v.left!=None):
            best,count=checknode(v.left,best,count,w)
            best,count=checknode(v.right,best,count,w)
    return best,count
            
def promsing(v,best,w):
    return (v.node_weight<=w) and (v.bound>best)