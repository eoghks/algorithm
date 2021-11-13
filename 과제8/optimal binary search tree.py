import loadfile as lf
import bsc as b
import tree as tr

data, probability=lf.load()
A,R= b.optsearchtree(probability)

#outcome
print("The number of basic operations performed : ", A[1][len(data)-1],"\n")

#tree생성
s=[]
tr.tree(1,len(data)-1,R,s)
bsctree=tr.BinarySearchTree()
for i in s:
    bsctree.insert(data[i])

#cmd 자동 종료방지
input("종료하시려면 Enter입력하세요")