import numpy as np
rawnb=99
colnb=99
forset=np.zeros((rawnb,colnb))
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
score = 2*forset.shape[0]+2*forset.shape[1]-4

for col  in range (1,forset.shape[0]-1):         
    for raw in range (1,forset.shape[1]-1):
        #left
        #extract all the previous elment in the desired col/line
        subForest = forset[raw,0:col]
        if ( np.max(subForest) < forset[raw,col]):
            score+=1
        else:
            #right
            #extract all the previous elment in the desired col/line
            subForest = forset[raw,col+1:forset.shape[0]]
            if ( np.max(subForest) < forset[raw,col]):
                score+=1
            
            else:
                #up
                #extract all the previous elment in the desired col/line
                subForest = forset[0:raw,col]
                if ( np.max(subForest) < forset[raw,col]):
                    score+=1
               
                else:
                    #below
                    #extract all the previous elment in the desired col/line
                    subForest = forset[raw+1: forset.shape[1],col]
                    if ( np.max(subForest) < forset[raw,col]):
                        score+=1
             
       
       
print("the ultimate score is :")
print(score)

    
    
