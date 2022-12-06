# read inputs
with open('input_day6.txt', 'r') as reader:
    line = reader.readline()
    
    while line != '':                     
        linespt =  line.strip("\n")  
        line = reader.readline()
        
#create a list of four(teen) letter that will be updated
fourLetter=[]
for i in range(0,14):
    fourLetter.append(linespt[i])
for i in range(15,len(linespt)):
    # if the four letter are different    
    if ( len(set(fourLetter)) == len(fourLetter) ):
        break
    #else delete the first letter and add the last
    fourLetter.pop(0)
    fourLetter.append(linespt[i])    
    
    
print("the ultimate score is :")
print(i)
    
    
