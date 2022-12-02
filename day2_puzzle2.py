'''
Created on Dec 2, 2022

@author: viennef1
'''
draw=3
win=6
loose=0

def rps(adv1, adv2):
    if (adv1 == "A"):
        if (adv2 == "X"):
            return draw
        elif (adv2 == "Y"):     
            return win       
        elif (adv2 == "Z"):
            return loose
        else:
            print("t es nul")
            
            
    elif (adv1 == "B"):
        if (adv2 == "X"):
            return loose
        elif (adv2 == "Y"):  
            return draw     
        elif (adv2 == "Z"):
            return win    
        else:
            print("t es nul")


    elif (adv1 == "C"):
        if (adv2 == "X"):
            return win                
        elif (adv2 == "Y"):   
            return loose  
        elif (adv2 == "Z"):
            return draw
        else:
            print("t es nul")
            
    else:
        print("t es nul")
            

with open('input_day2.txt', 'r') as reader:
    line = reader.readline()
    elf=[]
    
    while line != '':                
        linespt =  line.strip("\n").split(" ")
        elf.append(linespt)  
        
        line = reader.readline()
        
pts ={}
pts["X"]=1
pts["Y"]=2
pts["Z"]=3

score=0
for i in range(0,len(elf)):
    score += pts[elf[i][1]]
    score += rps(elf[i][0], elf[i][1])
    
print("the ultimate score is :")
print(score)
    
    
