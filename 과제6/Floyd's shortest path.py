import make as mk
#main

#새로운 그래프를 받거나 기존 그래프를 사용
choose =int(input("1. 강의자료 그래프 사용 2. 새로운 그래프 입력 => 1 혹은 2 입력 : "))
print("\ninfinit값은 999999입니다. vertex 1~n까지 존재합니다.\n")
#infinit => 매우큰수 99999를 사용하겠습니다.
infinit=999999
#강의 자료 그래프 사용
W=mk.mW(choose)
v1=int(input("출발지 vertex : "))
v2=int(input("도착지 vertex : "))

#D:최단 경로 길이 저장 P:path저장
P, D=mk.mD(W)

print("v"+str(v1)+" ->",end=" ")
mk.mkPath(v1,v2,P)
print("v"+str(v2), ", v"+str(v1)+" -> v"+str(v2)+"의 최단 경로 길이 : "+str(D[v1-1][v2-1]))

#cmd 자동종료 방지
input("종료하시려면 Enter키를 누르세요")