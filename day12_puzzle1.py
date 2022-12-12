import numpy as np

rawnb=41
colnb=101
# rawnb=5
# colnb=8
totalRecursivity=1000000
sizes={"E": 26, "S": 1, "a":1,"b":2,"c":3, "d":4,"e":5,"f":6, "g":7,"h":8,"i":9, "j":10,"k":11,"l":12,"m":13,"n":14,"o":15, "p":16,"q":17,"r":18, "s":19,"t":20,"u":21, "v":22,"w":23,"x":24, "y":25,"z":26}

class Tile():
    def __init__(self, raw, col, height):
        self.alreadyContaminated = False
        self.parent=None
        self.children=[]
        self.raw = raw
        self.col = col
        self.height = height
        
    def getAlreadyContaminated(self):
        return self.alreadyContaminated 
    
    def setAlreadyContaminated(self, alreadyContaminated):
        self.alreadyContaminated = alreadyContaminated        
        
    def getParent(self):
        return self.parent 
    
    def setParent(self, parent):
        self.parent = parent
    
    def getHeight(self):
        return self.height
    
    def getChildren(self):
        return self.children
            
    def deltaSize(self, heightToCompare):
        return sizes[heightToCompare] - sizes[self.height]
    
    def isParent(self, possibleChild):
        if possibleChild in self.children:
            return True
        else:
            return False
    
    def lookForAdj(self, grid):        
        if (self.col!=0) and (self.deltaSize(grid[self.raw][self.col-1].getHeight()) <= 1) and (grid[self.raw][self.col-1].isParent(self) == False):
            self.children.append(grid[self.raw][self.col-1])
        if (self.raw!=0) and (self.deltaSize(grid[self.raw-1][self.col].getHeight()) <= 1) and (grid[self.raw-1][self.col].isParent(self) == False):
            self.children.append(grid[self.raw-1][self.col])
        if (self.col!=grid.shape[1]-1) and (self.deltaSize(grid[self.raw][self.col+1].getHeight()) <= 1) and (grid[self.raw][self.col+1].isParent(self) == False):
            self.children.append(grid[self.raw][self.col+1])
        if (self.raw!=grid.shape[0]-1) and (self.deltaSize(grid[self.raw+1][self.col].getHeight()) <= 1) and (grid[self.raw+1][self.col].isParent(self) == False):
            self.children.append(grid[self.raw+1][self.col])
        # if (self.col!=0) and (self.deltaSize(grid[self.raw][self.col-1].getHeight()) <= 1) and (grid[self.raw][self.col-1].getAlreadyContaminated() == False):
        #     self.children.append(grid[self.raw][self.col-1])
        # if (self.raw!=0) and (self.deltaSize(grid[self.raw-1][self.col].getHeight()) <= 1) and (grid[self.raw-1][self.col].getAlreadyContaminated() == False):
        #     self.children.append(grid[self.raw-1][self.col])
        # if (self.col!=grid.shape[1]-1) and (self.deltaSize(grid[self.raw][self.col+1].getHeight()) <= 1) and (grid[self.raw][self.col+1].getAlreadyContaminated() == False):
        #     self.children.append(grid[self.raw][self.col+1])
        # if (self.raw!=grid.shape[0]-1) and (self.deltaSize(grid[self.raw+1][self.col].getHeight()) <= 1) and (grid[self.raw+1][self.col].getAlreadyContaminated() == False):
        #     self.children.append(grid[self.raw+1][self.col])           
        
    def dealWithChildren(self):
        for children in self.children:
            # children.setAlreadyContaminated(True)
            children.setParent(self)

grid=np.ndarray(shape=(rawnb,colnb), dtype=Tile)

# read inputs
with open('input_day12.txt', 'r') as reader:
# with open('input_test.txt', 'r') as reader:
    lineCounter=0
    line = reader.readline()
    
    while line != '':                     
        linespt =  line.strip("\n")
        
        colCounter=0
        for i in linespt:
            grid[lineCounter,colCounter]=Tile(lineCounter, colCounter, i)
            colCounter += 1
        
        line = reader.readline()
        lineCounter += 1
       

def recurseFindPath(startingSquare, grid, recursivity=0):
    global totalRecursivity
    recursivity += 1
    
    startingSquare.lookForAdj(grid)
    startingSquare.dealWithChildren()
    
    for child in startingSquare.getChildren():    
        if child.getHeight() == "E":    
            if recursivity < totalRecursivity:
                totalRecursivity = recursivity
        recurseFindPath(child, grid, recursivity)
                
    
       
startSquare=grid[20][0]
finalSquare=grid[20][77]
# startSquare=grid[0][0]
# finalSquare=grid[2][5]
#extract the visibilities
startSquare.setAlreadyContaminated(True)
recurseFindPath(startSquare, grid)

print(startSquare.height)
print(finalSquare.height)
while finalSquare.getHeight() != "S":     
    print('%s:%s' %(finalSquare.raw, finalSquare.col))
    finalSquare=finalSquare.getParent()

print("the ultimate score is :")
print(totalRecursivity)

    
    
