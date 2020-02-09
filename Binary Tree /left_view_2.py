class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def left_view(self, root):

        max_level = list()
        max_level = [0]
        current_level = 1
        self.pre_order(root, current_level, max_level)

    def pre_order(self, root, current_level, max_level):

        if root is None:
            return

        if current_level > max_level[0]:
            print(root.key)
            max_level[0] = current_level
        self.pre_order(root.left, current_level+1, max_level)
        self.pre_order(root.right, current_level+1, max_level)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)

    bt.left_view(bt.root)
