class Node:

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None


def inOrder(root):

	if root == None:
		return

	inOrder(root.left)
	print(root.data)
	inOrder(root.right)

def preOrder(root):

	if root == None:
		return

	print(root.data)
	inOrder(root.left)
	inOrder(root.right)


def postOrder(root):

	if root == None:
		return

	
	inOrder(root.left)
	inOrder(root.right)
	print(root.data)




if __name__ == '__main__':

	root = Node(1) 
	root.left = Node(2) 
	root.right = Node(3) 
	root.left.left = Node(4) 
	root.left.right = Node(5) 
	root.right.left = Node(6) 
	root.right.right = Node(7) 

	inOrder(root)
	preOrder(root)
	postOrder(root)