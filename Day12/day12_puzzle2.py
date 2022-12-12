import numpy as np

rawnb=41
colnb=101
sizes={"E": 26, "S": 1, "a":1,"b":2,"c":3, "d":4,"e":5,"f":6, "g":7,"h":8,"i":9, "j":10,"k":11,"l":12,"m":13,"n":14,"o":15, "p":16,"q":17,"r":18, "s":19,"t":20,"u":21, "v":22,"w":23,"x":24, "y":25,"z":26}

class Tile():
    def __init__(self, raw, col, height):
        self.alreadyContaminated = False
        self.parent=None
        self.children=[]
        self.raw = raw
        self.col = col
        self.height = height

    def reset(self):
        self.alreadyContaminated = False
        self.parent=None
        self.children=[]
        
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
        adjList=[]      
        if (self.col!=0) and (self.deltaSize(grid[self.raw][self.col-1].getHeight()) <= 1) and (grid[self.raw][self.col-1].getAlreadyContaminated() == False):
            adjList.append(grid[self.raw][self.col-1])
        if (self.raw!=0) and (self.deltaSize(grid[self.raw-1][self.col].getHeight()) <= 1) and (grid[self.raw-1][self.col].getAlreadyContaminated() == False):
            adjList.append(grid[self.raw-1][self.col])
        if (self.col!=grid.shape[1]-1) and (self.deltaSize(grid[self.raw][self.col+1].getHeight()) <= 1) and (grid[self.raw][self.col+1].getAlreadyContaminated() == False):
            adjList.append(grid[self.raw][self.col+1])
        if (self.raw!=grid.shape[0]-1) and (self.deltaSize(grid[self.raw+1][self.col].getHeight()) <= 1) and (grid[self.raw+1][self.col].getAlreadyContaminated() == False):
            adjList.append(grid[self.raw+1][self.col])   

        return adjList        


grid=np.ndarray(shape=(rawnb,colnb), dtype=Tile)

# read inputs
with open('input_day12.txt', 'r') as reader:
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
       

def FindPath(startingSquare, grid, recursivity=0):
    startingList=[]
    startingList.append(startingSquare)

    while recursivity < 1000: 
        recursivity += 1   
        newListAdj=[]        
        for _, elmt in enumerate(startingList):   
            childList=elmt.lookForAdj(grid)
            for _, child in enumerate(childList):
                child.setAlreadyContaminated(True)
                child.setParent(elmt)
                newListAdj.append(child)
                 
                if child.getHeight() == "E":    
                    return recursivity 
 
        startingList=newListAdj
    

def resetGrid(grid):         
    for raw in grid:
        for tile in raw:
            tile.reset()

startList=[]
#Find all starting point       
for raw in grid:
    for tile in raw:
        if sizes[tile.getHeight()] == 1:
            startList.append(tile)
        
finalSquare=grid[20][77]
#extract the visibilities
score = []
for _,startSquare in enumerate(startList):    
    startSquare.setAlreadyContaminated(True)
    score.append(FindPath(startSquare, grid))
    resetGrid(grid)

#remove None
res = [i for i in score if i is not None]
res.sort()

print("the ultimate score is :")
print(res[0])

    
    
