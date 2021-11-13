infinit=99999

#make W
def mW(choose):
    if(choose==1):
        W=[[0, 1, infinit, 1,5],
         [9, 0, 3, 2, infinit],
         [infinit, infinit, 0, 4, infinit ],
         [infinit, infinit, 2, 0, 3],
         [3, infinit, infinit, infinit, 0]]
#새로운 그래프 입력
    elif(choose==2):
        nov=int(input("vertex의 수 : "))
        W=[]
        for i in range(nov):
            str1=input("v"+str(i)+" edge의 weight(띄어쓰기로 구분, infinit=99999입니다.) : ")
            strarray=str1.split(" ")
            for j in range(nov):
                num=int(strarray[j])
                if(j==0):
                    num=[num]
                    W.append(num)
                else:
                    W[i].append(num)
    else:
        print("잘못된 수 입력")
        exit(0)
    return W

#index i-> vertext i+1을 가르킨다.
#make D,P
def mD(W):
    D=W
    P=[]
    for i in range(len(W)):
        for j in range(len(W)):
            if(j==0):
                P.append([0])
            else:
                P[i].append(0)
    for k in range(len(W)):
        for i in range(len(W)):
            for j in range(len(W)):
                if(D[i][j]> D[i][k]+D[k][j]):
                    P[i][j]=k+1
                    D[i][j]=D[i][k]+D[k][j]
    return P,D

#make Path
def mkPath(v1, v2, P):
    #vetex는 indext+1 => vetext i의 인덱스는 i-1이다.
    v1=v1-1
    v2=v2-1
    if(P[v1][v2]!=0):
        mkPath(v1+1, P[v1][v2],P)
        print("v"+str(P[v1][v2])+" ->",end=" ")
        mkPath(P[v1][v2],v2+1,P)