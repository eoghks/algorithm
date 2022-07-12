#*10^m 함수
def mulTenM(str1,m):
    result=str1
    for i in range(m):
        result=result+"0"
    return result

#/10^m 함수
def divTenM(list1, m):
    result=""
    #10^m이 더큰경우
    if(len(list1)-1<=m):
        return "0"
    #음수의 경우 -추가
    if(list1[0]==1):
        result='-'
    for i in range(len(list1)-1, m, -1):
        result=result+str(list1[i])

    return result

#%10^m 함수
def modTenM(list1, m):
    result=""
    if(list1[0]==1):
        result="-"
    for i in range(m,0,-1):
        result=result+str(list1[i])

    return result
