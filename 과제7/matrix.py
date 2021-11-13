def getmatrix(matrix):
    infile = open("matrix.txt", "r")

    #matrix 저장에 사용할 변수
    count=0
    row=0
    colum=0
    matrixNum=0

    for line in infile:
        line=line.rstrip()
        if(count==row):
            #row/colum 구하기
            lineList=line.split(" : ")
            rc=lineList[1]
            rcList=rc.split(", ")
            rcList=list(map(int, rcList))
            row=int(rcList[0])
            colum=int(rcList[1])
            #각 행렬의 matrix[i][0][0]=> row, matrix[i][0][1]=>colum을 나타낸다.
            matrix.append([rcList])
            count=0
        else:
            strList=line.split(" ")
            intList=[]
            #각 요소 int 로 배열에 저장
            for i in range(len(strList)):
                intList.append(int(strList[i]))
            #cloum의 수가 잘못된경우 종료
            if(len(intList) != colum):
                print("입력 matrix에 오류가 있습니다.")
                exit(0)
            #matrix에 각 행 추가
            matrix[matrixNum].append(intList)
            count+=1
            #입력된 행렬의수가 +1증가
            if(count==row):
                matrixNum+=1
