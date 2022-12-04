'''
Created on Dec 2, 2022

@author: viennef1
'''
import re
import sys

def findOverlap(sections1Beg, sections1End, sections2Beg, sections2End,):
    if ( (sections1Beg <= sections2Beg) and (sections1End >= sections2End)):
        return 1
    elif ((sections1Beg >= sections2Beg) and (sections1End <= sections2End)):
        return 1
    else:
        return 0

with open('input_day4.txt', 'r') as reader:
    line = reader.readline()
    elf=[]    
    while line != '':                
        linespt =  line.strip("\n")
        linespt= re.split(r'[,-]', linespt)
        elf.append(linespt)  
        
        line = reader.readline()


score=0

#Loop on all
#for i in range(0,10):
for i in range(0,len(elf)):
    #Return 1 if string 1 is contained into string 2 or opposite
    score+=findOverlap(int(elf[i][0]), int(elf[i][1]), int(elf[i][2]), int(elf[i][3]))

    
print("the ultimate score is :")
print(score)
    
    
