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
   
elf.sort(reverse=True)
        
print("food of top three  elf :" )
print(elf[0])
print(elf[1])
print(elf[2])
print("total food of top three  elf :" )
print(elf[0]+ elf[1] +elf[2])
    
