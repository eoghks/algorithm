def loadfile():
    infile=open("input.txt", "r")
    w=[]
    W=0
    lineList=[]
    for line in infile:
        line=line.rstrip()
        lineList.append(line)
    
    strsqe=lineList[0].split(" ")
    
    for i in strsqe:
        w.append(int(i))
    
    W=int(lineList[1])
    
    return w,W
    

lineList=loadfile()
            
        
    
    