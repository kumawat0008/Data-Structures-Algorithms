class node:

	def __init__(self,data):

		self.data = data
		self.left = None
		self.right = None


def height_of_BT(root):

	if root == None:
		return 0

	leftH = height_of_BT(root.left)
	rightH = height_of_BT(root.right)

	return max(leftH,rightH)+1



if __name__ == '__main__':

	root = node(1) 
	root.left = node(2) 
	root.right = node(3) 
	root.left.left = node(4) 
	root.left.right = node(5) 

	print(height_of_BT(root))