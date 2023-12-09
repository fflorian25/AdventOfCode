import math

class Node:
    def __init__(self, node, left, right):
        self.node = node
        self.end = node[2]
        self.left = left
        self.right = right

    def go_left_right(self, leftRight):
        if leftRight == "L":
            return self.left
        else :
            return self.right
        

        
        
# find all the Node finishing with a letter
def findAllEnding(networks, letter):
    found=[]
    for nod in networks:
        if getattr(nod, "end") == letter:
            found.append(nod)

    return found

def isFinishingWith(node, letter):
    if node[2] != letter:
        return False
    else :
        return True

# reading from file
filename = "2023/Day8/input.txt"
paths = None
networks = []

with open(filename, 'r') as f:
    lines = f.readlines()   
    paths = lines[0].strip() 
    for line in lines[2:]:
        nodeName, lr = line.split("=")
        left, right = lr.strip().split(",")
        network = Node(nodeName.strip(), left.strip("(").strip(), right.strip(")").strip())
        networks.append(network)


def print_cards_summary(nodes):
    for i, node in enumerate(nodes, start=1):
        print(f"Node {i}:")
        print(f"Node: .{node.node}.")
        print(f"Node End With: .{node.end}.")
        print(f"Left: .{node.left}.")
        print(f"Right: .{node.right}.")
        print("-------------------------")

#pretty print
#print_cards_summary(networks)

#find the end of the map
pathIndex=0
fromNodes=findAllEnding(networks, "A")
goTos=[]
empan=[]

for fromNode in fromNodes:
    goTos.append(fromNode.node)

nbSteps = 0
while len(goTos) != 0 :
    lr=paths[pathIndex]
    #search for the last goTo
    for i, goTo in enumerate(goTos):
        for nod in networks:
            if getattr(nod, "node") == goTo:
                goTos[i]=nod.go_left_right(lr)
                break  

    pathIndex = (pathIndex + 1) % len(paths)
    nbSteps += 1

    index = 0
    while index < len(goTos):
        goTo = goTos[index]
        
        if isFinishingWith(goTo, "Z"):
            # If the condition is met, delete the element and increment the counter
            del goTos[index]
            empan.append(nbSteps)
        else:
            index += 1  # Move to the next element only if no deletion occurred

# compute ppcm
# Start with the LCM of the first two numbers
lcm_result = abs(empan[0] * empan[1]) // math.gcd(empan[0], empan[1])

# Iterate through the remaining numbers and update the LCM
for number in empan[2:]:
    lcm_result = abs(lcm_result * number) // math.gcd(lcm_result, number)

print(f"Total steps: {lcm_result}")
