
class Object:
    def __init__(self, worriness):
        self.worriness=worriness

    def getWorriness(self):
        return self.worriness

    def setWorriness(self, worriness):
        self.worriness=worriness


class Monkey:
    def __init__(self, backlog, operation, operationType, test, monkeyTrue, monkeyFalse):
        self.totalInspections = 0
        self.operation = operation
        self.operationType = operationType
        self.test = test
        self.monkeyTrue = monkeyTrue
        self.monkeyFalse = monkeyFalse
        #Transform str to int and create the corresponding object
        self.backlog=[]
        for _, obj in enumerate(backlog):
            self.backlog.append(Object(int(obj)))

    def GetNumberOfInspection(self):
        return self.totalInspections

    def GetNumberOfItem(self):
        return len(self.backlog)

    def firstinLog(self):
        return self.backlog[0]

    def popFirstinLog(self):
        return self.backlog.pop(0)
        
    def pushLastinLog(self, object):
        return self.backlog.append(object)
        
    def doInspection(self):
        self.totalInspections += 1

    def doOperation(self):
        object = self.backlog[0]
        if self.operationType == "+":
            object.setWorriness(object.getWorriness() + self.operation)
            
        elif self.operationType == "*":
            object.setWorriness(object.getWorriness() * self.operation)            
            
        elif self.operationType == "2":
            object.setWorriness(object.getWorriness() * object.getWorriness())

        else :
            print("Operation not permitted !!!!")

    
    def doGetBored(self):
        object = self.backlog[0]
        object.setWorriness(int(object.getWorriness()/3))

    def doTest(self):
        object = self.backlog[0]
        worriness = object.getWorriness()
        if ( worriness % self.test == 0 ):
            return self.monkeyTrue
        else:
            return self.monkeyFalse

monkeyList=[]    

linespt=[]
# read inputs
with open('input_day11.txt', 'r') as reader:
    lineCounter=0
    line = reader.readline()

    backlog=[]
    operation=-1
    operationType="/"
    test=-1
    monkeyTrue=-1
    monkeyFalse=-1
    
    while line != '':                     
        linespt =  line.strip("\n")                
        #create the monkey
        if ( linespt.strip() == ""):
            monkeyList.append(Monkey(backlog, operation, operationType, test, monkeyTrue, monkeyFalse))
        #Monkey i not interresting      
        elif linespt[0] =="M":
            line = reader.readline()
            continue           
        #Starting 
        elif linespt[2] =="S":
            backlog = linespt.split(":")[1].split(",")
        #Operation and Operation Type 
        elif linespt[2] =="O":
            tmpOperation = linespt.split()[-1]
            tmpOperationType = linespt.split()[-2]
            if tmpOperation == "old":
                operation = 0
                operationType = "2"
            else:
                operation = int(tmpOperation)
                operationType = tmpOperationType
        #Test
        elif linespt[2] =="T":
            test = int(linespt.split()[-1])
        #true monkey
        elif  linespt[7] =="t":
            monkeyTrue = int(linespt.split()[-1])
        #false monkey
        elif  linespt[7] =="f":
            monkeyFalse = int(linespt.split()[-1])
        else:
            print(">>>>>>>>>>>>>> T'es nul")

            
            
        line = reader.readline()


for cycle in range(0,20):
    for _, monkey in enumerate(monkeyList):
        for _ in range(0, monkey.GetNumberOfItem()): 
            monkey.doInspection()
            monkey.doOperation()
            monkey.doGetBored()
            toMonkey=monkey.doTest()
            object = monkey.popFirstinLog()
            monkeyList[toMonkey].pushLastinLog(object)



print("the object of each monkey is :")
for _, monkey in enumerate(monkeyList):
    print(monkey.GetNumberOfItem())

print("the total inspection of each monkey is :")
totInpsections=[]
for _, monkey in enumerate(monkeyList):
    totInpsections.append(monkey.GetNumberOfInspection())
    print(monkey.GetNumberOfInspection())

totInpsections.sort()
score=totInpsections[-1]*totInpsections[-2]

print("the ultimate score is :")
print(score)