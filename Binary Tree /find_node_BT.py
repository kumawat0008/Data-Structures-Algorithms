class node:

	def __init__(self, data):

		self.data = data
		self.left = None
		self.right = None


def ifExist(root, key):

	if root == None:
		return False

	if root.data == key:
		return True

	left = ifExist(root.left,key)
	right = ifExist(root.right,key)

	return left or right



if __name__ == '__main__': 

    root = node(0)  
    root.left = node(1)  
    root.left.left = node(3)  
    root.left.left.left = node(7)  
    root.left.right = node(4)  
    root.left.right.left = node(8)  
    root.left.right.right = node(9)  
    root.right = node(2)  
    root.right.left = node(5)  
    root.right.right = node(6) 

    key = 4

    print(ifExist(root,key))

