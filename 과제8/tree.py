class Node ():
    def __init__(self, data) :
         self.data=data
         self.left=None
         self.right=None
    
class BinarySearchTree ():
    def __init__(self) :
        self.root=None
    
    def insert(self, data):
        self.root=self.insertValue(self.root, data)
        return self.root is not None

    def insertValue(self, node, data):
        if(node==None):
            node= Node(data)
        else:
            if data <= node.data:
                node.left=self.insertValue(node.left, data)
            else:
                node.right=self.insertValue(node.right, data)
        return node

#t=tree를 의미
def tree(i, j, R, sort):
    k=R[i][j]
    if(k==0):
        return
    else:
        sort.append(k)
        tree(i,k-1, R,sort)
        tree(k+1,j, R,sort)

