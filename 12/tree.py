import loadfile as ld

#node
class node(object):
    def __init__(self, profit, node_weight, depth,price_of_weight,w,weight,p,item) :
        self.profit=profit
        self.node_weight=node_weight
        self.depth=depth
        self.bound=self.mkbound(price_of_weight, w,weight,p,item)
        self.left=self.right=None
    #bound생성
    def mkbound(self, price_of_weight, w,weight,p,item) :
        bound=self.profit
        boundweight=self.node_weight
        for i in range(self.depth+1, len(price_of_weight)):
            if(boundweight+weight[item[i-1]]<=w):
                boundweight+=weight[item[i-1]]
                bound+=p[item[i-1]]
            else:
                bound+=price_of_weight[item[i-1]]*(w-boundweight)
                break;
        return bound
#tree만들기
def mktree(weight,S,p,w):
    item, price_of_weight=sortitem(p,weight)
    root=node(0, 0, 0,price_of_weight,w,weight,p,item)
    #1층
    child(root,price_of_weight,w,weight,p,item)
    return root

#tree의 left right달아주기    
def child(root,price_of_weight,w,weight,p,item):
    left=node(root.profit+p[item[root.depth]],root.node_weight+weight[item[root.depth]],root.depth+1,price_of_weight,w,weight,p,item)
    right=node(root.profit,root.node_weight,root.depth+1,price_of_weight,w,weight,p,item)
    root.left=left
    root.right=right
    #len(imte)-1인 이유 root의 depth로 보기때문
    if(root.depth<len(item)-1):
        child(left,price_of_weight,w,weight,p,item)
        child(right,price_of_weight,w,weight,p,item)
 
#item sort + weight당 price
def sortitem(p,weight):
    a=[0]
    for i in range(1,len(weight)):
        a.append(p[i]/weight[i])
    result=[]
    for i in range(len(a)-1):
        maxitem=max(a)
        itemindex=a.index(maxitem)
        result.append(itemindex)
        a[itemindex]=0
    for i in range(1,len(weight)):
        a[i]=(p[i]/weight[i])
    
    return result,a

    
w,S,p,weight=ld.load()
mktree(weight,S,p,w)
