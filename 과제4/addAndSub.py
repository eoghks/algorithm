#add function
def addLargeInt(u,v):
    result=[]
    #부호가 같은경우 -> 더해주고 같은부호
    if(u[0]==v[0]):
       sameMSB(u,v,result)

    #부호가 다른경우
    else:
        differentMSB(u,v,result)
    #결과 반환
    return result

#부호가 같은경우의 덧셈
def sameMSB(u,v,result):
    #각자리의 올림수, 더 짧은수의 길이, 긴수의 길이
        addtion= 0 #처음에는 0
        slength = -1
        length = -1
        #더 짧은 수 확인후 길이 정보 저장
        if(len(u)>len(v)) :
            slength= len(v)
            length= len(u)
        else:
            slength=len(u)
            length=len(v)
        #부호 결정
        result.append(u[0])
        #계산(0-> 부호비트 임으로 생략) -> 길이가 짧은수까지
        for i in range(1,slength):
            #올림수가 존재
            if(u[i]+v[i]+addtion>=10):
                result.append((u[i]+v[i]+addtion)%10)
                addtion=1
            #올림수가 없는경우
            else:
                result.append(u[i]+v[i]+addtion)
                addtion=0
        #더 긴쪽 남은 부분 더하기
        #u가 더긴경우
        if(len(u)==length):
            for i in range(slength,length):
                if(u[i]+addtion>=10):
                    result.append((u[i]+addtion)%10)
                    addtion=1
                else:
                    result.append((u[i]+addtion))
                    addtion =0
        #v가 더긴경우
        else:
            for i in range(slength,length):
                if(v[i]+addtion>=10):
                    result.append((v[i]+addtion)%10)
                    addtion=1
                else:
                    result.append((v[i]+addtion))
                    addtion =0

#부호가 다른경우의 덧셈
def differentMSB(u,v,result):
    #빌림수, 짧은숫자의 길이, 긴수의 길이로 구성
    rentNumber=0
    shortInt=[]
    longInt=[]
    #u가 v보다 긴경우
    if(len(u)>len(v)):
        for i in range(len(u)):
            longInt.append(u[i])
        for i in range(len(v)):
            shortInt.append(v[i])
    #u와 v의 길이 같은경우
    elif(len(u)==len(v)):
        #긴 숫자(기본값을 u로하여 두수가 완벽히 같을경우를 생각
        longNum="u"
        #첫자리수 부터 비교( 뒤에서 부터 비교) 
        for i in range(len(u)-1,0,-1):
            if(u[i]>v[i]):
               longNum ="u"
               break
            elif(u[i]<v[i]):
               longNum="v"
               break
            #완벽하게 같은겨우 00을 출력
            if(i==1):
                if(u[i]==v[i]):
                    result.append(0)
                    result.append(0)
                return
        #u가 더큰경우
        if(longNum=="u"):
            for i in range(len(u)):
                longInt.append(u[i])
            for i in range(len(v)):
                shortInt.append(v[i])
        #v가 더큰경우
        else:
            for i in range(len(u)):
                longInt.append(u[i])
            for i in range(len(v)):
                shortInt.append(v[i])
    #그외의 경우
    else:
        for i in range(len(v)):
            longInt.append(v[i])
        for i in range(len(u)):
            shortInt.append(u[i])
    #짧은수의 자릿수를 긴수의 자릿수와 맞춤 앞에 0추가
    for i in range(len(shortInt),len(longInt)):
        shortInt.append(0)
    #부호결정->큰수의 부호를 가짐
    result.append(longInt[0])
    #큰수에서 작은수를 빼줘야한다.
    for i in range(1,len(longInt)):
        #내림수가 필요한경우
        if(longInt[i]-rentNumber>=shortInt[i]):
             result.append(longInt[i]-rentNumber-shortInt[i])
             rentNumber=0
        else:
             result.append(longInt[i]+10-rentNumber-shortInt[i])
             rentNumber=1
    #자릿수가 줄어들어 0이 뒤에 있는경우를 제거 *u==v인경우 위에서 처리
    for i in range(len(result)-1,0,-1):
        if(result[i]==0):
            result.pop()
        else:
            break
    
#sub fucntion * v가 빼주는 수이다.
def subLargeInt(u,v):
    #v의 부호변경-> 덧셈으로 바꿔주기
    if(v[0]==0):
        v[0]=1
    else:
        v[0]=0
    result = addLargeInt(u,v)
    return result