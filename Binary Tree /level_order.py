class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def level_order(self, root):

        height = self.height(root)
        for i in range(height):
            self.print_level_order(root, i)

    def print_level_order(self, root, level):

        if root is None:
            return

        if level is 0:
            print(root.key)
        else:
            self.print_level_order(root.left, level-1)
            self.print_level_order(root.right, level-1)

    def height(self, root):

        if root is None:
            return 0

        return 1+max(self.height(root.left), self.height(root.right))


if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)

    bt.level_order(bt.root)
