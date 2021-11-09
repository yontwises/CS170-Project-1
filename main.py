import copy


class Node:
    def __init__(self,state):
    
        self.children = [] #list of children    
        # self.parent = None #deprecated bc don't need to move up tree
        self.h = 0 #heuristic cost
        self.depth = 0 #depth of node (g(n))
        self.visited = False #in place of visited list just set to true when expanding
        self.state = state #current state of puzzle 

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
def test_puzzle():
    #[1,2,3]
    #[4,5,6]
    #[7,8,0]

    # goal_state = ([1, 2, 3], [4,5,6], [0,7,8]) #depth 2
    goal_state = ([1, 2, 3], [5,0,6], [0,7,8]) #depth 4
    # goal_state = ([1, 3, 6], [5,0,2], [4,7,8]) #depth 8
    # goal_state = ([1, 3, 6], [5,0,7], [4,7,8]) #depth 12
    # goal_state = ([1, 6, 7], [5,0,3], [4,8,2]) #depth 16
    # goal_state = ([7, 1, 2], [4,8,5], [6,3,0]) #depth 20
    # goal_state = ([0, 7, 2], [4,6,1], [3,5,8]) #depth 24
    return goal_state

#return index where 0 is located     
#deprecated
# def find_index(puzzle,num):
#     count = 0
#     for node in puzzle:
#         count = count + 1
#         if(node.data == num):
#             index = count

#     # print(index)
#     return index

def goal_state(problem):
    goal_state = ([1, 2, 3], [4,5,6], [7,8,0]) 
    if(problem == goal_state):
        return True
    else:
        return False
    

#inspired by Professor's general search algorithm in slides
def UCS(problem):
    root = Node(problem)
    nodes = [] #create data structure to store initial state 
    nodes.append(root)  #store root inside datastructure
    visitedPuzzles = [] #list of visited puzzles (no longer using visited list for nodes) 
    path = [] #nodes we have seen already 
    expandCount = 0 #number of nodes expanded

    while True:
        if not nodes:
            return 'failure'
        
        node = nodes.pop(0) #popoff front node
        if node.visited is False:
            expandCount += 1
            node.visited = True
        
        if goal_state(node.state):
            return 'Success! Num of Expanded Nodes: ' + str(expandCount) + ' Depth: ' + str(node.depth)
        
        #Expand upon all operations on node and then put children into children list
        expandNode = expand_nodes(node,visitedPuzzles)

        #print(node.children[0])

        #Update g(n) aka depth in children to be visited
        for child in node.children:
            child.depth = node.depth + 1
            child.h = 0
            nodes.append(child)
            visitedPuzzles.append(child.state)
        

        

        
         
def expand_nodes(node,visited):
    rowIndex = 0
    columnIndex = 0

    #look for the index of 0
    for i in range(len(node.state)):
        for j in range(len(node.state)):
            if node.state[i][j] == 0:
                rowIndex = i
                columnIndex = j

    #operations: move left, right, up, down

    #Can move left if not on the first column
    if columnIndex > 0:
        # to move left just go back 1 column
        #get a copy of current state 
        left = copy.deepcopy(node.state)
        temp = left[rowIndex][columnIndex]
        left[rowIndex][columnIndex] = left[rowIndex][columnIndex - 1]
        left[rowIndex][columnIndex - 1] = temp

        if left not in visited:
            node.children.append(Node(left))

    #can move right if not at the last column
    if columnIndex < len(node.state) - 1:
        # to move right swap right in + 1 column
        right = copy.deepcopy(node.state)
        temp = right[rowIndex][columnIndex]
        right[rowIndex][columnIndex] = right[rowIndex][columnIndex + 1]
        right[rowIndex][columnIndex+1] = temp

        if right not in visited:
            node.children.append(Node(right))

    #can move up if not on first row 
    if rowIndex > 0:
        # to move up just decrement row 
        up = copy.deepcopy(node.state)
        temp = up[rowIndex][columnIndex]
        up[rowIndex][columnIndex] = up[rowIndex-1][columnIndex]
        up[rowIndex - 1][columnIndex] = temp

        if up not in visited:
            node.children.append(Node(up))
    #can move down if not last row 
    if rowIndex < len(node.state) - 1:
        down = copy.deepcopy(node.state)
        temp = down[rowIndex][columnIndex]
        down[rowIndex][columnIndex] = down[rowIndex + 1][columnIndex]
        down[rowIndex + 1][columnIndex] = temp

        if down not in visited:
            node.children.append(Node(down))
    
    return node

def manhattan(puzzle):
    goal_pzl = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    count = 0
    gr, gc, r, c = 0, 0, 0, 0

    for l in range(1, 9):
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if int(puzzle[i][j]) == l:
                    r = i
                    c = j
                if goal_pzl[i][j] == l:
                    gr = i
                    gc = j
        count += abs(gr-r) + abs(gc-c)

    return count




def main():

    print(UCS(test_puzzle()))
    # print(UCS(goal_state_0))
    # print(UCS(goal_state_2))
    # print(UCS(goal_state_4))
    # print(UCS(goal_state_8))
    # print(UCS(goal_state_12))
    # print(UCS(goal_state_16))
    # print(UCS(goal_state_20))
    # print(UCS(goal_state_24))
  
    

if __name__== "__main__":
    main()