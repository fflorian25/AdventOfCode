import numpy as np
import copy 
import math

linespt=[]
# read inputs
with open('input_day9.txt', 'r') as reader:
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

pos=np.zeros((10,2), dtype = int)
strPosT=[]

for _, line in enumerate(linespt): 
    nbRemainingSteps=int(line[1])
    dirSteps=direction[line[0]]
    
    while nbRemainingSteps!=0:
        strPosT.append(str(pos[9][0])+":"+str(pos[9][1]))
        
        pos[0] += dirSteps
        for i in range(1,10):
            distHT=pos[i-1]-pos[i]
            #if need to move
            if (abs(distHT[0]) > 1) or (abs(distHT[1]) > 1):
                #go to the nearest postion adjacent (not in diag) from pos[i-1].
                #distHT is necessary <= 2 on one axis, and =1 on the other. 
                #so np.fix(distHT/2) will be equal to [1,0], [-1,0], [0,1] or [-1, 0] depending on where the pos[i] is from pos[i-1]
                pos[i]= pos[i-1] - np.fix(distHT/2)
        nbRemainingSteps+=-1
    
strPosT.append(str(pos[9][0])+":"+str(pos[9][1]))  

score=len(set(strPosT))
print("the ultimate score is :")
print(score)