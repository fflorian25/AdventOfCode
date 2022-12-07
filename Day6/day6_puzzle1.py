# read inputs
with open('input_day6.txt', 'r') as reader:
    line = reader.readline()
    
    while line != '':                     
        linespt =  line.strip("\n")  
        line = reader.readline()
        
#create a list of four letter that will be updated
fourLetter=[linespt[0],linespt[1],linespt[2],linespt[3]]
for i in range(4,len(linespt)):
    # if the four letter are different    
    if ( len(set(fourLetter)) == len(fourLetter) ):
        break
    #else delete the first letter and add the last
    fourLetter.pop(0)
    fourLetter.append(linespt[i])    
    
    
print("the ultimate score is :")
print(i)
    
    
