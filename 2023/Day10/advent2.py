from enum import Enum
import copy

from functools import total_ordering

class Direction(Enum):
    GROUND = "."
    VERTICAL = "|"
    HORIZONTAL = "-"
    NORTHEAST = "L"
    NORTHWEST = "J"
    SOUTHWEST = "7"
    SOUTHEAST = "F"
    STARTING = "S"

    @classmethod
    def from_string(cls, value):
        mapping = {
            "." : cls.GROUND,
            "|" : cls.VERTICAL,
            "-" : cls.HORIZONTAL,
            "L" : cls.NORTHEAST,
            "J" : cls.NORTHWEST,
            "7" : cls.SOUTHWEST,
            "F" : cls.SOUTHEAST,
            "S" : cls.STARTING 
        }
        return mapping.get(value, None)
    
    def connected_to(self):
        connectsTo=[]
        if self == Direction.VERTICAL:
            connectsTo.append([ 0, 1])
            connectsTo.append([ 0,-1])
        if self == Direction.HORIZONTAL:
            connectsTo.append([ 1, 0])
            connectsTo.append([-1, 0])
        if self == Direction.NORTHEAST:
            connectsTo.append([ 0, 1])
            connectsTo.append([ 1, 0])
        if self == Direction.NORTHWEST:
            connectsTo.append([ 0, 1])
            connectsTo.append([-1, 0])
        if self == Direction.SOUTHEAST:
            connectsTo.append([ 0,-1])
            connectsTo.append([ 1, 0])
        if self == Direction.SOUTHWEST:
            connectsTo.append([ 0,-1])
            connectsTo.append([-1, 0])
        return connectsTo
    

class Tile:
    def __init__(self, wIndex, hIndex, string):
        #grid position
        self.widthIndex = wIndex
        self.heightIndex = hIndex

        self.direction = Direction.from_string(string)

        self.parent = None
        self.relativeParentWIndex = 0
        self.relativeParentHIndex = 0

        self.symbol=string

        #Currently only one parent and one child is possible (except starting point)
        self.child= None
        
        #How far are we from home ?
        self.childNumber = 0

    def compute_next_child_position(self):
        connectsTo = self.direction.connected_to()
        if connectsTo[1][0] == self.relativeParentWIndex and connectsTo[1][1] == self.relativeParentHIndex :
            connectsTo.pop(1)
        if connectsTo[0][0] == self.relativeParentWIndex and connectsTo[0][1] == self.relativeParentHIndex :
            connectsTo.pop(0)            
        #assert the size is only one, as it shall be
        assert len(connectsTo) == 1, f"Not One Child found for this tile"

        return connectsTo 
    
    def update(self, parent):
        self.parent = parent
        parent.child = self
        self.relativeParentWIndex = parent.widthIndex - self.widthIndex
        self.relativeParentHIndex = parent.heightIndex - self.heightIndex
        self.childNumber = parent.childNumber + 1

    #Find the tile (parent or child) with another height w/t to this one
    def other_height(self):
        if self.parent.heightIndex != self.heightIndex:
            return self.parent.heightIndex
        else:
            return self.child.heightIndex


def look_for_child_by_index(tiles, wIndex, hIndex):
    for tile in tiles:
        if getattr(tile, "widthIndex") == wIndex and getattr(tile, "heightIndex") == hIndex:
            return tile


# reading from file
filename = "2023/Day10/input.txt"
tiles = []

maxWidth=0
maxHeight=0
with open(filename, 'r') as f:
    lines = f.readlines() 
    for i, line in enumerate(lines):
        for j, letter in enumerate(line.rstrip()):
            tile=Tile(j,i,letter)
            tiles.append(tile)
            if j > maxWidth:
                maxWidth = j        
        if i > maxHeight:
            maxHeight = i

#For easier reading, renumber the height of the tile
for tile in tiles:
    tile.heightIndex = maxHeight - tile.heightIndex

def print_summary(tiles):
    for i, tile in enumerate(tiles, start=1):
        print(f"Tile {i}:")
        print(f"Width: .{tile.widthIndex}.")
        print(f"Height: .{tile.heightIndex}.")
        print(f"Direction: .{tile.direction}.")
        print(f"ChildNumber: .{tile.childNumber}.")
        print("-------------------------")
#print_summary(tiles)

#look for starting point
starting = None
for tile in tiles:
    if getattr(tile, "direction") == Direction.STARTING:
        starting = tile
        break  

#print(starting.widthIndex)
#print(starting.heightIndex)

#look for two children for the starting point on the four sides
left=None 
for tile in tiles:
    if getattr(tile, "widthIndex") == starting.widthIndex -1 :
        if getattr(tile, "heightIndex") == starting.heightIndex :
            left=tile    
            break    
        
right=None 
for tile in tiles:
    if getattr(tile, "widthIndex") == starting.widthIndex +1 :
        if getattr(tile, "heightIndex") == starting.heightIndex :
            right=tile    
            break       

top=None 
for tile in tiles:
    if getattr(tile, "widthIndex") == starting.widthIndex :
        if getattr(tile, "heightIndex") == starting.heightIndex + 1 :
            top=tile    
            break    
        
bottom=None 
for tile in tiles:
    if getattr(tile, "widthIndex") == starting.widthIndex :
        if getattr(tile, "heightIndex") == starting.heightIndex - 1 :
            bottom=tile    
            break     

children=[]

if (left != None and (left.direction == Direction.HORIZONTAL or left.direction == Direction.NORTHEAST or left.direction == Direction.SOUTHEAST)):
    left.update(starting)
    children.append(left)
   
if (right != None and (right.direction == Direction.HORIZONTAL or right.direction == Direction.NORTHWEST or right.direction == Direction.SOUTHWEST)):
    right.update(starting)
    children.append(right)
 
if (top != None and (top.direction == Direction.VERTICAL or top.direction == Direction.SOUTHEAST or top.direction == Direction.SOUTHWEST)):
    top.update(starting)
    children.append(top)
   
if (bottom != None and (bottom.direction == Direction.VERTICAL or bottom.direction == Direction.NORTHEAST or bottom.direction == Direction.NORTHWEST)):
    bottom.update(starting)
    children.append(bottom)

#assert the size is only two, as it shall be
assert len(children) == 2, f"List size is not equal to 2"

startingChildren = copy.copy(children)

#then browse the tiles to find each time a new child, on both size at the same time. Stop when then encounter each other
#we know that a tile has exactly one parent and one child
index=1
found = False
while found == False:
    #print_summary(children)
    index += 1 
    newChildren = []
    for child in children:
        connectsTo = child.compute_next_child_position()     
        newChild = look_for_child_by_index(tiles, child.widthIndex + connectsTo[0][0], child.heightIndex + connectsTo[0][1] )
        #End of the loop
        if newChild.parent != None:
            found = True   
            newChild.child = newChild.parent  
            newChild.update(child)       
            break

        newChild.update(child)
        newChildren.append(newChild)

    children = newChildren

   
print(f"Longest Distance : {index}")

isInside = 0
#For each tile which are not in the path, cast a ray to west (arvitrary) and see how many cross is done (odd=inside, even=outside)
hI=0
for tile in tiles:
    if hI != tile.heightIndex:
        hI = tile.heightIndex
        print("current Height :")        
        print(hI)
    if tile.parent == None and tile.direction != Direction.STARTING:
        wIndex=tile.widthIndex
        crossed=0
        vertexBefore=False
        previousVertexDirection=None
        while wIndex != 0:
            for tileOther in tiles:
                if getattr(tileOther, "widthIndex") == wIndex - 1 and getattr(tileOther, "heightIndex") == tile.heightIndex  :
                    #Check if the tile is in the path
                    if (tileOther.parent != None or tileOther.direction == Direction.STARTING) and tile.direction != Direction.STARTING:
                        #check if the tile is not the same line as the previous tile
                        #First the starting point case
                        if tileOther.direction == Direction.STARTING:
                            if startingChildren[0].heightIndex != startingChildren[1].heightIndex :
                                #If this is a vertex of the polygone
                                if startingChildren[0].heightIndex == tile.heightIndex or startingChildren[1].heightIndex == tile.heightIndex:
                                    if vertexBefore == False :
                                        vertexBefore = True
                                        if startingChildren[0].heightIndex != tileOther.heightIndex:
                                            previousVertexDirection = startingChildren[0].heightIndex
                                        else:
                                            previousVertexDirection = startingChildren[1].heightIndex
                                    else:
                                        vertexBefore = False
                                        if (previousVertexDirection != startingChildren[1].heightIndex and tileOther.heightIndex == startingChildren[0].heightIndex) or(previousVertexDirection != startingChildren[0].heightIndex and tileOther.heightIndex == startingChildren[1].heightIndex)  : #Not on On the top/bottom of the polygon
                                            crossed +=1             
                                else:
                                    crossed +=1

                        elif tileOther.parent.heightIndex != tileOther.child.heightIndex :
                            #If this is a vertex of the polygone
                            if tileOther.parent.heightIndex == tile.heightIndex or tileOther.child.heightIndex == tile.heightIndex:
                                if vertexBefore == False :
                                    vertexBefore = True
                                    previousVertexDirection = tileOther.other_height()
                                else:
                                    vertexBefore = False
                                    if previousVertexDirection != tileOther.other_height(): #Not on On the top/bottom of the polygon
                                        crossed +=1                                
                            else:
                                crossed +=1
                    wIndex += -1

        #Even number : we are inside
        if crossed %2 == 1:
            tile.symbol = "I"
            isInside+=1

# Create a 2D grid to store symbols
grid = [[' ' for _ in range(maxWidth + 1)] for _ in range(maxHeight + 1)]

# Populate the grid with symbols from the Tile objects
#for tile in tiles:
#    grid[maxHeight-tile.heightIndex][tile.widthIndex] = tile.symbol

# Print the grid as ASCII art
#for row in grid:
#    print(' '.join(row))

print(f"Number of Insides : {isInside}")
