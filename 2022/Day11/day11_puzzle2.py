import timeit

class Object:
    def __init__(self, worriness):
        self.worriness=worriness

    def getWorriness(self):
        return self.worriness

    def setWorriness(self, worriness):
        self.worriness=worriness


class Monkey:
    modulus = 1
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

    def doOperation(self,modulus):
        object = self.backlog[0]
        if self.operationType == "+":
            object.setWorriness(object.getWorriness() + self.operation)
            
        elif self.operationType == "*":
            object.setWorriness(object.getWorriness() * self.operation)            
            
        elif self.operationType == "2":
            object.setWorriness(object.getWorriness() * object.getWorriness())

        else :
            print("Operation not permitted !!!!")

        
        object.setWorriness(object.getWorriness() % modulus)

    
    def doGetBored(self):
        pass
        #object = self.backlog[0]
        #object.setWorriness(int(object.getWorriness()/3))

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


for _, monkey in enumerate(monkeyList): 
    Monkey.modulus *= monkey.test 

activateTrace = False
for cycle in range(0,10000):
    for _, monkey in enumerate(monkeyList):
        for _ in range(0, monkey.GetNumberOfItem()): 
            # record start time
            t_0 = timeit.default_timer()            
            monkey.doInspection()
            # record time
            t_1 = timeit.default_timer()
            monkey.doOperation(Monkey.modulus)
            # record time
            t_2 = timeit.default_timer()
            monkey.doGetBored()
            # record time
            t_3 = timeit.default_timer()
            toMonkey=monkey.doTest()
            # record time
            t_4 = timeit.default_timer()
            object = monkey.popFirstinLog()
            # record time
            t_5 = timeit.default_timer()
            monkeyList[toMonkey].pushLastinLog(object)
            # record time
            t_6 = timeit.default_timer()

            if (activateTrace == True):
                # calculate elapsed time and print
                elapsed_time1 = round((t_1 - t_0) * 10 ** 6, 3)
                print(f"doInpection: {elapsed_time1} µs") 
                elapsed_time2 = round((t_2 - t_1) * 10 ** 6, 3)
                print(f"doOperation: {elapsed_time2} µs") 
                elapsed_time3 = round((t_3 - t_2) * 10 ** 6, 3)
                print(f"doGetBored: {elapsed_time3} µs") 
                elapsed_time4 = round((t_4 - t_3) * 10 ** 6, 3)
                print(f"doTest: {elapsed_time4} µs") 
                elapsed_time5 = round((t_5 - t_4) * 10 ** 6, 3)
                print(f"popFirstinLog: {elapsed_time5} µs") 
                elapsed_time6 = round((t_6 - t_5) * 10 ** 6, 3)
                print(f"pushLastinLog: {elapsed_time6} µs") 



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