class History:
    def __init__(self, numbers):
        self.line = []
        firstLine = [int(num) for num in numbers] 
        self.line.append(firstLine)

    def compute_next_line(self):
        previousLine = self.line[-1]
        nextLine=[]

        firstItem = previousLine[0]
        for secondItem in previousLine[1:]:
            nextLine.append(secondItem-firstItem)
            firstItem=secondItem

        self.line.append(nextLine)

    def is_null_line(self):
        if sum(self.line[-1]) == 0:
            return True
        else:
            return False
        
    def add_next_history(self, iteration = 0):
        depth = len(self.line)-iteration-1-1
        self.line[depth].insert(0, self.line[depth][0] - self.line[depth+1][0])
        if depth != 0:
            self.add_next_history(iteration + 1)
     
    def last_in_history(self):
        return self.line[0][0]
        
    @classmethod
    def create_all_line(cls, histories):
        for history in histories:
            while not history.is_null_line():
                history.compute_next_line()


# reading from file
filename = "2023/Day9/input.txt"
histories = []

with open(filename, 'r') as f:
    lines = f.readlines()   
    for line in lines:
        numbers = line.split(" ")
        history=History(numbers)
        histories.append(history)
    

def print_summary(historis):
    for i, history in enumerate(historis, start=1):
        print(f"History {i}:")
        print(f"Line: .{history.line}.")
        print("-------------------------")
#print_summary(histories)

#create all line of each history
History.create_all_line(histories)
#print_summary(histories)

#extrapolate
for history in histories:
    history.add_next_history()
#print_summary(histories)

#look for prediction
tot=0
for history in histories:
    tot += history.last_in_history()

print(f"Total Extrapolation: {tot}")