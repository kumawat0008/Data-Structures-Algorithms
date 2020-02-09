class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def buildTree(inOrder, preOrder):

    
    if len(inOrder):
        if len(inOrder) == 1:
            # print('++++here',inOrder,preOrder)
            preOrder.pop(0)
            # print('++++after',inOrder,preOrder)
            return Node(inOrder[0])
        root_node = preOrder[0]
        # print('+++++rootnode',root_node)
        preOrder.pop(0)
        ino_index = inOrder.index(root_node)
        node = Node(root_node)
        node.left = buildTree(inOrder[0:ino_index],preOrder)
        node.right = buildTree(inOrder[ino_index+1:len(inOrder)],preOrder)

        return node

def printInorder(node): 
    if node is None: 
        return 
      
    printInorder(node.left) 
      
    print(node.data,end=" ") 
  
    printInorder(node.right) 
      
# Driver program to test above function 
inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preOrder = ['A', 'B', 'D', 'E', 'C', 'F'] 
root = buildTree(inOrder, preOrder) 
  
print("Inorder traversal of the constructed tree is")
printInorder(root) 