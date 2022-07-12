#make binomal coefficient
def makebin(n):
    list1=[]
    for i in range(n+1):
        #k<=n이므로 k가 n을 넘을 필요없다.
        for j in range(i+1):
            #j=0일때 이차원 list를 위해 [1]추가
            if(j==0):
                list1.append([1])
            #j=i일때 1
            elif(j==i):
                list1[i].append(1)
            #B[i][j]=B[i-1]B[j-1]+B[i-1][j]
            else:
                list1[i].append(list1[i-1][j-1]+list1[i-1][j])
    return list1

#expression of (a+b)^n 구하는 함수
def makeexpression(n,binList):
    output=""
    #sigma(i=0 to n) combine(n,i) a^i+b^n-i
    for i in range(n+1):
        section=""
        #binList[n][0]=1이므로 1생략
        if(i==0):
            section="+"+"b^"+str(n-i)
        #binList[n][n]=1이므로 1생략
        elif(i==n):
            section="a^"+str(i)
        else:
            #a^1 or b^1제거
            if(i==1):
                section="+"+str(binList[n][i])+"a"+"b^"+str(n-i)
            elif(i==n-1):
                section="+"+str(binList[n][i])+"a^"+str(i)+"b"
            else:
                section="+"+str(binList[n][i])+"a^"+str(i)+"b^"+str(n-i)
        #b^n부터 나오기때문에 a^n이 앞으로 나오도록 앞에 section을 더해줌
        output=section+output
    return output
#main
n = int(input("N : "))
#combine 저장 배열
binList=makebin(n)

#output
output=makeexpression(n,binList)
print("(a+b)^"+str(n)+" = "+output)

#cmd자동종료 방지
input("종료하시려면 Enter를 눌러주세요.")

