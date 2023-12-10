from enum import Enum

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
        if i > maxWidth:
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


#then browse the tiles to find each time a new child, on both size at the same time. Stop when then encounter each other
#we know that a tile has exactly one parent and one child
index=1
found = False
while found == False:
    print_summary(children)
    index += 1 
    newChildren = []
    for child in children:
        connectsTo = child.compute_next_child_position()     
        newChild = look_for_child_by_index(tiles, child.widthIndex + connectsTo[0][0], child.heightIndex + connectsTo[0][1] )

        #End of the loop
        if newChild.parent != None:
            found = True
            break

        newChild.update(child)
        newChildren.append(newChild)

    children = newChildren

   
print(f"Longest Distance : {index}")