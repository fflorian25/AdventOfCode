'''
Created on Dec 1, 2022

@author: viennef1
'''
with open('input_day1.txt', 'r') as reader:
    line = reader.readline()
    elf=[0]
    
    while line != '':                
        if line.strip() != "":
            elf[len(elf)-1] += int(line)            
        else :
             elf.append(0)
                          
        line = reader.readline()
        
max_elf=0
for i in range(1, len(elf)):
    if elf[i]>elf[max_elf]:
        max_elf=i
        
print("elf with max food :" )
print(max_elf+1)
print("food of this elf :" )
print(elf[max_elf])
    
