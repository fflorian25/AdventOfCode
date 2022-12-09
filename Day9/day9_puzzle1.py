import numpy as np

linespt=[]
# read inputs
with open('input_day9.txt', 'r') as reader:
# with open('input_test.txt', 'r') as reader:
    lineCounter=0
    line = reader.readline()
    
    while line != '':                     
        linespt.append( line.strip("\n").split())        
        line = reader.readline()
       
score = 0
direction={}
direction['R']=np.array([1,0])
direction['L']=np.array([-1,0])
direction['U']=np.array([0,1])
direction['D']=np.array([0,-1])

posH=np.array([0,0])
posT=np.array([0,0])
strPosT=[]

for _, line in enumerate(linespt): 
    nbRemainingSteps=int(line[1])
    dirSteps=direction[line[0]]
    
    while nbRemainingSteps!=0:
        strPosT.append(str(posT[0])+":"+str(posT[1]))
        
        posH += dirSteps
        distHT=posH-posT
        print(posH)
        print(posT)
        if (abs(distHT[0]) > 1) or (abs(distHT[1]) > 1):
            posT=posH -dirSteps
        
        nbRemainingSteps+=-1
    
strPosT.append(str(posT[0])+":"+str(posT[1]))    
print(strPosT) 

score=len(set(strPosT))
print(set(strPosT))
print("the ultimate score is :")
print(score)

    
    
