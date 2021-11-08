import heapq

class Node:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
def test_puzzle():
    #[1,2,3]
    #[4,5,6]
    #[7,8,0]



    testPuzzle = [Node(1),Node(2),Node(3),Node(4),Node(5),Node(6),Node(7),Node(8),Node(0)]
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
    while nodes:
        if not nodes:
            print("Empty queue. No solution")
        
        node = heapq.heappop(nodes)
        visited.append(node)
        if node.data == find_index(node.data) + 1:
            nodes = 







def main():
    test = test_puzzle()
    find_index(test)
    

if __name__== "__main__":
    main()