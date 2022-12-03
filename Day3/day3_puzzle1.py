'''
Created on Dec 2, 2022

@author: viennef1
'''

def findSame(pocket1, pocket2):
    errorLetter="0"
    for i in pocket1:
        for j in pocket2:
            if i==j:
                return i

    return errorLetter



priority = {"a":1,  "b":2,  "c":3,  "d": 4,  "e": 5,  "f": 6,  "g": 7,  "h":8,  "i":9,  "j": 10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26,
            "A":27, "B":28, "C":29, "D": 30, "E": 31, "F": 32, "G": 33, "H":34, "I":35, "J": 36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52   }


with open('input_day3.txt', 'r') as reader:
    line = reader.readline()
    elf=[]
    
    while line != '':                
        linespt =  line.strip("\n")
        elf.append(linespt)  
        
        line = reader.readline()


score=0

#Loop on all
for i in range(0,len(elf)):
    #Divide in two
    pocket1=elf[i][0:len(elf[i])/2]
    pocket2=elf[i][len(elf[i])/2:len(elf[i])]

    #Find Same caracter
    sameLetter = findSame(pocket1, pocket2)
    #Return 
    score+=priority[sameLetter]

    
print("the ultimate score is :")
print(score)
    
    
