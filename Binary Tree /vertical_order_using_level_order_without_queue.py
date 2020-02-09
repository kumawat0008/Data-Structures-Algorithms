class Node(object):

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def vertical_order(self, root, m):

        height = self.height(root)

        for i in range(1, height+1):
            self.level_order(root, 0, i, m)

    def level_order(self, root, hd, level, m):

        if root is None:
            return

        if level is 1:
            try:
                m[hd].append(root.key)
            except:
                m[hd] = [root.key]
        else:
            self.level_order(root.left, hd-1, level-1, m)
            self.level_order(root.right, hd+1, level-1, m)

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

    m = dict()

    bt.vertical_order(bt.root, m)

    print(sorted(m))
    for i in sorted(m):
        print(m[i])
