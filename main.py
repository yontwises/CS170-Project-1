
class Node:
    def __init__(self,data,h,g,depth,state):
        self.data = data
        self.children = []
        self.parent = None
        self.h = h #heuristic cost
        self.depth = depth #depth of node (g(n))
        self.visited = False #in place of visited list just set to true when expanding
        self.state = state

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
def test_puzzle():
    #[1,2,3]
    #[4,5,6]
    #[7,8,0]

    testPuzzle = [1, 2, 3], [4,5,6], [7,8,0]
    return testPuzzle

#return index where 0 is located     
def find_index(puzzle,num):
    count = 0
    for node in puzzle:
        count = count + 1
        if(node.data == num):
            index = count

    # print(index)
    return index

def goal_state(problem):
    goal_state = [1, 2, 3], [4,5,6], [7,8,0]
    if(problem == goal_state):
        return True
    else:
        return False
    

#inspired by Professor's general search algorithm
def UCS(problem):
    rootIndex = find_index(problem,0) #get rood index
    nodes = [] #create data structure to store initial state 
    nodes.append(problem[rootIndex - 1])  #store root inside datastructure
    #visited = [] #list of visited nodes 
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
            return 'Success + print more info...'
        
        print('')

        
         

        



def expand_nodes(node):
    #012
    #345
    #678
    expandCount = 0
    match index:
        case 0:
            expandCount = 2
            node.add_child(problem[1])
            node.add_child(problem[3])
            return expandCount
        case 1:
            expandCount = 3
            node.add_child(problem[0])
            node.add_child(problem[2])
            node.add_child(problem[4])
            return expandCount
        case 2: 
            expandCount = 2
            node.add_child(problem[1])
            node.add_child(problem[5])
            return expandCount
        case 3: 
            expandCount = 3
            node.add_child(problem[0])
            node.add_child(problem[4])
            node.add_child(problem[6])
            return expandCount
        case 4: 
            expandCount = 4
            node.add_child(problem[1])
            node.add_child(problem[3])
            node.add_child(problem[5])
            node.add_child(problem[7])
            return expandCount
        case 5: 
            expandCount = 3
            node.add_child(problem[2])
            node.add_child(problem[4])
            node.add_child(problem[8])
            return expandCount
        case 6: 
            expandCount = 2
            node.add_child(problem[3])
            node.add_child(problem[7])
            return expandCount
        case 7:
            expandCount = 3
            node.add_child(problem[4])
            node.add_child(problem[6])
            node.add_child(problem[8])
            return expandCount
        case 8:
            expandCount = 2
            node.add_child(problem[5])
            node.add_child(problem[7])
            return expandCount
    

            
            



def swap(tree,pos1,pos2):
    tree[pos1], tree[pos2] = tree[pos2], tree[pos1]
    return tree




def main():
    test = test_puzzle()
    # for node in test:
    #     print(str(node.data) + ',')
    
    expandCount = UCS(test)
    print('expand count: ' + str(expandCount))
    

if __name__== "__main__":
    main()