import numpy as np
import copy 
import math

cycleToBeLookFor=[20, 60, 100, 140, 180, 220]

def updateScore(X, nbcycle):
    score = 0        
    if (  nbcycle in cycleToBeLookFor ):
        score = nbcycle * X        
    return score

linespt=[]
# read inputs
with open('input_day10.txt', 'r') as reader:
    lineCounter=0
    line = reader.readline()
    
    while line != '':                     
        linespt.append( line.strip("\n").split())        
        line = reader.readline()
       
X=1
score=0
nbcycle=1

for _, line in enumerate(linespt):
    if line[0] == "noop":
        score += updateScore(X, nbcycle) 
        nbcycle +=1
    else:   
        nbRemainingSteps=2
        while nbRemainingSteps != 1:
            score += updateScore(X, nbcycle)
            nbcycle +=1
            nbRemainingSteps += -1

        score += updateScore(X, nbcycle)
        X += int(line[1])
        #print(int(line[1]))
        nbcycle +=1

print("the ultimate score is :")
print(score)