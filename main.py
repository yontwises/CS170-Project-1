import heapq

class Node:
    def __init__(self,data,h,g):
        self.data = data
        self.children = []
        self.parent = None
        self.h = h #heuristic cost
        self.g = g #cost to get to depth to depth

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
def test_puzzle():
    #[1,2,3]
    #[4,5,6]
    #[7,8,0]



    testPuzzle = [Node(1,0,1),Node(2,0,1),Node(3,0,1),Node(4,0,1),Node(5,0,1),Node(6,0,1),Node(7,0,1),Node(8,0,1),Node(0,0,1)]
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

def UCS(test_tree):
    rootIndex = find_index(test_tree,0) #create root
    nodes = heapq.heapify(test_tree[rootIndex]) #create data structure to store initial state 
    visited = []
    depth = 0
    path = []
    while nodes:
        if not nodes:
            print("Empty queue. No solution")
        
        node = heapq.heappop(nodes)
        visited.append(node)
        depth = depth + 1
        if node.data == find_index(node.data) + 1:
            path.append(node)


def expand_nodes(self,test_tree,index):
    match index:
        case '0':
            if 




def swap(tree,pos1,pos2):
    tree[pos1], tree[pos2] = tree[pos2], tree[pos1]
    return tree




def main():
    test = test_puzzle()
    find_index(test)
    

if __name__== "__main__":
    main()