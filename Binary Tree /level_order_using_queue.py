class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def level_order(self, root):

        queue = []
        queue.append(root)
        while(len(queue) > 0):
            front = queue.pop(0)
            print(front.key)
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)

    bt.level_order(bt.root)
