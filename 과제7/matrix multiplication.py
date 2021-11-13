import matrix as mt
import chainedmatrix as cm

matrix=[]
#matirx 얻기
mt.getmatrix(matrix)

'''#매트릭스 확인
for i in range(len(matrix)):
    print("matrix %d"%(i+1))
    for j in range(len(matrix[i][0])+1):
        print(matrix[i][j])'''
#matrix의 수 dlist생성 d0~dn까지 존재
matrixNum=len(matrix)
d=[]
for i in range(matrixNum):
    d.append(matrix[i][0][0])
d.append(matrix[matrixNum-1][0][1])

M,P=cm.minmulti(matrixNum,d)

#out put
print("number of basic operations : ", M[0][matrixNum-1])
print("the optimal sequence of multiplication : ",end="")
cm.order(0,matrixNum-1,P)
print("")

input("종료하시려면 enter를 누르세요.")

