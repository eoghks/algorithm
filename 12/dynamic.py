#dynamic approach
import loadfile as ld
#필요한 정보 upload
def knapsack(S,w,p,weight):
    #배열 생성
    P=[]
    for i in range (len(S)+1):
        P.append([0])
    for i in range (w):
        P[0].append(0)
    #기본 작업수
    count=0
    for i in range(1,len(S)+1):
        for j in range (1,w+1):
            if (weight[i]<=j):
                P[i].append(max(P[i-1][j], P[i-1][j-weight[i]]+p[i]))
            else:
                P[i].append(P[i-1][j])
            count+=1
    return P[len(S)][w],count
    
