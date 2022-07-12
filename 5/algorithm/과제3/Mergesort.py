#str->int[]
def strToIntArray(str):
    strList=str.split(" ")
    intList=[]
    for i in strList:
        intList.append(int(i))
    return intList

#int[]->str
def intArrayToStr(intArray):
    output=""
    for i in intArray:
        output=output+str(i)+" "
    return output

#나누고 합병하는 함수
def mergesort(intArray, start, end):
    if(start<end):#나눌것이 있으면
        mid=(start+end)//2
        #divde
        mergesort(intArray,start,mid)
        mergesort(intArray,mid+1,end)
        global divide
        divide= divide+1
        #conquer
        merge(intArray,start,mid,end)
        global conquer
        conquer=conquer+1

#순서대로 정렬하면서 합병하는 함수
def merge(intArray,start,mid,end):
    #start,mid를 증가시키며 비교를 통해 저장할것이므로 처음 start와 mid를 저장
    startpoint=start
    midpoint=mid+1
    #정렬된 배열 저장
    sortedList=[]

    #각수를 비교하여 적은숫자 새로운 리스트에 삽입
    while(startpoint<=mid and midpoint<=end):
        if(intArray[startpoint]<intArray[midpoint]):
            sortedList.append(intArray[startpoint])
            startpoint=startpoint+1
        else:
            sortedList.append(intArray[midpoint])
            midpoint=midpoint+1

    if(startpoint>mid):#앞부분이 다들어간경우
        for i in range(midpoint, end+1):
            sortedList.append(intArray[i])

    else:#뒷부분이 다들어간경우
        for i in range(startpoint, mid+1):
            sortedList.append(intArray[i])

    #정렬전 리스트 ->정렬후 리스트이 값으로 교체
    for i in range(start,end+1):
        intArray[i]=sortedList[i-start]#i-start의이유 intarry는 start~end지점까지 인덱스를 sortedList의경우 start-start~end-start의 인덱스이 크기를 가지기 때문

#main    
divide=0;#나눈횟수
conquer=0#conquer한 횟수  

inputStr=input("any strings having a squence of integer : ")
intArray=strToIntArray(inputStr)
mergesort(intArray,0,len(intArray)-1)
output=intArrayToStr(intArray)
print(output)
print("divde : ", divide, "conquer : ", conquer)

#cmd로 실행시 종료되지 않도록
input("종료하시려면 엔터키를 눌러주세요.")
