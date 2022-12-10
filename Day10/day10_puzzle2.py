import numpy as np
import copy 
import math

display="." * 240

def addPointCTR(strToReplace, pos):
    return strToReplace[:pos] + "#" + strToReplace[pos+1:]

def updateScore(X, nbcycle, display):
    if (nbcycle == 41):
        a=4
    if ((X-1<=((nbcycle-1) % 40)) and (((nbcycle-1) % 40)<=X+1)):
        display = addPointCTR(display, nbcycle-1)
    return display

linespt=[]
# read inputs
with open('input_day10.txt', 'r') as reader:
    lineCounter=0
    line = reader.readline()
    
    while line != '':                     
        linespt.append( line.strip("\n").split())        
        line = reader.readline()
       
X=1
nbcycle=1

for _, line in enumerate(linespt):
    if line[0] == "noop":
        display = updateScore(X, nbcycle, display) 
        nbcycle +=1
    else:   
        nbRemainingSteps=2
        while nbRemainingSteps != 1:
            display = updateScore(X, nbcycle, display)
            nbcycle +=1
            nbRemainingSteps += -1

        display = updateScore(X, nbcycle, display)
        X += int(line[1])
        #print(int(line[1]))
        nbcycle +=1

print("the ultimate score is :")
for i in range(0,6):
    print(display[40*i:40*i+40])


