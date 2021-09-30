#String -> int[]함수
def inputStringToIntArray(inputString):
    stringList=inputString.split(" ")
    intarray=[]
    for i in stringList:
        intarray.append(int(i))
    return intarray
#search 함수
def binarysearch(sortedint, key):
    start=0 #시작 index
    end=len(sortedint)-1 #마지막 index
    while(start<=end):
        #중간값 확인
        mid=(start+end)//2
        #중간 값과 같을경우 mid값 리턴
        if key == sortedint[mid]: 
            return mid
        #key<중간값인경우 왼쪽 배열확인
        elif key < sortedint[mid]:
            end = mid-1
        #key>중간값인경우 오른쪽 배열확
        else :
            start = mid+1
    return "none"

#입력    
inputString=input("String with a sequence of sorted integers: ")
key=int(input("target integer :"))
sortedint=inputStringToIntArray(inputString)
#출력
output = binarysearch(sortedint, key)
if output=="none":
    print(output)
else :
    print("%d는 %d번째에 위치합니다."%(key, output+1))

#cmd자동꺼짐 방지
input("종료하시려면 엔터키를 누르세요.")

