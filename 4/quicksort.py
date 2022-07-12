def quicksort(intList,sortList,prepivotindex,output):
    #배열에 아무것도 없는경우
    if(len(intList)==0):
        return 
    pivot=intList[0]
    #함수에 처음들어온경우
    if(prepivotindex==-1):
         sortList.append(pivot)
         prepivotindex=0
    #재귀가 일어난경우
    else:
        #이전 pivot>현재 pivot
        if(sortList[prepivotindex]>pivot):
             sortList.insert(prepivotindex,pivot)
             #새로운  pivot을 넣었으니 이전 pivot인덱스는 현재 pivot인덱스
             prepivotindex=prepivotindex
         #이전 pivot<현재 pivot
        else:
            sortList.insert(prepivotindex+1,pivot)
            #새로운  pivot을 넣었으니 이전 pivot인덱스는 현재 pivot인덱스
            prepivotindex=prepivotindex+1
        output[1]=output[1]+1
    #더이상 나눌 배열이 없는경우 리턴
    if(len(intList)==1):
        return 
    #배열의 크기가 2인상인경우
    else:
        lowList=[]
        highList=[]
        #2개의 배열로 나누기 pivot작으면 lowlist, pivot보다 크면 highlsit
        for i in range(1,len(intList)):
            if(pivot>intList[i]):
                lowList.append(intList[i])
            else:
                highList.append(intList[i])
        output[0]=output[0]+1
        quicksort(highList,sortList,prepivotindex,output)
        prepivotindex=sortList.index(pivot)
        quicksort(lowList,sortList,prepivotindex,output)
        return 

    