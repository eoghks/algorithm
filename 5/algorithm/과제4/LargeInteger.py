from addAndSub import *
from math10M import *

#String to intArray function
def saveArray(largeInt, list1):
    #음수->1
    if(largeInt[0]=='-'):
        list1.append(1)
    #양수->0 
    else :
        list1.append(0)
    #reminder save
    for i in range(len(largeInt)-1,0,-1) :
        list1.append(int(largeInt[i]))
    #양수일 경우 str[0] save
    if(list1[0]==0):
        list1.append(int(largeInt[0]))

#Array->string
def arrayToString(u):
    str1=""
    #음수인 경우 -부호 추가
    if(u[0]==1):
        str1="-"
    else:
        str1=""
    for i in range(len(u)-1,0,-1):
        str1=str1+str(u[i])
    return str1

#main
uString=input("u : ")
vString=input("v : ")
m =int(input("m : "))

#String to intArray
u=[] 
v=[]
saveArray(uString,u)
saveArray(vString,v)

#+,-확인
uAddv=addLargeInt(u,v)
uSubv=subLargeInt(u,v)
struAddv=arrayToString(uAddv)
struSubv=arrayToString(uSubv)
print("u + v = Large Integer :", struAddv)
print("u - v = Large Integer :", struSubv)
print("u*10^%d= LaregeInteger : %s"%(m,mulTenM(uString, m)))
print("u/10^%d= LaregeInteger : %s"%(m,divTenM(u,m)))
print("u%10",end="")
print("^%d= LaregeInteger : %s"%(m,modTenM(u,m)))
#cmd실행시 자동종료 방지
input("종료하시려면 Enter를 입력하세요.")
