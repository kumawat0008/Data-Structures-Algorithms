class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def clockwise_spiral_order(self, root):
        i = 1
        j = self.height(root)
        flag = 0

        while(i <= j):
            if flag is 0:
                self.print_left_to_right(root, i)
                i += 1
                flag = 1
            else:
                self.print_right_to_left(root, j)
                j -= 1
                flag = 0

    def print_left_to_right(self, root, level):

        if root is None:
            return

        if level is 1:
            print(root.key)
        else:
            self.print_left_to_right(root.left, level-1)
            self.print_left_to_right(root.right, level-1)

    def print_right_to_left(self, root, level):

        if root is None:
            return

        if level is 1:
            print(root.key)
        else:
            self.print_right_to_left(root.right, level-1)
            self.print_right_to_left(root.left, level-1)

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

    bt.clockwise_spiral_order(bt.root)
