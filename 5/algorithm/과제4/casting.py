#str->intArray
def strToIntArray(str1):
    result=[]
    strList=str1.split(" ")
    for i in range(len(strList)):
        result.append(int(strList[i]))
    return result