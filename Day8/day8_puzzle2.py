import numpy as np
rawnb=99
colnb=99
forset=np.zeros((rawnb,colnb))

def distantTaller(subForest, value):
    dist=0
    for i in range(0, len(subForest)):
        if subForest[i] >= value:
            dist+=1
            return dist
        else:
            dist+=1
    return dist



# read inputs
with open('input_day8.txt', 'r') as reader:
    lineCounter=0
    line = reader.readline()
    
    while line != '':                     
        linespt =  line.strip("\n")
        
        colCounter=0
        for i in linespt:
            forset[lineCounter,colCounter]=int(i)
            colCounter += 1
        
        line = reader.readline()
        lineCounter += 1
       
       
#extract the visibilities
score = 0

for col  in range (1,forset.shape[0]-1):         
    for raw in range (1,forset.shape[1]-1):
        scoreTree=1
        #left
        #extract all the previous elment in the desired col/line
        subForest = forset[raw,0:col]
        scoreTree = scoreTree * distantTaller(np.flip(subForest), forset[raw,col])
        
        #right
        #extract all the previous elment in the desired col/line
        subForest = forset[raw,col+1:forset.shape[0]]            
        scoreTree  = scoreTree * distantTaller(subForest, forset[raw,col])
            
        #up
        #extract all the previous elment in the desired col/line
        subForest = forset[0:raw,col]
        scoreTree = scoreTree * distantTaller(np.flip(subForest), forset[raw,col])
        
        #below
        #extract all the previous elment in the desired col/line
        subForest = forset[raw+1: forset.shape[1],col] 
        scoreTree = scoreTree * distantTaller(subForest, forset[raw,col])
                    
        if scoreTree > score :
            score = scoreTree

print("the ultimate score is :")
print(score)

    
    
