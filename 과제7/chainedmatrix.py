def minM(i,j,M,d):
    element=[]
    for k in range(i,j):
        element.append(M[i][k]+M[k+1][j]+d[i]*d[k+1]*d[j+1])
    #i+k의 inde가 최소이기 때무넹 i를 element index에 더해준다.
    return min(element), i+element.index(min(element))

def minmulti(matrixNum,d):
    M=[]
    P=[]
    for i in range (matrixNum):
        M.append([])
        P.append([])
        for j in range(i+1):
            if(i==j):
                M[i].append(0)
            #쓰지 않는 곳은 -1로 초기화 해놓기(list는 앞에를 채워줘야 하기때문)
            else:
                M[i].append(-1)
            #P배열중 안쓸곳 -1로 채워 놓기
            P[i].append(-1)    
    for diag in range(1, matrixNum):
        for i in range(matrixNum-diag):
            j=i+diag
            min_mul, k=minM(i,j,M,d)
            M[i].append(min_mul)
            P[i].append(k)
    return M,P

def order(i,j,P):
    if(i==j):
        print(i+1,end="")
    else:
        k=P[i][j]
        print("(",end="")
        order(i,k,P)
        order(k+1,j,P)
        print(")",end="")
