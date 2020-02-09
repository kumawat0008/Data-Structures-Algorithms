class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def printInorder(node): 
    if node is None: 
        return
  
    printInorder(node.left) 
  
    print(node.data, end=" ") 
  
    printInorder(node.right) 


def buildTree(level, inorder):

    # print('+++++',level,inorder)

    if len(inorder) == 1:
        return Node(inorder[0])
    ino_index = 0
    for i in range(len(level)):
        if level[i] in inorder:
            node = Node(level[i])
            ino_index = inorder.index(level[i])
            break


    node.left = buildTree(level, inorder[0:ino_index])
    node.right = buildTree(level, inorder[ino_index+1:len(inorder)])
    return node




levelorder = [20, 8, 22, 4, 12, 10, 14] 
inorder = [4, 8, 10, 12, 14, 20, 22] 

ino_len = len(inorder) 
root = buildTree(levelorder, inorder) 

print ("Inorder traversal of the constructed tree is") 
printInorder(root) 