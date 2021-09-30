from casting import *
from quicksort import *
#main
#input
inStr=input("any strings having a sequence of integers : ")
inArray=strToIntArray(inStr)
#ouput변수
prepviotindex=-1
sortList=[]
output=[0,0]#dvide, conquer
#연산
quicksort(inArray,sortList,prepviotindex,output)
#output
print(sortList)
print("divide : %d, conquer : %d"%(output[0], output[1]))
#cmd자동종료 방지
input("종료하시려면 Enter키를 눌러주세요")