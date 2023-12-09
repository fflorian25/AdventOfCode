class Node:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right

    def go_left_right(self, leftRight):
        if leftRight == "L":
            return self.left
        else :
            return self.right

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
        print(f"Left: .{node.left}.")
        print(f"Right: .{node.right}.")
        print("-------------------------")

#pretty print
#print_cards_summary(networks)

#find the end of the map
pathIndex=0
goTo="AAA"
nbSteps = 0
while True :
    lr=paths[pathIndex]
    #search for the last goTo
    for nod in networks:
        if getattr(nod, "node") == goTo:
            goTo=nod.go_left_right(lr)
            break  

    pathIndex = (pathIndex + 1) % len(paths)
    nbSteps += 1
    if goTo == "ZZZ":
        break

# print total steps
print(f"Total steps: {nbSteps}")
