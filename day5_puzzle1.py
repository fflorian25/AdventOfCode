

stacks=[[],[],[],[],[],[],[],[],[]]
operations = []
score = 0


def doOperation(stacks, ope):
    for i in range(0,ope[0]):
        stacks[ope[2]-1].append(stacks[ope[1]-1].pop())

with open('input_day5.txt', 'r') as reader:
    line = reader.readline()
    
    while line != '':                     
        linespt =  line.strip("\n")                
        #ininterresting part
        if ( linespt.strip() == "" or linespt[1] == "1"):
            line = reader.readline()
            continue        
        
        #second part        
        elif linespt[0] =="m":
            lineSplit = linespt.split()
            operations.append([int(lineSplit[1]),int(lineSplit[3]),int(lineSplit[5])])
        
        #fisrt part of the input file
        #store each crane in the appropriate stack         
        else :
            for i in range(0,9):
                #take the good number of crane
                crane = linespt[4*i+1]
                if crane != " ":
                    stacks[i].append(crane)
            
        line = reader.readline()
        
#reorder stacks
for i in range(0,9):
    stacks[i].reverse()
    
for ope in operations:
    doOperation(stacks, ope)
  
score=""
for i in range(0,9):
    score += stacks[i].pop()
    
print("the ultimate score is :")
print(score)
    
    
