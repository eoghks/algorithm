import loadfile as lf

def optsearchtree(p):
    #index0은 임의로 집어넣엇으니 총 수는 len-1
    num=len(p)-1
    A,R= mkMatrix(num)

    for i in range (1,num+1):
        for j in range(i):
            A[i].append(0)
            R[i].append(0)
        A[i].append(p[i])
        R[i].append(i)
        
    for i in range(num+1):
        A[num+1].append(0)
        R[num+1].append(0)

    for diag in range(1,num):
        for i in range(1,num-diag+1):
            j= i+diag
            minAIJ=minimize(i,j,A,R)+sumP(i,j,p)
            A[i].append(minAIJ)
    return A,R

def minimize(i,j,A,R):
    list1=[999999]
    for k in range(i,j+1):
        list1.append(A[i][k-1]+A[k+1][j])
    mini=min(list1)
    R[i].append(i-1+list1.index(mini))
    return mini    

def sumP(i,j,p):
    sump=0
    for k in range(i,j+1):
        sump+=p[k]
    return sump

def mkMatrix(num):
    A=[]
    R=[]

    #0~n까지 index필요 1~n+1까지 index 필요 -> 1~n+1까지 index필요
    for i in range (num+2):
        A.append([])
        R.append([])
    
    return A,R

