import loadfile as ld

def sum_of_subests(i, weight,total, include):
    new_include=include
    if (promising(i, weight, total)):
        if(weight==W):
            for j in range(1,len(w)):
                if(include[j]==1):
                    print(w[j], end=" ")
                if(j==len(w)-1):
                    print("\n")
        else:
            new_include[i+1]=1
            sum_of_subests(i+1, weight+w[i+1], total-w[i+1], new_include)
            new_include[i+1]=0
            sum_of_subests(i+1, weight, total-w[i+1], new_include)

def promising(i, weight, total):
    check=((weight+total >=W) and (weight==W or weight+w[i+1] <=W))
    return check


w,W=ld.loadfile()
#w배열을 0~n까지 존재하게하기위해 
w.insert(0, -1)
#include 초기화 0=no, 1=yes
include=[]
for i in range(len(w)):
    include.append(0)
#total구하기
total=0
for i in range(1,len(w)):
    total=total+w[i]


sum_of_subests(0,0,total,include)

